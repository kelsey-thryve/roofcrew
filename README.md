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

Seven template pages (the other 13 are duplicated from these):

| Page | File |
| --- | --- |
| Home | `v2/index.html` |
| About | `v2/about/` |
| Contact | `v2/contact/` |
| Services collection | `v2/services/` |
| Service page (Reroofing) | `v2/services/reroofing/` |
| Locations | `v2/locations/` |
| Region / suburb page (East Auckland) | `v2/locations/east-auckland/` |

- Yellow highlights (`<mark class="ph">`) are content the client supplies or confirms: Google rating and reviews, stats, price ranges, photos, Mike's wording. The yellow strip at the top can hide them.
- Links to pages not in this set are disabled (`class="soon"`) until those pages exist.
- Quote forms only show a confirmation on staging; connect them to email or a CRM before launch.
- Pages are `noindex` while on staging.
- Edit and rebuild with `python3 tools/build_v2.py` (pages are generated from shared header, footer and form code); styles are in `v2/assets/css/site.css`.

## WordPress theme (v2 design)

`wordpress/roofcrew-theme.zip` is the v2 site as a WordPress theme. Rebuild it after changing the design: `python3 tools/build_v2.py && python3 tools/build_wp_theme.py`.

- **Install:** Appearance → Themes → Add New → Upload, activate, then Settings → The Roof Crew → **Import starter content**. That creates Home, About, Contact, Free quote, Services (5 service pages) and Locations (4 area pages). Reroofing and East Auckland are published; the others are drafts to fill in and publish.
- **Services and Locations are ordinary pages.** Each is a child of the Services or Locations page using the "Service page" or "Location page" template. Add one with Pages → Add New (set the parent and template), or use the **Duplicate** link under any page in Pages → All Pages. Published ones appear in the menus, the footer, the home page and the index pages automatically; drafts show as "coming soon".
- **Editing:** on Service and Location pages, the editor text fills the intro section, the "Page details" box holds the heading, hero line, suburbs, tick list and so on, the Excerpt is the card text and the Featured image is the hero photo. Home, About, Contact, Free quote, Services and Locations take their layout and wording from the theme (the editor shows a note saying so).
- **Quote forms** keep the site's design. Each request is saved under Quote requests and emailed to the address in Settings → The Roof Crew, through Resend if an API key is saved there, otherwise through WordPress's normal mail. Old addresses from the current site (/replacement-roofs/, /contact-us/ and so on) redirect to the new pages.
