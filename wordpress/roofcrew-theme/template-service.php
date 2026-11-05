<?php
/**
 * Template Name: Service page
 *
 * For pages under Services. Text comes from the editor and the "Page details" box,
 * the hero photo from the Featured image, the card text from the Excerpt.
 */

the_post();
$title  = get_the_title();
$h1     = rc_field( 'rc_h1' ) ? rc_field( 'rc_h1' ) : $title . ' in Auckland';
$reroof = '1' === rc_field( 'rc_reroof' );
rc_meta( $h1 . ' | The Roof Crew', wp_strip_all_tags( get_the_excerpt() ) );
get_header();

$parent = wp_get_post_parent_id( get_the_ID() );
$crumb  = $parent ? '<a href="' . esc_url( get_permalink( $parent ) ) . '" style="color:inherit">' . esc_html( get_the_title( $parent ) ) . '</a> / ' . esc_html( $title ) : esc_html( $title );
rc_hero( rc_image( 'hero-metal-tile.jpg' ), $crumb, $h1, rc_field( 'rc_lede' ) );

$included = rc_lines( 'rc_included' );
?>
<section><div class="wrap split">
  <div>
    <span class="eyebrow"><?php echo $reroof ? "What's included" : esc_html( $title ); ?></span>
    <?php if ( rc_field( 'rc_intro_heading' ) ) : ?><h2 style="margin-bottom:18px"><?php echo esc_html( rc_field( 'rc_intro_heading' ) ); ?></h2><?php endif; ?>
    <div class="prose entry"><?php the_content(); ?></div>
    <?php if ( $included ) : ?><ul class="ticks"><?php foreach ( $included as $i ) : ?><li><?php echo esc_html( $i ); ?></li><?php endforeach; ?></ul><?php endif; ?>
  </div>
  <div class="photo" style="min-height:420px"><img src="<?php echo esc_url( rc_image( 'colorsteel-installed.jpg' ) ); ?>" alt="<?php echo esc_attr( $title ); ?> by The Roof Crew" loading="lazy"></div>
</div></section>

<?php if ( $reroof ) : ?>
<section class="alt"><div class="wrap">
  <span class="eyebrow">When you need it</span><h2>Signs it's time for a new roof</h2>
  <div class="card" style="margin-top:28px"><?php get_template_part( 'parts/signs' ); ?></div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">How it works</span><h2 style="margin-bottom:32px">How a reroof works</h2>
  <div class="grid-3">
    <div class="card"><div class="icon"><?php echo rc_icon( 'search' ); // phpcs:ignore ?></div><h3>1. Free site visit</h3><p>We measure up and check what's underneath, usually within 3 working days.</p></div>
    <div class="card"><div class="icon"><?php echo rc_icon( 'build' ); // phpcs:ignore ?></div><h3>2. Clean install</h3><p>Scaffold up, old roof off, new roof on, with a tidy site at the end of every day.</p></div>
    <div class="card"><div class="icon"><?php echo rc_icon( 'shield' ); // phpcs:ignore ?></div><h3>3. Sign-off and guarantee</h3><p>A final check together, then your workmanship and product guarantees.</p></div>
  </div>
</div></section>
<section class="alt" id="options"><div class="wrap">
  <span class="eyebrow">Options and price ranges</span><h2 style="margin-bottom:32px">Choose your roof.</h2>
  <?php get_template_part( 'parts/systems' ); ?>
  <?php get_template_part( 'parts/pricing' ); ?>
</div></section>
<section id="work"><div class="wrap ba-wrap">
  <div class="ba-side"><div><span class="eyebrow">Project photos</span><h2>A real Auckland reroof.</h2><p class="lede">Drag the slider to compare.</p></div>
    <?php get_template_part( 'parts/review-one' ); ?></div>
  <?php get_template_part( 'parts/before-after' ); ?>
</div></section>
<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">Questions people ask us</h2><?php get_template_part( 'parts/faqs' ); ?></div></section>
<?php get_template_part( 'parts/faq-schema' ); ?>
<?php endif; ?>

<?php
$others = array_filter( rc_children( 'services' ), function ( $p ) {
	return $p->ID !== get_the_ID();
} );
if ( $others ) :
	?>
<section<?php echo $reroof ? '' : ' class="alt"'; ?>><div class="wrap">
  <div class="card"><h3>Other services</h3><ul class="ticks"><?php foreach ( $others as $p ) : ?><li><a <?php echo rc_link_post( $p, 'link' ); // phpcs:ignore ?>><?php echo esc_html( get_the_title( $p ) ); ?></a></li><?php endforeach; ?></ul></div>
</div></section>
<?php endif; ?>

<?php get_template_part( 'parts/closing', null, array( 'heading' => $reroof ? 'Get a fixed price for your new roof.' : 'Get your free quote.' ) ); ?>
<?php
get_footer();
