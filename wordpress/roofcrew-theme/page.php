<?php
/* Any other page (privacy policy, terms, a new page): the editor content in the site's layout. */
the_post();
rc_meta( get_the_title() . ' | The Roof Crew', wp_strip_all_tags( get_the_excerpt() ) );
get_header();
rc_hero( rc_image( 'bg-local-street.jpg' ), 'The Roof Crew', get_the_title(), '', false );
?>
<section><div class="wrap"><div class="prose page-content entry"><?php the_content(); ?></div></div></section>
<?php
get_footer();
