<?php
/**
 * Template Name: Location page
 *
 * For pages under Locations. Text comes from the editor and the "Page details" box,
 * the hero photo from the Featured image, the card text from the Excerpt.
 */

the_post();
$title = get_the_title();
$h1    = rc_field( 'rc_h1' ) ? rc_field( 'rc_h1' ) : 'Reroofing in ' . $title;
rc_meta( $h1 . ' | The Roof Crew', wp_strip_all_tags( get_the_excerpt() ) );
get_header();

$parent = wp_get_post_parent_id( get_the_ID() );
$crumb  = $parent ? '<a href="' . esc_url( get_permalink( $parent ) ) . '" style="color:inherit">' . esc_html( get_the_title( $parent ) ) . '</a> / ' . esc_html( $title ) : esc_html( $title );
rc_hero( rc_image( 'bg-sunset.jpg' ), $crumb, $h1, rc_field( 'rc_lede' ) );

$suburbs = rc_lines( 'rc_suburbs' );
$map     = rc_field( 'rc_map' ) ? rc_field( 'rc_map' ) : RC_MAP_AUCKLAND;
?>
<section><div class="wrap split">
  <div class="prose"><span class="eyebrow">Roofing in <?php echo esc_html( $title ); ?></span><h2 style="margin-bottom:18px"><?php echo esc_html( rc_field( 'rc_intro_heading' ) ? rc_field( 'rc_intro_heading' ) : 'Your local reroofing crew.' ); ?></h2>
    <div class="entry"><?php the_content(); ?></div></div>
  <div class="photo" style="min-height:360px"><img src="<?php echo esc_url( rc_image( 'bg-sunset.jpg' ) ); ?>" alt="Roof in <?php echo esc_attr( $title ); ?>" loading="lazy"></div>
</div></section>

<section class="alt"><div class="wrap">
  <span class="eyebrow">Services</span><h2 style="margin-bottom:32px">What we do in <?php echo esc_html( $title ); ?></h2>
  <div class="grid-3">
  <?php foreach ( rc_children( 'services' ) as $p ) : ?>
    <article class="card"><div class="icon"><?php echo rc_icon( rc_field( 'rc_icon', $p ) ); // phpcs:ignore ?></div><h3><?php echo esc_html( get_the_title( $p ) ); ?></h3><a <?php echo rc_link_post( $p, 'link' ); // phpcs:ignore ?>><?php echo esc_html( get_the_title( $p ) . ' in ' . $title ); ?> →</a></article>
  <?php endforeach; ?>
  </div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">What Auckland homeowners say</h2>
  <?php get_template_part( 'parts/reviews' ); ?>
</div></section>

<section class="alt"><div class="wrap areas" style="align-items:start">
  <div><span class="eyebrow">Suburbs we cover</span><h2><?php echo esc_html( $title ); ?> suburbs</h2>
    <p class="lede">Don't see yours? We probably still cover it, just ask.</p>
    <?php if ( $suburbs ) : ?><div class="suburbs"><?php foreach ( $suburbs as $s ) : ?><span><?php echo esc_html( $s ); ?></span><?php endforeach; ?></div><?php endif; ?></div>
  <div class="map"><iframe title="Map of <?php echo esc_attr( $title ); ?>" src="<?php echo esc_url( $map ); ?>" loading="lazy"></iframe></div>
</div></section>

<?php get_template_part( 'parts/closing', null, array( 'heading' => 'Get a free quote in ' . $title . '.' ) ); ?>
<?php
get_footer();
