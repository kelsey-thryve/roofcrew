#!/usr/bin/env python3
"""Builds the v2 staging site (7 pages) into v2/.  Run from the repo root:  python3 tools/build_v2.py

Pages: Home, About, Contact, Services (collection), Reroofing (service template),
Locations, East Auckland (region/suburb template). Shared header, footer and quote form.
<mark class="ph"> = content the client supplies or confirms (shows yellow on staging).
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "v2")
PHONE, TEL = "021 903 822", "+6421903822"
EMAIL = "mike@theroofcrew.co.nz"


def P(t):
    return f'<mark class="ph">{t}</mark>'


RATING, NREV = P("4.7"), P("28")
SERVICES = [  # (slug, name, short, built)
    ("reroofing", "Reroofing", "Old roof leaking, rusting or just tired? We strip it, dispose of it responsibly and install a new roof with flashings, ridge capping and full scaffolding.", True),
    ("new-roof-installation", "New roof installation", "New build roofs for homeowners, builders and developers, on time and to spec.", False),
    ("roof-repairs", "Roof repairs", "Leaks, storm damage and slipped or cracked tiles, sorted properly.", False),
    ("guttering-and-downpipes", "Guttering and downpipes", "New spouting and downpipes in colours to match your roof.", False),
    ("roof-inspections", "Roof inspections and reports", "An honest check of your roof's condition, with photos and a written report.", False),
]
REGIONS = [  # (slug, name, blurb, built)
    ("east-auckland", "East Auckland", "Howick, Botany, Pakuranga, Flat Bush, Beachlands and nearby", True),
    ("north-shore", "North Shore", "Takapuna, Devonport, Albany, Glenfield and nearby", False),
    ("south-auckland", "South Auckland", "Manukau, Papakura, Takanini, Pukekohe and nearby", False),
    ("west-auckland", "West Auckland", "Henderson, Te Atatū, Titirangi, Kumeū and nearby", False),
]
SYSTEMS = [
    ("COLORSTEEL® long-run", "colorsteel-installed.jpg", "COLORSTEEL long-run roof", ["40 to 60 year life", "Our most popular option"]),
    ("Pressed metal tile", "hero-metal-tile.jpg", "Pressed metal tile roof", ["The look of tile, the strength of steel", "Light, strong and durable"]),
    ("Concrete tile", "concrete-after.jpg", "Concrete tile roof", ["Thermal and acoustic performance", "Heavier, may need a structural check"]),
]
PRICES = {  # whole-home ranges (placeholders until Mike confirms)
    "longrun": ("$12k to $18k", "$16k to $28k", "$25k to $40k+"),
    "metal": ("[$ range]", "[$ range]", "[$ range]"),
    "concrete": ("[$ range]", "[$ range]", "[$ range]"),
}
PROJECTS = {
    "p1": ("concrete-before.jpg", "concrete-after.jpg", "Concrete tile to new roof", f"{P('[Suburb]')} reroof, concrete tile"),
    "p2": ("colorsteel-before.jpg", "colorsteel-after.jpg", "Tired roof to COLORSTEEL long-run", f"{P('[Suburb]')} reroof, COLORSTEEL® long-run"),
    "p3": ("metaltile-before.jpg", "metaltile-after.jpg", "Old roof to pressed metal tile", f"{P('[Suburb]')} reroof, pressed metal tile"),
}
EAST_SUBURBS = ["Howick", "Botany", "Pakuranga", "Half Moon Bay", "Bucklands Beach", "Cockle Bay", "Dannemora",
                "Flat Bush", "Highland Park", "Eastern Beach", "Shelly Park", "Mellons Bay", "Sunnyhills", "Farm Cove",
                "Burswood", "Golflands", "Whitford", "Beachlands", "Maraetai"]
SUBURB_PAGES = {"Howick", "Botany"}  # planned suburb pages (not in this staging set)
MAP_AUCKLAND = "https://www.openstreetmap.org/export/embed.html?bbox=174.45%2C-37.25%2C175.15%2C-36.62&layer=mapnik"
MAP_EAST = "https://www.openstreetmap.org/export/embed.html?bbox=174.83%2C-36.99%2C175.06%2C-36.84&layer=mapnik"

ICONS = {
    "home": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
    "search": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "drop": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/></svg>',
    "wrench": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/></svg>',
    "build": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><path d="M5 21V9l7-5 7 5v12"/><path d="M9 21v-6h6v6"/></svg>',
    "family": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3 2.5-5 5-5s5 2 5 5"/><path d="M14 20c0-2.5 1.5-4 3.5-4S21 17.5 21 20"/></svg>',
    "clock": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "shield": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "card": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "google": '<svg width="18" height="18" viewBox="0 0 48 48"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2.1 5-4.4 6.6v5.5h7.1C42.6 36.8 45 31.2 45 24.5z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.3c-.4-1.3-.7-2.7-.7-4.3s.3-3 .7-4.3V14H4.5C3 17 2 20.4 2 24s1 7 2.5 10l7.3-5.7z"/><path fill="#EA4335" d="M24 10.7c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg>',
}
SVC_ICON = {"reroofing": "home", "new-roof-installation": "build", "roof-repairs": "wrench", "guttering-and-downpipes": "drop", "roof-inspections": "search"}
LOGO = '<svg width="30" height="30" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="currentColor"/><path d="M7 16l9-8 9 8M10 14v10h12V14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


class Page:
    def __init__(self, path):
        self.path = path  # e.g. "services/reroofing/"
        depth = path.count("/")
        self.r = "../" * depth

    def u(self, target):  # link to another page in v2
        return self.r + target

    def svc_link(self, slug, built):
        return (f'href="{self.u("services/" + slug + "/")}"' if built else 'href="#" class="soon"')

    def region_link(self, slug, built, cls=""):
        if built:
            return f'href="{self.u("locations/" + slug + "/")}"' + (f' class="{cls}"' if cls else "")
        return f'href="#" class="soon{(" " + cls) if cls else ""}"'


def header(pg, current):
    svc_items = "".join(f'<a {pg.svc_link(s, b)}>{n}</a>' for s, n, _, b in SERVICES)
    reg_items = "".join(f'<a {pg.region_link(s, b)}>{n}</a>' for s, n, _, b in REGIONS)
    cur = lambda k: ' aria-current="page"' if current == k else ""
    return f'''<div class="staging" role="note"><div class="wrap"><span><b>Staging preview, not live.</b> <mark>Yellow</mark> = content to supply or confirm.</span><button type="button">Hide highlights</button></div></div>
<div class="topbar"><div class="wrap"><span>Free reroof quotes right across Auckland</span><span>Call or text Mike: <a href="tel:{TEL}">{PHONE}</a></span></div></div>
<header class="site-header"><div class="wrap">
  <a class="logo" href="{pg.u("")}" aria-label="The Roof Crew home">{LOGO}The Roof Crew</a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  <nav class="nav" id="nav" aria-label="Main">
    <div class="dd"><button aria-expanded="false"{cur("services")}>Services <span aria-hidden="true">▾</span></button>
      <div class="dd-menu"><a class="first" href="{pg.u("services/")}">All services</a>{svc_items}</div></div>
    <a href="{pg.u("#options")}">Roofing options</a>
    <a href="{pg.u("#work")}">Our work</a>
    <a href="{pg.u("about/")}"{cur("about")}>About</a>
    <div class="dd"><button aria-expanded="false"{cur("locations")}>Locations <span aria-hidden="true">▾</span></button>
      <div class="dd-menu"><a class="first" href="{pg.u("locations/")}">All areas we cover</a>{reg_items}</div></div>
  </nav>
  <div class="header-actions">
    <a class="btn btn-outline" href="tel:{TEL}">{ICONS["phone"]}{PHONE}</a>
    <a class="btn btn-primary" href="#get-quote"><span class="lg">Get my free quote</span><span class="sm">Free quote</span></a>
  </div>
</div></header>'''


def footer(pg):
    svc = "".join(f'<li><a {pg.svc_link(s, b)}>{n}</a></li>' for s, n, _, b in SERVICES)
    sysl = "".join(f'<li><a href="{pg.u("#options")}">{n}</a></li>' for n, *_ in SYSTEMS)
    reg = "".join(f'<li><a {pg.region_link(s, b)}>{n}</a></li>' for s, n, _, b in REGIONS)
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div><a class="logo" href="{pg.u("")}">{LOGO}The Roof Crew</a>
      <p style="margin-top:14px">{P("Family-owned Auckland roofers. Reroofing, new roofs, repairs, spouting and inspections.")}</p>
      <p class="trust">{P("RANZ member")} · Fully guaranteed · Finance available</p></div>
    <div><h4>Services</h4><ul>{svc}</ul></div>
    <div><h4>Roofing options</h4><ul>{sysl}</ul></div>
    <div><h4>Locations</h4><ul><li><a href="{pg.u("locations/")}">All areas</a></li>{reg}</ul></div>
    <div><h4>Talk to Mike</h4><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{P(EMAIL)}</a></li><li><a href="{pg.u("about/")}">About us</a></li><li><a href="{pg.u("contact/")}">Contact</a></li></ul>
      <a class="btn btn-primary" style="margin-top:18px" href="#get-quote">Get my free quote</a></div>
  </div>
  <div class="legal"><span>© The Roof Crew, Auckland</span><span>Staging preview, not live</span></div>
</div></footer>
<script src="{pg.r}assets/js/site.js"></script>'''


OPTIONS = ["New roof (reroof)", "Leaks keep coming back", "Not sure, please check it", "Roof repair", "Spouting or downpipes", "Inspection or report", "New build roof"]


def quote_form(fid, title="Get a free quote", sub="Free, no pressure. We usually visit within 3 working days.", pre="New roof (reroof)", tag="h2"):
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
    <p class="full fine">Mike will call you back personally. No sales pressure.</p>
  </form>
  <div class="form-done" tabindex="-1"><strong>Thanks, <span data-first></span>.</strong>Mike will be in touch to book your free site visit. (Staging preview: this form is not connected yet.)</div>
</div>'''


def closing(pg, pre="New roof (reroof)", heading="Your roof, your real number."):
    return f'''<section id="request"><div class="wrap closing">
  <div>
    <span class="eyebrow">Request a quote</span>
    <h2>{heading}</h2>
    <p class="lede">Tell us a bit about your property and Mike will get back to you personally.</p>
    <ol class="steps">
      <li><span class="n">1</span><div><b>Send your details</b><span>Takes about a minute, or just call or text.</span></div></li>
      <li><span class="n">2</span><div><b>Mike gets in touch</b><span>Usually with a site visit within 3 working days.</span></div></li>
      <li><span class="n">3</span><div><b>A clear, itemised quote</b><span>Fixed, transparent and no pressure.</span></div></li>
    </ol>
    <div class="contact-box"><a href="tel:{TEL}">{ICONS["phone"]} {PHONE}</a><a href="mailto:{EMAIL}">{ICONS["mail"]} {P(EMAIL)}</a></div>
  </div>
  {quote_form("get-quote", "Get your free quote", "Free and no pressure.", pre)}
</div></section>'''


def signs_list():
    items = ["Leaks keep coming back after repairs", "Roof is 30+ years old", "Water stains on your ceilings",
             "Rust, lifting sheets or cracked tiles", "Faded, chalky or mossy surface", P("[Sign 6, from Mike]")]
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def pricing_panel(pg, heading="What a whole reroof roughly costs"):
    groups = ""
    labels = [("Small home", "Roof area under 100m²"), ("Standard home", "Roof 100 to 180m²"), ("Large or complex", "Roof 180m²+")]
    for key, vals in PRICES.items():
        bands = "".join(f'<div class="band"><small>{l}</small><b>{P(v)}</b><span>{s}</span></div>' for (l, s), v in zip(labels, vals))
        groups += f'<div class="bands" data-prices="{key}"{"" if key == "longrun" else " hidden"}>{bands}</div>'
    return f'''<div class="card prices">
  <div class="prices-head"><div><h3>{heading}</h3><p style="color:var(--gray-500);font-size:15px;margin-top:4px">Indicative {P("2026")} Auckland ranges, not a fixed quote.</p></div>
    <div><span class="filter-label">Filter: roof type</span><div class="track" data-track="prices"><button type="button" data-value="longrun" aria-pressed="true">Long-run</button><button type="button" data-value="metal" aria-pressed="false">Metal tile</button><button type="button" data-value="concrete" aria-pressed="false">Concrete tile</button></div></div></div>
  {groups}
  <div class="prices-foot"><span>{P("12")} COLORSTEEL® colours available · <a class="link soon" href="#">See the colour range</a></span><a class="btn btn-primary" href="#get-quote">Get my exact price →</a></div>
</div>'''


def systems_cards(pg):
    out = ""
    for n, img, alt, pts in SYSTEMS:
        lis = "".join(f"<li>{p}</li>" for p in pts)
        out += f'<article class="card system"><div class="img"><img src="{pg.r}assets/img/{img}" alt="{alt}" loading="lazy"></div><div class="body"><h3>{n}</h3><ul class="mini">{lis}</ul></div></article>'
    return f'<div class="grid-3">{out}</div>'


def services_grid(pg, wide=False):
    feat = SERVICES[0]
    others = ""
    for s, n, short, b in SERVICES[1:]:
        others += f'<article class="card"><div class="icon">{ICONS[SVC_ICON[s]]}</div><h3>{n}</h3><p>{short}</p><a class="link" {pg.svc_link(s, b)}>Learn more →</a></article>'
    feature = f'''<article class="card feature"><div class="feature-img"><img src="{pg.r}assets/img/colorsteel-installed.jpg" alt="New COLORSTEEL roof installed by The Roof Crew" loading="lazy"></div>
      <div class="body"><span class="badge">Most requested</span><h3 style="font-size:26px">{feat[1]}</h3><p>{feat[2]}</p>
      <a class="btn btn-primary" href="{pg.u("services/reroofing/")}">See reroofing →</a></div></article>'''
    if wide:
        return f'<div class="services services-wide">{feature}</div><div class="grid-4" style="margin-top:20px">{others}</div>'
    return f'<div class="services">{others}{feature}</div>'


def reviews_row(pg, which="home"):
    topics = {"home": ["[Real review: leaks fixed for good by a reroof]", "[Real review about a reroof]", "[Real review: tidy site, the crew, the finish]"],
              "about": ["[Real review that mentions Mike or the crew by name]", "[Real review about communication and turning up on time]", "[Real review about value or the guarantee]"],
              "reroof": ["[Real review from a reroof customer]"],
              "east": ["[Real review from an East Auckland customer]"]}[which]
    cards = "".join(f'<figure class="card review"><div class="stars">★★★★★</div><blockquote>{P(t)}</blockquote><cite>{P("[Name]")} · {P("[Suburb]")}</cite></figure>' for t in topics)
    if which in ("reroof", "east"):
        return cards
    return f'''<div class="reviews">
  <div class="card rating-card"><span class="g">{ICONS["google"]} Google reviews</span><b>{RATING}</b><div class="stars">★★★★★</div>
    <p style="font-size:15px;color:var(--gray-500)">Based on {NREV} reviews</p><a class="link" href="#" style="display:inline-block;margin-top:12px">Read all reviews on Google →</a></div>
  {cards}</div>'''


def faq_block(items):
    return '<div class="faqs">' + "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i, (q, a) in enumerate(items)) + "</div>"


def faq_schema(items):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items if not q.startswith("<mark")]}


def merge_classes(html):
    """Join tags that ended up with two class attributes (a link class plus "soon")."""
    import re
    def fix(m):
        tag = m.group(0)
        classes = re.findall(r'\sclass="([^"]*)"', tag)
        if len(classes) < 2:
            return tag
        tag = re.sub(r'\sclass="[^"]*"', "", tag)
        return tag.replace(">", f' class="{" ".join(classes)}">', 1) if tag.endswith(">") else tag
    return re.sub(r"<a\b[^>]*>", fix, html)


def page(pg, title, desc, current, body, schema=None):
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    html = f'''<!doctype html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{pg.r}assets/css/site.css">
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
    dest = os.path.join(OUT, pg.path, "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)


def hero_page(pg, img, eyebrow, h1, lede, extra=""):
    return f'''<section class="hero page-hero"><div class="hero-bg" style="background-image:url('{pg.r}assets/img/{img}')"></div>
<div class="wrap"><div>
  <span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{lede}</p>
  <div class="hero-actions"><a class="btn btn-primary" href="#get-quote">Get my free quote →</a><a class="btn btn-outline-light" href="tel:{TEL}">Call or text Mike · {PHONE}</a></div>{extra}
</div></div></section>'''


# ------------------------------------------------------------------ HOME
def build_home():
    pg = Page("")
    faqs = [
        ("How do I know if my roof needs replacing?", "If leaks keep coming back after repairs, the roof is 30 or more years old, or you can see rust, lifting sheets, cracked tiles or water stains on your ceilings, it is usually time to look at a new roof. Mike will check it on a free site visit and tell you straight whether a repair will do."),
        ("How much does a reroof cost in Auckland?", f"It depends on the size and shape of your roof, access, and the material you choose. The ranges above are a rough guide for small, standard and large homes. After a free site visit you get a fixed, itemised price, so there are no surprises. {P('[Mike to confirm ranges]')}"),
        ("Is it worth repairing my roof, or should I replace it?", "A repair makes sense for a one-off problem on a roof that is otherwise sound. If you are patching the same roof every winter, the money usually goes further on a new roof with a fresh guarantee. We will tell you honestly which one you need."),
        ("How long does a reroof take, and can we stay home?", f"Most homes take {P('[X to Y working days, from Mike]')}, depending on size and weather. You can usually stay home while we work, and we tidy the site at the end of every day."),
        ("Do you offer finance?", f"Yes. Finance is available so you can spread the cost of a new roof. {P('[Finance provider and terms, from Mike]')} Just ask when you book your free quote."),
        (P("[Top question from search / Google Business Profile data]"), P("[A 40 to 60 word answer]")),
    ]
    projects_js = "window.RC_PROJECTS=" + json.dumps({k: {"before": f"assets/img/{b}", "after": f"assets/img/{a}", "alt": alt, "caption": cap} for k, (b, a, alt, cap) in PROJECTS.items()}) + ";"
    p1 = PROJECTS["p1"]
    regions = "".join(f'<a {pg.region_link(s, b)}>{n} <span aria-hidden="true">→</span></a>' for s, n, _, b in REGIONS)
    body = f'''
<section class="hero"><div class="hero-bg" style="background-image:url('assets/img/hero-metal-tile.jpg')"></div>
<div class="wrap">
  <div>
    <div class="chips"><span class="chip rating">{ICONS["google"]} {RATING} <span class="stars">★★★★★</span> {NREV} Google reviews</span><span class="chip">Auckland roofing specialists</span></div>
    <h1>{P("Patched your roof one too many times?")} <span class="accent">Get a new one, at a fixed price.</span></h1>
    <p class="lede">{P("[One sentence, reroof-led, e.g. Auckland's family reroofing crew. We'll check your roof, tell you straight if it's time, and give you a fixed price.]")}</p>
    <div class="hero-actions"><a class="btn btn-outline-light" href="tel:{TEL}">{ICONS["phone"]} Call or text Mike · {PHONE}</a></div>
  </div>
  {quote_form("hero-quote", "Get a free quote", "Free, no pressure. We usually visit within 3 working days.")}
</div></section>

<section class="stats"><div class="wrap grid">
  <div class="stat"><b>{P("1,000+")}</b><span>Auckland roofs completed</span></div>
  <div class="stat"><b>{P("30+")}</b><span>Years roofing Auckland</span></div>
  <div class="stat"><b>{P("RANZ")}</b><span>Roofing Association of NZ member</span></div>
</div></section>

<section class="alt" style="margin-top:-60px;padding-top:140px"><div class="wrap">
  <h2>Signs it's time for a new roof</h2>
  <p class="lede">If two or more of these sound familiar, another patch is likely money down the drain.</p>
  <div class="signs" style="margin-top:32px">
    <div class="card">{signs_list()}</div>
    <div class="photo"><img src="assets/img/colorsteel-before.jpg" alt="An old, tired roof ready for replacement" loading="lazy"></div>
  </div>
  <div class="card unsure"><p><b>Not sure?</b> Mike will check your roof and tell you straight whether it's time.</p>
    <div class="acts"><a class="link" {pg.svc_link("roof-repairs", False)}>Just one leak? We do repairs too →</a><a class="btn btn-primary" href="#get-quote">Get my free reroof quote →</a></div></div>
</div></section>

<section><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">What we do</span><h2>Five services, all done by<br>the same family crew.</h2></div>
    <p class="lede">Not sure which one you need? Give Mike a call and he'll talk you through it. No jargon.</p></div>
  {services_grid(pg)}
</div></section>

<section class="alt"><div class="wrap center">
  <span class="eyebrow">The Roof Crew difference</span>
  <h2>Why Auckland chooses us</h2>
  <p class="lede">{P("[One line from: An honest roofing crew, straight up. A straight price, a tidy site, the same crew from quote to finish.]")}</p>
  <div class="grid-4" style="margin-top:36px;text-align:left">
    <div class="card"><div class="icon">{ICONS["family"]}</div><h3>Family-owned</h3><p>Three decades in the trade, still run by the same crew that picks up the phone.</p></div>
    <div class="card"><div class="icon">{ICONS["clock"]}</div><h3>Fast, free quotes</h3><p>No call centres. You deal with Mike from the first call to the final check.</p></div>
    <div class="card"><div class="icon">{ICONS["shield"]}</div><h3>Fully guaranteed</h3><p>Workmanship and product are both covered, so there are no fine-print surprises.</p></div>
    <div class="card"><div class="icon">{ICONS["card"]}</div><h3>Finance available</h3><p>Spread the cost of a reroof with flexible payment options.</p></div>
  </div>
  <p style="margin-top:30px"><a class="link" href="about/">Meet the crew →</a></p>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">What Auckland homeowners say</h2>
  {reviews_row(pg)}
</div></section>

<section class="alt" id="options"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Roofing options</span><h2>Three roofing systems,<br>made for Auckland weather.</h2></div>
    <p class="lede">Not sure which suits your home? We'll bring real samples and help you choose at your free site visit.</p></div>
  {systems_cards(pg)}
  {pricing_panel(pg)}
</div></section>

<section id="work"><div class="wrap ba-wrap">
  <div class="ba-side">
    <div><span class="eyebrow">See the difference</span><h2>The upgrade your whole street notices.</h2><p class="lede">Drag the slider to see a real Auckland reroof, start to finish.</p></div>
    <div><span class="filter-label">Filter: choose a project</span>
      <div class="track" data-track="projects"><button type="button" data-value="p1" aria-pressed="true">Concrete tile</button><button type="button" data-value="p2" aria-pressed="false">Long-run</button><button type="button" data-value="p3" aria-pressed="false">Metal tile</button></div></div>
    <p data-project-caption style="font-size:15px;color:var(--gray-500)">{p1[3]}</p>
    <a class="link soon" href="#">See more reroofs in {P("[Suburb]")} →</a>
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
    <p class="lede">From the North Shore to Pukekohe. Find your area.</p>
    <div class="region-links">{regions}<a class="ask" href="tel:{TEL}">Not sure? Ask Mike <span aria-hidden="true">→</span></a></div>
    <p class="popular">Popular suburbs: <a href="#" class="soon">{P("Howick")}</a> · <a href="#" class="soon">{P("Botany")}</a> · <a href="#" class="soon">{P("Takapuna")}</a></p>
    <p style="margin-top:14px"><a class="link" href="locations/">See all areas we cover →</a></p>
  </div>
  <div class="map"><iframe title="Map of the areas The Roof Crew covers" src="{MAP_AUCKLAND}" loading="lazy"></iframe></div>
</div></section>

<section class="band-cta"><div class="wrap"><div class="inner">
  <div><h2>Ready for a roof that's sorted before the next storm?</h2><p>Get it checked now, not after the next downpour.</p></div>
  <a class="btn btn-white" href="#get-quote">Get my free quote →</a>
</div></div></section>

<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">Questions people ask us</h2>{faq_block(faqs)}</div></section>
{closing(pg).replace('id="get-quote"', 'id="quote-bottom"')}'''
    # header and CTA buttons on the home page go to the hero form
    body = body.replace('id="hero-quote"', 'id="get-quote"')
    business = {"@context": "https://schema.org", "@type": "RoofingContractor", "name": "The Roof Crew", "telephone": "+64 21 903 822",
                "email": EMAIL, "areaServed": [n for _, n, _, _ in REGIONS], "address": {"@type": "PostalAddress", "addressLocality": "Auckland", "addressCountry": "NZ"}}
    page(pg, "Reroofing Auckland | The Roof Crew", "Family-owned Auckland reroofing crew. Free, no-pressure quotes, whole-home price ranges and a fixed price after a free site visit.", "home", body, [business, faq_schema(faqs)])


# ------------------------------------------------------------------ SERVICES
def build_services():
    pg = Page("services/")
    body = hero_page(pg, "bg-colorsteel.jpg", "Services", "Roofing services for Auckland homes",
                     "From a full reroof to a single leak, the same family crew quotes, builds and guarantees every job.")
    body += f'''
<section><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">What we do</span><h2>Start with the roof itself.</h2></div><p class="lede">Most of our work is full roof replacement. Every other service is done by the same crew, to the same standard.</p></div>
  {services_grid(pg, wide=True)}
</div></section>
<section class="alt"><div class="wrap">
  <div class="head-split"><div><span class="eyebrow">Roofing systems</span><h2>Three roofing systems.</h2></div><p class="lede">COLORSTEEL® long-run, pressed metal tile and concrete tile. We'll help you choose at your free site visit.</p></div>
  {systems_cards(pg)}
</div></section>
<section><div class="wrap"><div class="card unsure" style="margin:0">
  <p><b>Not sure what you need?</b> Call Mike, or book an inspection and get a written report on your roof.</p>
  <div class="acts"><a class="link" {pg.svc_link("roof-inspections", False)}>Book an inspection →</a><a class="btn btn-primary" href="tel:{TEL}">{ICONS["phone"]} Call Mike · {PHONE}</a></div>
</div></div></section>
{closing(pg)}'''
    page(pg, "Roofing services in Auckland | The Roof Crew", "Reroofing, new roof installation, roof repairs, guttering and roof inspections across Auckland, all by the same family crew.", "services", body)


# ------------------------------------------------------------------ REROOFING
def build_reroofing():
    pg = Page("services/reroofing/")
    faqs = [
        ("Do I need building consent to reroof?", P("[Mike to confirm wording: when a like-for-like reroof does and does not need building consent, and who sorts it.]")),
        ("What if my roof has asbestos?", P("[Mike to confirm: how asbestos is identified and removed, and by whom.]")),
        ("How long does a reroof take?", f"Most homes take {P('[X to Y working days, from Mike]')}, depending on size, access and weather. You can usually stay home while we work."),
        ("Can I change from tiles to long-run?", "Usually, yes. It is one of the most common upgrades. Mike checks the roof framing at your site visit and explains anything that needs to change."),
    ]
    included = ["Old roof stripped and disposed of responsibly", "New underlay, flashings and ridge capping", "Rotten battens or purlins found and replaced",
                "Full scaffolding and edge protection", "Fully guaranteed workmanship and product", "Finance available"]
    p1 = PROJECTS["p2"]
    other = "".join(f'<li><a class="link" {pg.svc_link(s, b)}>{n}</a></li>' for s, n, _, b in SERVICES[1:])
    areas = "".join(f'<li><a class="link" {pg.region_link(s, b)}>Reroofing in {n}</a></li>' for s, n, _, b in REGIONS)
    body = hero_page(pg, "hero-metal-tile.jpg", f'<a href="{pg.u("services/")}" style="color:inherit">Services</a> / Reroofing', "Reroofing in Auckland",
                     "Old roof leaking, rusting or just tired? A new roof is the biggest upgrade you can make to your home, and the first thing a buyer notices.")
    body += f'''
<section><div class="wrap split">
  <div><span class="eyebrow">What's included</span><h2>Same house. A completely new roof.</h2>
    <p class="lede">We strip your old roof, dispose of it responsibly and install new underlay, flashings, ridge capping and your choice of roofing, all under full scaffolding.</p>
    <ul class="ticks">{"".join(f"<li>{i}</li>" for i in included)}</ul></div>
  <div class="photo" style="min-height:420px"><img src="{pg.r}assets/img/colorsteel-installed.jpg" alt="A new COLORSTEEL long-run roof" loading="lazy"></div>
</div></section>
<section class="alt"><div class="wrap">
  <span class="eyebrow">When you need it</span><h2>Signs it's time for a new roof</h2>
  <div class="card" style="margin-top:28px">{signs_list()}</div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">How it works</span><h2 style="margin-bottom:32px">How a reroof works</h2>
  <div class="grid-3">
    <div class="card"><div class="icon">{ICONS["search"]}</div><h3>1. Free site visit</h3><p>We measure up and check what's underneath, usually within 3 working days.</p></div>
    <div class="card"><div class="icon">{ICONS["build"]}</div><h3>2. Clean install</h3><p>Scaffold up, old roof off, new roof on, with a tidy site at the end of every day.</p></div>
    <div class="card"><div class="icon">{ICONS["shield"]}</div><h3>3. Sign-off and guarantee</h3><p>A final check together, then your workmanship and product guarantees.</p></div>
  </div>
</div></section>
<section class="alt" id="options"><div class="wrap">
  <span class="eyebrow">Options and price ranges</span><h2 style="margin-bottom:32px">Choose your roof.</h2>
  {systems_cards(pg)}
  {pricing_panel(pg, "What a reroof roughly costs")}
</div></section>
<section id="work"><div class="wrap ba-wrap">
  <div class="ba-side"><div><span class="eyebrow">Project photos</span><h2>A real Auckland reroof.</h2><p class="lede">Drag the slider to compare.</p></div>
    {reviews_row(pg, "reroof")}</div>
  <div class="ba"><img class="before" src="{pg.r}assets/img/{p1[0]}" alt="Before the reroof"><img class="after" src="{pg.r}assets/img/{p1[1]}" alt="{p1[2]}">
    <span class="lbl l">Before</span><span class="lbl r">After</span><div class="handle"></div><div class="knob">‹›</div><input type="range" min="0" max="100" value="50" aria-label="Compare before and after"></div>
</div></section>
<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">Reroofing questions</h2>{faq_block(faqs)}</div></section>
<section><div class="wrap grid-2">
  <div class="card"><h3>Other services</h3><ul class="ticks">{other}</ul></div>
  <div class="card"><h3>Reroofing near you</h3><ul class="ticks">{areas}</ul></div>
</div></section>
{closing(pg, "New roof (reroof)", "Get a fixed price for your new roof.")}'''
    page(pg, "Reroofing in Auckland | The Roof Crew", "Full roof replacement across Auckland: old roof stripped and removed, new underlay, flashings and roofing, fully guaranteed. Free quotes.", "services", body, [faq_schema(faqs)])


# ------------------------------------------------------------------ LOCATIONS
def build_locations():
    pg = Page("locations/")
    cards = "".join(f'<a class="card region-card" {pg.region_link(s, b)}><h3>{n}</h3><small>{blurb}</small><span class="link" style="margin-top:8px">{"See " + n if b else "Page coming"} →</span></a>' for s, n, blurb, b in REGIONS)
    body = hero_page(pg, "bg-local-street.jpg", "Locations", "Roofing across Auckland",
                     "The same family crew and the same standard on every roof, from the North Shore to Pukekohe.")
    body += f'''
<section><div class="wrap">
  <span class="eyebrow">Areas we cover</span><h2 style="margin-bottom:32px">Find your region.</h2>
  <div class="grid-4">{cards}</div>
</div></section>
<section class="alt"><div class="wrap areas" style="align-items:start">
  <div><span class="eyebrow">Service area</span><h2>All over Auckland.</h2><p class="lede">Not sure if you're on our patch? Call or text Mike on {PHONE} and he'll tell you straight.</p>
    <p style="margin-top:22px"><a class="btn btn-primary" href="#get-quote">Get my free quote →</a></p></div>
  <div class="map"><iframe title="Map of Auckland service area" src="{MAP_AUCKLAND}" loading="lazy"></iframe></div>
</div></section>
{closing(pg)}'''
    page(pg, "Areas we cover in Auckland | The Roof Crew", "The Roof Crew reroofs homes in East Auckland, the North Shore, South Auckland and West Auckland.", "locations", body)


# ------------------------------------------------------------------ EAST AUCKLAND (region + suburb template)
def build_east():
    pg = Page("locations/east-auckland/")
    subs = "".join((f'<a href="#" class="soon">{s}</a>' if s in SUBURB_PAGES else f"<span>{s}</span>") for s in EAST_SUBURBS)
    svc = "".join(f'<article class="card"><div class="icon">{ICONS[SVC_ICON[s]]}</div><h3>{n}</h3><a class="link" {pg.svc_link(s, b)}>{n} in East Auckland →</a></article>' for s, n, _, b in SERVICES)
    body = hero_page(pg, "bg-sunset.jpg", f'<a href="{pg.u("locations/")}" style="color:inherit">Locations</a> / East Auckland', "Reroofing in East Auckland",
                     "Free, no-pressure reroof quotes from Howick and Pakuranga to Flat Bush and Beachlands.")
    body += f'''
<section><div class="wrap split">
  <div class="prose"><span class="eyebrow">Roofing in East Auckland</span><h2 style="margin-bottom:18px">Your local reroofing crew.</h2>
    <p>{P("[2 to 3 sentences of genuine local detail from Mike: the homes and roofs he sees most in East Auckland, coastal wind and salt near the beaches, recent jobs nearby.]")}</p>
    <p>From Howick to Beachlands, the same family crew quotes, builds and guarantees every roof.</p></div>
  <div class="photo" style="min-height:360px"><img src="{pg.r}assets/img/bg-sunset.jpg" alt="{''}Roof in East Auckland" loading="lazy"></div>
</div></section>
<section class="alt"><div class="wrap">
  <span class="eyebrow">Services</span><h2 style="margin-bottom:32px">What we do in East Auckland</h2>
  <div class="grid-3">{svc}</div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">Local proof</span><h2 style="margin-bottom:32px">Recent East Auckland roofs</h2>
  <div class="grid-3">
    <div class="ph-box" style="min-height:240px">{P("[Job photo: East Auckland reroof]")}</div>
    <div class="ph-box" style="min-height:240px">{P("[Job photo: East Auckland reroof]")}</div>
    {reviews_row(pg, "east")}
  </div>
</div></section>
<section class="alt"><div class="wrap areas" style="align-items:start">
  <div><span class="eyebrow">Suburbs we cover</span><h2>East Auckland suburbs</h2>
    <p class="lede">Highlighted suburbs have their own page. Don't see yours? We probably still cover it, just ask.</p>
    <div class="suburbs">{subs}</div></div>
  <div class="map"><iframe title="Map of East Auckland" src="{MAP_EAST}" loading="lazy"></iframe></div>
</div></section>
{closing(pg, "New roof (reroof)", "Get a free quote in East Auckland.")}'''
    page(pg, "Reroofing in East Auckland | The Roof Crew", "Reroofing and roofing services in Howick, Botany, Pakuranga, Flat Bush and across East Auckland. Free, no-pressure quotes.", "locations", body)


# ------------------------------------------------------------------ ABOUT
def build_about():
    pg = Page("about/")
    crew = "".join(f'<div class="crew"><div class="ph-box">{P("[Photo]")}</div><h3>{P(n)}</h3><p style="color:var(--gray-500)">{P(r)}</p></div>'
                   for n, r in [("Mike", "Owner"), ("[Name]", "[Role]"), ("[Name]", "[Role]"), ("[Name]", "[Role]")])
    body = f'''<section class="hero page-hero"><div class="hero-bg" style="background-image:url('{pg.r}assets/img/bg-crew.jpg')"></div>
<div class="wrap"><div><span class="eyebrow">About us</span><h1>A family crew that turns up.</h1>
<p class="lede">{P("[One line from Mike about the business]")}</p>
<div class="hero-actions"><a class="btn btn-primary" href="#get-quote">Get my free quote →</a></div></div></div></section>
<section><div class="wrap split">
  <div class="prose"><span class="eyebrow">Our story</span><h2 style="margin-bottom:18px">Family-owned, three decades in.</h2>
    <p>{P("[Mike's story in his own words: how The Roof Crew started, the family behind it, and why the same crew still answers the phone.]")}</p>
    <p>{P("[What a customer can expect: straight prices, tidy sites, turning up when we say we will.]")}</p></div>
  <div class="photo" style="min-height:400px"><img src="{pg.r}assets/img/bg-crew.jpg" alt="The Roof Crew team on site" loading="lazy"></div>
</div></section>
<section class="alt"><div class="wrap"><span class="eyebrow">Meet the crew</span><h2 style="margin-bottom:32px">The people on your roof.</h2><div class="grid-4">{crew}</div></div></section>
<section><div class="wrap"><span class="eyebrow">Accreditations and warranty</span><h2 style="margin-bottom:32px">What's backed, in writing.</h2>
  <div class="grid-3">
    <div class="card"><div class="icon">{ICONS["shield"]}</div><h3>{P("RANZ member")}</h3><p>{P("[Confirm membership]")}</p></div>
    <div class="card"><div class="icon">{ICONS["home"]}</div><h3>Workmanship guarantee</h3><p>{P("[Length and terms, from Mike]")}</p></div>
    <div class="card"><div class="icon">{ICONS["build"]}</div><h3>Product warranty</h3><p>{P("[Manufacturer warranty terms, e.g. COLORSTEEL®]")}</p></div>
  </div>
  <p style="margin-top:18px;font-size:14px;color:var(--gray-500)">Only confirmed accreditations go live.</p>
</div></section>
<section class="alt"><div class="wrap"><span class="eyebrow">Reviews</span><h2 style="margin-bottom:32px">What our customers say</h2>{reviews_row(pg, "about")}</div></section>
{closing(pg)}'''
    page(pg, "About The Roof Crew | Family-owned Auckland roofers", "Meet Mike and the family crew behind The Roof Crew, Auckland's reroofing specialists.", "about", body)


# ------------------------------------------------------------------ CONTACT
def build_contact():
    pg = Page("contact/")
    faqs = [
        ("What happens after I get in touch?", f"Mike calls you back, {P('[usually the same or next working day]')}, asks a few questions and books a free site visit."),
        ("Is the quote really free?", "Yes. The site visit and quote are free, with no obligation and no sales pressure."),
        ("Do you cover my area?", "We cover East Auckland, the North Shore, South Auckland and West Auckland. If you're not sure, just ask."),
    ]
    regs = "".join(f'<a {pg.region_link(s, b)}>{n}</a>' for s, n, _, b in REGIONS)
    body = f'''<section class="hero page-hero" style="padding-block:56px 64px"><div class="hero-bg" style="background-image:url('{pg.r}assets/img/bg-local-street.jpg')"></div>
<div class="wrap"><div><span class="eyebrow">Contact</span><h1>Talk to Mike.</h1><p class="lede">Call, text or send your details and Mike will get back to you personally.</p></div></div></section>
<section><div class="wrap closing">
  <div><h2>Get in touch</h2>
    <div class="contact-box" style="margin-top:24px"><a href="tel:{TEL}">{ICONS["phone"]} {PHONE}</a><a href="mailto:{EMAIL}">{ICONS["mail"]} {P(EMAIL)}</a><span>Hours: {P("[Hours, from Mike]")}</span></div>
    <h3 style="margin-top:36px">Areas we cover</h3>
    <div class="suburbs">{regs}</div>
    <p style="margin-top:14px;font-size:15px;color:var(--gray-500)">We come to you. No street address is listed because the crew works on site across Auckland.</p>
  </div>
  {quote_form("get-quote", "Get your free quote", "Free and no pressure.")}
</div></section>
<section class="alt"><div class="wrap"><h2 style="margin-bottom:30px">What happens next</h2>{faq_block(faqs)}</div></section>'''
    page(pg, "Contact The Roof Crew | Free roof quotes in Auckland", "Call or text Mike on 021 903 822, or send your details for a free, no-pressure roof quote.", "contact", body)


def main():
    img_src = os.path.join(ROOT, "assets", "images")
    img_dst = os.path.join(OUT, "assets", "img")
    os.makedirs(img_dst, exist_ok=True)
    for f in os.listdir(img_src):
        shutil.copy2(os.path.join(img_src, f), os.path.join(img_dst, f))
    for b in (build_home, build_services, build_reroofing, build_locations, build_east, build_about, build_contact):
        b()
    print("built v2:", sorted(os.path.relpath(os.path.join(d, f), OUT) for d, _, fs in os.walk(OUT) for f in fs if f.endswith(".html")))


if __name__ == "__main__":
    main()
