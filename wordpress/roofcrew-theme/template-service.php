<?php
/**
 * Template Name: Service page
 *
 * For service and roofing material pages (children of Services, or top-level pages in the Services
 * group such as /colour-steel-roofing/). Text comes from the editor and the "Page details" box: the
 * editor text before the first H2 sits beside the photo, and each H2 starts its own section.
 * The hero photo is the Featured image, the card text is the Excerpt.
 */

the_post();
$title  = get_the_title();
$h1     = rc_field( 'rc_h1' ) ? rc_field( 'rc_h1' ) : $title . ' in Auckland';
$reroof = '1' === rc_field( 'rc_reroof' );
rc_meta( rc_field( 'rc_meta_title' ) ? rc_field( 'rc_meta_title' ) : wp_strip_all_tags( $h1 ) . ' | The Roof Crew', rc_field( 'rc_meta_desc' ) ? rc_field( 'rc_meta_desc' ) : wp_strip_all_tags( get_the_excerpt() ) );
get_header();

$group = rc_group_page();
$crumb = $group ? '<a href="' . esc_url( get_permalink( $group ) ) . '" style="color:inherit">' . esc_html( get_the_title( $group ) ) . '</a> / ' . esc_html( $title ) : esc_html( $title );
rc_hero( rc_image( 'hero-metal-tile.jpg' ), $crumb, $h1, rc_field( 'rc_lede' ) );
if ( rc_field( 'rc_hold' ) ) {
	echo '<div class="hold-note"><div class="wrap">' . wp_kses_post( rc_field( 'rc_hold' ) ) . '</div></div>';
}

list( $intro, $sections ) = rc_sections( apply_filters( 'the_content', get_the_content() ) );
$included = rc_lines( 'rc_included' );
$alt      = false;
if ( trim( wp_strip_all_tags( $intro ) ) || $included || rc_field( 'rc_intro_heading' ) ) :
	$alt = true;
	?>
<section><div class="wrap split">
  <div>
    <span class="eyebrow"><?php echo esc_html( $title ); ?></span>
	<?php if ( rc_field( 'rc_intro_heading' ) ) : ?><h2 style="margin-bottom:18px"><?php echo wp_kses_post( rc_field( 'rc_intro_heading' ) ); ?></h2><?php endif; ?>
    <div class="prose entry"><?php echo $intro; // phpcs:ignore WordPress.Security.EscapeOutput ?></div>
	<?php if ( $included ) : ?><ul class="ticks"><?php foreach ( $included as $i ) : ?><li><?php echo esc_html( $i ); ?></li><?php endforeach; ?></ul><?php endif; ?>
  </div>
  <div class="photo" style="min-height:420px"><img src="<?php echo esc_url( rc_photo( 'colorsteel-installed.jpg' ) ); ?>" alt="<?php echo esc_attr( $title ); ?> by The Roof Crew" loading="lazy"></div>
</div></section>
	<?php
endif;

if ( $reroof ) {
	get_template_part( 'parts/reroof-extra' );
	$alt = false;
}
$alt = rc_print_sections( $sections, esc_html( $title ), $alt );
$alt = rc_faq_section( rc_field( 'rc_faq_title' ) ? rc_field( 'rc_faq_title' ) : 'Questions people ask us', $alt );

$others = array_filter( rc_children( 'services' ), function ( $p ) {
	return get_the_ID() !== $p->ID;
} );
if ( $others ) :
	?>
<section<?php echo $alt ? ' class="alt"' : ''; ?>><div class="wrap">
  <div class="card"><h3>Other services</h3><ul class="ticks cols-2"><?php foreach ( $others as $p ) : ?><li><a <?php echo rc_link_post( $p, 'link' ); // phpcs:ignore ?>><?php echo esc_html( get_the_title( $p ) ); ?></a></li><?php endforeach; ?></ul></div>
</div></section>
<?php endif; ?>

<?php get_template_part( 'parts/closing', null, array( 'heading' => rc_field( 'rc_closing' ) ? rc_field( 'rc_closing' ) : 'Get your free quote.' ) ); ?>
<?php
get_footer();
