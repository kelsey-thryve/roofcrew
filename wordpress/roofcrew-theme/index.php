<?php
/* Fallback for posts and archives. */
get_header();
rc_hero( rc_theme_uri() . '/assets/img/bg-local-street.jpg', 'The Roof Crew', is_singular() ? get_the_title() : wp_strip_all_tags( get_the_archive_title() ), '', false );
?>
<section><div class="wrap"><div class="prose page-content entry">
<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
  <article style="margin-bottom:40px">
    <?php if ( ! is_singular() ) : ?><h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2><?php endif; ?>
    <?php is_singular() ? the_content() : the_excerpt(); ?>
  </article>
<?php endwhile; else : ?>
  <p>Nothing here yet.</p>
<?php endif; ?>
</div></div></section>
<?php
get_footer();
