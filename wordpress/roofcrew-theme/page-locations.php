<?php
/* Locations (all areas). Generated from the v2 design by tools/build_wp_theme.py: edit the generator, not this file. */
rc_meta( "Areas we cover in Auckland | The Roof Crew", "The Roof Crew reroofs homes in East Auckland, the North Shore, South Auckland and West Auckland." );
get_header(); ?>

<section class="hero page-hero"><div class="hero-bg" style="background-image:url('<?php echo rc_theme_uri(); ?>/assets/img/bg-local-street.jpg')"></div>
<div class="wrap"><div>
  <span class="eyebrow">Locations</span><h1>Roofing across Auckland</h1><p class="lede">The same family crew and the same standard on every roof, from the North Shore to Pukekohe.</p>
  <div class="hero-actions"><a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my free quote →</a><a class="btn btn-outline-light" href="tel:+6421903822">Call or text Mike · 021 903 822</a></div>
</div></div></section>
<section><div class="wrap">
  <span class="eyebrow">Areas we cover</span><h2 style="margin-bottom:32px">Find your region.</h2>
  <div class="grid-4"><?php rc_region_cards(); ?></div>
</div></section>
<section class="alt"><div class="wrap areas" style="align-items:start">
  <div><span class="eyebrow">Service area</span><h2>All over Auckland.</h2><p class="lede">Not sure if you're on our patch? Call or text Mike on 021 903 822 and he'll tell you straight.</p>
    <p style="margin-top:22px"><a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my free quote →</a></p></div>
  <div class="map"><iframe title="Map of Auckland service area" src="https://www.openstreetmap.org/export/embed.html?bbox=174.45%2C-37.25%2C175.15%2C-36.62&layer=mapnik" loading="lazy"></iframe></div>
</div></section>
<section id="request"><div class="wrap closing">
  <div>
    <span class="eyebrow">Request a quote</span>
    <h2>Your roof, your real number.</h2>
    <p class="lede">Tell us a bit about your property and Mike will get back to you personally.</p>
    <ol class="steps">
      <li><span class="n">1</span><div><b>Send your details</b><span>Takes about a minute, or just call or text.</span></div></li>
      <li><span class="n">2</span><div><b>Mike gets in touch</b><span>Usually with a site visit within 3 working days.</span></div></li>
      <li><span class="n">3</span><div><b>A clear, itemised quote</b><span>Fixed, transparent and no pressure.</span></div></li>
    </ol>
    <div class="contact-box"><a href="tel:+6421903822"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg> 021 903 822</a><a href="mailto:mike@theroofcrew.co.nz"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg> mike@theroofcrew.co.nz</a></div>
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
    <p class="full fine">Mike will call you back personally. No sales pressure.</p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks<?php echo rc_sent_name(); ?>.</strong>Mike will be in touch to book your free site visit.</div>
</div>
</div></section>
<?php get_footer();
