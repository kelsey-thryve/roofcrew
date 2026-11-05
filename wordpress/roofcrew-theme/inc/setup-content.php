<?php
/**
 * "Import starter content" button (Settings → The Roof Crew).
 * Creates the fixed pages, the Services and Locations parent pages and their child pages
 * (from inc/seed.php, generated from the v2 design), and sets Home as the front page.
 * Re-running keeps what exists: pages are matched by their path.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Create a page if no page exists at that path. Returns the page ID. */
function rc_ensure_page( $path, $args, &$made ) {
	$p = get_page_by_path( $path );
	if ( $p ) {
		return $p->ID;
	}
	$id = wp_insert_post( array_merge( array( 'post_type' => 'page', 'post_status' => 'publish' ), $args ) );
	if ( $id && ! is_wp_error( $id ) ) {
		$made++;
		return $id;
	}
	return 0;
}

/** Attach a theme image to a page as its featured image. */
function rc_attach_theme_image( $post_id, $file ) {
	if ( ! $post_id || ! $file || has_post_thumbnail( $post_id ) ) {
		return;
	}
	$src = get_theme_file_path( 'assets/img/' . $file );
	if ( ! file_exists( $src ) ) {
		return;
	}
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/image.php';
	$tmp = wp_tempnam( $file );
	if ( $tmp && copy( $src, $tmp ) ) {
		$att = media_handle_sideload( array( 'name' => $file, 'tmp_name' => $tmp ), $post_id );
		if ( is_wp_error( $att ) ) {
			@unlink( $tmp ); // phpcs:ignore WordPress.PHP.NoSilencedErrors
		} else {
			set_post_thumbnail( $post_id, $att );
		}
	}
}

function rc_import_starter_content() {
	$seed = require get_theme_file_path( 'inc/seed.php' );
	$made = 0;

	$home = rc_ensure_page( 'home', array( 'post_title' => 'Home', 'post_name' => 'home' ), $made );
	foreach ( array( 'about' => 'About', 'contact' => 'Contact', 'quote' => 'Free quote', 'services' => 'Services', 'locations' => 'Locations' ) as $slug => $title ) {
		rc_ensure_page( $slug, array( 'post_title' => $title, 'post_name' => $slug ), $made );
	}
	if ( $home ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_on_front', $home );
	}

	foreach ( array( 'services' => 'template-service.php', 'locations' => 'template-location.php' ) as $parent_slug => $tpl ) {
		$parent = get_page_by_path( $parent_slug );
		if ( ! $parent ) {
			continue;
		}
		foreach ( $seed[ $parent_slug ] as $i => $item ) {
			$path = $parent_slug . '/' . $item['slug'];
			if ( get_page_by_path( $path ) ) {
				continue;
			}
			$id = rc_ensure_page( $path, array(
				'post_title'   => $item['title'],
				'post_name'    => $item['slug'],
				'post_parent'  => $parent->ID,
				'post_status'  => $item['publish'] ? 'publish' : 'draft',
				'post_content' => $item['content'],
				'post_excerpt' => $item['excerpt'],
				'menu_order'   => $i,
			), $made );
			if ( ! $id ) {
				continue;
			}
			update_post_meta( $id, '_wp_page_template', $tpl );
			foreach ( $item['fields'] as $k => $v ) {
				update_post_meta( $id, '_' . $k, $v );
			}
			rc_attach_theme_image( $id, $item['image'] );
		}
	}

	// Pretty links (/services/reroofing/) need the "Post name" permalink setting.
	if ( '' === (string) get_option( 'permalink_structure' ) ) {
		update_option( 'permalink_structure', '/%postname%/' );
	}
	flush_rewrite_rules();

	return $made;
}

add_action( 'admin_post_rc_setup_content', function () {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( 'Not allowed.' );
	}
	check_admin_referer( 'rc_setup_content' );
	@set_time_limit( 300 ); // phpcs:ignore WordPress.PHP.NoSilencedErrors
	$made = rc_import_starter_content();
	$msg  = sprintf( 'Done. %d pages created. Home is set as the front page. Draft service and area pages are under Pages, ready to fill in and publish.', $made );
	wp_safe_redirect( add_query_arg( 'rc_setup', rawurlencode( $msg ), admin_url( 'options-general.php?page=rc-settings' ) ) );
	exit;
} );

/* After activating the theme, point the admin to the import button. */
add_action( 'admin_notices', function () {
	if ( ! current_user_can( 'manage_options' ) || ( get_option( 'page_on_front' ) && get_page_by_path( 'services/reroofing' ) ) ) {
		return;
	}
	echo '<div class="notice notice-info"><p><strong>The Roof Crew theme:</strong> go to <a href="' . esc_url( admin_url( 'options-general.php?page=rc-settings' ) ) . '">Settings → The Roof Crew</a> and click <em>Import starter content</em> to create the pages.</p></div>';
} );
