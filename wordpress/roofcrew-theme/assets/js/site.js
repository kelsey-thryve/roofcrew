/* The Roof Crew v2: shared behaviour. No dependencies. */
(function () {
  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Dropdowns: click to open on touch screens
  document.querySelectorAll('.dd > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var dd = b.parentElement, open = !dd.classList.contains('open');
      document.querySelectorAll('.dd.open').forEach(function (d) { d.classList.remove('open'); });
      dd.classList.toggle('open', open);
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.dd')) document.querySelectorAll('.dd.open').forEach(function (d) { d.classList.remove('open'); });
  });

  // Filter tracks: pick one option, change the content in place
  document.querySelectorAll('[data-track]').forEach(function (track) {
    track.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      track.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      track.dispatchEvent(new CustomEvent('pick', { detail: b.dataset.value }));
    });
  });

  // Whole-home price bands by roofing type
  var priceTrack = document.querySelector('[data-track="prices"]');
  if (priceTrack) {
    priceTrack.addEventListener('pick', function (e) {
      document.querySelectorAll('[data-prices]').forEach(function (g) { g.hidden = g.dataset.prices !== e.detail; });
    });
  }

  // Count-up stats: 0 to the target in 2 seconds when they scroll into view
  var counters = document.querySelectorAll('[data-count]');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (counters.length && 'IntersectionObserver' in window && !reduce) {
    var fmt = function (n) { return n.toLocaleString('en-NZ'); };
    var run = function (el) {
      var target = +el.dataset.count, suffix = el.dataset.suffix || '', start = null;
      var step = function (t) {
        if (start === null) start = t;
        var p = Math.min((t - start) / 2000, 1), eased = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(Math.round(target * eased)) + (p === 1 ? suffix : '');
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { io.unobserve(en.target); run(en.target); } });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { io.observe(el); });
  }

  // Scroll motion: reveal content as it comes into view, header shadow, gentle hero parallax
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header = document.querySelector('.site-header');
  var heroBg = document.querySelector('.hero-bg');
  var onScroll = function () {
    var y = window.scrollY;
    if (header) header.classList.toggle('scrolled', y > 8);
    if (heroBg && !calm && y < 900) heroBg.style.translate = '0 ' + (y * 0.25) + 'px';
  };
  window.addEventListener('scroll', function () { requestAnimationFrame(onScroll); }, { passive: true });
  onScroll();
  if (!calm && 'IntersectionObserver' in window) {
    var sel = 'main section:not(.hero) .eyebrow, main section:not(.hero) h2, main section:not(.hero) .lede, .card, .stat, .photo, .ba, .map, .faqs details, .steps li, .band-cta .inner, .contact-box, .region-links a, .ph-box, .crew, .ticks li, .checks li';
    var fold = window.innerHeight;
    var items = [].filter.call(document.querySelectorAll(sel), function (el) {
      return !el.closest('.hero') && !el.parentElement.closest('.rv-skip') && el.getBoundingClientRect().top > fold * 0.95;
    });
    var seen = new Set();
    items.forEach(function (el) {
      if ([].some.call(items, function (o) { return o !== el && o.contains(el); })) return; // animate the outer box only
      var sibs = [].filter.call(el.parentElement.children, function (c) { return items.indexOf(c) > -1; });
      var i = sibs.indexOf(el);
      el.style.setProperty('--d', Math.min(i, 5) * 0.08 + 's');
      el.classList.add('rv');
      if (el.matches('.photo, .ba, .map')) el.classList.add('rv-img');
      seen.add(el);
    });
    var rio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); rio.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    seen.forEach(function (el) { rio.observe(el); });
  }

  // Before / after slider (keyboard friendly: it is a range input)
  document.querySelectorAll('.ba').forEach(function (ba) {
    var range = ba.querySelector('input[type=range]');
    if (range) range.addEventListener('input', function () { ba.style.setProperty('--pos', range.value + '%'); });
  });
  var projTrack = document.querySelector('[data-track="projects"]');
  if (projTrack) {
    projTrack.addEventListener('pick', function (e) {
      var ba = document.querySelector('.ba');
      var p = (window.RC_PROJECTS || {})[e.detail];
      if (!ba || !p) return;
      ba.querySelector('img.before').src = p.before;
      ba.querySelector('img.after').src = p.after;
      ba.querySelector('img.after').alt = p.alt;
      var cap = document.querySelector('[data-project-caption]');
      if (cap) cap.innerHTML = p.caption;
    });
  }

  // Quote forms: staging only shows a confirmation (connect to email or a CRM before launch)
  document.querySelectorAll('form[data-quote]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = (form.querySelector('[name=name]') || {}).value || '';
      var done = form.parentElement.querySelector('.form-done');
      if (done) {
        done.querySelector('[data-first]').textContent = name.split(' ')[0] || 'there';
        done.classList.add('show');
        form.hidden = true;
        done.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  });

  // Links to pages in the full build (not part of this staging set)
  document.querySelectorAll('a.soon').forEach(function (a) {
    a.setAttribute('title', 'This page comes with the full 20-page build');
    a.addEventListener('click', function (e) { e.preventDefault(); });
  });

  // Staging note: toggle the yellow placeholder highlights
  var st = document.querySelector('.staging button');
  if (st) st.addEventListener('click', function () {
    var hidden = document.body.classList.toggle('hide-ph');
    st.textContent = hidden ? 'Show highlights' : 'Hide highlights';
  });
})();
