<?php
/* Free quote page. Generated from the v2 design by tools/build_wp_theme.py: edit the generator, not this file. */
rc_meta( "Get a free roof quote | The Roof Crew", "Free, no-pressure reroof and repair quotes across Auckland. Send your details and Mike gets back to you with a fixed price." );
get_header(); ?>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "What happens after I send my details?", "acceptedAnswer": {"@type": "Answer", "text": "We aim to respond within 3 hours. Mike calls you back personally, asks a few questions about your roof and books a free site visit, usually within the next working day."}}, {"@type": "Question", "name": "Is the quote really free?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The site visit and quote are free, with no obligation and no sales pressure."}}, {"@type": "Question", "name": "Will the price change later?", "acceptedAnswer": {"@type": "Answer", "text": "No. After the site visit you get a fixed, itemised price, so there are no surprises."}}, {"@type": "Question", "name": "Do you do repairs as well as reroofs?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Whether it's one leak or a whole new roof, use the same form and tell us what's going on."}}]}</script>
<section class="hero page-hero" style="padding-block:56px 64px"><div class="hero-bg" style="background-image:url('<?php echo rc_theme_uri(); ?>/assets/img/hero-metal-tile.jpg')"></div>
<div class="wrap"><div><span class="eyebrow">Free quote</span><h1>Get your free roof quote.</h1><p class="lede">Reroof or repair, tell us about your roof and Mike will get back to you personally with a fixed price.</p>
<div class="chips" style="margin-top:22px"><span class="chip rating"><svg width="18" height="18" viewBox="0 0 48 48"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2.1 5-4.4 6.6v5.5h7.1C42.6 36.8 45 31.2 45 24.5z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.3c-.4-1.3-.7-2.7-.7-4.3s.3-3 .7-4.3V14H4.5C3 17 2 20.4 2 24s1 7 2.5 10l7.3-5.7z"/><path fill="#EA4335" d="M24 10.7c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg> 4.7 <span class="stars">★★★★★</span> Google rating</span><span class="chip">30+ years roofing Auckland</span></div></div></div></section>
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
<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">What happens next</h2><div class="faqs"><details open><summary>What happens after I send my details?</summary><p>We aim to respond within 3 hours. Mike calls you back personally, asks a few questions about your roof and books a free site visit, usually within the next working day.</p></details><details><summary>Is the quote really free?</summary><p>Yes. The site visit and quote are free, with no obligation and no sales pressure.</p></details><details><summary>Will the price change later?</summary><p>No. After the site visit you get a fixed, itemised price, so there are no surprises.</p></details><details><summary>Do you do repairs as well as reroofs?</summary><p>Yes. Whether it's one leak or a whole new roof, use the same form and tell us what's going on.</p></details></div></div></section>
<?php get_footer();
