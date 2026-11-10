<?php
/**
 * Extra boxes on the page editor for the "Service page" and "Location page" templates.
 * The main editor content fills the intro section of those pages; the Excerpt is the short
 * text on cards and in search results; the Featured image is the hero photo.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Field types: text, textarea (plain lines), html (may hold links and the yellow <mark class="ph">
 * highlights), url, checkbox, icon, select (options in the 4th item).
 */
function rc_field_defs() {
	$seo = array(
		'rc_meta_title' => array( 'SEO title', 'text', 'Browser tab and Google title. Defaults to the main heading.' ),
		'rc_meta_desc'  => array( 'Meta description', 'textarea', 'Google snippet. Defaults to the Excerpt.' ),
	);
	$faqs = array(
		'rc_faq_title' => array( 'Questions heading', 'text', 'e.g. "Reroofing questions".' ),
		'rc_faqs'      => array( 'Questions', 'html', 'One question per block: the question on the first line, the answer on the next, then a blank line before the next question. Leave empty to hide.' ),
	);
	return array(
		'template-service.php'  => array_merge( array(
			'rc_kind'          => array( 'Type', 'select', 'Services show in the services grid; roofing materials show as roofing options.', array( 'service' => 'Service', 'material' => 'Roofing material' ) ),
			'rc_h1'            => array( 'Main heading', 'html', 'Defaults to "[Page title] in Auckland".' ),
			'rc_lede'          => array( 'Line under the heading', 'html', 'The intro in the hero.' ),
			'rc_hold'          => array( 'Notice under the hero (optional)', 'html', 'e.g. a page that is waiting on Mike. Leave empty to hide.' ),
			'rc_intro_heading' => array( 'Intro heading', 'html', 'Heading of the first section, beside the photo. Each H2 heading in the editor text starts a new section below it.' ),
			'rc_included'      => array( "What's included (one per line)", 'textarea', 'Shown as a tick list under the intro text. Leave empty to hide.' ),
			'rc_photo'         => array( 'Photo beside the intro (optional)', 'text', 'A theme image file name (e.g. colorsteel-installed.jpg) or an image URL. Defaults to the Featured image.' ),
			'rc_icon'          => array( 'Card icon', 'icon', 'Icon on the service cards.' ),
			'rc_reroof'        => array( 'Reroof sections', 'checkbox', 'Show "How a reroof works", roof options and prices, and the before/after slider.' ),
		), $faqs, array(
			'rc_closing'       => array( 'Quote section heading', 'text', 'Defaults to "Get your free quote."' ),
		), $seo ),
		'template-location.php' => array_merge( array(
			'rc_kind'          => array( 'Type', 'select', 'Regions show in the menus and region cards; areas show as Popular areas.', array( 'region' => 'Region', 'area' => 'Area (suburb or town)' ) ),
			'rc_region'        => array( 'Region (areas only)', 'text', 'Shown on the Popular areas card, e.g. "South Auckland".' ),
			'rc_h1'            => array( 'Main heading', 'html', 'Defaults to "Reroofing in [Page title]".' ),
			'rc_lede'          => array( 'Line under the heading', 'html', 'One or two sentences in the hero.' ),
			'rc_intro_heading' => array( 'Local section heading', 'html', 'Defaults to "Your local reroofing crew." Each H2 heading in the editor text starts a new section further down.' ),
			'rc_job'           => array( 'Local job (optional)', 'html', 'Shown beside the local section instead of the photo.' ),
			'rc_photo'         => array( 'Photo beside the local section (optional)', 'text', 'A theme image file name or an image URL. Defaults to the Featured image.' ),
			'rc_review'        => array( 'Review to show', 'html', 'Two lines: the review, then the name and suburb. Leave empty to show the usual three reviews.' ),
		), $faqs, array(
			'rc_suburbs'       => array( 'Suburbs (one per line)', 'html', 'Shown in the "Suburbs we cover" section. A suburb with its own Location page links to it. A line starting with "# " starts a new group with that heading.' ),
			'rc_map'           => array( 'Map link (optional)', 'url', 'An OpenStreetMap "Share → HTML" embed link. Leave empty for the Auckland map.' ),
		), $seo ),
	);
}

add_action( 'add_meta_boxes_page', function ( $post ) {
	add_meta_box( 'rc_fields', 'Page details (The Roof Crew)', 'rc_fields_box', 'page', 'normal', 'high' );
} );

function rc_fields_box( $post ) {
	$tpl  = get_page_template_slug( $post );
	$defs = rc_field_defs();
	if ( ! isset( $defs[ $tpl ] ) ) {
		$fixed = array( 'about', 'contact', 'quote', 'services', 'locations' );
		if ( (int) get_option( 'page_on_front' ) === $post->ID || in_array( $post->post_name, $fixed, true ) ) {
			echo '<p>This page\'s layout and wording come from the theme, so the editor above is not shown on the site. Ask Thryve Growth to change it.</p>';
		} else {
			echo '<p>For a service or an area page, set <strong>Template</strong> to "Service page" or "Location page" (Page panel on the right), choose <strong>Services</strong> or <strong>Locations</strong> as the parent, then save and reload to see its boxes here.</p>';
		}
		return;
	}
	wp_nonce_field( 'rc_fields', 'rc_fields_nonce' );
	echo '<table class="form-table" role="presentation">';
	foreach ( $defs[ $tpl ] as $key => $d ) {
		list( $label, $type, $help ) = $d;
		$v = get_post_meta( $post->ID, '_' . $key, true );
		echo '<tr><th scope="row"><label for="' . esc_attr( $key ) . '">' . esc_html( $label ) . '</label></th><td>';
		if ( 'textarea' === $type || 'html' === $type ) {
			echo '<textarea id="' . esc_attr( $key ) . '" name="' . esc_attr( $key ) . '" rows="4" class="large-text">' . esc_textarea( $v ) . '</textarea>';
		} elseif ( 'checkbox' === $type ) {
			echo '<label><input type="checkbox" id="' . esc_attr( $key ) . '" name="' . esc_attr( $key ) . '" value="1" ' . checked( $v, '1', false ) . '> Show</label>';
		} elseif ( 'select' === $type ) {
			echo '<select id="' . esc_attr( $key ) . '" name="' . esc_attr( $key ) . '">';
			foreach ( $d[3] as $k => $l ) {
				echo '<option value="' . esc_attr( $k ) . '" ' . selected( $v, $k, false ) . '>' . esc_html( $l ) . '</option>';
			}
			echo '</select>';
		} elseif ( 'icon' === $type ) {
			echo '<select id="' . esc_attr( $key ) . '" name="' . esc_attr( $key ) . '">';
			foreach ( array( 'home' => 'House', 'build' => 'New build', 'wrench' => 'Repair', 'drop' => 'Water drop', 'search' => 'Inspection', 'layers' => 'Roofing material', 'shield' => 'Shield' ) as $k => $l ) {
				echo '<option value="' . esc_attr( $k ) . '" ' . selected( $v, $k, false ) . '>' . esc_html( $l ) . '</option>';
			}
			echo '</select>';
		} else {
			echo '<input type="' . ( 'url' === $type ? 'url' : 'text' ) . '" id="' . esc_attr( $key ) . '" name="' . esc_attr( $key ) . '" value="' . esc_attr( $v ) . '" class="large-text">';
		}
		echo '<p class="description">' . esc_html( $help ) . '</p></td></tr>';
	}
	echo '</table><p class="description">The Excerpt (Page panel on the right) is the short text on cards. The Featured image is the photo at the top.</p>';
}

add_action( 'save_post_page', function ( $post_id ) {
	if ( ! isset( $_POST['rc_fields_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['rc_fields_nonce'] ), 'rc_fields' ) ) {
		return;
	}
	if ( ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) || ! current_user_can( 'edit_page', $post_id ) ) {
		return;
	}
	$defs = rc_field_defs();
	$tpl  = get_page_template_slug( $post_id );
	if ( ! isset( $defs[ $tpl ] ) ) {
		return;
	}
	foreach ( $defs[ $tpl ] as $key => $d ) {
		$type = $d[1];
		$raw  = isset( $_POST[ $key ] ) ? wp_unslash( $_POST[ $key ] ) : ''; // phpcs:ignore WordPress.Security.ValidatedSanitizedInput
		if ( 'checkbox' === $type ) {
			$val = $raw ? '1' : '';
		} elseif ( 'textarea' === $type ) {
			$val = sanitize_textarea_field( $raw );
		} elseif ( 'html' === $type ) {
			$val = wp_kses_post( $raw );
		} elseif ( 'select' === $type ) {
			$val = isset( $d[3][ $raw ] ) ? $raw : '';
		} elseif ( 'url' === $type ) {
			$val = esc_url_raw( $raw );
		} else {
			$val = sanitize_text_field( $raw );
		}
		update_post_meta( $post_id, '_' . $key, $val );
	}
} );

/* On the fixed pages, a reminder at the top of the editor that their wording lives in the theme. */
add_action( 'admin_notices', function () {
	$screen = get_current_screen();
	if ( ! $screen || 'page' !== $screen->id || empty( $_GET['post'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification
		return;
	}
	$p = get_post( absint( $_GET['post'] ) ); // phpcs:ignore WordPress.Security.NonceVerification
	if ( ! $p ) {
		return;
	}
	$fixed = array( 'about', 'contact', 'quote', 'services', 'locations' );
	if ( (int) get_option( 'page_on_front' ) === $p->ID || ( 0 === (int) $p->post_parent && in_array( $p->post_name, $fixed, true ) ) ) {
		echo '<div class="notice notice-info"><p><strong>The Roof Crew:</strong> this page\'s layout and wording come from the theme, so changes typed here won\'t show on the site. Service and area pages (under Services and Locations) are fully editable here.</p></div>';
	}
} );
