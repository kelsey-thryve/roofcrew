<?php
/* Home page. Generated from the v2 design by tools/build_wp_theme.py: edit the generator, not this file. */
rc_meta( "Reroofing Auckland | The Roof Crew", "Family-owned Auckland reroofing crew. Free, no-pressure quotes, whole-home price ranges and a fixed price after a free site visit." );
get_header(); ?>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "RoofingContractor", "name": "The Roof Crew", "telephone": "+64 21 903 822", "email": "mike@theroofcrew.co.nz", "areaServed": ["East Auckland", "North Shore", "South Auckland", "West Auckland"], "address": {"@type": "PostalAddress", "addressLocality": "Auckland", "addressCountry": "NZ"}}</script><script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "How do I know if my roof needs replacing?", "acceptedAnswer": {"@type": "Answer", "text": "If leaks keep coming back after repairs, the roof is 30 or more years old, or you can see rust, lifting sheets, cracked tiles or water stains on your ceilings, it is usually time to look at a new roof. Mike will check it on a free site visit and tell you straight whether a repair will do."}}, {"@type": "Question", "name": "How much does a reroof cost in Auckland?", "acceptedAnswer": {"@type": "Answer", "text": "It depends on the size and shape of your roof, access, and the material you choose. The ranges above are a rough guide for small, standard and large homes. After a free site visit you get a fixed, itemised price, so there are no surprises."}}, {"@type": "Question", "name": "Is it worth repairing my roof, or should I replace it?", "acceptedAnswer": {"@type": "Answer", "text": "A repair makes sense for a one-off problem on a roof that is otherwise sound. If you are patching the same roof every winter, the money usually goes further on a new roof with a fresh guarantee. We will tell you honestly which one you need."}}, {"@type": "Question", "name": "How long does a reroof take, and can we stay home?", "acceptedAnswer": {"@type": "Answer", "text": "An average 3-bedroom house takes about 3 to 4 days, weather pending. Mike gives you a timeframe with your fixed quote, so you know what to expect before we start. You can usually stay home while we work, and we tidy the site at the end of every day."}}, {"@type": "Question", "name": "Do you offer finance?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Finance is available so you can spread the cost of a new roof. Just ask when you book your free quote."}}, {"@type": "Question", "name": "Which roofing material is best for Auckland homes?", "acceptedAnswer": {"@type": "Answer", "text": "For most Auckland homes, COLORSTEEL® long-run is the popular choice: it's light, handles coastal wind and rain well, and comes in a wide range of colours. Pressed metal tile gives the look of tile with the strength of steel, while concrete tile offers good thermal and acoustic performance but is heavier. Mike brings samples to your free site visit."}}]}</script>

<section class="hero"><div class="hero-bg" style="background-image:url('<?php echo rc_theme_uri(); ?>/assets/img/hero-metal-tile.jpg')"></div>
<div class="wrap">
  <div>
    <div class="chips"><span class="chip rating"><svg width="18" height="18" viewBox="0 0 48 48"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2.1 5-4.4 6.6v5.5h7.1C42.6 36.8 45 31.2 45 24.5z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.3c-.4-1.3-.7-2.7-.7-4.3s.3-3 .7-4.3V14H4.5C3 17 2 20.4 2 24s1 7 2.5 10l7.3-5.7z"/><path fill="#EA4335" d="M24 10.7c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg> 4.7 <span class="stars">★★★★★</span> Google rating</span><span class="chip">Auckland roofing specialists</span></div>
    <h1>Auckland Roofing Done Right</h1>
    <p class="lede">With more than 30 years experience reroofing, building, and repairing Auckland homes. Get a free quote today with a fixed price.</p>
    <div class="hero-actions"><a class="btn btn-outline-light" href="tel:+6421903822"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg> Call or text Mike · 021 903 822</a></div>
  </div>
  <div class="quote-card<?php echo rc_sent( 'get-quote' ) ? ' is-sent' : ''; ?>" id="get-quote">
  <h2>Get a free quote</h2><p class="sub">Free, no pressure. We usually visit within 3 working days.</p>
  <?php rc_form_open('get-quote'); ?>
    <div><label for="hero-quote-name">Name</label><input id="hero-quote-name" name="name" autocomplete="name" required></div>
    <div><label for="hero-quote-phone">Phone</label><input id="hero-quote-phone" name="phone" type="tel" autocomplete="tel" required></div>
    <div class="full"><label for="hero-quote-email">Email</label><input id="hero-quote-email" name="email" type="email" autocomplete="email"></div>
    <div class="full"><label for="hero-quote-addr">Suburb or address</label><input id="hero-quote-addr" name="address" autocomplete="street-address"></div>
    <div class="full"><label for="hero-quote-need">What's going on with your roof?</label><select id="hero-quote-need" name="need"><option selected>New roof (reroof)</option><option>Leaks keep coming back</option><option>Not sure, please check it</option><option>Roof repair</option><option>Spouting or downpipes</option><option>Inspection or report</option><option>New build roof</option></select></div>
    <div class="full"><label for="hero-quote-msg">Anything else? (optional)</label><textarea id="hero-quote-msg" name="message"></textarea></div>
    <div class="full"><button class="btn btn-primary btn-block" type="submit">Get my free quote →</button></div>
    <div class="full hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
    <p class="full fine">Mike will call you back personally. No sales pressure.</p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks<?php echo rc_sent_name(); ?>.</strong>Mike will be in touch to book your free site visit.</div>
</div>
</div></section>

<section class="stats"><div class="wrap grid">
  <div class="stat"><b data-count="1000" data-suffix="+">1,000+</b><span>Auckland roofs completed</span></div>
  <div class="stat"><b>30+</b><span>Years roofing Auckland</span></div>
  <div class="stat"><b>RANZ</b><span>Roofing Association of NZ member</span></div>
</div></section>

<section class="alt" style="margin-top:-60px;padding-top:140px"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">What we do</span><h2>Solution Focused Roofing Specialists</h2></div>
    <p class="lede">Not sure which one you need? Give Mike a call and he'll talk you through it. No jargon.</p></div>
  <?php rc_services_grid(false); ?>
</div></section>

<section class="dark" id="options"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Roofing options</span><h2>Three roofing systems,<br>made for Auckland weather.</h2></div>
    <p class="lede">Not sure which suits your home? We'll bring real samples and help you choose at your free site visit.</p></div>
  <div class="grid-3"><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-installed.jpg" alt="COLORSTEEL long-run roof" loading="lazy"></div><div class="body"><h3>COLORSTEEL® long-run</h3><ul class="mini"><li>A huge range of colours and profiles</li><li>Our most popular option</li></ul></div></article><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/hero-metal-tile.jpg" alt="Pressed metal tile roof" loading="lazy"></div><div class="body"><h3>Pressed metal tile</h3><ul class="mini"><li>The look of tile, the strength of steel</li><li>Light, strong and durable</li></ul></div></article><article class="card system"><div class="img"><img src="<?php echo rc_theme_uri(); ?>/assets/img/concrete-tile.jpg" alt="Concrete tile roof" loading="lazy"></div><div class="body"><h3>Concrete tile</h3><ul class="mini"><li>Thermal and acoustic performance</li><li>Heavier, may need a structural check</li></ul></div></article></div>
  <div class="card prices">
  <div class="prices-head"><div><h3>What a whole reroof roughly costs</h3><p style="color:var(--gray-500);font-size:15px;margin-top:4px">Indicative 2026 Auckland ranges, not a fixed quote.</p></div>
    <div><span class="filter-label">Filter: roof type</span><div class="track" data-track="prices"><button type="button" data-value="longrun" aria-pressed="true">COLORSTEEL</button><button type="button" data-value="metal" aria-pressed="false">Metal tile</button><button type="button" data-value="concrete" aria-pressed="false">Concrete tile</button></div></div></div>
  <div class="bands" data-prices="longrun"><div class="band"><small>Small home</small><b>$12k to $18k</b><span>Roof area under 100m²</span></div><div class="band"><small>Standard home</small><b>$16k to $28k</b><span>Roof 100 to 180m²</span></div><div class="band"><small>Large or complex</small><b>$25k to $40k+</b><span>Roof 180m²+</span></div></div><div class="bands" data-prices="metal" hidden><div class="band"><small>Small home</small><b class="ask">Fixed quote on site</b><span>Roof area under 100m²</span></div><div class="band"><small>Standard home</small><b class="ask">Fixed quote on site</b><span>Roof 100 to 180m²</span></div><div class="band"><small>Large or complex</small><b class="ask">Fixed quote on site</b><span>Roof 180m²+</span></div></div><div class="bands" data-prices="concrete" hidden><div class="band"><small>Small home</small><b class="ask">Fixed quote on site</b><span>Roof area under 100m²</span></div><div class="band"><small>Standard home</small><b class="ask">Fixed quote on site</b><span>Roof 100 to 180m²</span></div><div class="band"><small>Large or complex</small><b class="ask">Fixed quote on site</b><span>Roof 180m²+</span></div></div>
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
    <p data-project-caption style="font-size:15px;color:var(--gray-500)">Concrete tile reroof</p>
    <hr>
    <a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my free quote →</a>
  </div>
  <div class="ba" aria-label="Before and after slider">
    <img class="before" src="<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-before.jpg" alt="Before the reroof">
    <img class="after" src="<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-after.jpg" alt="Concrete tile to new roof">
    <span class="lbl l">Before</span><span class="lbl r">After</span>
    <div class="handle"></div><div class="knob">‹›</div>
    <input type="range" min="0" max="100" value="50" aria-label="Compare before and after">
  </div>
</div></section>
<script>window.RC_PROJECTS={"p1": {"before": "<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-before.jpg", "after": "<?php echo rc_theme_uri(); ?>/assets/img/concretetile-reroof-after.jpg", "alt": "Concrete tile to new roof", "caption": "Concrete tile reroof"}, "p2": {"before": "<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-reroof-before.jpg", "after": "<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-reroof-after.jpg", "alt": "Tired roof to COLORSTEEL long-run", "caption": "COLORSTEEL\u00ae long-run reroof"}, "p3": {"before": "<?php echo rc_theme_uri(); ?>/assets/img/metaltile-before.jpg", "after": "<?php echo rc_theme_uri(); ?>/assets/img/metaltile-after.jpg", "alt": "Old roof to pressed metal tile", "caption": "Pressed metal tile reroof"}};</script>

<section class="dark" id="areas"><div class="wrap areas">
  <div>
    <span class="eyebrow">Where we work</span><h2>Reroofing right across Auckland.</h2>
    <p class="lede">From the North Shore to Pukekohe. Find your area.</p>
    <div class="region-links"><?php rc_region_links(); ?><a class="ask" href="tel:+6421903822">Not sure? Ask Mike <span aria-hidden="true">→</span></a></div>
    <p class="popular">Popular suburbs: <a href="#" class="soon">Howick</a> · <a href="#" class="soon">Botany</a> · <a href="#" class="soon">Takapuna</a></p>
    <p style="margin-top:14px"><a class="link" href="locations/">See all areas we cover →</a></p>
  </div>
  <div class="map"><iframe title="Map of the areas The Roof Crew covers" src="https://www.openstreetmap.org/export/embed.html?bbox=174.45%2C-37.25%2C175.15%2C-36.62&layer=mapnik" loading="lazy"></iframe></div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Signs it's time for a new roof</h2>
  <p class="lede">If two or more of these sound familiar, another patch is likely money down the drain.</p>
  <div class="signs" style="margin-top:32px">
    <div class="card"><ul class="checks"><li>Leaks keep coming back after repairs</li><li>Roof is 30+ years old</li><li>Water stains on your ceilings</li><li>Rust, lifting sheets or cracked tiles</li><li>Faded, chalky or mossy surface</li><li>Increased energy bills from leakages</li></ul></div>
    <div class="photo"><img src="<?php echo rc_theme_uri(); ?>/assets/img/colorsteel-before.jpg" alt="An old, tired roof ready for replacement" loading="lazy"></div>
  </div>
  <div class="card unsure"><p><b>Not sure?</b> Mike will check your roof and tell you straight whether it's time.</p>
    <div class="acts"><a class="btn btn-primary" href="<?php echo rc_url('quote'); ?>">Get my free reroof or repair quote</a></div></div>
</div></section>

<section class="dark why"><div class="wrap">
  <span class="eyebrow">The Roof Crew difference</span>
  <h2>Why Auckland chooses us</h2>
  <hr class="rule">
  <div class="why-grid">
    <div class="why-photo"><img src="<?php echo rc_theme_uri(); ?>/assets/img/photo-sunset-roof.jpg" alt="A new roof finished by The Roof Crew at sunset" loading="lazy"><div class="why-badge"><b>30+</b><span>Years on Auckland roofs</span></div></div>
    <div>
      <p class="lede">There's a reason we have a 4.7 star rating.</p>
      <ol class="why-list">
        <li><span class="num">01</span><div><h3>Family-owned</h3><p>Three decades in the trade, still run by the same crew that picks up the phone.</p></div></li>
        <li><span class="num">02</span><div><h3>Fast, free quotes</h3><p>No call centres. You deal with Mike from the first call to the final check.</p></div></li>
        <li><span class="num">03</span><div><h3>Fully guaranteed</h3><p>Workmanship and product are both covered, so there are no fine-print surprises.</p></div></li>
        <li><span class="num">04</span><div><h3>Finance available</h3><p>Spread the cost of a reroof with flexible payment options.</p></div></li>
      </ol>
      <p style="margin-top:26px"><a class="link" href="about/">Meet the crew →</a></p>
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

<section class="dark"><div class="wrap"><h2 style="margin-bottom:30px">Questions people ask us</h2><div class="faqs"><details open><summary>How do I know if my roof needs replacing?</summary><p>If leaks keep coming back after repairs, the roof is 30 or more years old, or you can see rust, lifting sheets, cracked tiles or water stains on your ceilings, it is usually time to look at a new roof. Mike will check it on a free site visit and tell you straight whether a repair will do.</p></details><details><summary>How much does a reroof cost in Auckland?</summary><p>It depends on the size and shape of your roof, access, and the material you choose. The ranges above are a rough guide for small, standard and large homes. After a free site visit you get a fixed, itemised price, so there are no surprises.</p></details><details><summary>Is it worth repairing my roof, or should I replace it?</summary><p>A repair makes sense for a one-off problem on a roof that is otherwise sound. If you are patching the same roof every winter, the money usually goes further on a new roof with a fresh guarantee. We will tell you honestly which one you need.</p></details><details><summary>How long does a reroof take, and can we stay home?</summary><p>An average 3-bedroom house takes about 3 to 4 days, weather pending. Mike gives you a timeframe with your fixed quote, so you know what to expect before we start. You can usually stay home while we work, and we tidy the site at the end of every day.</p></details><details><summary>Do you offer finance?</summary><p>Yes. Finance is available so you can spread the cost of a new roof. Just ask when you book your free quote.</p></details><details><summary>Which roofing material is best for Auckland homes?</summary><p>For most Auckland homes, COLORSTEEL® long-run is the popular choice: it's light, handles coastal wind and rain well, and comes in a wide range of colours. Pressed metal tile gives the look of tile with the strength of steel, while concrete tile offers good thermal and acoustic performance but is heavier. Mike brings samples to your free site visit.</p></details></div></div></section>
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
    <p class="full fine">Mike will call you back personally. No sales pressure.</p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks<?php echo rc_sent_name(); ?>.</strong>Mike will be in touch to book your free site visit.</div>
</div>
</div></section>
<?php get_footer();
