<?php
/**
 * Template Name: Location page
 *
 * For region and area pages (children of Locations, or top-level pages in the Locations group such
 * as /roofers-in-pukekohe/). The editor text before the first H2 is the local section; each H2
 * (e.g. a cost section) starts its own section further down. Other text comes from the
 * "Page details" box. The hero photo is the Featured image, the card text is the Excerpt.
 */

the_post();
$title = get_the_title();
$h1    = rc_field( 'rc_h1' ) ? rc_field( 'rc_h1' ) : 'Reroofing in ' . $title;
rc_meta( rc_field( 'rc_meta_title' ) ? rc_field( 'rc_meta_title' ) : wp_strip_all_tags( $h1 ) . ' | The Roof Crew', rc_field( 'rc_meta_desc' ) ? rc_field( 'rc_meta_desc' ) : wp_strip_all_tags( get_the_excerpt() ) );
get_header();

$group = rc_group_page();
$crumb = $group ? '<a href="' . esc_url( get_permalink( $group ) ) . '" style="color:inherit">' . esc_html( get_the_title( $group ) ) . '</a> / ' . esc_html( $title ) : esc_html( $title );
rc_hero( rc_image( 'bg-sunset.jpg' ), $crumb, $h1, rc_field( 'rc_lede' ) );

list( $intro, $sections ) = rc_sections( apply_filters( 'the_content', get_the_content() ) );
list( $chips, $linked )   = rc_suburb_chips();
$map = rc_field( 'rc_map' ) ? rc_field( 'rc_map' ) : RC_MAP_AUCKLAND;
?>
<section><div class="wrap split">
  <div class="prose"><span class="eyebrow">Roofing in <?php echo esc_html( $title ); ?></span><h2 style="margin-bottom:18px"><?php echo wp_kses_post( rc_field( 'rc_intro_heading' ) ? rc_field( 'rc_intro_heading' ) : 'Your local reroofing crew.' ); ?></h2>
    <div class="entry"><?php echo $intro; // phpcs:ignore WordPress.Security.EscapeOutput ?></div></div>
  <?php if ( rc_field( 'rc_job' ) ) : ?>
  <div class="ph-box ph-job"><?php echo wp_kses_post( rc_field( 'rc_job' ) ); ?></div>
  <?php else : ?>
  <div class="photo" style="min-height:360px"><img src="<?php echo esc_url( rc_photo( 'bg-sunset.jpg' ) ); ?>" alt="Roof in <?php echo esc_attr( $title ); ?>" loading="lazy"></div>
  <?php endif; ?>
</div></section>

<section class="alt"><div class="wrap">
  <span class="eyebrow">Services</span><h2 style="margin-bottom:32px">What we do in <?php echo esc_html( $title ); ?></h2>
  <div class="grid-3">
  <?php foreach ( rc_children( 'services', 'service' ) as $p ) : ?>
    <article class="card"><div class="icon"><?php echo rc_icon( rc_field( 'rc_icon', $p ) ); // phpcs:ignore ?></div><h3><?php echo esc_html( get_the_title( $p ) ); ?></h3><a <?php echo rc_link_post( $p, 'link' ); // phpcs:ignore ?>><?php echo esc_html( get_the_title( $p ) . ' in ' . $title ); ?> →</a></article>
  <?php endforeach; ?>
  </div>
</div></section>

<?php $alt = rc_print_sections( $sections, 'Cost', false ); ?>
<section<?php echo $alt ? ' class="alt"' : ''; ?>><div class="wrap">
  <span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">What Auckland homeowners say</h2>
  <?php get_template_part( rc_field( 'rc_review' ) ? 'parts/reviews-local' : 'parts/reviews' ); ?>
</div></section>
<?php $alt = rc_faq_section( rc_field( 'rc_faq_title' ) ? rc_field( 'rc_faq_title' ) : $title . ' questions', ! $alt ); ?>

<section<?php echo $alt ? ' class="alt"' : ''; ?>><div class="wrap areas" style="align-items:start">
  <div><span class="eyebrow">Suburbs we cover</span><h2><?php echo esc_html( $title ); ?> suburbs</h2>
    <p class="lede"><?php echo $linked ? 'Highlighted suburbs have their own page. ' : ''; ?>Don't see yours? We probably still cover it, just ask.</p>
    <?php if ( $chips ) : ?><div class="suburbs"><?php echo $chips; // phpcs:ignore WordPress.Security.EscapeOutput ?></div><?php endif; ?></div>
  <div class="map"><iframe title="Map of <?php echo esc_attr( $title ); ?>" src="<?php echo esc_url( $map ); ?>" loading="lazy"></iframe></div>
</div></section>

<?php get_template_part( 'parts/closing', null, array( 'heading' => 'Get a free quote in ' . $title . '.' ) ); ?>
<?php
get_footer();
