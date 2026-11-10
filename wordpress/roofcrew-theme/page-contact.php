<?php
/* Contact page. Generated from the v2 design by tools/build_wp_theme.py: edit the generator, not this file. */
rc_meta( "Contact The Roof Crew | Free roof quotes in Auckland", "Call or text Mike on 021 903 822, or send your details for a free, no-pressure roof quote." );
get_header(); ?>

<section class="hero page-hero" style="padding-block:56px 64px"><div class="hero-bg" style="background-image:url('<?php echo rc_theme_uri(); ?>/assets/img/bg-local-street.jpg')"></div>
<div class="wrap"><div><span class="eyebrow">Contact</span><h1>Talk to Mike.</h1><p class="lede">Call, text or send your details and Mike will get back to you personally.</p></div></div></section>
<section><div class="wrap closing">
  <div><h2>Get in touch</h2>
    <div class="contact-box" style="margin-top:24px"><a href="tel:+6421903822"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg> 021 903 822</a><a href="mailto:mike@theroofcrew.co.nz"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg> mike@theroofcrew.co.nz</a><span>Hours: Mon to Fri 8am to 6pm, Sat 9am to 1pm, Sun closed</span></div>
    <h3 style="margin-top:36px">Areas we cover</h3>
    <div class="suburbs"><a <?php echo rc_link('locations/east-auckland'); ?>>East Auckland</a><a <?php echo rc_link('locations/north-shore'); ?>>North Shore</a><a <?php echo rc_link('locations/south-auckland'); ?>>South Auckland</a><a <?php echo rc_link('locations/west-auckland'); ?>>West Auckland</a></div>
    <p style="margin-top:14px;font-size:15px;color:var(--gray-500)">We come to you. No street address is listed because the crew works on site across Auckland.</p>
  </div>
  <div class="quote-card<?php echo rc_sent( 'get-quote' ) ? ' is-sent' : ''; ?>" id="get-quote">
  <h2>Get your free quote</h2><p class="sub">Free and no pressure.</p>
  <?php rc_form_open('get-quote'); ?>
    <div><label for="get-quote-name">Name</label><input id="get-quote-name" name="name" autocomplete="name" required></div>
    <div><label for="get-quote-phone">Phone</label><input id="get-quote-phone" name="phone" type="tel" autocomplete="tel" required></div>
    <div class="full"><label for="get-quote-email">Email</label><input id="get-quote-email" name="email" type="email" autocomplete="email"></div>
    <div class="full"><label for="get-quote-addr">Suburb or address</label><input id="get-quote-addr" name="address" autocomplete="street-address"></div>
    <div class="full"><label for="get-quote-need">What's going on with your roof?</label><select id="get-quote-need" name="need"><option selected>New roof (reroof)</option><option>Leaks keep coming back</option><option>Not sure, please check it</option><option>Roof repair</option><option>Spouting or downpipes</option><option>Inspection or report</option><option>New build roof</option></select></div>
    <div class="full"><label for="get-quote-msg">Anything else? (optional)</label><textarea id="get-quote-msg" name="message"></textarea></div>
    <div class="full"><button class="btn btn-primary btn-block" type="submit">Get my free quote →</button></div>
    <div class="full hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
    <p class="full fine">Mike will call you back personally. No sales pressure. <a href="<?php echo rc_url('privacy-policy'); ?>">Privacy policy</a></p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks<?php echo rc_sent_name(); ?>.</strong>Mike will be in touch to book your free site visit.</div>
</div>
</div></section>
<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">What happens next</h2><div class="faqs"><details open><summary>What happens after I get in touch?</summary><p>We aim to respond within 3 hours. Mike calls you back personally, asks a few questions and books a free site visit, usually within the next working day.</p></details><details><summary>Is the quote really free?</summary><p>Yes. The site visit and quote are free, with no obligation and no sales pressure.</p></details><details><summary>Do you cover my area?</summary><p>We cover the wider Auckland region, from Whangaparāoa and the North Shore to West, East and South Auckland, and down to Pukekohe, Franklin and south of the Bombay Hills. If you're not sure, just ask.</p></details></div></div></section>
<?php get_footer();
