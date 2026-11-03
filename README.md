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

`v2/` is the new build the client approved: Design A's look (dark photo hero with the quote form, overlapping stat tiles, "Why Auckland chooses us") on the combined wireframe structure, reroofing-first throughout.

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
