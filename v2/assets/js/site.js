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
