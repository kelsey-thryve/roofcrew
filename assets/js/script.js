// The Roof Crew — shared site behaviour
(function () {
  "use strict";

  /* Sticky header shadow */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Mobile nav */
  var navToggle = document.querySelector(".nav-toggle");
  var mobileNav = document.querySelector(".mobile-nav");
  var navScrim = document.querySelector(".nav-scrim");
  function closeMobileNav() {
    if (!navToggle) return;
    navToggle.classList.remove("is-open");
    navToggle.setAttribute("aria-expanded", "false");
    mobileNav.classList.remove("is-open");
    navScrim.classList.remove("is-open");
    document.body.style.overflow = "";
  }
  if (navToggle && mobileNav && navScrim) {
    navToggle.addEventListener("click", function () {
      var open = navToggle.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      mobileNav.classList.toggle("is-open", open);
      navScrim.classList.toggle("is-open", open);
      document.body.style.overflow = open ? "hidden" : "";
    });
    navScrim.addEventListener("click", closeMobileNav);
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeMobileNav);
    });
    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeMobileNav();
    });
  }

  /* Scroll reveal */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* Animated stat counters */
  var counters = document.querySelectorAll("[data-count]");
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 1200;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      var value = Math.round(target * eased);
      el.textContent = value + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window && counters.length) {
    var cio = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            cio.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* Before / after slider */
  document.querySelectorAll(".ba-slider").forEach(function (slider) {
    var afterImg = slider.querySelector(".ba-after");
    var handle = slider.querySelector(".ba-handle");
    var dragging = false;

    function setPosition(clientX) {
      var rect = slider.getBoundingClientRect();
      var pct = ((clientX - rect.left) / rect.width) * 100;
      pct = Math.max(0, Math.min(100, pct));
      afterImg.style.clipPath = "inset(0 0 0 " + pct + "%)";
      handle.style.left = pct + "%";
    }
    function start(e) { dragging = true; }
    function move(e) {
      if (!dragging) return;
      var x = e.touches ? e.touches[0].clientX : e.clientX;
      setPosition(x);
    }
    function end() { dragging = false; }

    handle.addEventListener("mousedown", start);
    handle.addEventListener("touchstart", start, { passive: true });
    window.addEventListener("mousemove", move);
    window.addEventListener("touchmove", move, { passive: true });
    window.addEventListener("mouseup", end);
    window.addEventListener("touchend", end);
    slider.addEventListener("click", function (e) {
      if (e.target === handle) return;
      setPosition(e.clientX);
    });
  });

  /* FAQ accordion */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var btn = item.querySelector(".faq-q");
    var answer = item.querySelector(".faq-a");
    if (!btn || !answer) return;
    btn.addEventListener("click", function () {
      var isOpen = item.classList.contains("is-open");
      item.parentElement.querySelectorAll(".faq-item.is-open").forEach(function (other) {
        if (other !== item) {
          other.classList.remove("is-open");
          other.querySelector(".faq-a").style.maxHeight = null;
        }
      });
      item.classList.toggle("is-open", !isOpen);
      answer.style.maxHeight = !isOpen ? answer.scrollHeight + "px" : null;
    });
  });

  /* Quote form validation */
  document.querySelectorAll(".quote-form").forEach(function (form) {
    var formEl = form.querySelector("form");
    var successEl = form.querySelector(".form-success");
    if (!formEl) return;

    formEl.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;
      formEl.querySelectorAll("[required]").forEach(function (field) {
        var wrapper = field.closest(".field");
        var ok = field.value.trim() !== "";
        if (field.type === "email" && ok) {
          ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value.trim());
        }
        if (wrapper) wrapper.classList.toggle("has-error", !ok);
        if (!ok) valid = false;
      });
      if (!valid) return;

      var data = new FormData(formEl);
      var subject = encodeURIComponent("Free quote request — " + (data.get("name") || "website"));
      var lines = [];
      formEl.querySelectorAll("[name]").forEach(function (field) {
        var label = field.closest(".field") && field.closest(".field").querySelector("label");
        lines.push((label ? label.textContent : field.name) + ": " + field.value);
      });
      var body = encodeURIComponent(lines.join("\n"));
      var mailto = "mailto:mike@theroofcrew.co.nz?subject=" + subject + "&body=" + body;

      formEl.style.display = "none";
      if (successEl) successEl.classList.add("is-visible");
      window.location.href = mailto;
    });
  });

  /* Review track arrows */
  document.querySelectorAll("[data-review-track]").forEach(function (wrap) {
    var track = wrap.querySelector(".review-track");
    var prev = wrap.querySelector("[data-review-prev]");
    var next = wrap.querySelector("[data-review-next]");
    if (!track) return;
    function scrollBy(dir) {
      var card = track.querySelector(".review-card");
      var amount = card ? card.getBoundingClientRect().width + 22 : 300;
      track.scrollBy({ left: dir * amount, behavior: "smooth" });
    }
    if (prev) prev.addEventListener("click", function () { scrollBy(-1); });
    if (next) next.addEventListener("click", function () { scrollBy(1); });
  });
})();
