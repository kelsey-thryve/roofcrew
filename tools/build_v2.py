#!/usr/bin/env python3
"""Builds the v2 staging site into v2/.  Run from the repo root:  python3 tools/build_v2.py

Pages: Home, About, Contact, Free quote, Services (collection), service and material pages, Locations
(collection), region and area pages, Blog (index and posts) and the Privacy policy, plus small
redirect pages for old addresses. Shared header, footer and quote form. Page copy lives in
tools/content_v2.py (from Kelsey's content doc).
<mark class="ph"> = content Mike still has to confirm or supply (shows yellow on staging; the
question for Mike shows on hover).
"""
import json, os, re, shutil, sys, html as _html
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content_v2 as C  # noqa: E402
from content_v2 import P  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "v2")
PHONE, TEL = "021 903 822", "+6421903822"
EMAIL = "mike@theroofcrew.co.nz"

RATING = "4.7"
GOOGLE_REVIEWS = "https://www.google.com/search?q=The+Roof+Crew+Auckland+reviews"
REAL_REVIEWS = [  # real Google reviews supplied by the client
    ("Mike from the roof crew was very professional, fairly priced and very easy to work with. He worked in seamlessly with other contractors we had on-site. We are so pleased with the final result of our new roof.", "Suzann Pepping"),
    ("I recently had my roof work completed by The Roof Crew, and I couldn't be happier with the experience. Mike was fantastic from the start, friendly, approachable, and very knowledgeable when it came to providing the quote and guiding me on the best product to choose. The entire process was smooth and hassle-free, with great communication and timely follow-ups throughout.", "Sriharan S"),
    ("Excellent experience with The Roof Crew from the quote to the completion of the job. I was kept informed through the entire process. The team that replaced the roof were very friendly &amp; professional. They job completed the job in one day &amp; when they left you would never have known they had been here. I would highly recommend them.", "Jenny Thurston"),
]
# Menus. The WordPress build empties these and fills the menus from its pages instead.
NAV_SERVICES = [(s["path"], s["name"]) for s in C.SERVICE_PAGES]
NAV_REGIONS = [(r["path"], r["name"]) for r in C.REGIONS]
FOOT_SERVICES = [(s["path"], s["name"]) for s in C.SERVICES_ONLY]
PRICES = {  # whole-home ranges; None = no published range yet (shows "Fixed quote on site")
    "longrun": ("$12k to $18k", "$16k to $28k", "$25k to $40k+"),
    "metal": (None, None, None),
}
PROJECTS = {
    "p1": ("concretetile-reroof-before.jpg", "concretetile-reroof-after.jpg", "Concrete tile roof replaced with a new roof", "Concrete tile roof replacement"),
    "p2": ("colorsteel-reroof-before.jpg", "colorsteel-reroof-after.jpg", "Tired roof to COLORSTEEL long-run", "COLORSTEEL® long-run reroof"),
    "p3": ("metaltile-before.jpg", "metaltile-after.jpg", "Old roof to pressed metal tile", "Pressed metal tile reroof"),
}
MAP_AUCKLAND = "https://www.openstreetmap.org/export/embed.html?bbox=174.45%2C-37.25%2C175.15%2C-36.62&layer=mapnik"

ICONS = {
    "home": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
    "search": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "drop": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/></svg>',
    "wrench": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/></svg>',
    "build": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><path d="M5 21V9l7-5 7 5v12"/><path d="M9 21v-6h6v6"/></svg>',
    "layers": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/></svg>',
    "family": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3 2.5-5 5-5s5 2 5 5"/><path d="M14 20c0-2.5 1.5-4 3.5-4S21 17.5 21 20"/></svg>',
    "clock": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "shield": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "card": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "google": '<svg width="18" height="18" viewBox="0 0 48 48"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2.1 5-4.4 6.6v5.5h7.1C42.6 36.8 45 31.2 45 24.5z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.3c-.4-1.3-.7-2.7-.7-4.3s.3-3 .7-4.3V14H4.5C3 17 2 20.4 2 24s1 7 2.5 10l7.3-5.7z"/><path fill="#EA4335" d="M24 10.7c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg>',
}
LOGO = '<svg width="30" height="30" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="currentColor"/><path d="M7 16l9-8 9 8M10 14v10h12V14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


class Page:
    def __init__(self, path):
        self.path = path  # e.g. "services/reroofing/"
        depth = path.count("/")
        self.r = "../" * depth

    def u(self, target):  # link to another page in v2
        return self.r + target

    def link(self, path, cls=""):
        """href (and class) for a link to another page of the site."""
        return f'href="{self.u(path)}"' + (f' class="{cls}"' if cls else "")


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def paras(items):
    return "".join(f"<p>{p}</p>" for p in items)


def sec(alt):
    return '<section class="alt">' if alt else "<section>"


def header(pg, current):
    svc_items = "".join(f'<a {pg.link(p)}>{n}</a>' for p, n in NAV_SERVICES)
    reg_items = "".join(f'<a {pg.link(p)}>{n}</a>' for p, n in NAV_REGIONS)
    cur = lambda k: ' aria-current="page"' if current == k else ""
    return f'''<div class="topbar"><div class="wrap"><span>Free reroof quotes right across Auckland</span><span>Call or text Mike: <a href="tel:{TEL}">{PHONE}</a></span></div></div>
<header class="site-header"><div class="wrap">
  <a class="logo" href="{pg.u("")}" aria-label="The Roof Crew home">{LOGO}The Roof Crew</a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  <nav class="nav" id="nav" aria-label="Main">
    <div class="dd"><button aria-expanded="false"{cur("services")}>Services <span aria-hidden="true">▾</span></button>
      <div class="dd-menu"><a class="first" href="{pg.u("services/")}">All services</a>{svc_items}</div></div>
    <a href="{pg.u("about/")}"{cur("about")}>About</a>
    <div class="dd"><button aria-expanded="false"{cur("locations")}>Locations <span aria-hidden="true">▾</span></button>
      <div class="dd-menu"><a class="first" href="{pg.u("locations/")}">All areas we cover</a>{reg_items}</div></div>
    <a href="{pg.u("blog/")}"{cur("blog")}>Blog</a>
  </nav>
  <div class="header-actions">
    <a class="btn btn-outline" href="tel:{TEL}">{ICONS["phone"]}{PHONE}</a>
    <a class="btn btn-primary" href="#get-quote"><span class="lg">Get my free quote</span><span class="sm">Free quote</span></a>
  </div>
</div></header>'''


def footer(pg):
    svc = "".join(f'<li><a {pg.link(p)}>{n}</a></li>' for p, n in FOOT_SERVICES)
    sysl = "".join(f'<li><a {pg.link(m["path"])}>{m["name"]}</a></li>' for m in C.MATERIALS)
    reg = "".join(f'<li><a {pg.link(p)}>{n}</a></li>' for p, n in NAV_REGIONS)
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div><a class="logo" href="{pg.u("")}">{LOGO}The Roof Crew</a>
      <p style="margin-top:14px">Family-owned Auckland roofers. Reroofing, new roofs, repairs, spouting and inspections.</p>
      <p class="trust">RANZ member · Fully guaranteed · Finance available</p></div>
    <div><h4>Services</h4><ul>{svc}</ul></div>
    <div><h4>Roofing options</h4><ul>{sysl}</ul></div>
    <div><h4>Locations</h4><ul><li><a href="{pg.u("locations/")}">All areas</a></li>{reg}</ul></div>
    <div><h4>Talk to Mike</h4><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{pg.u("about/")}">About us</a></li><li><a href="{pg.u("blog/")}">Blog</a></li><li><a href="{pg.u("contact/")}">Contact</a></li></ul>
      <a class="btn btn-primary" style="margin-top:18px" href="#get-quote">Get my free quote</a></div>
  </div>
  <div class="legal"><span>© The Roof Crew, Auckland · <a href="{pg.u("privacy-policy/")}">Privacy policy</a></span><span>Staging preview, not live</span></div>
</div></footer>
<script src="{pg.r}assets/js/site.js"></script>'''


OPTIONS = ["New roof (reroof)", "Leaks keep coming back", "Not sure, please check it", "Roof repair", "Spouting or downpipes", "Inspection or report", "New build roof"]
VISIT_SUB = "Free, no pressure. " + C.RESPOND


def quote_form(pg, fid, title="Get a free quote", sub=VISIT_SUB, pre="New roof (reroof)", tag="h2"):
    opts = "".join(f'<option{" selected" if o == pre else ""}>{o}</option>' for o in OPTIONS)
    return f'''<div class="quote-card" id="{fid}">
  <{tag}>{title}</{tag}><p class="sub">{sub}</p>
  <form class="form" data-quote>
    <div><label for="{fid}-name">Name</label><input id="{fid}-name" name="name" autocomplete="name" required></div>
    <div><label for="{fid}-phone">Phone</label><input id="{fid}-phone" name="phone" type="tel" autocomplete="tel" required></div>
    <div class="full"><label for="{fid}-email">Email</label><input id="{fid}-email" name="email" type="email" autocomplete="email"></div>
    <div class="full"><label for="{fid}-addr">Suburb or address</label><input id="{fid}-addr" name="address" autocomplete="street-address"></div>
    <div class="full"><label for="{fid}-need">What's going on with your roof?</label><select id="{fid}-need" name="need">{opts}</select></div>
    <div class="full"><label for="{fid}-msg">Anything else? (optional)</label><textarea id="{fid}-msg" name="message"></textarea></div>
    <div class="full"><button class="btn btn-primary btn-block" type="submit">Get my free quote →</button></div>
    <p class="full fine">Mike will call you back personally. No sales pressure. <a href="{pg.u("privacy-policy/")}">Privacy policy</a></p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks, <span data-first></span>.</strong>Mike will be in touch to book your free site visit. (Staging preview: this form is not connected yet.)</div>
</div>'''


def closing(pg, pre="New roof (reroof)", heading="Your roof, your real number.", lede="Tell us a bit about your property and Mike will get back to you personally."):
    return f'''<section id="request"><div class="wrap closing">
  <div>
    <span class="eyebrow">Request a quote</span>
    <h2>{heading}</h2>
    <p class="lede">{lede}</p>
    <ol class="steps">
      <li><span class="n">1</span><div><b>Send your details</b><span>Takes about a minute, or just call or text.</span></div></li>
      <li><span class="n">2</span><div><b>Mike gets in touch</b><span>We aim to respond within 3 hours, and usually visit within the next working day.</span></div></li>
      <li><span class="n">3</span><div><b>A clear, itemised quote</b><span>Fixed, transparent and no pressure.</span></div></li>
    </ol>
    <div class="contact-box"><a href="tel:{TEL}">{ICONS["phone"]} {PHONE}</a><a href="mailto:{EMAIL}">{ICONS["mail"]} {EMAIL}</a></div>
  </div>
  {quote_form(pg, "get-quote", "Get your free quote", "Free and no pressure.", pre)}
</div></section>'''


def signs_list(items=None):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in (items or C.HOME["signs"])) + "</ul>"


COLOURS = [("Titania", "#e4e1d6"), ("Gull Grey", "#a4a9a7"), ("Desert Sand", "#c8b58f"), ("Sandstone Grey", "#8a897f"),
           ("Thunder Grey", "#5d605f"), ("Karaka", "#3a4a3e"), ("Grey Friars", "#4a4c4f"), ("Ironsand", "#3a3631")]  # approximate screen shades


def swatches():
    return '<ul class="swatches">' + "".join(f'<li><span class="sw" style="--c:{c}"></span>{n}</li>' for n, c in COLOURS) + "</ul>"


def pricing_panel(pg, heading, intro):
    groups = ""
    labels = [("Small home", "Roof area under 100m²"), ("Standard home", "Roof 100 to 180m²"), ("Large or complex", "Roof 180m²+")]
    ask = "Fixed quote on site"
    for key, vals in PRICES.items():
        bands = "".join(f'<div class="band"><small>{l}</small>' + (f'<b>{v}</b>' if v else f'<b class="ask">{ask}</b>') + f'<span>{s}</span></div>' for (l, s), v in zip(labels, vals))
        groups += f'<div class="bands" data-prices="{key}"{"" if key == "longrun" else " hidden"}>{bands}</div>'
    return f'''<div class="card prices">
  <div class="prices-head"><div><h3>{heading}</h3><div class="prices-intro">{intro}</div></div>
    <div><span class="filter-label">Filter: roof type</span><div class="track" data-track="prices"><button type="button" data-value="longrun" aria-pressed="true">COLORSTEEL</button><button type="button" data-value="metal" aria-pressed="false">Metal tile</button></div></div></div>
  {groups}
  <div class="colours"><div><h3>Pick your colour</h3><p>A few popular COLORSTEEL® colours. Shades are approximate on screen, we'll bring real samples to your quote.</p></div>
    {swatches()}</div>
  <div class="prices-foot"><span>A huge range of COLORSTEEL® colours and profiles</span><a class="btn btn-primary" href="#get-quote">Get my exact price →</a></div>
</div>'''


def material_card(pg, m, title, text, more):
    alt = _html.escape(m.get("system_alt") or strip_tags(m["system"]) + " roof")
    return (f'<article class="card system"><div class="img"><img src="{pg.r}assets/img/{m["system_img"]}" alt="{alt}" loading="lazy"></div>'
            f'<div class="body"><h3>{title}</h3><p>{text}</p><a {pg.link(m["path"], "link")}>{more}</a></div></article>')


def systems_cards(pg):
    return '<div class="grid-3">' + "".join(material_card(pg, m, m["system"], m["system_text"], f'{m["name"]} →') for m in C.MATERIALS) + "</div>"


def services_grid(pg, wide=False):
    feat = C.SERVICE_PAGES[0]
    others = ""
    for s in C.SERVICES_ONLY[1:]:
        text = s["card"] if wide else s["home_card"]
        others += f'<article class="card"><div class="icon">{ICONS[s["icon"]]}</div><h3>{s["name"]}</h3><p>{text}</p><a {pg.link(s["path"], "link")}>Learn more →</a></article>'
    ftext = feat["card"] if wide else feat["home_card"]
    feature = f'''<article class="card feature"><div class="feature-img"><img src="{pg.r}assets/img/colorsteel-installed.jpg" alt="New COLORSTEEL roof installed by The Roof Crew" loading="lazy"></div>
      <div class="body"><span class="badge">Most requested</span><h3 style="font-size:26px">{feat["name"]}</h3><p>{ftext}</p>
      <a class="btn btn-primary" href="{pg.u(feat["path"])}">See reroofing →</a></div></article>'''
    if wide:
        return f'<div class="services services-wide">{feature}</div><div class="grid-4" style="margin-top:20px">{others}</div>'
    return f'<div class="services">{others}{feature}</div>'


def review_card(review):
    if isinstance(review, str):  # a placeholder: the review is still to be picked
        return f'<figure class="card review"><div class="stars">★★★★★</div><blockquote>{review}</blockquote></figure>'
    t, n = review
    return f'<figure class="card review"><div class="stars">★★★★★</div><blockquote>{t}</blockquote><cite>{n}</cite></figure>'


def rating_card():
    return f'''<div class="card rating-card"><span class="g">{ICONS["google"]} Google reviews</span><b>{RATING}</b><div class="stars">★★★★★</div>
    <p style="font-size:15px;color:var(--gray-500)">Google rating</p><a class="link" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener" style="display:inline-block;margin-top:12px">Read all reviews on Google →</a></div>'''


def reviews_row(pg, which="home", local=None):
    """home/about: the three real reviews. With local: the page's own review first, then two of the real ones."""
    if which == "reroof":
        return "".join(review_card(r) for r in REAL_REVIEWS[2:])
    reviews = [local] + REAL_REVIEWS[:2] if local else REAL_REVIEWS
    return f'<div class="reviews">\n  {rating_card()}\n  {"".join(review_card(r) for r in reviews)}</div>'


def faq_block(items):
    return '<div class="faqs">' + "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i, (q, a) in enumerate(items)) + "</div>"


def faq_section(title, items, alt):
    return f'{sec(alt)}<div class="wrap"><h2 style="margin-bottom:30px">{title}</h2>{faq_block(items)}</div></section>'


def faq_schema(items):
    # questions whose answer is still only a placeholder for Mike stay out of the schema
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
        for q, a in items if not strip_tags(a).startswith("[")]}


def merge_classes(html):
    """Join tags that ended up with two class attributes."""
    def fix(m):
        tag = m.group(0)
        classes = re.findall(r'\sclass="([^"]*)"', tag)
        if len(classes) < 2:
            return tag
        tag = re.sub(r'\sclass="[^"]*"', "", tag)
        return tag.replace(">", f' class="{" ".join(classes)}">', 1) if tag.endswith(">") else tag
    return re.sub(r"<a\b[^>]*>", fix, html)


def write(path, html):
    dest = os.path.join(OUT, path, "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)


def page(pg, title, desc, current, body, schema=None):
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    html = f'''<!doctype html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title, quote=False)}</title>
<meta name="description" content="{_html.escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{pg.r}assets/css/site.css">
<link rel="icon" href="{pg.r}assets/icons/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="{pg.r}assets/icons/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{pg.r}assets/icons/favicon-192.png">
<link rel="apple-touch-icon" href="{pg.r}assets/icons/apple-touch-icon.png">
{ld}
</head>
<body>
{header(pg, current)}
<main>
{body}
</main>
{footer(pg)}
</body>
</html>
'''
    html = merge_classes(html)
    if pg.path != "quote/":  # every quote button goes to the quote page
        html = html.replace('href="#get-quote"', f'href="{pg.u("quote/")}"')
    write(pg.path, html)


def hero_page(pg, img, eyebrow, h1, lede, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="hero page-hero"><div class="hero-bg" style="background-image:url('{pg.r}assets/img/{img}')"></div>
<div class="wrap"><div>
  <span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{lede_html}
  <div class="hero-actions"><a class="btn btn-primary" href="#get-quote">Get my free quote →</a><a class="btn btn-outline-light" href="tel:{TEL}">Call or text Mike · {PHONE}</a></div>{extra}
</div></div></section>'''


def hold_note(text):
    """Page-wide notice under the hero for a page that is waiting on Mike."""
    return f'\n<div class="hold-note"><div class="wrap">{text}</div></div>' if text else ""


def crumb(pg, parent_path, parent_name, name):
    return f'<a href="{pg.u(parent_path)}" style="color:inherit">{parent_name}</a> / {name}'


def section_block(eyebrow, heading, html, alt):
    return f'''
{sec(alt)}<div class="wrap narrow">
  <span class="eyebrow">{eyebrow}</span><h2 style="margin-bottom:22px">{heading}</h2>
  <div class="prose">{html}</div>
</div></section>'''


# ------------------------------------------------------------------ HOME
def build_home():
    pg = Page("")
    H = C.HOME
    projects_js = "window.RC_PROJECTS=" + json.dumps({k: {"before": f"assets/img/{b}", "after": f"assets/img/{a}", "alt": alt, "caption": cap} for k, (b, a, alt, cap) in PROJECTS.items()}) + ";"
    p1 = PROJECTS["p1"]
    regions = "".join(f'<a {pg.link(r["path"])}>{r["name"]} <span aria-hidden="true">→</span></a>' for r in C.REGIONS)
    popular = " · ".join(f'<a {pg.link(C.LOC_BY_SLUG[s]["path"])}>{C.LOC_BY_SLUG[s]["name"]}</a>' for s in C.LOCATIONS_PAGE["popular"])
    why = "".join(f'<li><span class="num">{i + 1:02d}</span><div><h3>{h}</h3><p>{t}</p></div></li>' for i, (h, t) in enumerate(H["why"]))
    body = f'''
<section class="hero"><div class="hero-bg" style="background-image:url('assets/img/hero-metal-tile.jpg')"></div>
<div class="wrap">
  <div>
    <div class="chips"><span class="chip rating">{ICONS["google"]} {RATING} <span class="stars">★★★★★</span> Google rating</span><span class="chip">Auckland roofing specialists</span></div>
    <h1>{H["h1"]}</h1>
    <p class="lede">{H["intro"]}</p>
    <div class="hero-actions"><a class="btn btn-outline-light" href="tel:{TEL}">{ICONS["phone"]} Call or text Mike · {PHONE}</a></div>
  </div>
  {quote_form(pg, "hero-quote", "Get a free quote")}
</div></section>

<section class="stats"><div class="wrap grid">
  <div class="stat"><b>1,000+</b><span>Auckland roofs completed</span></div>
  <div class="stat"><b>35+</b><span>Years in the building industry</span></div>
  <div class="stat"><b>RANZ</b><span>Roofing Association of NZ member</span></div>
</div></section>

<section class="alt" style="margin-top:-60px;padding-top:140px"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Services</span><h2>What we do</h2></div>
    <p class="lede">{H["what_we_do"]}</p></div>
  {services_grid(pg)}
</div></section>

<section class="dark" id="options"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Roofing options</span><h2>{H["options_h2"]}</h2></div>
    <p class="lede">{H["options_lede"]}</p></div>
  {systems_cards(pg)}
  {pricing_panel(pg, H["cost_h"], H["cost_html"])}
</div></section>

<section class="alt" id="work"><div class="wrap ba-wrap">
  <div class="ba-side">
    <div><span class="eyebrow">See the difference</span><h2>The upgrade your whole street notices.</h2><p class="lede">Drag the slider to see a real Auckland reroof, start to finish.</p></div>
    <div><span class="filter-label">Filter: choose a project</span>
      <div class="track" data-track="projects"><button type="button" data-value="p1" aria-pressed="true">Concrete tile</button><button type="button" data-value="p2" aria-pressed="false">COLORSTEEL</button><button type="button" data-value="p3" aria-pressed="false">Metal tile</button></div></div>
    <p data-project-caption style="font-size:15px;color:var(--gray-500)">{p1[3]}</p>
    <hr>
    <a class="btn btn-primary" href="#get-quote">Get my free quote →</a>
  </div>
  <div class="ba" aria-label="Before and after slider">
    <img class="before" src="assets/img/{p1[0]}" alt="Before the reroof">
    <img class="after" src="assets/img/{p1[1]}" alt="{p1[2]}">
    <span class="lbl l">Before</span><span class="lbl r">After</span>
    <div class="handle"></div><div class="knob">‹›</div>
    <input type="range" min="0" max="100" value="50" aria-label="Compare before and after">
  </div>
</div></section>
<script>{projects_js}</script>

<section class="dark" id="areas"><div class="wrap areas">
  <div>
    <span class="eyebrow">Where we work</span><h2>Reroofing right across Auckland.</h2>
    <p class="lede">From Warkworth in the north to Franklin and south of the Bombay Hills. Find your area.</p>
    <div class="region-links">{regions}<a class="ask" href="tel:{TEL}">Not sure? Ask Mike <span aria-hidden="true">→</span></a></div>
    <p class="popular">Popular areas: {popular}</p>
    <p style="margin-top:14px"><a class="link" href="locations/">See all areas we cover →</a></p>
  </div>
  <div class="map"><iframe title="Map of the areas The Roof Crew covers" src="{MAP_AUCKLAND}" loading="lazy"></iframe></div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>Signs it's time for a new roof</h2>
  <div class="signs" style="margin-top:32px">
    <div class="card">{signs_list()}</div>
    <div class="photo"><img src="assets/img/colorsteel-before.jpg" alt="An old, tired roof ready for replacement" loading="lazy"></div>
  </div>
  <div class="card unsure"><p>{H["signs_after"]}</p>
    <div class="acts"><a class="btn btn-primary" href="#get-quote">Get my free reroof or repair quote</a></div></div>
</div></section>

<section class="dark why"><div class="wrap">
  <span class="eyebrow">The Roof Crew difference</span>
  <h2>{H["why_h2"]}</h2>
  <hr class="rule">
  <div class="why-grid">
    <div class="why-photo"><img src="assets/img/photo-sunset-roof.jpg" alt="A new roof finished by The Roof Crew at sunset" loading="lazy"><div class="why-badge"><b>Since 2014</b><span>Roofing Auckland homes</span></div></div>
    <div>
      <p class="lede">There's a reason we have a 4.7 star rating.</p>
      <ol class="why-list">{why}</ol>
      <p style="margin-top:26px"><a class="link" href="about/">About us →</a></p>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">What Auckland homeowners say</h2>
  {reviews_row(pg)}
</div></section>

<section class="band-cta"><div class="wrap"><div class="inner">
  <div><h2>Ready for a roof that's sorted before the next storm?</h2><p>Get it checked now, not after the next downpour.</p></div>
  <a class="btn btn-white" href="#get-quote">Get my free quote →</a>
</div></div></section>

<section class="dark"><div class="wrap"><h2 style="margin-bottom:30px">Common questions</h2>{faq_block(H["faqs"])}</div></section>
{closing(pg, heading=H["cta_h"], lede=H["cta_text"]).replace('id="get-quote"', 'id="quote-bottom"')}'''
    # header and CTA buttons on the home page go to the hero form
    body = body.replace('id="hero-quote"', 'id="get-quote"')
    business = {"@context": "https://schema.org", "@type": "RoofingContractor", "name": "The Roof Crew", "telephone": "+64 21 903 822",
                "email": EMAIL, "areaServed": [r["name"] for r in C.REGIONS], "address": {"@type": "PostalAddress", "addressLocality": "Auckland", "addressCountry": "NZ"}}
    page(pg, H["title"], H["desc"], "home", body, [business, faq_schema(H["faqs"])])


# ------------------------------------------------------------------ SERVICES
def build_services():
    pg = Page("services/")
    S = C.SERVICES_PAGE
    materials = "".join(material_card(pg, m, m["name"], m["card"], "Learn more →") for m in C.MATERIALS)
    body = hero_page(pg, "bg-colorsteel.jpg", "Services", S["h1"], S["intro"])
    body += f'''
<section><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">What we do</span><h2>Our services</h2></div></div>
  {services_grid(pg, wide=True)}
</div></section>
<section class="alt"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Roofing options</span><h2>Roofing materials</h2></div></div>
  <div class="grid-3">{materials}</div>
</div></section>
<section><div class="wrap"><div class="card unsure" style="margin:0">
  <div><h3>{S["cta_h"]}</h3><p>{S["cta_text"]}</p></div>
  <div class="acts"><a {pg.link("services/roof-inspections/", "link")}>Book an inspection →</a><a class="btn btn-primary" href="tel:{TEL}">{ICONS["phone"]} Call Mike · {PHONE}</a></div>
</div></div></section>
{closing(pg)}'''
    page(pg, S["title"], S["desc"], "services", body)


def reroof_extra(pg):
    """Reroofing page: how a reroof works, the cost section with the options and price panel, the before/after slider."""
    p = PROJECTS["p2"]
    steps = "".join(f'<li><span class="n">{i + 1}</span><div><b>{h}</b><span>{t}</span></div></li>' for i, (h, t) in enumerate(C.REROOF_STEPS))
    return f'''
<section class="alt"><div class="wrap">
  <span class="eyebrow">How it works</span><h2>How a reroof works</h2>
  <ol class="steps steps-row">{steps}</ol>
</div></section>
<section id="options"><div class="wrap">
  <span class="eyebrow">Options and price ranges</span><h2 style="margin-bottom:32px">Choose your roof.</h2>
  {systems_cards(pg)}
  {pricing_panel(pg, C.REROOF_COST_H, C.REROOF_COST)}
</div></section>
<section class="alt" id="work"><div class="wrap ba-wrap">
  <div class="ba-side"><div><span class="eyebrow">Project photos</span><h2>A real Auckland reroof.</h2><p class="lede">Drag the slider to compare.</p></div>
    {reviews_row(pg, "reroof")}</div>
  <div class="ba"><img class="before" src="{pg.r}assets/img/{p[0]}" alt="Before the reroof"><img class="after" src="{pg.r}assets/img/{p[1]}" alt="{p[2]}">
    <span class="lbl l">Before</span><span class="lbl r">After</span><div class="handle"></div><div class="knob">‹›</div><input type="range" min="0" max="100" value="50" aria-label="Compare before and after"></div>
</div></section>'''


def fill(html):
    """Section html with the colour swatches filled in."""
    return html.replace("__SWATCHES__", swatches())


# ------------------------------------------------------------------ SERVICE AND MATERIAL PAGES (one template)
def build_service(s):
    pg = Page(s["path"])
    name = strip_tags(s["name"])
    body = hero_page(pg, s["hero"], crumb(pg, "services/", "Services", name), s["h1"], s["lede"])
    body += hold_note(s.get("hold"))
    secs = s["sections"]
    if secs:
        h, html = secs[0]
        body += f'''
<section><div class="wrap split">
  <div><span class="eyebrow">{s["name"]}</span><h2 style="margin-bottom:18px">{h}</h2><div class="prose">{fill(html)}</div></div>
  <div class="photo" style="min-height:420px"><img src="{pg.r}assets/img/{s["photo"]}" alt="{_html.escape(name)} by The Roof Crew" loading="lazy"></div>
</div></section>'''
    alt = bool(secs)
    if s.get("reroof"):
        body += reroof_extra(pg)
        alt = False
    for h, html in secs[1:]:
        body += section_block(s["name"], h, fill(html), alt)
        alt = not alt
    if s["faqs"]:
        body += faq_section(s["faq_h"], s["faqs"], alt)
        alt = not alt
    other = "".join(f'<li><a {pg.link(o["path"], "link")}>{o["name"]}</a></li>' for o in C.SERVICE_PAGES if o is not s)
    body += f'''
{sec(alt)}<div class="wrap">
  <div class="card"><h3>Other services</h3><ul class="ticks cols-2">{other}</ul></div>
</div></section>
{closing(pg, s["pre"], s["closing"])}'''
    page(pg, s["title"], s["desc"], "services", body, [faq_schema(s["faqs"])] if s["faqs"] else None)


# ------------------------------------------------------------------ LOCATIONS
def area_card(pg, l, small):
    return f'<a class="card region-card" {pg.link(l["path"])}><h3>{l["name"]}</h3><small>{small}</small><span class="link" style="margin-top:8px">See {l["name"]} →</span></a>'


def build_locations():
    pg = Page("locations/")
    L = C.LOCATIONS_PAGE
    regions = "".join(area_card(pg, r, r["blurb"]) for r in C.REGIONS)
    areas = "".join(area_card(pg, C.LOC_BY_SLUG[s], C.LOC_BY_SLUG[s]["region"]) for s in L["popular"])
    body = hero_page(pg, "bg-local-street.jpg", "Locations", L["h1"], L["intro"])
    body += f'''
<section><div class="wrap">
  <span class="eyebrow">Areas we cover</span><h2 style="margin-bottom:32px">{L["find_h"]}</h2>
  <div class="grid-4" data-regions>{regions}</div>
</div></section>
<section class="alt"><div class="wrap">
  <span class="eyebrow">Suburbs</span><h2 style="margin-bottom:32px">{L["popular_h"]}</h2>
  <div class="grid-3" data-areas>{areas}</div>
</div></section>
<section><div class="wrap areas" style="align-items:start">
  <div><span class="eyebrow">Service area</span><h2>{L["ask_h"]}</h2><p class="lede">{L["ask_text"]}</p>
    <p style="margin-top:22px"><a class="btn btn-primary" href="#get-quote">Get my free quote →</a></p></div>
  <div class="map"><iframe title="Map of Auckland service area" src="{MAP_AUCKLAND}" loading="lazy"></iframe></div>
</div></section>
{closing(pg)}'''
    page(pg, L["title"], L["desc"], "locations", body)


def suburb_chips(pg, l):
    out = ""
    for s in l["suburbs"]:
        if s.startswith("# "):  # a group heading, e.g. "South of the Bombay Hills"
            out += f'</div><h3 style="margin-top:28px">{s[2:]}</h3><div class="suburbs">'
            continue
        other = C.LOC_BY_NAME.get(s)
        label = P(s, l["suburbs_q"]) if l.get("suburbs_q") else s
        out += f'<a {pg.link(other["path"])}>{label}</a>' if other and other is not l else f"<span>{label}</span>"
    return out


# ------------------------------------------------------------------ REGION AND AREA PAGES (the East Auckland template)
def build_location(l):
    pg = Page(l["path"])
    name = l["name"]
    svc = "".join(f'<article class="card"><div class="icon">{ICONS[s["icon"]]}</div><h3>{s["name"]}</h3><a {pg.link(s["path"], "link")}>{s["name"]} in {name} →</a></article>' for s in C.SERVICES_ONLY)
    photo = l.get("photo", l["hero"])
    side = (f'<div class="ph-box ph-job">{l["job"]}</div>' if l.get("job")
            else f'<div class="photo" style="min-height:360px"><img src="{pg.r}assets/img/{photo}" alt="Roof in {name}" loading="lazy"></div>')
    linked = any(C.LOC_BY_NAME.get(s) not in (None, l) for s in l["suburbs"])
    body = hero_page(pg, l["hero"], crumb(pg, "locations/", "Locations", name), l["h1"], l["lede"])
    body += f'''
<section><div class="wrap split">
  <div class="prose"><span class="eyebrow">Roofing in {name}</span><h2 style="margin-bottom:18px">{l["local_h"]}</h2>
    {l["local"]}</div>
  {side}
</div></section>
<section class="alt"><div class="wrap">
  <span class="eyebrow">Services</span><h2 style="margin-bottom:32px">What we do in {name}</h2>
  <div class="grid-3">{svc}</div>
</div></section>'''
    alt = False
    if l.get("cost"):
        body += section_block("Cost", l["cost"][0], l["cost"][1], alt)
        alt = not alt
    body += f'''
{sec(alt)}<div class="wrap">
  <span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">What Auckland homeowners say</h2>
  {reviews_row(pg, local=l.get("review"))}
</div></section>'''
    alt = not alt
    if l["faqs"]:
        body += faq_section(l["faq_h"], l["faqs"], alt)
        alt = not alt
    note = ("Highlighted suburbs have their own page. " if linked else "") + "Don't see yours? We probably still cover it, just ask."
    body += f'''
{sec(alt)}<div class="wrap areas" style="align-items:start">
  <div><span class="eyebrow">Suburbs we cover</span><h2>{name} suburbs</h2>
    <p class="lede">{note}</p>
    <div class="suburbs">{suburb_chips(pg, l)}</div></div>
  <div class="map"><iframe title="Map of {name}" src="{l["map"]}" loading="lazy"></iframe></div>
</div></section>
{closing(pg, "New roof (reroof)", f"Get a free quote in {name}.")}'''
    page(pg, l["title"], l["desc"], "locations", body, [faq_schema(l["faqs"])] if l["faqs"] else None)


# ------------------------------------------------------------------ ABOUT
def build_about():
    pg = Page("about/")
    A = C.ABOUT
    cards = "".join(f'<div class="card"><div class="icon">{ICONS[i]}</div><h3>{h}</h3><p>{t}</p></div>' for i, h, t in A["backed"])
    body = f'''<section class="hero page-hero"><div class="hero-bg" style="background-image:url('{pg.r}assets/img/bg-crew.jpg')"></div>
<div class="wrap"><div><span class="eyebrow">About us</span><h1>{A["h1"]}</h1>
<p class="lede">{A["intro"]}</p>
<div class="hero-actions"><a class="btn btn-primary" href="#get-quote">Get my free quote →</a></div></div></div></section>
<section><div class="wrap split">
  <div class="prose"><span class="eyebrow">Our story</span><h2 style="margin-bottom:18px">{A["why_h"]}</h2>
    {paras(A["why"])}</div>
  <div class="photo" style="min-height:400px"><img src="{pg.r}assets/img/bg-crew.jpg" alt="The Roof Crew team on site" loading="lazy"></div>
</div></section>
<section class="alt"><div class="wrap narrow"><span class="eyebrow">On site</span><h2 style="margin-bottom:22px">{A["care_h"]}</h2>
  <div class="prose">{paras(A["care"])}</div>
</div></section>
<section><div class="wrap"><span class="eyebrow">Accreditations and warranty</span><h2 style="margin-bottom:32px">{A["backed_h"]}</h2>
  <div class="grid-3">{cards}</div>
</div></section>
<section class="alt"><div class="wrap"><span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">{A["reviews_h"]}</h2>{reviews_row(pg, "about")}</div></section>
{closing(pg)}'''
    page(pg, A["title"], A["desc"], "about", body)


# ------------------------------------------------------------------ QUOTE
def build_quote():
    pg = Page("quote/")
    faqs = [
        ("What happens after I send my details?", "We aim to respond within 3 hours. Mike calls you back personally, asks a few questions about your roof and books a free site visit, usually within the next working day."),
        ("Is the quote really free?", "Yes. The site visit and quote are free, with no obligation and no sales pressure."),
        ("Will the price change later?", "No. After the site visit you get a fixed, itemised price, so there are no surprises."),
        ("Do you do repairs as well as reroofs?", "Yes. Whether it's one leak or a whole new roof, use the same form and tell us what's going on."),
    ]
    body = f'''<section class="hero page-hero" style="padding-block:56px 64px"><div class="hero-bg" style="background-image:url('{pg.r}assets/img/hero-metal-tile.jpg')"></div>
<div class="wrap"><div><span class="eyebrow">Free quote</span><h1>Get your free roof quote.</h1><p class="lede">Reroof or repair, tell us about your roof and Mike will get back to you personally with a fixed price.</p>
<div class="chips" style="margin-top:22px"><span class="chip rating">{ICONS["google"]} {RATING} <span class="stars">★★★★★</span> Google rating</span><span class="chip">Roofing Auckland since 2014</span></div></div></div></section>
{closing(pg, "New roof (reroof)", "Your roof, your real number.")}
<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">What happens next</h2>{faq_block(faqs)}</div></section>'''
    page(pg, "Get a free roof quote | The Roof Crew", "Free, no-pressure reroof and repair quotes across Auckland. Send your details and Mike gets back to you with a fixed price.", "quote", body, [faq_schema(faqs)])


# ------------------------------------------------------------------ CONTACT
def build_contact():
    pg = Page("contact/")
    faqs = [
        ("What happens after I get in touch?", "We aim to respond within 3 hours. Mike calls you back personally, asks a few questions and books a free site visit, usually within the next working day."),
        ("Is the quote really free?", "Yes. The site visit and quote are free, with no obligation and no sales pressure."),
        ("Do you cover my area?", "We cover the wider Auckland region, " + C.AREA_LINE + ". If you're not sure, just ask."),
    ]
    regs = "".join(f'<a {pg.link(r["path"])}>{r["name"]}</a>' for r in C.REGIONS)
    body = f'''<section class="hero page-hero" style="padding-block:56px 64px"><div class="hero-bg" style="background-image:url('{pg.r}assets/img/bg-local-street.jpg')"></div>
<div class="wrap"><div><span class="eyebrow">Contact</span><h1>Talk to Mike.</h1><p class="lede">Call, text or send your details and Mike will get back to you personally.</p></div></div></section>
<section><div class="wrap closing">
  <div><h2>Get in touch</h2>
    <div class="contact-box" style="margin-top:24px"><a href="tel:{TEL}">{ICONS["phone"]} {PHONE}</a><a href="mailto:{EMAIL}">{ICONS["mail"]} {EMAIL}</a><span>Hours: Mon to Fri 8am to 6pm, Sat 9am to 1pm, Sun closed</span></div>
    <h3 style="margin-top:36px">Areas we cover</h3>
    <div class="suburbs">{regs}</div>
    <p style="margin-top:14px;font-size:15px;color:var(--gray-500)">We come to you. No street address is listed because the crew works on site across Auckland.</p>
  </div>
  {quote_form(pg, "get-quote", "Get your free quote", "Free and no pressure.")}
</div></section>
<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">What happens next</h2>{faq_block(faqs)}</div></section>'''
    page(pg, "Contact The Roof Crew | Free roof quotes in Auckland", "Call or text Mike on 021 903 822, or send your details for a free, no-pressure roof quote.", "contact", body)


# ------------------------------------------------------------------ BLOG AND PRIVACY (current live copy, moved across)
def nz_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def live_links(html, to_url):
    """Point links at the current site to the same page on the new site."""
    def fix(m):
        path = m.group(1)
        return f'href="{to_url(C.LINK_MAP[path])}"' if path in C.LINK_MAP else m.group(0)
    return re.sub(r'href="' + re.escape(C.LIVE) + r'([^"#?]*)"', fix, html)


def excerpt(p, words=26):
    body = re.sub(r"<p><em>.*?</em></p>", "", p["html"])
    first = re.search(r"<p>(.*?)</p>", body, re.S)
    w = _html.unescape(strip_tags(first.group(1) if first else "")).split()
    return _html.escape(" ".join(w[:words]), quote=False) + ("…" if len(w) > words else "")


def post_card(pg, p):
    return (f'<a class="card post-card" href="{pg.u(p["slug"] + "/")}"><div class="img"><img src="{pg.r}assets/img/{p["image"]}" alt="" loading="lazy"></div>'
            f'<div class="body"><small>{nz_date(p["date"])}</small><h3>{p["title"]}</h3><p>{excerpt(p)}</p><span class="link">Read more →</span></div></a>')


def build_blog():
    pg = Page("blog/")
    B = C.BLOG_PAGE
    cards = "".join(post_card(pg, p) for p in C.POSTS)
    body = hero_page(pg, "bg-local-street.jpg", "The Roof Crew", B["h1"], "")
    body += f'''
<section><div class="wrap"><div class="grid-3 posts">{cards}</div></div></section>
{closing(pg)}'''
    page(pg, B["title"], B["desc"], "blog", body)


def build_post(p):
    pg = Page(p["slug"] + "/")
    content = live_links(p["html"], pg.u)
    more = "".join(f'<li><a class="link" href="{pg.u(o["slug"] + "/")}">{o["title"]}</a></li>' for o in C.POSTS if o is not p)
    body = hero_page(pg, "bg-local-street.jpg", f'<a href="{pg.u("blog/")}" style="color:inherit">Blog</a> / {nz_date(p["date"])}', p["title"], "")
    body += f'''
<section><div class="wrap narrow">
  <figure class="post-img"><img src="{pg.r}assets/img/{p["image"]}" alt=""></figure>
  <article class="prose post-body">{content}</article>
</div></section>
<section class="band-cta"><div class="wrap"><div class="inner">
  <div><h2>Ready for a roof that's sorted before the next storm?</h2><p>Get it checked now, not after the next downpour.</p></div>
  <a class="btn btn-white" href="#get-quote">Get my free quote →</a>
</div></div></section>
<section class="alt"><div class="wrap"><div class="card"><h3>More from the blog</h3><ul class="ticks">{more}</ul></div></div></section>
{closing(pg)}'''
    article = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": strip_tags(p["title"]), "datePublished": p["date"], "author": {"@type": "Organization", "name": "The Roof Crew"}}
    page(pg, p["seo_title"], p["desc"], "blog", body, [article])


def build_privacy():
    pg = Page("privacy-policy/")
    pr = C.PRIVACY
    body = hero_page(pg, "bg-local-street.jpg", "The Roof Crew", pr["title"], "")
    body += f'\n<section><div class="wrap narrow"><div class="prose post-body">{pr["html"]}</div></div></section>'
    page(pg, pr["seo_title"], pr["desc"], "", body)


def build_redirects():
    """Old addresses: a small page that sends the visitor (and search engines) to the new one."""
    for old, new in C.REDIRECTS.items():
        to = Page(old).u(new)
        write(old, f'''<!doctype html>
<html lang="en-NZ"><head><meta charset="utf-8"><title>Moved | The Roof Crew</title>
<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{to}">
</head><body><p>This page has moved: <a href="{to}">continue to the new page</a>.</p></body></html>
''')


def main():
    img_src = os.path.join(ROOT, "assets", "images")
    img_dst = os.path.join(OUT, "assets", "img")
    os.makedirs(img_dst, exist_ok=True)
    for f in os.listdir(img_src):
        shutil.copy2(os.path.join(img_src, f), os.path.join(img_dst, f))
    for b in (build_home, build_services, build_locations, build_about, build_contact, build_quote, build_blog, build_privacy, build_redirects):
        b()
    for s in C.SERVICE_PAGES:
        build_service(s)
    for l in C.LOCATION_PAGES:
        build_location(l)
    for p in C.POSTS:
        build_post(p)
    pages = [os.path.relpath(os.path.join(d, f), OUT) for d, _, fs in os.walk(OUT) for f in fs if f.endswith(".html")]
    print(f"built v2: {len(pages)} html files")


if __name__ == "__main__":
    main()
