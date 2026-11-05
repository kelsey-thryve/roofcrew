<?php
/**
 * Quote form handler. The forms keep the site's own design (no form plugin needed).
 * Each request is saved (wp-admin → Quote requests) and emailed to the address in
 * Settings → The Roof Crew, through Resend when a key is saved, otherwise through wp_mail().
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'init', function () {
	register_post_type( 'rc_enquiry', array(
		'labels'          => array(
			'name'          => 'Quote requests',
			'singular_name' => 'Quote request',
			'edit_item'     => 'Quote request',
		),
		'public'          => false,
		'show_ui'         => true,
		'menu_icon'       => 'dashicons-email-alt',
		'menu_position'   => 22,
		'supports'        => array( 'title', 'editor' ),
		'capability_type' => 'post',
		'capabilities'    => array( 'create_posts' => 'do_not_allow' ),
		'map_meta_cap'    => true,
	) );
} );

/** Send one email through the Resend API. Returns true on success. */
function rc_send_resend( $to, $subject, $text, $reply_to ) {
	$key  = rc_setting( 'resend_key' );
	$from = rc_setting( 'from_email' );
	if ( ! $key || ! $from ) {
		return false;
	}
	$body = array(
		'from'    => 'The Roof Crew website <' . $from . '>',
		'to'      => array( $to ),
		'subject' => $subject,
		'text'    => $text,
	);
	if ( $reply_to ) {
		$body['reply_to'] = $reply_to;
	}
	$res = wp_remote_post( 'https://api.resend.com/emails', array(
		'timeout' => 15,
		'headers' => array(
			'Authorization' => 'Bearer ' . $key,
			'Content-Type'  => 'application/json',
		),
		'body'    => wp_json_encode( $body ),
	) );
	$code = is_wp_error( $res ) ? 0 : (int) wp_remote_retrieve_response_code( $res );
	return $code >= 200 && $code < 300;
}

function rc_handle_quote() {
	$back = isset( $_POST['back'] ) ? esc_url_raw( wp_unslash( $_POST['back'] ) ) : home_url( '/' );
	$back = wp_validate_redirect( $back, home_url( '/' ) );
	$fid  = isset( $_POST['form_id'] ) ? sanitize_key( wp_unslash( $_POST['form_id'] ) ) : 'get-quote';

	if ( ! isset( $_POST['rc_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['rc_nonce'] ), 'rc_quote' ) ) {
		wp_safe_redirect( $back . '#' . $fid );
		exit;
	}
	$name = sanitize_text_field( wp_unslash( isset( $_POST['name'] ) ? $_POST['name'] : '' ) );
	$done = add_query_arg( array( 'sent' => $fid, 'n' => rawurlencode( strtok( $name . ' ', ' ' ) ) ), $back ) . '#' . $fid;

	// Honeypot: bots fill the hidden "website" field. Pretend it worked.
	if ( ! empty( $_POST['website'] ) ) {
		wp_safe_redirect( $done );
		exit;
	}

	$f = array(
		'Name'           => $name,
		'Phone'          => sanitize_text_field( wp_unslash( isset( $_POST['phone'] ) ? $_POST['phone'] : '' ) ),
		'Email'          => sanitize_email( wp_unslash( isset( $_POST['email'] ) ? $_POST['email'] : '' ) ),
		'Suburb/address' => sanitize_text_field( wp_unslash( isset( $_POST['address'] ) ? $_POST['address'] : '' ) ),
		'Roof'           => sanitize_text_field( wp_unslash( isset( $_POST['need'] ) ? $_POST['need'] : '' ) ),
		'Message'        => sanitize_textarea_field( wp_unslash( isset( $_POST['message'] ) ? $_POST['message'] : '' ) ),
	);
	if ( '' === $f['Name'] || '' === $f['Phone'] ) {
		wp_safe_redirect( $back . '#' . $fid );
		exit;
	}

	$text = '';
	foreach ( $f as $k => $v ) {
		$text .= $k . ': ' . $v . "\n";
	}
	$text .= "\nSent from: " . $back;

	wp_insert_post( array(
		'post_type'    => 'rc_enquiry',
		'post_status'  => 'private',
		'post_title'   => $f['Name'] . ' (' . $f['Roof'] . ')',
		'post_content' => $text,
	) );

	$to = rc_setting( 'enquiry_email' );
	if ( $to ) {
		$subject  = 'New quote request: ' . $f['Name'];
		$reply_to = $f['Email'] ? $f['Name'] . ' <' . $f['Email'] . '>' : '';
		if ( ! rc_send_resend( $to, $subject, $text, $reply_to ) ) {
			$headers = $reply_to ? array( 'Reply-To: ' . $reply_to ) : array();
			if ( rc_setting( 'from_email' ) ) {
				$headers[] = 'From: The Roof Crew website <' . rc_setting( 'from_email' ) . '>';
			}
			wp_mail( $to, $subject, $text, $headers );
		}
	}

	wp_safe_redirect( $done );
	exit;
}
add_action( 'admin_post_nopriv_rc_quote', 'rc_handle_quote' );
add_action( 'admin_post_rc_quote', 'rc_handle_quote' );
