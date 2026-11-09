"""Page copy for the v2 site, from Kelsey's content doc ("The Roof Crew: On Page Content").

Imported by tools/build_v2.py (static site) and, through it, tools/build_wp_theme.py (WordPress theme).

P(text, question) marks content that is waiting on Mike: it shows yellow on the site, and the
question shows on hover (title attribute). Every highlighted item is listed in the
"questions for Mike" document, which is compiled from these marks.
Kelsey-only notes in the doc (launch checklist, "why this page", URL notes) are not page copy.
"""
import html as _html
import json
import os

PHONE = "021 903 822"


def P(text, q):
    """Yellow highlight: content Mike still has to confirm or supply. q = the question for Mike."""
    return f'<mark class="ph" title="Question for Mike: {_html.escape(q)}">{text}</mark>'


# ---------------------------------------------------------------- questions (one per claim)
Q_YEARS = "Is '30+ years' right? Some old ads said 35+. Pick one number to use everywhere."
Q_YEARS_INDUSTRY = "Confirm 'over 30 years in the building industry' (some old ads said 35+)."
Q_ROOFS = "How many roofs have you completed? Staging says 1,000+, but current ads say 850+. Pick one true number."
Q_RANZ = "Are you a current RANZ (Roofing Association of NZ) member? If not, RANZ comes off everywhere."
Q_RANZ_ABOUT = "RANZ card on the About page: only shown if you confirm current RANZ membership. Are you a member?"
Q_PRICES = ("Are you happy to publish the COLORSTEEL reroof ranges: about $12,000 to $18,000 for roofs under 100m², "
            "$16,000 to $28,000 for a standard home (100 to 180m²), $25,000 to $40,000+ for large or complex roofs?")
Q_PRICES_OTHER = "Do you want to publish price ranges for metal tile and concrete tile reroofs, or keep 'Fixed quote on site'?"
Q_WARRANTY = "Is the 5-year workmanship warranty still current?"
Q_FINANCE = "Is finance still available? Which provider, and do the terms still apply?"
Q_VISIT = "Is 'we'll usually visit within 3 working days' still realistic?"
Q_DAYS = "Does an average three-bedroom reroof take about 3 to 4 days?"
Q_INSURED = "Can we say you're fully insured (public liability)?"
Q_GERARD = ("How should we describe your Gerard relationship? Your email signature says 'Licenced Resellers & Installers of "
            "Gerard Products'. The site says 'resellers and installers of Gerard products' (we don't use 'licensed', "
            "so it doesn't read like an LBP claim).")
Q_GERARD_HOME = "OK to call the metal tile option 'Gerard metal tile' on the homepage? (Gerard wording)"
Q_GERARD_CARD = "Gerard wording: is this the right description of the metal tile roofs you install?"
Q_CONCRETE = ("Do you still offer concrete tile roofs? If yes, the concrete tile page stays. If not, it comes down "
              "(with a redirect to keep its Google traffic) and concrete tile is removed from the other pages.")
Q_CONCRETE_REROOF = "Do you still offer concrete tile on reroofs?"
Q_STAY_HOME = "Do people need to move out during a reroof? Suggested answer shown."
Q_BUILDS = "New roof installation: what kinds of builds do you do most, and what's a typical lead time?"
Q_CS_LIFE = "COLORSTEEL lifespan: OK to say around 18 years for colour fade and 30 years for perforation, as a guide?"
Q_CS_LIFE2 = "OK to say COLORSTEEL typically lasts around 30 years before perforation, as a guide?"
Q_METROTILE = ("Is Metrotile now part of the Gerard brand? If they're separate brands, this answer comes off. "
               "(Staging used to say 'distributors and installers for Metrotile NZ, part of the RossRoof Group'; that line has been removed.)")
Q_NOISY = "Are metal tile roofs noisy in the rain? Please answer in your own words (a common question worth covering)."
Q_REPAIRS_PAGE = "Do you want roof repair leads? This page only goes live if yes."
Q_URGENT = "Do you take urgent leak or storm jobs? How quickly can you get there?"
Q_INSPECT_PAGE = "Do you offer roof inspections and written reports? This page only goes live if yes."
Q_REPORT = "What does an inspection report cover, and is there a fee?"
Q_STORY = "In your own words, 2 or 3 sentences on how the business started, and who's in the family and crew today."
Q_LOCAL_JOB = "Local job for {place}: a recent job there (suburb, what you did, a photo if you have one)."
Q_PICK_REVIEW = "{who}: pick a Google review to show on this page."
Q_RURAL = "Are you happy to take jobs on rural properties and Franklin lifestyle blocks?"
Q_PUKE_SUBURBS = "Pukekohe page: are these the right areas to list (Pukekohe, Paerata, Patumāhoe, Buckland, Karaka, Waiuku, Bombay, Tuakau)?"
Q_NEWBUILD_SOUTH = "Do you do new build roofs around Takanini and Drury?"
Q_RENTALS = "Do you work on rental properties, with landlords and property managers? Suggested answer shown."

PH_PRICE_STD = lambda: P("$16,000 to $28,000", Q_PRICES)


def ticks(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def paras(*ps):
    return "".join(f"<p>{p}</p>" for p in ps)


# ---------------------------------------------------------------- HOME
HOME = dict(
    title="Roofing Auckland | Reroofing & New Roofs | The Roof Crew",
    desc="Family-owned Auckland roofers with 30+ years' experience. Reroofs, new roofs and repairs, with a free site visit and a fixed quote.",
    h1="Roofing Auckland homes for " + P("over 30 years", Q_YEARS),
    intro="The Roof Crew is a family-owned Auckland roofing company. We replace old roofs, install new ones and fix the ones that won't stop leaking. You'll deal with Mike from the first call to the final check, and you'll get a fixed price after a free site visit.",
    what_we_do="Most of our work is full roof replacement. Whatever the job, the same crew quotes it, does it and stands behind it.",
    options_h2="Three roofing systems for Auckland homes",
    options_lede="The right roof depends on your house, your budget and how close you are to the sea. Mike will talk you through it at your site visit.",
    cost_h="How much does a new roof cost in Auckland?",
    cost_html=paras(
        "A COLORSTEEL® reroof usually costs about " + PH_PRICE_STD() + " on a standard Auckland home with a roof of 100 to 180m². Smaller roofs start at around "
        + P("$12,000", Q_PRICES) + ", and large or complex ones can pass " + P("$40,000", Q_PRICES) + ".",
        "The final cost comes down to the size and pitch of your roof, access, and what we find under the old one. That's why you get a fixed, itemised price after we've been out to see it."),
    signs=["Leaks keep coming back after repairs", "The roof is 30 or more years old", "There are water stains on your ceilings",
           "You can see rust, lifting sheets or cracked tiles", "The surface looks faded, chalky or mossy"],
    signs_after="Don't wait until it's dripping through the ceiling. By then, the damage underneath is often worse than the roof itself.",
    why_h2="Why Auckland homeowners choose us",
    why=[("You deal with Mike", "There's no call centre, and no salesperson handing you over to someone else."),
         ("Fixed pricing", "Your quote is itemised, so you know what you're paying for."),
         ("Backed in writing", "You get a " + P("5-year workmanship warranty", Q_WARRANTY) + ", plus the manufacturer's product warranty."),
         (P("Finance available", Q_FINANCE), "You can spread the cost if that helps.")],
    faqs=[("How long does a reroof take?", "An average three-bedroom house takes " + P("about 3 to 4 days", Q_DAYS) + ", depending on the weather."),
          ("Can you reroof in winter?", "Yes. Auckland's weather lets us replace roofs all year, and we work around the wet days."),
          ("Do I need a repair or a whole new roof?", "If it's the original roof, it's usually near the end of its life and worth replacing. If it's newer, a repair might be all you need. Mike will tell you straight after he's had a look."),
          ("What happens to my old roof?", "We take it away and dispose of it responsibly."),
          ("Can I put solar panels on a new roof?", "Yes, but check with the roofing manufacturer first, as it can affect your warranty."),
          ("Where do you work?", "Right across Auckland, from Whangaparāoa and the North Shore to West, East and South Auckland, and down to Pukekohe.")],
    cta_h="Find out what your new roof will really cost",
    cta_text=f"Call or text Mike on {PHONE}, or send us your details. We'll usually visit " + P("within 3 working days", Q_VISIT) + ".",
)

# ---------------------------------------------------------------- SERVICES COLLECTION
SERVICES_PAGE = dict(
    title="Roofing Services Auckland | The Roof Crew",
    desc="Reroofing, new roofs, repairs, guttering and roof inspections across Auckland, from one family-owned crew. Free site visits and fixed quotes.",
    h1="Roofing services for Auckland homes",
    intro="Most of our work is full roof replacement, but we look after the rest of your roof too. Whichever job you need, the same family crew quotes it, does it and guarantees it.",
    cta_h="Not sure what you need?",
    cta_text=f"Call or text Mike on {PHONE}. He'll talk you through it, with no jargon and no pressure.",
)

# ---------------------------------------------------------------- ABOUT
ABOUT = dict(
    title="About The Roof Crew | Family-Owned Auckland Roofers",
    desc="The Roof Crew is a family-owned Auckland roofing company with over 30 years in the building industry. Meet Mike and find out how we work.",
    h1="A family roofing crew that turns up",
    intro="The Roof Crew is a family-owned Auckland roofing company with " + P("over 30 years in the building industry", Q_YEARS_INDUSTRY) + ". When you call us, you get Mike, and he stays with your job until it's finished.",
    why_h="Why we do it this way",
    why=["We know that sinking feeling when a stain appears on the ceiling. You start wondering how bad it is, how much it'll cost, and who you can trust to tell you the truth. We meet people feeling exactly that every week.",
         "So we keep it simple. Mike comes out, looks at the roof and tells you what it needs. If a repair will do, he'll say so. If it's time for a new roof, you'll get a fixed, itemised price and no pressure to go ahead.",
         P("[Mike: how the business started, and who's in the family and crew today]", Q_STORY)],
    care_h="How we look after your home",
    care=["A roof job puts a crew on top of your house for days, so how we work matters. We set up scaffolding and edge protection, meet our health and safety obligations, and leave the site tidy at the end of each day. We take the old roof away and dispose of it responsibly.",
          "Sometimes we find problems we couldn't see until the roof came off, especially on older villas. When that happens, we'll show you, explain the options and bring in a builder we trust if timber work is needed."],
    backed_h="What's backed in writing",
    backed=[("shield", "Workmanship", "Every job comes with a " + P("5-year workmanship warranty", Q_WARRANTY) + "."),
            ("build", "Products", "The manufacturer's warranty covers the products on top of that."),
            ("home", "Insurance", "We're " + P("fully insured", Q_INSURED) + "."),
            ("layers", "Gerard", P("We're resellers and installers of Gerard products.", Q_GERARD)),
            ("search", "RANZ", P("[RANZ membership: only shown if Mike confirms]", Q_RANZ_ABOUT))],
    reviews_h="Rated 4.7 stars on Google",
)

# ---------------------------------------------------------------- LOCATIONS COLLECTION
LOCATIONS_PAGE = dict(
    title="Roofers Across Auckland | Areas We Cover | The Roof Crew",
    desc="The Roof Crew covers all of Auckland, from Whangaparāoa and the North Shore to East, West and South Auckland and Pukekohe. Free site visits.",
    h1="Roofers right across Auckland",
    intro="We work all over Auckland, from Whangaparāoa and the North Shore down to Pukekohe. Wherever you are, it's the same family crew, the same quote process and the same warranty.",
    find_h="Find your area",
    popular_h="Popular areas",
    popular=["pukekohe", "papakura", "glenfield", "manukau", "manurewa", "howick"],
    ask_h="Not sure if we cover you?",
    ask_text=f"Just ask. Call or text Mike on {PHONE} and he'll tell you straight.",
)

# ---------------------------------------------------------------- SERVICE AND MATERIAL PAGES
# kind: "service" (child of /services/) or "material" (keeps its old root URL).
# sections: [(heading, html)]. The first one sits beside the photo, the rest are full sections.
REROOF_STEPS = [("Free site visit", "Mike measures up and checks the roof, usually " + P("within 3 working days", Q_VISIT) + "."),
                ("Fixed quote", "You get an itemised price, with no pressure to go ahead."),
                ("Scaffolding goes up", "We book it in and work around the weather."),
                ("Old roof off, new roof on", "An average three-bedroom house takes " + P("about 3 to 4 days", Q_DAYS) + "."),
                ("Final check", "We walk through it with you, then you get your warranty details.")]
REROOF_COST_H = "How much does a reroof cost in Auckland?"
REROOF_COST = paras(
    "A COLORSTEEL® reroof usually costs about " + PH_PRICE_STD() + " on a standard home. Roofs under 100m² are around " + P("$12,000 to $18,000", Q_PRICES)
    + ", and large or complex roofs run from " + P("$25,000 to $40,000 or more", Q_PRICES) + ".",
    "These are rough ranges, not quotes. Pitch, access and what's under the old roof all affect the final price.")

COLORSTEEL_TABLE = ('<table class="spec"><thead><tr><th>Product</th><th>Best for</th></tr></thead><tbody>'
                    "<tr><td>COLORSTEEL® Endura®</td><td>Homes in moderate inland through to severe coastal conditions</td></tr>"
                    "<tr><td>COLORSTEEL® Maxx®</td><td>Rugged coastlines with higher salt in the air</td></tr>"
                    "<tr><td>ZINCALUME®</td><td>Moderate conditions, including roofing, cladding, gutters and downpipes</td></tr></tbody></table>")
GERARD_PDFS = [("Gerard CF Shake (textured)", "gerard-cf-shake-textured-2021.pdf"), ("Gerard CF Shingle (textured)", "gerard-cf-shingle-textured-2022.pdf"),
               ("Gerard CF Slate (textured)", "gerard-cf-slate-textured-2022.pdf"), ("Gerard angle trim", "gerard-angle-trim.pdf"),
               ("Gerard long angle trim", "gerard-long-angle-trim.pdf"), ("Gerard barrel trim", "gerard-barrel-trim.pdf"), ("Gerard box trim", "gerard-box-trim.pdf")]
GERARD_PDF_BASE = "https://theroofcrew.co.nz/wp-content/uploads/2023/05/"

CONCRETE_HOLD = "On hold until Mike confirms we still offer concrete tile. If the page stays, this is the draft."
C = lambda t: P(t, Q_CONCRETE)  # everything on the concrete tile page is unconfirmed

SERVICE_PAGES = [
    dict(slug="reroofing", path="services/reroofing/", kind="service", name="Reroofing", icon="home",
         title="Reroofing Auckland | Roof Replacement | The Roof Crew",
         desc="Need a new roof? We strip the old one, fix what's underneath and install a new roof, with a fixed price after a free site visit.",
         h1="Reroofing in Auckland",
         lede="Reroofing means taking your old roof off and installing a new one on the same house. It's the right call when leaks keep coming back or the roof has reached the end of its life. We handle the whole job, from scaffolding to taking the old roof away.",
         home_card="We strip the old roof, sort out what's underneath and put on a new one.",
         card="If your roof keeps leaking or has simply had its day, we'll take it off and start again. We strip the old roof, replace any rotten timber we find, and fit new underlay, flashings and your choice of roofing. It's all done under full scaffolding, and we take the old roof away.",
         hero="hero-metal-tile.jpg", photo="colorsteel-installed.jpg", reroof=True,
         sections=[("What's included", ticks(["Scaffolding and edge protection", "Stripping and disposing of the old roof", "Replacing rotten battens or purlins we find",
                                              "New underlay, flashings and ridge capping", "Your choice of COLORSTEEL®, metal tile or " + P("concrete tile", Q_CONCRETE_REROOF),
                                              "A workmanship warranty, plus the manufacturer's product warranty"]))],
         faq_h="Reroofing questions",
         faqs=[("Do I need to move out during a reroof?", P("No, most people stay home, though it can be noisy.", Q_STAY_HOME)),
               ("Can you replace a tile roof with steel?", "Yes. Plenty of people switch to a lighter roof. Mike will explain what's involved at your site visit."),
               ("What if you find rot under the old roof?", "We'll show you what we've found and explain your options before going further. If it needs structural timber work, we'll bring in a builder we trust.")],
         closing="Get a fixed price for your new roof.", pre="New roof (reroof)"),
    dict(slug="new-roof-installation", path="services/new-roof-installation/", kind="service", name="New roof installation", icon="build",
         title="New Roof Installation Auckland | New Builds | The Roof Crew",
         desc="New roofs for new builds and extensions across Auckland. We work with homeowners, builders and developers. Talk to Mike for a free quote.",
         h1="New roof installation in Auckland",
         lede="Building a new home or adding an extension? We install new roofs for homeowners, builders and developers across Auckland. We'll help you choose the roof, fascia and spouting, then get it done on time and to spec.",
         home_card="Roofs for new builds and extensions, for homeowners, builders and developers.",
         card="Building a new home or adding an extension? We work with homeowners, builders and developers, and help you choose the roof, fascia and spouting to suit the job.",
         hero="bg-colorsteel.jpg", photo="photo-sunset-roof.jpg",
         sections=[("Choosing your roof", paras("Start with the roof type: COLORSTEEL® long-run, metal tile or concrete tile. Then choose your colour. We have samples, so you can see how it'll look before you commit.")),
                   ("Working with builders and developers", paras("We fit in with the other trades on site and take site safety seriously, with safety netting and edge protection. "
                                                                  + P("[Mike: the kinds of builds you do most, and typical lead time]", Q_BUILDS)))],
         faq_h="New build questions",
         faqs=[("When should I talk to you about a new build roof?", "As early as you can, ideally when you have plans. That gives us time to advise on materials and fit your build schedule."),
               ("Can you roof an unusual design?", "Yes. We just need to make sure it's done to the Building Code.")],
         closing="Talk to Mike about your new build roof.", pre="New build roof"),
    dict(slug="colour-steel-roofing", path="colour-steel-roofing/", kind="material", name="COLORSTEEL® roofing", icon="layers",
         title="Colour Steel Roofing Auckland | COLORSTEEL® | The Roof Crew",
         desc="COLORSTEEL® long-run roofing for Auckland homes, in a huge range of colours and profiles. Reroofs and new builds, with free site visits.",
         h1="COLORSTEEL® roofing in Auckland",
         lede="COLORSTEEL® is pre-painted steel roofing made for New Zealand conditions, and it's the most popular option we install. It comes in a huge range of colours and profiles, and it suits reroofs and new builds.",
         system="COLORSTEEL® long-run", system_text="Our most popular option, with a huge range of colours and profiles.",
         card="This is the long-run steel you see on homes all over New Zealand, and it's our most popular option. There's a huge range of colours and profiles, including options made for coastal areas.",
         hero="bg-colorsteel.jpg", photo="colorsteel-installed.jpg", system_img="colorsteel-installed.jpg",
         sections=[("Which COLORSTEEL® is right for my home?", paras("It mostly depends on how close you are to the sea, as salt is hard on steel.") + COLORSTEEL_TABLE
                    + paras("Mike will check your site and recommend the right one.")),
                   ("Popular colours", "__SWATCHES__" + paras("Gull Grey, Desert Sand, Sandstone Grey, Thunder Grey, Karaka, Grey Friars, Ironsand and Titania. Colours look different on a screen, so we'll bring real samples to your quote."))],
         faq_h="COLORSTEEL® questions",
         faqs=[("Is COLORSTEEL® the same as long-run roofing?", "Long-run is the style of roofing, with sheets that run the length of the roof. COLORSTEEL® is the pre-painted steel it's commonly made from."),
               ("How long does a COLORSTEEL® roof last?", "It depends on where you live. As a guide, you can typically expect " + P("around 18 years for colour fade and 30 years for perforation", Q_CS_LIFE) + ". Check the warranty for your product and location."),
               ("How much does a COLORSTEEL® roof cost?", "On a standard Auckland home, a reroof usually costs about " + PH_PRICE_STD() + ".")],
         closing="Get a price for your COLORSTEEL® roof.", pre="New roof (reroof)"),
    dict(slug="metal-tile-roofing", path="metal-tile-roofing/", kind="material", name="Metal tile roofing", icon="layers",
         title="Metal Tile Roofing Auckland | Gerard Roofs | The Roof Crew",
         desc="Gerard metal tile roofs for Auckland homes. Get the look of a tiled roof with a lighter, more durable roof. Reroofs and new builds.",
         h1="Metal tile roofing in Auckland",
         lede="Metal tiles give you the look of a traditional tiled roof, but they're lighter and more durable. " + P("We're resellers and installers of Gerard products", Q_GERARD) + ", and we install metal tile roofs on reroofs and new builds across Auckland.",
         system=P("Gerard metal tile", Q_GERARD_HOME), system_text="The look of a tiled roof, but much lighter.",
         card=P("Metal tiles give you the look of a tiled roof at a fraction of the weight. They're a popular way to replace an old tile roof without losing its character.", Q_GERARD_CARD),
         hero="hero-metal-tile.jpg", photo="metaltile-after.jpg", system_img="hero-metal-tile.jpg",
         sections=[("Why choose a metal tile roof?", ticks(["<b>It's light:</b> That takes weight off the house, which is handy when replacing a heavy tile roof.",
                                                            "<b>It keeps the tiled look:</b> It suits homes where long-run wouldn't look right.",
                                                            "<b>There's plenty of choice:</b> Profiles range from the organic grooves of Stratos to the classic arches of Milano."])),
                   ("Popular colours", paras("Smooth colours include Ebony, Windsor Grey, Flax, Ironsands, Sandstone Grey and Grey Friars. Textured colours include Ashwood, Charcoal, Eclipse, Onyx, Teak and Midnight.")
                    + '<ul class="downloads">' + "".join(f'<li><a href="{GERARD_PDF_BASE}{f}" target="_blank" rel="noopener">{n} (PDF)</a></li>' for n, f in GERARD_PDFS) + "</ul>")],
         faq_h="Metal tile questions",
         faqs=[("Is Metrotile the same as Gerard?", P("Metrotile is now part of the Gerard brand, so you may see both names. If you've got an older Metrotile roof, we can still talk through your options.", Q_METROTILE)),
               ("Can metal tiles replace concrete tiles?", "Yes, it's a common swap. Mike will check the roof and talk you through it."),
               ("Are metal tile roofs noisy in the rain?", P("[Mike: answer in your own words]", Q_NOISY))],
         closing="Get a price for your metal tile roof.", pre="New roof (reroof)"),
    dict(slug="concrete-tile-roofing", path="concrete-tile-roofing/", kind="material", name="Concrete tile roofing", icon="layers",
         title="Concrete Tile Roofing Auckland | The Roof Crew",
         desc="Concrete tile roofs for Auckland homes. Strong, non-corrosive and available in plenty of profiles. Talk to Mike about a free site visit.",
         h1="Concrete tile roofing in Auckland",
         lede=C("Concrete tiles are strong, non-corrosive and built to handle New Zealand weather. They come in a wide range of profiles and offer good thermal and acoustic performance. They're also heavy, so we check the structure first."),
         hold=C(CONCRETE_HOLD),
         system="Concrete tile", system_text=C("Heavy, solid and good at keeping noise out. It may need a structural check first."),
         card=C("Concrete tiles are strong, don't corrode and come in plenty of profiles. They're heavy, so we'll check your house can take them first."),
         hero="concrete-tile.jpg", photo="concrete-tile.jpg", system_img="concrete-tile.jpg",
         sections=[],
         faq_h="Concrete tile questions",
         faqs=[("Should I replace concrete tiles or switch to something lighter?", C("It depends on the condition of your roof and the look you want. Mike will give you the pros and cons of each.")),
               ("Can you repair a few cracked tiles?", C("Yes. If the rest of the roof is sound, a repair may be all you need."))],
         closing="Talk to Mike about your tile roof.", pre="New roof (reroof)"),
    dict(slug="roof-repairs", path="services/roof-repairs/", kind="service", name="Roof repairs", icon="wrench",
         title="Roof Repairs Auckland | Leaks & Storm Damage | The Roof Crew",
         desc="Roof leaking in Auckland? We fix leaks, storm damage and slipped or cracked tiles, and we'll tell you straight if a repair won't solve it.",
         h1="Roof repairs in Auckland",
         lede="We fix leaks, storm damage and slipped or cracked tiles across Auckland. We find out why the roof is leaking first, so you're not paying for the same fix twice.",
         hold=P("Waiting on Mike: this page goes live once he confirms he wants repair leads.", Q_REPAIRS_PAGE),
         home_card="Leaks, storm damage and slipped or cracked tiles.",
         card="We fix leaks, storm damage and slipped or cracked tiles. If a repair won't solve the problem, we'll tell you before you spend money on it.",
         hero="bg-local-street.jpg", photo="colorsteel-before.jpg",
         sections=[("Repair or replace?", paras("A repair usually makes sense when the damage is in one spot and the roof has years left in it. If leaks are showing up in different places, or it's the home's original roof, a reroof may be better value."))],
         faq_h="Roof repair questions",
         faqs=[("Can you come out urgently?", P("[Mike: whether you take urgent leak or storm jobs, and how quickly]", Q_URGENT)),
               ("What should I do if my roof is leaking?", f"Put a bucket under the drip and move anything valuable out of the way. Don't get on the roof yourself, then call or text Mike on {PHONE}.")],
         closing="Get your roof repair sorted.", pre="Roof repair"),
    dict(slug="guttering-downpipes", path="services/guttering-downpipes/", kind="service", name="Guttering and downpipes", icon="drop",
         title="Guttering & Downpipes Auckland | The Roof Crew",
         desc="New spouting, fascia and downpipes for Auckland homes, in colours that match your roof. Often best done alongside a reroof.",
         h1="Guttering and downpipes in Auckland",
         lede="We install new spouting, fascia and downpipes in colours that match your roof. Many people do this alongside a reroof, as the scaffolding is already up and everything is finished together.",
         home_card="New spouting and downpipes in colours that match your roof.",
         card="We install new spouting and downpipes in colours that match your roof. It's worth doing with a reroof, when the scaffolding is already up.",
         hero="bg-sunset.jpg", photo="colorsteel-reroof-after.jpg",
         sections=[("Signs your spouting needs replacing", ticks(["Water spills over the edge when it rains", "Joints are leaking or sagging", "You can see rust or holes", "Water marks are running down your walls"]))],
         faq_h="", faqs=[],
         closing="Get a quote for new spouting.", pre="Spouting or downpipes"),
    dict(slug="roof-inspections", path="services/roof-inspections/", kind="service", name="Roof inspections and reports", icon="search",
         title="Roof Inspections & Reports Auckland | The Roof Crew",
         desc="An honest check of your roof's condition, with photos and a written report. Useful before buying or selling, or when you're chasing a leak.",
         h1="Roof inspections and reports in Auckland",
         lede="A roof inspection tells you what condition your roof is really in. We check it properly and give you a written report with photos, so you know what needs doing and what can wait.",
         hold=P("Waiting on Mike: this page goes live once he confirms he offers inspections.", Q_INSPECT_PAGE),
         home_card="An honest look at your roof, with photos and a written report.",
         card="Not sure what shape your roof is in? We'll check it and give you a written report with photos, which is handy before buying or selling.",
         hero="bg-local-street.jpg", photo="concretetile-reroof-before.jpg",
         sections=[("When an inspection is worth it", ticks(["You're buying or selling a home", "You've got a leak you can't track down", "Your roof is 30 or more years old", "There's been storm damage"])
                    + paras(P("[Mike: what the report covers, and whether there's a fee]", Q_REPORT)))],
         faq_h="", faqs=[],
         closing="Book a roof inspection.", pre="Inspection or report"),
]
SERVICES_ONLY = [s for s in SERVICE_PAGES if s["kind"] == "service"]
MATERIALS = [s for s in SERVICE_PAGES if s["kind"] == "material"]


# ---------------------------------------------------------------- LOCATION PAGES
def osm(w, s, e, n):
    return f"https://www.openstreetmap.org/export/embed.html?bbox={w}%2C{s}%2C{e}%2C{n}&layer=mapnik"


EAST_SUBURBS = ["Howick", "Botany", "Pakuranga", "Half Moon Bay", "Bucklands Beach", "Cockle Bay", "Dannemora",
                "Flat Bush", "Highland Park", "Eastern Beach", "Shelly Park", "Mellons Bay", "Sunnyhills", "Farm Cove",
                "Burswood", "Golflands", "Whitford", "Beachlands", "Maraetai"]


def local_job(place):
    return P(f"[Local job: a recent {place} roof, with a photo]", Q_LOCAL_JOB.format(place=place))


def pick_review(who, area):
    return P(f"[Mike or Josh: pick a Google review from {area}]", Q_PICK_REVIEW.format(who=who))


LOCATION_PAGES = [
    dict(slug="east-auckland", path="locations/east-auckland/", kind="region", name="East Auckland",
         blurb="Howick, Botany, Pakuranga, Flat Bush, Beachlands and nearby.",
         title="Reroofing in East Auckland | The Roof Crew",
         desc="Reroofing and roofing services in Howick, Botany, Pakuranga, Flat Bush and across East Auckland. Free, no-pressure quotes.",
         h1="Reroofing in East Auckland", lede="Free, no-pressure reroof quotes from Howick and Pakuranga to Flat Bush and Beachlands.",
         local_h="Your local reroofing crew.", local=paras("From Howick to Beachlands, the same family crew quotes, builds and guarantees every roof."),
         hero="bg-sunset.jpg", photo="bg-sunset.jpg", reviews="home", faqs=[], suburbs=EAST_SUBURBS,
         map=osm(174.83, -36.99, 175.06, -36.84)),
    dict(slug="north-shore", path="locations/north-shore/", kind="region", name="North Shore",
         blurb="Glenfield, Albany, Takapuna, Devonport and nearby.",
         title="Roofers North Shore | Reroofing & Repairs | The Roof Crew",
         desc="Reroofing, new roofs and repairs across the North Shore, from Albany to Devonport. Free site visits and fixed, itemised quotes from a family crew.",
         h1="Reroofing on the North Shore", lede="Free, no-pressure reroof quotes from Albany and Glenfield to Takapuna and Devonport.",
         local_h="Your North Shore roofing crew",
         local=paras("From Albany to Devonport and up to Whangaparāoa, the same family crew quotes, builds and guarantees every roof. Many Shore homes still have their original roof, so if yours is getting on, it's worth a check before it starts leaking."),
         cost=("What does a new roof cost on the North Shore?", paras("A COLORSTEEL® reroof on a standard North Shore home usually costs about " + PH_PRICE_STD() + ". Steep sections, access and what we find under the old roof all affect the price, which is why you get a fixed, itemised quote after a free site visit.")),
         hero="bg-local-street.jpg", photo="colorsteel-after.jpg",
         review=pick_review("North Shore (not the one used on the Glenfield page)", "a North Shore customer"), faqs=[],
         suburbs=["Glenfield", "Albany", "Takapuna", "Devonport", "Birkenhead", "Northcote", "Milford", "Browns Bay", "Mairangi Bay", "Torbay", "Hillcrest", "Beach Haven", "Sunnynook", "Forrest Hill", "Castor Bay", "Greenhithe", "Whangaparāoa"],
         map=osm(174.62, -36.87, 174.84, -36.58)),
    dict(slug="south-auckland", path="locations/south-auckland/", kind="region", name="South Auckland",
         blurb="Manukau, Manurewa, Papakura, Takanini, Pukekohe and nearby.",
         title="Roofers South Auckland | Reroofing & Repairs | The Roof Crew",
         desc="Roofers across South Auckland, from Manukau and Papatoetoe to Papakura and Pukekohe. Reroofs, new roofs and repairs, with free site visits.",
         h1="Reroofing in South Auckland", lede="Free, no-pressure reroof quotes from Manukau and Manurewa to Papakura and Pukekohe.",
         local_h="Your South Auckland roofing crew",
         local=paras("From Papatoetoe to Pukekohe, the same family crew quotes, builds and guarantees every roof. South Auckland has plenty of older homes due for a new roof, "
                     + P("as well as new builds around Takanini and Drury, and we look after both", Q_NEWBUILD_SOUTH) + "."),
         hero="bg-sunset.jpg", photo="colorsteel-reroof-after.jpg",
         review=pick_review("South Auckland (not one used on the Papakura or Pukekohe pages)", "a South Auckland customer"), faqs=[],
         suburbs=["Manukau", "Manurewa", "Papakura", "Pukekohe", "Papatoetoe", "Ōtāhuhu", "Māngere", "Ōtara", "Takanini", "Wattle Downs", "Clendon Park", "Weymouth", "Drury", "Karaka"],
         map=osm(174.74, -37.26, 175.02, -36.92)),
    dict(slug="west-auckland", path="locations/west-auckland/", kind="region", name="West Auckland",
         blurb="Henderson, Massey, Te Atatū, Titirangi, Kumeū and nearby.",
         title="Roofers West Auckland | Reroofing & Repairs | The Roof Crew",
         desc="Reroofing, new roofs and repairs across West Auckland, from Henderson and Te Atatū to Titirangi and Kumeū. Free site visits and fixed quotes.",
         h1="Reroofing in West Auckland", lede="Free, no-pressure reroof quotes from Henderson and Massey to Titirangi and Kumeū.",
         local_h="Your West Auckland roofing crew",
         local=paras("From Te Atatū to Titirangi, the same family crew quotes, builds and guarantees every roof. Plenty of West Auckland homes sit among trees or on steep sections, where leaves block spouting and moss builds up, so we check the roof, spouting and access and recommend what suits your site."),
         hero="bg-local-street.jpg", photo="photo-sunset-roof.jpg",
         review=pick_review("West Auckland (if there is one)", "a West Auckland customer"), faqs=[],
         suburbs=["Henderson", "Massey", "Te Atatū", "Titirangi", "Kumeū", "Huapai", "Glen Eden", "New Lynn", "Kelston", "Swanson", "Ranui", "Hobsonville", "West Harbour", "Green Bay", "Laingholm"],
         map=osm(174.45, -36.98, 174.72, -36.74)),
    dict(slug="pukekohe", path="roofers-in-pukekohe/", kind="area", region="South Auckland", name="Pukekohe",
         title="Roofers in Pukekohe | Reroofing & Repairs | The Roof Crew",
         desc="Need a roofer in Pukekohe? We do reroofs, new roofs and repairs across Pukekohe and Franklin, with a free site visit and a fixed quote.",
         h1="Roofers in Pukekohe", lede="Free, no-pressure roof quotes across Pukekohe and the wider Franklin area.",
         local_h="Your roofing crew for Pukekohe and Franklin",
         local=paras("We make the trip down to Pukekohe for reroofs, new roofs and repairs. " + P("Whether you're in town or out on a lifestyle block, you'll get the same fixed quote and deal with Mike the whole way through.", Q_RURAL)),
         job=local_job("Pukekohe"), hero="bg-sunset.jpg",
         review=("Thanks for the awesome roof!!! Excellent experience all around.", "Julie and Trev, Tuakau"),
         faq_h="Pukekohe questions",
         faqs=[("Do you really come out to Pukekohe?", "Yes. We work right across Auckland, and Pukekohe is well within our area."),
               ("How long does a reroof take in Pukekohe?", "An average three-bedroom house takes " + P("about 3 to 4 days", Q_DAYS) + ", depending on the weather.")],
         suburbs=["Pukekohe", "Paerata", "Patumāhoe", "Buckland", "Karaka", "Waiuku", "Bombay", "Tuakau"], suburbs_q=Q_PUKE_SUBURBS,
         map=osm(174.80, -37.27, 175.02, -37.13)),
    dict(slug="papakura", path="locations/papakura/", kind="area", region="South Auckland", name="Papakura",
         title="Roofers in Papakura | Reroofing & Repairs | The Roof Crew",
         desc="Roofers in Papakura for reroofs, new roofs and leak repairs. A family-owned crew, a free site visit and a fixed quote. Call or text Mike.",
         h1="Roofers in Papakura", lede="Free, no-pressure roof quotes across Papakura, Takanini and Drury.",
         local_h="A family crew that's already worked in Papakura",
         local=paras("We've replaced roofs in Papakura, and we're happy to come and look at yours. If your roof keeps leaking, we'll work out whether a repair will fix it or whether it's time for a new one. "
                     + P("If it's a new build around Takanini or Drury, we can help there too.", Q_NEWBUILD_SOUTH)),
         job=local_job("Papakura"), hero="bg-local-street.jpg",
         review=("Great job by The Roof Crew. Finished our roofing project on time and in budget. Would highly recommend.", "Sandra, Papakura"),
         faq_h="Papakura questions",
         faqs=[("How much does a new roof cost in Papakura?", "A COLORSTEEL® reroof on a standard home usually costs about " + PH_PRICE_STD() + ". You'll get a fixed price after a free site visit."),
               ("Can you just repair my roof?", "Often, yes. If the roof has good years left, Mike will tell you, and won't push a full reroof.")],
         suburbs=["Papakura", "Takanini", "Red Hill", "Pahurehure", "Conifer Grove", "Rosehill", "Opaheke", "Drury"],
         map=osm(174.89, -37.11, 175.0, -37.0)),
    dict(slug="glenfield", path="locations/glenfield/", kind="area", region="North Shore", name="Glenfield",
         title="Roofers in Glenfield | North Shore Roofing | The Roof Crew",
         desc="Roofers in Glenfield and the North Shore for reroofs, repairs and new spouting. Free site visits and fixed quotes from a family-owned crew.",
         h1="Roofers in Glenfield", lede="Free, no-pressure roof quotes across Glenfield and the central North Shore.",
         local_h="Reroofing homes across Glenfield",
         local=paras("If your Glenfield home still has its original roof, it's worth getting it checked before it starts leaking. We'll look at the roof, tell you honestly how long it's got, and give you a fixed price if it's time for a new one. Many people replace the spouting at the same time, as the scaffolding is already up."),
         job=local_job("Glenfield"), hero="bg-colorsteel.jpg",
         review=("Great job guys! I shall certainly recommend you when I can.", "Nancy, Glenfield"),
         faq_h="Glenfield questions",
         faqs=[("How do I know if my roof needs replacing?", "Look for leaks that keep coming back, rust, lifting sheets or cracked tiles. If it's the original roof, it's usually near the end of its life."),
               ("Do you cover the rest of the North Shore?", "Yes. We work right across the Shore, from Albany to Devonport.")],
         suburbs=["Glenfield", "Hillcrest", "Birkdale", "Beach Haven", "Birkenhead", "Totara Vale", "Bayview", "Marlborough", "Sunnynook", "Wairau Valley"],
         map=osm(174.66, -36.81, 174.78, -36.75)),
    dict(slug="manukau", path="locations/manukau/", kind="area", region="South Auckland", name="Manukau",
         title="Roofers in Manukau | Reroofing & Repairs | The Roof Crew",
         desc="Roofers in Manukau for reroofs and roof repairs. Talk to Mike directly, get a free site visit and a fixed, itemised quote.",
         h1="Roofers in Manukau", lede="Free, no-pressure roof quotes across Manukau and Papatoetoe.",
         local_h="Straight answers on your Manukau roof",
         local=paras("A roof is a big expense, so you should know exactly what you're paying for. We'll come out, check the roof and give you an itemised, fixed price. "
                     + P("There's finance available if you'd rather spread the cost.", Q_FINANCE)),
         job=local_job("Manukau"), hero="bg-sunset.jpg",
         review=pick_review("Manukau", "a South Auckland customer"),
         faq_h="Manukau questions",
         faqs=[("Do you work on rental properties?", P("Yes, we work with landlords and property managers too.", Q_RENTALS)),
               ("Can I spread the cost of a new roof?", P("Yes, finance is available.", Q_FINANCE) + " Talk to Mike about the options.")],
         suburbs=["Manukau", "Papatoetoe", "Wiri", "Goodwood Heights", "Totara Heights", "Clover Park", "Ōtara"],
         map=osm(174.82, -37.03, 174.94, -36.93)),
    dict(slug="manurewa", path="locations/manurewa/", kind="area", region="South Auckland", name="Manurewa",
         title="Roofers in Manurewa | Roof Replacement | The Roof Crew",
         desc="Leaking roof in Manurewa? We repair and replace roofs across Manurewa and Wattle Downs, with a free site visit and a fixed quote.",
         h1="Roofers in Manurewa", lede="Free, no-pressure roof quotes across Manurewa and Wattle Downs.",
         local_h="Leak keep coming back?",
         local=paras("When a leak keeps coming back, the problem usually isn't where the water is showing. We'll find out what's actually going on and tell you whether a repair will last. If the roof is done, we'll give you a fixed price to replace it."),
         job=local_job("Manurewa"), hero="bg-local-street.jpg",
         review=pick_review("Manurewa", "a South Auckland customer"),
         faq_h="Manurewa questions",
         faqs=[("How long does a new roof last?", "It depends on the product and location. As a guide, COLORSTEEL® typically lasts " + P("around 30 years before perforation", Q_CS_LIFE2) + "."),
               ("Is there a good time of year to reroof?", "Not really. We can replace roofs all year in Auckland, and it's better not to wait until it's leaking.")],
         suburbs=["Manurewa", "Wattle Downs", "Clendon Park", "Weymouth", "Hillpark", "Randwick Park", "Homai"],
         map=osm(174.84, -37.07, 174.95, -36.99)),
    dict(slug="howick", path="locations/howick/", kind="area", region="East Auckland", name="Howick",
         title="Roofers in Howick | Coastal Roofing | The Roof Crew",
         desc="Roofers in Howick and East Auckland for reroofs and repairs, including options for coastal homes. Free site visits and fixed quotes.",
         h1="Roofers in Howick", lede="Free, no-pressure roof quotes across Howick and the eastern bays.",
         local_h="Roofs that suit a coastal home",
         local=paras("Salt in the air is hard on a roof, so what works inland may not be right near the water. If you're close to the coast around Howick, we'll check your site and recommend a product suited to it, such as COLORSTEEL® Endura® or Maxx®. We've also replaced roofs in nearby Mellons Bay."),
         job=local_job("Howick"), hero="bg-sunset.jpg",
         review=("Excellent job done! The roof looks great, also the new cladding to the gables and the new spouting is fantastic. Highly recommend.", "Anne and Richard, Mellons Bay"),
         faq_h="Howick questions",
         faqs=[("Which roof is best near the sea?", "It depends how exposed your home is. COLORSTEEL® Maxx® is made for rugged coastlines, and Mike will recommend what suits your site."),
               ("Can you replace the spouting too?", "Yes. It makes sense to do it with a reroof, as the scaffolding is already up.")],
         suburbs=["Howick", "Cockle Bay", "Mellons Bay", "Shelly Park", "Eastern Beach", "Bucklands Beach", "Half Moon Bay", "Sunnyhills"],
         map=osm(174.88, -36.92, 174.97, -36.86)),
]
REGIONS = [l for l in LOCATION_PAGES if l["kind"] == "region"]
AREAS = [l for l in LOCATION_PAGES if l["kind"] == "area"]
LOC_BY_SLUG = {l["slug"]: l for l in LOCATION_PAGES}
LOC_BY_NAME = {l["name"]: l for l in LOCATION_PAGES}

# ---------------------------------------------------------------- BLOG (current live copy, moved across as is)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog_posts.json"), encoding="utf-8") as _f:
    _blog = json.load(_f)
POSTS = _blog["posts"]
PRIVACY = _blog["privacy"]
BLOG_PAGE = dict(title="Roofing Blog NZ | Tips, Guides & Updates | The Roof Crew",
                 desc="Explore The Roof Crew's blog for expert roofing tips and updates. Learn about roof care, repairs, and maintenance to protect your home year-round.",
                 h1="Blog")

# Links in the moved blog posts that point at the current site: where they go on the new site.
LIVE = "https://theroofcrew.co.nz/"
LINK_MAP = {"": "", "replacement-roofs/": "services/reroofing/", "concrete-tile-roofing/": "concrete-tile-roofing/",
            "metal-tile-roofing/": "metal-tile-roofing/", "colour-steel-roofing/": "colour-steel-roofing/",
            # not moving in this round: point at About until Kelsey decides
            "choose-the-best-roofing-specialist-auckland/": "about/"}

# Old addresses that now live somewhere else (static: a meta refresh page; WordPress: functions.php redirects).
REDIRECTS = {
    "services/guttering-and-downpipes/": "services/guttering-downpipes/",  # earlier staging slug
    "locations/pukekohe/": "roofers-in-pukekohe/",
    "replacement-roofs/": "services/reroofing/", "re-roofing/": "services/reroofing/", "roofing-faqs/": "services/reroofing/",
    "new-roof/": "services/new-roof-installation/", "new-build-roofing/": "services/new-roof-installation/",
    "fascia-spouting-safety/": "services/guttering-downpipes/",
    "products/": "services/", "roofing-specialists/": "services/",
    "roofing-south-auckland/": "locations/south-auckland/", "roofers-east-auckland/": "locations/east-auckland/",
    "contact-us/": "contact/", "roofing-quotes/": "quote/",
}
