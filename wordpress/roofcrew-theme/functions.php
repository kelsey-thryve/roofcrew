<?php
/**
 * The Roof Crew theme.
 *
 * Fixed pages (Home, About, Contact, Free quote, Services, Locations) use their own templates,
 * generated from the v2 design. Services and Locations are ordinary pages: each one is a child of
 * the Services or Locations page and uses the "Service page" or "Location page" template, so new
 * ones can be added (or duplicated) in wp-admin and appear in the menus automatically.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'RC_VERSION', '1.0.0' );
define( 'RC_PHONE', '021 903 822' );
define( 'RC_TEL', '+6421903822' );
define( 'RC_MAP_AUCKLAND', 'https://www.openstreetmap.org/export/embed.html?bbox=174.45%2C-37.25%2C175.15%2C-36.62&layer=mapnik' );

require_once get_theme_file_path( 'inc/settings.php' );
require_once get_theme_file_path( 'inc/enquiries.php' );
require_once get_theme_file_path( 'inc/fields.php' );
require_once get_theme_file_path( 'inc/duplicate.php' );
require_once get_theme_file_path( 'inc/setup-content.php' );

/* ---------- Theme basics ---------- */

add_action( 'after_setup_theme', function () {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'responsive-embeds' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	add_post_type_support( 'page', 'excerpt' );
} );

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'rc-fonts', 'https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=swap', array(), null );
	foreach ( array( 'rc-site' => 'assets/css/site.css', 'rc-wp' => 'wp.css' ) as $handle => $file ) {
		$path = get_theme_file_path( $file );
		wp_enqueue_style( $handle, get_theme_file_uri( $file ), array( 'rc-fonts' ), file_exists( $path ) ? filemtime( $path ) : RC_VERSION );
	}
	$js = get_theme_file_path( 'assets/js/site.js' );
	wp_enqueue_script( 'rc-site', get_theme_file_uri( 'assets/js/site.js' ), array(), file_exists( $js ) ? filemtime( $js ) : RC_VERSION, true );
} );

add_filter( 'wp_resource_hints', function ( $urls, $relation ) {
	if ( 'preconnect' === $relation ) {
		$urls[] = 'https://fonts.googleapis.com';
		$urls[] = array( 'href' => 'https://fonts.gstatic.com', 'crossorigin' );
	}
	return $urls;
}, 10, 2 );

/* Favicon from the theme, unless a Site Icon is set in Appearance → Customize. */
add_action( 'wp_head', function () {
	if ( has_site_icon() ) {
		return;
	}
	$u = rc_theme_uri() . '/assets/icons/';
	echo '<link rel="icon" href="' . esc_url( $u . 'favicon.ico' ) . '" sizes="48x48">' . "\n";
	echo '<link rel="icon" type="image/png" sizes="32x32" href="' . esc_url( $u . 'favicon-32.png' ) . '">' . "\n";
	echo '<link rel="apple-touch-icon" href="' . esc_url( $u . 'apple-touch-icon.png' ) . '">' . "\n";
}, 5 );

/* ---------- Page title and description ---------- */

$GLOBALS['rc_meta'] = array( 'title' => '', 'desc' => '' );

/** Set the browser title and meta description for the current template. */
function rc_meta( $title, $desc ) {
	$GLOBALS['rc_meta'] = array( 'title' => (string) $title, 'desc' => (string) $desc );
}

add_filter( 'pre_get_document_title', function ( $t ) {
	return $GLOBALS['rc_meta']['title'] ? $GLOBALS['rc_meta']['title'] : $t;
} );

add_action( 'wp_head', function () {
	if ( $GLOBALS['rc_meta']['desc'] ) {
		echo '<meta name="description" content="' . esc_attr( $GLOBALS['rc_meta']['desc'] ) . '">' . "\n";
	}
}, 2 );

/* ---------- Helpers used by the templates ---------- */

function rc_theme_uri() {
	return esc_url( get_template_directory_uri() );
}

/** A page by its path ("services/reroofing"), if it exists and is not in the bin. */
function rc_page( $path ) {
	$p = $path ? get_page_by_path( trim( $path, '/' ) ) : null;
	return ( $p && 'trash' !== $p->post_status ) ? $p : null;
}

/** URL of a page by path. Uses the real permalink when the page exists. Empty path is the home page. */
function rc_url( $path = '' ) {
	$path = trim( (string) $path, '/' );
	if ( '' === $path ) {
		return esc_url( home_url( '/' ) );
	}
	$p = rc_page( $path );
	if ( $p && 'publish' === $p->post_status ) {
		return esc_url( get_permalink( $p ) );
	}
	return esc_url( home_url( '/' . $path . '/' ) );
}

/**
 * href (and class) for a link to a page. Published pages link normally; drafts, or pages that
 * don't exist yet, become a disabled "soon" link, like the static preview.
 */
function rc_link( $path, $class = '' ) {
	$p = rc_page( $path );
	if ( $p && 'publish' === $p->post_status ) {
		return 'href="' . esc_url( get_permalink( $p ) ) . '"' . ( $class ? ' class="' . esc_attr( $class ) . '"' : '' );
	}
	return 'href="#" class="' . esc_attr( trim( $class . ' soon' ) ) . '"';
}

/** href/class for a page object. */
function rc_link_post( $p, $class = '' ) {
	if ( 'publish' === $p->post_status ) {
		return 'href="' . esc_url( get_permalink( $p ) ) . '"' . ( $class ? ' class="' . esc_attr( $class ) . '"' : '' );
	}
	return 'href="#" class="' . esc_attr( trim( $class . ' soon' ) ) . '"';
}

/**
 * Child pages of Services or Locations, in menu order. Drafts are included so they show as
 * "coming soon" (disabled) until they are published; private and binned pages are not.
 */
function rc_children( $parent_path ) {
	$parent = rc_page( $parent_path );
	if ( ! $parent ) {
		return array();
	}
	return get_posts( array(
		'post_type'      => 'page',
		'post_parent'    => $parent->ID,
		'post_status'    => array( 'publish', 'draft' ),
		'orderby'        => array( 'menu_order' => 'ASC', 'title' => 'ASC' ),
		'posts_per_page' => -1,
	) );
}

/** Menu links for the header dropdowns ($li = false) or the footer lists ($li = true). */
function rc_menu( $parent_path, $li = false ) {
	foreach ( rc_children( $parent_path ) as $p ) {
		$a = '<a ' . rc_link_post( $p ) . '>' . esc_html( get_the_title( $p ) ) . '</a>';
		echo $li ? '<li>' . $a . '</li>' : $a; // phpcs:ignore WordPress.Security.EscapeOutput
	}
}

/** aria-current for the nav: the page itself, or any page under it. */
function rc_current( $path ) {
	if ( ! is_page() ) {
		return '';
	}
	$p = rc_page( $path );
	if ( ! $p ) {
		return '';
	}
	$id = get_queried_object_id();
	return ( $id === $p->ID || in_array( $p->ID, get_post_ancestors( $id ), true ) ) ? ' aria-current="page"' : '';
}

/** SVG icon by name (home, build, wrench, drop, search, shield, ...). */
function rc_icon( $name ) {
	static $icons = null;
	if ( null === $icons ) {
		$icons = require get_theme_file_path( 'parts/icons.php' );
	}
	return isset( $icons[ $name ] ) ? $icons[ $name ] : $icons['home'];
}

/** A text field saved on a page (see inc/fields.php). */
function rc_field( $key, $post = null ) {
	return (string) get_post_meta( $post ? $post : get_the_ID(), '_' . $key, true );
}

/** Lines of a textarea field, trimmed, without empty lines. */
function rc_lines( $key, $post = null ) {
	return array_values( array_filter( array_map( 'trim', preg_split( '/\r\n|\r|\n/', rc_field( $key, $post ) ) ) ) );
}

/** Short card text for a page: its excerpt. */
function rc_blurb( $p ) {
	return $p->post_excerpt ? $p->post_excerpt : wp_trim_words( wp_strip_all_tags( $p->post_content ), 24 );
}

/** The services grid (home page and Services page), built from the Services child pages. */
function rc_services_grid( $wide = false ) {
	$all = rc_children( 'services' );
	if ( ! $all ) {
		return;
	}
	$feature = $all[0];
	foreach ( $all as $p ) {
		if ( 'reroofing' === $p->post_name ) {
			$feature = $p;
		}
	}
	$others = '';
	foreach ( $all as $p ) {
		if ( $p->ID === $feature->ID ) {
			continue;
		}
		$others .= '<article class="card"><div class="icon">' . rc_icon( rc_field( 'rc_icon', $p ) ) . '</div><h3>' . esc_html( get_the_title( $p ) ) . '</h3><p>' . esc_html( rc_blurb( $p ) ) . '</p><a ' . rc_link_post( $p, 'link' ) . '>Learn more →</a></article>';
	}
	$img = has_post_thumbnail( $feature ) ? get_the_post_thumbnail_url( $feature, 'large' ) : rc_theme_uri() . '/assets/img/colorsteel-installed.jpg';
	$f   = '<article class="card feature"><div class="feature-img"><img src="' . esc_url( $img ) . '" alt="' . esc_attr( get_the_title( $feature ) ) . ' by The Roof Crew" loading="lazy"></div>'
		. '<div class="body"><span class="badge">Most requested</span><h3 style="font-size:26px">' . esc_html( get_the_title( $feature ) ) . '</h3><p>' . esc_html( rc_blurb( $feature ) ) . '</p>'
		. '<a ' . rc_link_post( $feature, 'btn btn-primary' ) . '>See ' . esc_html( strtolower( get_the_title( $feature ) ) ) . ' →</a></div></article>';
	if ( $wide ) {
		echo '<div class="services services-wide">' . $f . '</div>' . ( $others ? '<div class="grid-4" style="margin-top:20px">' . $others . '</div>' : '' ); // phpcs:ignore WordPress.Security.EscapeOutput
	} else {
		echo '<div class="services">' . $others . $f . '</div>'; // phpcs:ignore WordPress.Security.EscapeOutput
	}
}

/** Region buttons on the home page. */
function rc_region_links() {
	foreach ( rc_children( 'locations' ) as $p ) {
		echo '<a ' . rc_link_post( $p ) . '>' . esc_html( get_the_title( $p ) ) . ' <span aria-hidden="true">→</span></a>'; // phpcs:ignore WordPress.Security.EscapeOutput
	}
}

/** Region cards on the Locations page. */
function rc_region_cards() {
	foreach ( rc_children( 'locations' ) as $p ) {
		$live = 'publish' === $p->post_status;
		echo '<a class="card region-card" ' . preg_replace( '/^href="#" class="soon"$/', 'href="#"', rc_link_post( $p ) ) . ( $live ? '' : ' data-soon' ) . '><h3>' . esc_html( get_the_title( $p ) ) . '</h3><small>' . esc_html( rc_blurb( $p ) ) . '</small><span class="link" style="margin-top:8px">' . ( $live ? 'See ' . esc_html( get_the_title( $p ) ) : 'Page coming' ) . ' →</span></a>'; // phpcs:ignore WordPress.Security.EscapeOutput
	}
}

/** Hero section shared by the Service, Location and other page templates. */
function rc_hero( $img, $eyebrow, $h1, $lede, $actions = true ) {
	?>
<section class="hero page-hero"><div class="hero-bg" style="background-image:url('<?php echo esc_url( $img ); ?>')"></div>
<div class="wrap"><div>
  <span class="eyebrow"><?php echo wp_kses_post( $eyebrow ); ?></span><h1><?php echo esc_html( $h1 ); ?></h1><?php if ( $lede ) : ?><p class="lede"><?php echo esc_html( $lede ); ?></p><?php endif; ?>
  <?php if ( $actions ) : ?><div class="hero-actions"><a class="btn btn-primary" href="<?php echo rc_url( 'quote' ); ?>">Get my free quote →</a><a class="btn btn-outline-light" href="tel:<?php echo esc_attr( RC_TEL ); ?>">Call or text Mike · <?php echo esc_html( RC_PHONE ); ?></a></div><?php endif; ?>
</div></div></section>
	<?php
}

/** Featured image URL of the current page, or a default image from the theme. */
function rc_image( $default ) {
	return has_post_thumbnail() ? get_the_post_thumbnail_url( null, 'full' ) : rc_theme_uri() . '/assets/img/' . $default;
}

/* ---------- Quote forms ---------- */

/** True after a successful quote request from the form with this id. */
function rc_sent( $form_id ) {
	return isset( $_GET['sent'] ) && sanitize_key( wp_unslash( $_GET['sent'] ) ) === sanitize_key( $form_id ); // phpcs:ignore WordPress.Security.NonceVerification
}

/** ", Jane" for the thank-you message. */
function rc_sent_name() {
	$n = isset( $_GET['n'] ) ? sanitize_text_field( wp_unslash( $_GET['n'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification
	return $n ? ', ' . esc_html( $n ) : '';
}

/** Opening tag and hidden fields of a quote form. */
function rc_form_open( $form_id ) {
	$back = is_singular() ? get_permalink() : home_url( '/' );
	echo '<form class="form" method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '">';
	echo '<input type="hidden" name="action" value="rc_quote">';
	echo '<input type="hidden" name="back" value="' . esc_url( $back ) . '">';
	echo '<input type="hidden" name="form_id" value="' . esc_attr( $form_id ) . '">';
	wp_nonce_field( 'rc_quote', 'rc_nonce' );
}

/* ---------- Old addresses from the current theroofcrew.co.nz site ---------- */

add_action( 'template_redirect', function () {
	if ( ! is_404() ) {
		return;
	}
	$map  = array(
		'replacement-roofs'      => 'services/reroofing',
		'new-build-roofing'      => 'services/new-roof-installation',
		'fascia-spouting-safety' => 'services/guttering-and-downpipes',
		'contact-us'             => 'contact',
		'roofing-faqs'           => 'services/reroofing',
		'products'               => '#options',
		'metal-tile-roofing'     => '#options',
		'concrete-tile-roofing'  => '#options',
		'colour-steel-roofing'   => '#options',
	);
	$path = trim( (string) wp_parse_url( isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '', PHP_URL_PATH ), '/' ); // phpcs:ignore WordPress.Security.ValidatedSanitizedInput
	$slug = basename( $path );
	if ( isset( $map[ $slug ] ) ) {
		$to = $map[ $slug ];
		$p  = '#' === $to[0] ? null : rc_page( $to );
		if ( '#' === $to[0] ) {
			wp_safe_redirect( home_url( '/' ) . $to, 301 );
			exit;
		}
		if ( $p && 'publish' === $p->post_status ) {
			wp_safe_redirect( get_permalink( $p ), 301 );
			exit;
		}
		wp_safe_redirect( home_url( '/' ), 302 );
		exit;
	}
} );
