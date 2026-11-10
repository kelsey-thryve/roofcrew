<?php
/* Services (all services). Generated from the v2 design by tools/build_wp_theme.py: edit the generator, not this file. */
rc_meta( "Roofing Services Auckland | The Roof Crew", "Reroofing, new roofs, repairs, guttering and roof inspections across Auckland, from one family-owned crew. Free site visits and fixed quotes." );
get_header(); ?>

<section class="hero page-hero"><div class="hero-bg" style="background-image:url('<?php echo rc_theme_uri(); ?>/assets/img/bg-colorsteel.jpg')"></div>
<div class="wrap"><div>
  <span class="eyebrow">Services</span><h1>Roofing services for Auckland homes</h1><p class="lede">Most of our work is full roof replacement, but we look after the rest of your roof too. Whichever job you need, the same family crew quotes it, does it and guarantees it.</p>
  <div class="hero-actions"><a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my free quote →</a><a class="btn btn-outline-light" href="tel:+6421903822">Call or text Mike · 021 903 822</a></div>
</div></div></section>
<section><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">What we do</span><h2>Our services</h2></div></div>
  <?php rc_services_grid(true); ?>
</div></section>
<section class="alt"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Roofing options</span><h2>Roofing materials</h2></div></div>
  <div class="grid-3"><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-installed.jpg" alt="COLORSTEEL® long-run roof" loading="lazy"></div><div class="body"><h3>COLORSTEEL® roofing</h3><p>This is the long-run steel you see on homes all over New Zealand, and it's our most popular option. There's a huge range of colours and profiles, including options made for coastal areas.</p><a <?php echo rc_link('colour-steel-roofing', 'link'); ?>>Learn more →</a></div></article><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/hero-metal-tile.jpg" alt="Gerard metal tile roof" loading="lazy"></div><div class="body"><h3>Metal tile roofing</h3><p>Metal tiles give you the look of a tiled roof at a fraction of the weight. They're a popular way to replace an old tile roof without losing its character.</p><a <?php echo rc_link('metal-tile-roofing', 'link'); ?>>Learn more →</a></div></article><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/concrete-tile.jpg" alt="Concrete tile roof" loading="lazy"></div><div class="body"><h3>Concrete tile replacement</h3><p>We specialise in converting existing concrete tile roofs to modern long-run COLORSTEEL® or metal tile.</p><a <?php echo rc_link('concrete-tile-roofing', 'link'); ?>>Learn more →</a></div></article></div>
</div></section>
<section><div class="wrap"><div class="card unsure" style="margin:0">
  <div><h3>Not sure what you need?</h3><p>Call or text Mike on 021 903 822. He'll talk you through it, with no jargon and no pressure.</p></div>
  <div class="acts"><a <?php echo rc_link('services/roof-inspections', 'link'); ?>>Book an inspection →</a><a class="btn btn-primary" href="tel:+6421903822"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg> Call Mike · 021 903 822</a></div>
</div></div></section>
<section id="request"><div class="wrap closing">
  <div>
    <span class="eyebrow">Request a quote</span>
    <h2>Your roof, your real number.</h2>
    <p class="lede">Tell us a bit about your property and Mike will get back to you personally.</p>
    <ol class="steps">
      <li><span class="n">1</span><div><b>Send your details</b><span>Takes about a minute, or just call or text.</span></div></li>
      <li><span class="n">2</span><div><b>Mike gets in touch</b><span>We aim to respond within 3 hours and usually visit within the next working day.</span></div></li>
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
    <p class="full fine">Mike will call you back personally. No sales pressure. <a href="<?php echo rc_url('privacy-policy'); ?>">Privacy policy</a></p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks<?php echo rc_sent_name(); ?>.</strong>Mike will be in touch to book your free site visit.</div>
</div>
</div></section>
<?php get_footer();
