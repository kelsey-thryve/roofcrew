<?php
/* Home page. Generated from the v2 design by tools/build_wp_theme.py: edit the generator, not this file. */
rc_meta( "Roofing Auckland | Reroofing & New Roofs | The Roof Crew", "Family-owned Auckland roofers, roofing since 2014 with 35+ years in building. Reroofs, new roofs and repairs, with a free site visit and a fixed quote." );
get_header(); ?>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "RoofingContractor", "name": "The Roof Crew", "telephone": "+64 21 903 822", "email": "mike@theroofcrew.co.nz", "areaServed": ["East Auckland", "North Shore", "South Auckland", "West Auckland"], "address": {"@type": "PostalAddress", "addressLocality": "Auckland", "addressCountry": "NZ"}}</script><script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "How long does a reroof take?", "acceptedAnswer": {"@type": "Answer", "text": "An average three-bedroom house takes about 3 to 4 days, depending on the weather."}}, {"@type": "Question", "name": "Can you reroof in winter?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Auckland's weather lets us replace roofs all year, and we work around the wet days."}}, {"@type": "Question", "name": "Do I need a repair or a whole new roof?", "acceptedAnswer": {"@type": "Answer", "text": "If it's the original roof, it's usually near the end of its life and worth replacing. If it's newer, a repair might be all you need. Mike will tell you straight after he's had a look."}}, {"@type": "Question", "name": "What happens to my old roof?", "acceptedAnswer": {"@type": "Answer", "text": "We take it away and dispose of it responsibly."}}, {"@type": "Question", "name": "Can I put solar panels on a new roof?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, but check with the roofing manufacturer first, as it can affect your warranty."}}, {"@type": "Question", "name": "Where do you work?", "acceptedAnswer": {"@type": "Answer", "text": "Right across Auckland, from Warkworth in the north to Franklin and south of the Bombay Hills."}}]}</script>

<section class="hero"><div class="hero-bg" style="background-image:url('<?php echo rc_theme_uri(); ?>/assets/img/hero-metal-tile.jpg')"></div>
<div class="wrap">
  <div>
    <div class="chips"><span class="chip rating"><svg width="18" height="18" viewBox="0 0 48 48"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2.1 5-4.4 6.6v5.5h7.1C42.6 36.8 45 31.2 45 24.5z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.3c-.4-1.3-.7-2.7-.7-4.3s.3-3 .7-4.3V14H4.5C3 17 2 20.4 2 24s1 7 2.5 10l7.3-5.7z"/><path fill="#EA4335" d="M24 10.7c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg> 4.7 <span class="stars">★★★★★</span> Google rating</span><span class="chip">Auckland roofing specialists</span></div>
    <h1>Roofing Auckland homes since 2014</h1>
    <p class="lede">The Roof Crew is a family-owned Auckland roofing company. We replace old roofs, install new ones and fix the ones that won't stop leaking. You'll deal with Mike from the first call to the final check, and you'll get a fixed price after a free site visit.</p>
    <div class="hero-actions"><a class="btn btn-outline-light" href="tel:+6421903822"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg> Call or text Mike · 021 903 822</a></div>
  </div>
  <div class="quote-card<?php echo rc_sent( 'get-quote' ) ? ' is-sent' : ''; ?>" id="get-quote">
  <h2>Get a free quote</h2><p class="sub">Free, no pressure. We aim to respond within 3 hours and usually visit within the next working day.</p>
  <?php rc_form_open('get-quote'); ?>
    <div><label for="hero-quote-name">Name</label><input id="hero-quote-name" name="name" autocomplete="name" required></div>
    <div><label for="hero-quote-phone">Phone</label><input id="hero-quote-phone" name="phone" type="tel" autocomplete="tel" required></div>
    <div class="full"><label for="hero-quote-email">Email</label><input id="hero-quote-email" name="email" type="email" autocomplete="email"></div>
    <div class="full"><label for="hero-quote-addr">Suburb or address</label><input id="hero-quote-addr" name="address" autocomplete="street-address"></div>
    <div class="full"><label for="hero-quote-need">What's going on with your roof?</label><select id="hero-quote-need" name="need"><option selected>New roof (reroof)</option><option>Leaks keep coming back</option><option>Not sure, please check it</option><option>Roof repair</option><option>Spouting or downpipes</option><option>Inspection or report</option><option>New build roof</option></select></div>
    <div class="full"><label for="hero-quote-msg">Anything else? (optional)</label><textarea id="hero-quote-msg" name="message"></textarea></div>
    <div class="full"><button class="btn btn-primary btn-block" type="submit">Get my free quote →</button></div>
    <div class="full hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
    <p class="full fine">Mike will call you back personally. No sales pressure. <a href="<?php echo rc_url('privacy-policy'); ?>">Privacy policy</a></p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks<?php echo rc_sent_name(); ?>.</strong>Mike will be in touch to book your free site visit.</div>
</div>
</div></section>

<section class="stats"><div class="wrap grid">
  <div class="stat"><b>1,000+</b><span>Auckland roofs completed</span></div>
  <div class="stat"><b>35+</b><span>Years in the building industry</span></div>
  <div class="stat"><b>RANZ</b><span>Roofing Association of NZ member</span></div>
</div></section>

<section class="alt" style="margin-top:-60px;padding-top:140px"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Services</span><h2>What we do</h2></div>
    <p class="lede">Most of our work is full roof replacement. Whatever the job, the same crew quotes it, does it and stands behind it.</p></div>
  <?php rc_services_grid(false); ?>
</div></section>

<section class="dark" id="options"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Roofing options</span><h2>Roofing options for Auckland homes</h2></div>
    <p class="lede">The right roof depends on your house, your budget and how close you are to the sea. Mike will talk you through it at your site visit.</p></div>
  <div class="grid-3"><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-installed.jpg" alt="COLORSTEEL® long-run roof" loading="lazy"></div><div class="body"><h3>COLORSTEEL® long-run</h3><p>Our most popular option, with a huge range of colours and profiles.</p><a <?php echo rc_link('colour-steel-roofing', 'link'); ?>>COLORSTEEL® roofing →</a></div></article><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/hero-metal-tile.jpg" alt="Gerard metal tile roof" loading="lazy"></div><div class="body"><h3>Gerard metal tile</h3><p>The look of a tiled roof, but much lighter.</p><a <?php echo rc_link('metal-tile-roofing', 'link'); ?>>Metal tile roofing →</a></div></article><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/concrete-tile.jpg" alt="Concrete tile roof" loading="lazy"></div><div class="body"><h3>Replacing a concrete tile roof</h3><p>We specialise in converting old concrete tile roofs to long-run COLORSTEEL® or metal tile.</p><a <?php echo rc_link('concrete-tile-roofing', 'link'); ?>>Concrete tile replacement →</a></div></article></div>
  <div class="card prices">
  <div class="prices-head"><div><h3>How much does a new roof cost in Auckland?</h3><div class="prices-intro"><p>A COLORSTEEL® reroof usually costs about $16,000 to $28,000 on a standard Auckland home with a roof of 100 to 180m². Smaller roofs start at around $12,000, and large or complex ones can pass $40,000.</p><p>The final cost comes down to the size and pitch of your roof, access, and what we find under the old one. That's why you get a fixed, itemised price after we've been out to see it.</p></div></div>
    <div><span class="filter-label">Filter: roof type</span><div class="track" data-track="prices"><button type="button" data-value="longrun" aria-pressed="true">COLORSTEEL</button><button type="button" data-value="metal" aria-pressed="false">Metal tile</button></div></div></div>
  <div class="bands" data-prices="longrun"><div class="band"><small>Small home</small><b>$12k to $18k</b><span>Roof area under 100m²</span></div><div class="band"><small>Standard home</small><b>$16k to $28k</b><span>Roof 100 to 180m²</span></div><div class="band"><small>Large or complex</small><b>$25k to $40k+</b><span>Roof 180m²+</span></div></div><div class="bands" data-prices="metal" hidden><div class="band"><small>Small home</small><b class="ask">Fixed quote on site</b><span>Roof area under 100m²</span></div><div class="band"><small>Standard home</small><b class="ask">Fixed quote on site</b><span>Roof 100 to 180m²</span></div><div class="band"><small>Large or complex</small><b class="ask">Fixed quote on site</b><span>Roof 180m²+</span></div></div>
  <div class="colours"><div><h3>Pick your colour</h3><p>A few popular COLORSTEEL® colours. Shades are approximate on screen, we'll bring real samples to your quote.</p></div>
    <ul class="swatches"><li><span class="sw" style="--c:#e4e1d6"></span>Titania</li><li><span class="sw" style="--c:#a4a9a7"></span>Gull Grey</li><li><span class="sw" style="--c:#c8b58f"></span>Desert Sand</li><li><span class="sw" style="--c:#8a897f"></span>Sandstone Grey</li><li><span class="sw" style="--c:#5d605f"></span>Thunder Grey</li><li><span class="sw" style="--c:#3a4a3e"></span>Karaka</li><li><span class="sw" style="--c:#4a4c4f"></span>Grey Friars</li><li><span class="sw" style="--c:#3a3631"></span>Ironsand</li></ul></div>
  <div class="prices-foot"><span>A huge range of COLORSTEEL® colours and profiles</span><a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my exact price →</a></div>
</div>
</div></section>

<section class="alt" id="work"><div class="wrap ba-wrap">
  <div class="ba-side">
    <div><span class="eyebrow">See the difference</span><h2>The upgrade your whole street notices.</h2><p class="lede">Drag the slider to see a real Auckland reroof, start to finish.</p></div>
    <div><span class="filter-label">Filter: choose a project</span>
      <div class="track" data-track="projects"><button type="button" data-value="p1" aria-pressed="true">Concrete tile</button><button type="button" data-value="p2" aria-pressed="false">COLORSTEEL</button><button type="button" data-value="p3" aria-pressed="false">Metal tile</button></div></div>
    <p data-project-caption style="font-size:15px;color:var(--gray-500)">Concrete tile roof replacement</p>
    <hr>
    <a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my free quote →</a>
  </div>
  <div class="ba" aria-label="Before and after slider">
    <img class="before" src="<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-before.jpg" alt="Before the reroof">
    <img class="after" src="<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-after.jpg" alt="Concrete tile roof replaced with a new roof">
    <span class="lbl l">Before</span><span class="lbl r">After</span>
    <div class="handle"></div><div class="knob">‹›</div>
    <input type="range" min="0" max="100" value="50" aria-label="Compare before and after">
  </div>
</div></section>
<script>window.RC_PROJECTS={"p1": {"before": "<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-before.jpg", "after": "<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-after.jpg", "alt": "Concrete tile roof replaced with a new roof", "caption": "Concrete tile roof replacement"}, "p2": {"before": "<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-reroof-before.jpg", "after": "<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-reroof-after.jpg", "alt": "Tired roof to COLORSTEEL long-run", "caption": "COLORSTEEL\u00ae long-run reroof"}, "p3": {"before": "<?php echo rc_theme_uri(); ?>/assets/img/metaltile-before.jpg", "after": "<?php echo rc_theme_uri(); ?>/assets/img/metaltile-after.jpg", "alt": "Old roof to pressed metal tile", "caption": "Pressed metal tile reroof"}};</script>

<section class="dark" id="areas"><div class="wrap areas">
  <div>
    <span class="eyebrow">Where we work</span><h2>Reroofing right across Auckland.</h2>
    <p class="lede">From Warkworth in the north to Franklin and south of the Bombay Hills. Find your area.</p>
    <div class="region-links"><?php rc_region_links(); ?><a class="ask" href="tel:+6421903822">Not sure? Ask Mike <span aria-hidden="true">→</span></a></div>
    <p class="popular">Popular areas: <a <?php echo rc_link('roofers-in-pukekohe'); ?>>Pukekohe</a> · <a <?php echo rc_link('locations/papakura'); ?>>Papakura</a> · <a <?php echo rc_link('locations/glenfield'); ?>>Glenfield</a> · <a <?php echo rc_link('locations/manukau'); ?>>Manukau</a> · <a <?php echo rc_link('locations/manurewa'); ?>>Manurewa</a> · <a <?php echo rc_link('locations/howick'); ?>>Howick</a></p>
    <p style="margin-top:14px"><a class="link" href="locations/">See all areas we cover →</a></p>
  </div>
  <div class="map"><iframe title="Map of the areas The Roof Crew covers" src="https://www.openstreetmap.org/export/embed.html?bbox=174.45%2C-37.25%2C175.15%2C-36.62&layer=mapnik" loading="lazy"></iframe></div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Signs it's time for a new roof</h2>
  <div class="signs" style="margin-top:32px">
    <div class="card"><ul class="checks"><li>Leaks keep coming back after repairs</li><li>The roof is 30 or more years old</li><li>There are water stains on your ceilings</li><li>You can see rust, lifting sheets or cracked tiles</li><li>The surface looks faded, chalky or mossy</li></ul></div>
    <div class="photo"><img src="<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-before.jpg" alt="An old, tired roof ready for replacement" loading="lazy"></div>
  </div>
  <div class="card unsure"><p>Don't wait until it's dripping through the ceiling. By then, the damage underneath is often worse than the roof itself.</p>
    <div class="acts"><a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my free reroof or repair quote</a></div></div>
</div></section>

<section class="dark why"><div class="wrap">
  <span class="eyebrow">The Roof Crew difference</span>
  <h2>Why Auckland homeowners choose us</h2>
  <hr class="rule">
  <div class="why-grid">
    <div class="why-photo"><img src="<?php echo rc_theme_uri(); ?>/assets/img/photo-sunset-roof.jpg" alt="A new roof finished by The Roof Crew at sunset" loading="lazy"><div class="why-badge"><b>Since 2014</b><span>Roofing Auckland homes</span></div></div>
    <div>
      <p class="lede">There's a reason we have a 4.7 star rating.</p>
      <ol class="why-list"><li><span class="num">01</span><div><h3>You deal with Mike</h3><p>There's no call centre, and no salesperson handing you over to someone else.</p></div></li><li><span class="num">02</span><div><h3>Fixed pricing</h3><p>Your quote is itemised, so you know what you're paying for.</p></div></li><li><span class="num">03</span><div><h3>Backed in writing</h3><p>You get a 5-year workmanship warranty (conditions apply), plus the manufacturer's product warranty.</p></div></li><li><span class="num">04</span><div><h3>Finance available</h3><p>You can spread the cost if that helps.</p></div></li></ol>
      <p style="margin-top:26px"><a class="link" href="about/">About us →</a></p>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">What Auckland homeowners say</h2>
  <div class="reviews">
  <div class="card rating-card"><span class="g"><svg width="18" height="18" viewBox="0 0 48 48"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2.1 5-4.4 6.6v5.5h7.1C42.6 36.8 45 31.2 45 24.5z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.3c-.4-1.3-.7-2.7-.7-4.3s.3-3 .7-4.3V14H4.5C3 17 2 20.4 2 24s1 7 2.5 10l7.3-5.7z"/><path fill="#EA4335" d="M24 10.7c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg> Google reviews</span><b>4.7</b><div class="stars">★★★★★</div>
    <p style="font-size:15px;color:var(--gray-500)">Google rating</p><a class="link" href="https://www.google.com/search?q=The+Roof+Crew+Auckland+reviews" target="_blank" rel="noopener" style="display:inline-block;margin-top:12px">Read all reviews on Google →</a></div>
  <figure class="card review"><div class="stars">★★★★★</div><blockquote>Mike from the roof crew was very professional, fairly priced and very easy to work with. He worked in seamlessly with other contractors we had on-site. We are so pleased with the final result of our new roof.</blockquote><cite>Suzann Pepping</cite></figure><figure class="card review"><div class="stars">★★★★★</div><blockquote>I recently had my roof work completed by The Roof Crew, and I couldn't be happier with the experience. Mike was fantastic from the start, friendly, approachable, and very knowledgeable when it came to providing the quote and guiding me on the best product to choose. The entire process was smooth and hassle-free, with great communication and timely follow-ups throughout.</blockquote><cite>Sriharan S</cite></figure><figure class="card review"><div class="stars">★★★★★</div><blockquote>Excellent experience with The Roof Crew from the quote to the completion of the job. I was kept informed through the entire process. The team that replaced the roof were very friendly &amp; professional. They job completed the job in one day &amp; when they left you would never have known they had been here. I would highly recommend them.</blockquote><cite>Jenny Thurston</cite></figure></div>
</div></section>

<section class="band-cta"><div class="wrap"><div class="inner">
  <div><h2>Ready for a roof that's sorted before the next storm?</h2><p>Get it checked now, not after the next downpour.</p></div>
  <a class="btn btn-white" href="<?php echo rc_url('quote'); ?>">Get my free quote →</a>
</div></div></section>

<section class="dark"><div class="wrap"><h2 style="margin-bottom:30px">Common questions</h2><div class="faqs"><details open><summary>How long does a reroof take?</summary><p>An average three-bedroom house takes about 3 to 4 days, depending on the weather.</p></details><details><summary>Can you reroof in winter?</summary><p>Yes. Auckland's weather lets us replace roofs all year, and we work around the wet days.</p></details><details><summary>Do I need a repair or a whole new roof?</summary><p>If it's the original roof, it's usually near the end of its life and worth replacing. If it's newer, a repair might be all you need. Mike will tell you straight after he's had a look.</p></details><details><summary>What happens to my old roof?</summary><p>We take it away and dispose of it responsibly.</p></details><details><summary>Can I put solar panels on a new roof?</summary><p>Yes, but check with the roofing manufacturer first, as it can affect your warranty.</p></details><details><summary>Where do you work?</summary><p>Right across Auckland, from Warkworth in the north to Franklin and south of the Bombay Hills.</p></details></div></div></section>
<section id="request"><div class="wrap closing">
  <div>
    <span class="eyebrow">Request a quote</span>
    <h2>Find out what your new roof will really cost</h2>
    <p class="lede">Call or text Mike on 021 903 822, or send us your details. We aim to respond within 3 hours and usually visit within the next working day.</p>
    <ol class="steps">
      <li><span class="n">1</span><div><b>Send your details</b><span>Takes about a minute, or just call or text.</span></div></li>
      <li><span class="n">2</span><div><b>Mike gets in touch</b><span>We aim to respond within 3 hours, and usually visit within the next working day.</span></div></li>
      <li><span class="n">3</span><div><b>A clear, itemised quote</b><span>Fixed, transparent and no pressure.</span></div></li>
    </ol>
    <div class="contact-box"><a href="tel:+6421903822"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg> 021 903 822</a><a href="mailto:mike@theroofcrew.co.nz"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg> mike@theroofcrew.co.nz</a></div>
  </div>
  <div class="quote-card<?php echo rc_sent( 'quote-bottom' ) ? ' is-sent' : ''; ?>" id="quote-bottom">
  <h2>Get your free quote</h2><p class="sub">Free and no pressure.</p>
  <?php rc_form_open('quote-bottom'); ?>
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
