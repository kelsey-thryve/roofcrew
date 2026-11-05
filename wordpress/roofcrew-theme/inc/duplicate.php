<?php
/**
 * "Duplicate" link under each page in Pages → All Pages.
 * Copies the page (content, excerpt, template, parent, fields and featured image) as a draft,
 * e.g. duplicate East Auckland to start North Shore.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_filter( 'page_row_actions', function ( $actions, $post ) {
	if ( current_user_can( 'edit_pages' ) ) {
		$url                   = wp_nonce_url( admin_url( 'admin-post.php?action=rc_duplicate&post=' . $post->ID ), 'rc_duplicate_' . $post->ID );
		$actions['rc_duplicate'] = '<a href="' . esc_url( $url ) . '">Duplicate</a>';
	}
	return $actions;
}, 10, 2 );

add_action( 'admin_post_rc_duplicate', function () {
	$id = isset( $_GET['post'] ) ? absint( $_GET['post'] ) : 0;
	check_admin_referer( 'rc_duplicate_' . $id );
	$src = get_post( $id );
	if ( ! $src || 'page' !== $src->post_type || ! current_user_can( 'edit_pages' ) ) {
		wp_die( 'Not allowed.' );
	}
	$new = wp_insert_post( array(
		'post_type'    => 'page',
		'post_status'  => 'draft',
		'post_title'   => $src->post_title . ' (copy)',
		'post_content' => $src->post_content,
		'post_excerpt' => $src->post_excerpt,
		'post_parent'  => $src->post_parent,
		'menu_order'   => $src->menu_order + 1,
	) );
	if ( ! $new || is_wp_error( $new ) ) {
		wp_die( 'Could not duplicate the page.' );
	}
	foreach ( get_post_meta( $src->ID ) as $key => $values ) {
		if ( in_array( $key, array( '_edit_lock', '_edit_last', '_wp_old_slug' ), true ) ) {
			continue;
		}
		foreach ( $values as $v ) {
			add_post_meta( $new, $key, maybe_unserialize( $v ) );
		}
	}
	wp_safe_redirect( admin_url( 'post.php?action=edit&post=' . $new ) );
	exit;
} );
