# The Roof Crew — website

Static multi-page site for The Roof Crew (Auckland roofing). Plain HTML/CSS/JS, no build step — ready for GitHub Pages or any static host.

- `index.html`, `about.html`, `contact.html`
- `services/` — reroofing, new-build, spouting, inspections, repairs
- `products/` — colorsteel, metal-tile, concrete-tile
- `locations/` — pukekohe, east-auckland, north-shore, west-auckland, south-auckland
- `assets/css/style.css`, `assets/js/script.js`, `assets/images/`

## To do before launch
- Replace placeholder review cards with real Google reviews
- Connect the quote form to a real endpoint (currently opens a pre-filled email to mike@theroofcrew.co.nz)
- Swap in the official logo file if there is one

## v2: combined design (staging)

`v2/` is the new build from the client's final wireframe: its structure and its styling (navy and white, Inter, white header, dark hero with the quote form, overlapping stat tiles), reroofing-first throughout.

Live preview: https://kelsey-thryve.github.io/roofcrew/v2/

Page copy comes from Kelsey's content doc ("The Roof Crew: On Page Content") and lives in `tools/content_v2.py`. URLs follow the doc: material pages and Pukekohe keep their old top-level addresses.

| Page | Address |
| --- | --- |
| Home | `/` |
| Services collection, service pages | `/services/`, `/services/reroofing/`, `/services/new-roof-installation/`, `/services/roof-repairs/`, `/services/guttering-downpipes/`, `/services/roof-inspections/` |
| Roofing material pages | `/colour-steel-roofing/`, `/metal-tile-roofing/`, `/concrete-tile-roofing/` (on hold until Mike confirms) |
| Locations collection, regions | `/locations/`, `/locations/east-auckland/`, `/locations/north-shore/`, `/locations/south-auckland/`, `/locations/west-auckland/` |
| Area pages | `/roofers-in-pukekohe/`, `/locations/papakura/`, `/locations/glenfield/`, `/locations/manukau/`, `/locations/manurewa/`, `/locations/howick/` |
| About, Contact, Free quote | `/about/`, `/contact/`, `/quote/` |
| Blog and posts (current live copy, moved across as is) | `/blog/` and the five post URLs from the current site (copy in `tools/blog_posts.json`) |
| Privacy policy (current live copy) | `/privacy-policy/` |

- Yellow highlights (`<mark class="ph">`, made with `P(text, question)` in `tools/content_v2.py`) are content Mike still has to confirm or supply. Hover over one to see the question for Mike.
- Old addresses (`REDIRECTS` in `tools/content_v2.py`) get a small redirect page here, and a 301 in the WordPress theme.
- Quote forms only show a confirmation on staging; connect them to email or a CRM before launch.
- Pages are `noindex` while on staging.
- Edit and rebuild with `python3 tools/build_v2.py` (pages are generated from shared header, footer and form code); styles are in `v2/assets/css/site.css`.

## WordPress theme (v2 design)

`wordpress/roofcrew-theme.zip` is the v2 site as a WordPress theme. Rebuild it after changing the design: `python3 tools/build_v2.py && python3 tools/build_wp_theme.py`.

- **Install:** Appearance → Themes → Add New → Upload, activate, then Settings → The Roof Crew → **Import starter content**. That creates Home, About, Contact, Free quote, Services (5 services and 3 roofing material pages), Locations (4 regions and 6 areas), the Blog page with its 5 posts, and the Privacy policy, all with the content doc's copy and its yellow highlights.
- **Services and Locations are ordinary pages.** Each is a child of the Services or Locations page using the "Service page" or "Location page" template. Pages that keep an old top-level address (the material pages and Pukekohe) belong to their group through a hidden `_rc_group` field. In the editor text, each H2 heading starts a new section; FAQs, the review and the suburbs are in the "Page details" box. Add one with Pages → Add New (set the parent and template), or use the **Duplicate** link under any page in Pages → All Pages. Published ones appear in the menus, the footer, the home page and the index pages automatically; drafts show as "coming soon".
- **Editing:** on Service and Location pages, the editor text fills the intro section, the "Page details" box holds the heading, hero line, suburbs, tick list and so on, the Excerpt is the card text and the Featured image is the hero photo. Home, About, Contact, Free quote, Services and Locations take their layout and wording from the theme (the editor shows a note saying so).
- **Quote forms** keep the site's design. Each request is saved under Quote requests and emailed to the address in Settings → The Roof Crew, through Resend if an API key is saved there, otherwise through WordPress's normal mail. Old addresses from the current site (/replacement-roofs/, /contact-us/ and so on) redirect to the new pages.
