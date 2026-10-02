import os, json, datetime
BASE = "https://bryanbyfield0-creator.github.io/ie-tree-quotes"
BRAND = "Inland Empire Tree Quotes"
EMAIL = "bryanbyfield0@gmail.com"
PHONE = "909-361-0443"
TODAY = datetime.date.today().isoformat()

CITIES = {
 "san-bernardino": ("San Bernardino", "From the foothill neighborhoods below the San Bernardino Mountains to older streets near downtown with big, mature trees, San Bernardino properties often need large removals, dead-wood pruning, and palm trimming. Homes near the foothills sit close to wildland areas, so many owners also want dry brush and dead trees cleared before fire season.", ["Highland","Rialto","Colton","Loma Linda"]),
 "fontana": ("Fontana", "Fontana gets some of the strongest Santa Ana winds in the region, especially in the north end near the Cajon Pass corridor. Wind-damaged limbs, leaning eucalyptus and pine, and tall palms that drop heavy fronds are common reasons Fontana homeowners ask for tree work.", ["Rialto","Rancho Cucamonga","Ontario","San Bernardino"]),
 "rialto": ("Rialto", "Rialto yards often have mature shade trees, fan palms, and fruit trees that need regular trimming. Wind events can bring down limbs onto roofs, fences, and power drops, which makes storm cleanup and preventive pruning popular requests.", ["Fontana","San Bernardino","Colton"]),
 "redlands": ("Redlands", "Redlands is known for its older neighborhoods, large historic street trees, and leftover citrus groves. Owners often need careful pruning of big, mature trees, removal of dead or declining citrus, and palm trimming that won't damage nearby structures.", ["Loma Linda","Highland","Yucaipa","San Bernardino"]),
 "highland": ("Highland", "Highland runs up to the foothills of the San Bernardino Mountains, and many properties border open land. Dead tree removal, brush clearance, and thinning trees near the house are common requests, along with routine trimming and stump grinding.", ["San Bernardino","Redlands","Yucaipa"]),
 "colton": ("Colton", "Colton has a mix of older homes, commercial lots, and properties along the Santa Ana River corridor. Common jobs include removing overgrown trees, trimming palms, clearing lots, and grinding stumps left after old removals.", ["San Bernardino","Rialto","Loma Linda","Grand Terrace"]),
 "yucaipa": ("Yucaipa", "Yucaipa's larger lots, oak woodland, and foothill terrain mean bigger trees and more brush. Homeowners commonly want dead or diseased trees removed, oaks and pines pruned, and defensible space cleared around the home.", ["Redlands","Calimesa","Highland"]),
 "rancho-cucamonga": ("Rancho Cucamonga", "Rancho Cucamonga homes, especially north of Base Line toward the foothills, deal with strong winds and larger landscape trees. Popular requests include crown thinning to reduce wind damage, palm trimming, removals for remodels, and stump grinding.", ["Fontana","Ontario","Upland"]),
}

SERVICES = [
 ("tree-removal","Tree Removal","Removing dead, dying, leaning, or unwanted trees, including large trees close to houses, fences, and power lines. Pros usually take the tree down in sections, haul the wood away, and can grind the stump if you want."),
 ("tree-trimming","Tree Trimming & Pruning","Crown thinning, raising the canopy, removing dead wood, and clearing branches away from roofs and walls. Good pruning reduces wind damage and keeps trees healthy."),
 ("palm-tree-trimming","Palm Tree Trimming","Removing dead fronds, seed pods, and skirts from fan palms, queen palms, date palms, and Mexican fan palms. Dead fronds can fall in wind and can be a fire hazard, so many owners trim palms once a year."),
 ("stump-grinding","Stump Grinding","Grinding stumps below grade so you can replant, lay sod, or pave. It's usually much cheaper than full stump excavation."),
 ("emergency-storm","Emergency & Storm Cleanup","Fallen trees and broken limbs after Santa Ana winds or storms, including trees on roofs, cars, or fences. Many tree companies offer same-day or next-day emergency service."),
 ("brush-clearance","Brush Clearance & Defensible Space","Clearing dry brush, dead trees, and overgrowth to create defensible space around homes near the foothills and open land, and handling weed abatement notices."),
]

CSS = """
*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1f2a1f;line-height:1.6;background:#fff}
a{color:#2e6b30}header{background:#1f4d22;color:#fff}header .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.5rem}
.brand{color:#fff;text-decoration:none;font-weight:700;font-size:1.15rem}nav a{color:#e6f2e6;text-decoration:none;margin-left:1rem;font-size:.95rem}
.wrap{max-width:1040px;margin:0 auto;padding:1rem 1.25rem}.hero{background:linear-gradient(135deg,#2e6b30,#4f8f3a);color:#fff}
.hero h1{font-size:2rem;line-height:1.2;margin:.5rem 0}.hero p{font-size:1.1rem;max-width:700px}
.btn{display:inline-block;background:#f2b33d;color:#1f2a1f;padding:.8rem 1.4rem;border-radius:6px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-size:1rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}.card{border:1px solid #dfe8df;border-radius:8px;padding:1rem;background:#fafdf9}
.card h3{margin-top:0}.note{background:#fff8e6;border-left:4px solid #f2b33d;padding:.8rem 1rem;border-radius:4px}
form label{display:block;font-weight:600;margin-top:.8rem}form input,form select,form textarea{width:100%;padding:.6rem;border:1px solid #b9c9b9;border-radius:6px;font:inherit}
form textarea{min-height:110px}.small{font-size:.85rem;color:#4a5a4a}footer{background:#f0f5ef;margin-top:2rem;font-size:.9rem}
ul.cities{columns:2;padding-left:1.2rem}@media(max-width:600px){nav a{margin:0 .8rem 0 0}.hero h1{font-size:1.6rem}}
"""

def page(path, title, desc, body, schema=None):
    depth = path.count("/")
    rel = "../"*depth
    canon = f"{BASE}/{path}".replace("index.html","")
    sch = f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ""
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="google-site-verification" content="QTObMCEV5W0Joa9lOXm7iWNE78Jmfe1DUmOx7eiV0R4" />
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="stylesheet" href="{rel}style.css">{sch}</head><body>
<header><div class="wrap"><a class="brand" href="{rel}index.html">🌳 {BRAND}</a>
<nav><a href="{rel}services.html">Services</a><a href="{rel}areas.html">Service Areas</a><a href="{rel}how-it-works.html">How It Works</a><a href="{rel}contact.html">Get Quotes</a></nav></div></header>
{body}
<footer><div class="wrap"><p><strong>{BRAND}</strong> is a free referral service. We are <strong>not a tree service company</strong>, we don't do tree work, and we don't hold a contractor's license. When you send a request, we pass it to independent local tree service providers who can contact you with quotes. Any provider you hire is solely responsible for its work, licensing, and insurance. Always check a contractor's license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> and ask for proof of insurance before hiring.</p>
<p><a href="{rel}services.html">Services</a> · <a href="{rel}areas.html">Service Areas</a> · <a href="{rel}how-it-works.html">How It Works</a> · <a href="{rel}privacy.html">Privacy</a> · <a href="{rel}contact.html">Contact</a></p>
<p class="small">© {datetime.date.today().year} {BRAND}. Serving San Bernardino County and nearby Inland Empire communities.</p></div></footer>
</body></html>"""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path,"w").write(html)

def cta(rel=""):
    return f'<p><a class="btn" href="{rel}contact.html">Get free tree service quotes</a></p>'

pages=[]
# HOME
svc_cards="".join(f'<div class="card"><h3>{n}</h3><p>{d}</p><a href="services.html#{s}">Learn more</a></div>' for s,n,d in SERVICES)
city_links="".join(f'<li><a href="areas/{k}.html">{v[0]} tree service</a></li>' for k,v in CITIES.items())
faq=[("Is this service free?","Yes. Requesting quotes through this site is free for homeowners, and there's no obligation to hire anyone."),
("Are you a tree company?","No. We're a referral service that connects you with independent local tree service providers. We don't do tree work ourselves."),
("How much does tree removal cost in the Inland Empire?","It depends on the tree's size, species, location (near the house, power lines, or a slope), access, and whether you want the stump ground. Small jobs can be a few hundred dollars; large or difficult removals can run into the thousands. Getting more than one quote is the best way to know."),
("Do tree companies need a license in California?","In California, tree work above the state's minor-work dollar limit generally requires a contractor's license from the Contractors State License Board (CSLB). Look up any company at cslb.ca.gov before hiring, and ask for proof of liability and workers' comp insurance."),
("Do I need a permit to remove a tree?","Some cities and HOAs regulate removal of certain trees, especially street trees or protected species. Check with your city or HOA before removing a large tree.")]
faq_html="".join(f"<h3>{q}</h3><p>{a}</p>" for q,a in faq)
faq_schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
page("index.html", f"Tree Removal & Palm Tree Trimming Quotes | San Bernardino, Fontana, Redlands | {BRAND}",
 "Get free quotes from local tree service pros for tree removal, trimming, palm tree trimming, and stump grinding in San Bernardino, Fontana, Rialto, Redlands, and nearby Inland Empire cities.",
f"""<section class="hero"><div class="wrap"><h1>Tree removal, trimming & palm tree service quotes in the Inland Empire</h1>
<p>Tell us about your tree job once and we'll connect you with local tree service providers in San Bernardino, Fontana, Rialto, Redlands, and nearby cities. It's free, and you don't have to hire anyone.</p>
<p><a class="btn" href="contact.html">Request free quotes</a></p></div></section>
<main class="wrap">
<p class="note"><strong>Plain-English disclosure:</strong> {BRAND} is a referral service, not a tree company. We pass your request to independent local providers who can contact you. We don't do the work, and we can't vouch for any provider's license or insurance, so please verify both before you hire.</p>
<h2>Tree services we can help you find</h2><div class="grid">{svc_cards}</div>
<h2>How it works</h2><ol><li><strong>Describe the job</strong>: what kind of tree, how big, where it is, and how soon you need it done.</li><li><strong>We match you</strong> with independent tree service providers who serve your city.</li><li><strong>Compare quotes</strong> and hire whoever you choose, or nobody at all.</li></ol>
{cta()}
<h2>Cities we cover</h2><ul class="cities">{city_links}</ul>
<h2>Tips before you hire a tree service</h2><ul><li>Get at least two or three written quotes that list exactly what's included (haul-away, stump grinding, cleanup).</li><li>Check the company's license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> and ask for its certificate of insurance.</li><li>Be careful with door-to-door "storm chasers" who want cash up front.</li><li>Never try to work on trees near power lines yourself. Call your utility.</li></ul>
<h2>Frequently asked questions</h2>{faq_html}{cta()}</main>""", faq_schema)

# SERVICES
svc_html="".join(f'<section id="{s}"><h2>{n}</h2><p>{d}</p><p><a href="contact.html?service={s}">Get {n.lower()} quotes</a></p></section>' for s,n,d in SERVICES)
page("services.html", f"Tree Services: Removal, Trimming, Palm Trimming, Stump Grinding | {BRAND}",
 "Tree removal, tree trimming, palm tree trimming, stump grinding, storm cleanup, and brush clearance quotes from local Inland Empire providers.",
f'<main class="wrap"><h1>Tree services in the Inland Empire</h1><p>Here are the most common tree jobs homeowners and property managers ask about. Send one request and local providers can quote your job.</p>{svc_html}<p class="note">Prices depend on tree size, species, access, and hazards. The only reliable number is a written quote from a licensed, insured provider who has seen the job.</p>{cta()}</main>')

# AREAS index
page("areas.html", f"Service Areas: San Bernardino County Tree Service Quotes | {BRAND}",
 "Tree service quotes for San Bernardino, Fontana, Rialto, Redlands, Highland, Colton, Yucaipa, and Rancho Cucamonga.",
f'<main class="wrap"><h1>Service areas</h1><p>We currently take requests from these Inland Empire communities. If your city isn\'t listed, send a request anyway and we\'ll try to find a provider nearby.</p><ul class="cities">{"".join(f"<li><a href=areas/{k}.html>{v[0]}</a></li>" for k,v in CITIES.items())}</ul>{cta()}</main>')

for k,(name,blurb,near) in CITIES.items():
    svc_list="".join(f"<li><strong>{n}</strong>: {d}</li>" for s,n,d in SERVICES)
    near_links=", ".join(f'<a href="{(c.lower().replace(" ","-"))}.html">{c}</a>' if c.lower().replace(" ","-") in CITIES else c for c in near)
    sch={"@context":"https://schema.org","@type":"Service","serviceType":"Tree service referral","name":f"Tree service quotes in {name}, CA","areaServed":{"@type":"City","name":f"{name}, California"},"provider":{"@type":"Organization","name":BRAND,"url":BASE+"/"},"description":f"Free referral service that connects {name} property owners with independent local tree service providers."}
    page(f"areas/{k}.html", f"Tree Removal & Trimming Quotes in {name}, CA | {BRAND}",
     f"Free tree removal, tree trimming, palm tree trimming, and stump grinding quotes from local providers serving {name}, California.",
f"""<main class="wrap"><h1>Tree service quotes in {name}, CA</h1>
<p>{blurb}</p>
<p>Send us one request and we'll pass it to independent tree service providers who work in {name}. It's free, and you don't have to hire anyone.</p>
{cta("../")}
<h2>Common tree jobs in {name}</h2><ul>{svc_list}</ul>
<h2>Before you hire in {name}</h2><ul><li>Ask whether your job needs a city permit (some cities regulate street trees or certain species). The City of {name} or your HOA can tell you.</li><li>Check the contractor's license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> and get proof of insurance.</li><li>Get the scope in writing: haul-away, stump grinding, and cleanup.</li><li>For trees touching power lines, contact your electric utility first.</li></ul>
<p>Nearby areas: {near_links}.</p>
<p class="note">{BRAND} is a referral service, not a tree company. Independent providers do all the work.</p>{cta("../")}</main>""", sch)

# HOW IT WORKS
page("how-it-works.html", f"How It Works | {BRAND}", "How our free tree service referral works and what we do with your request.",
f"""<main class="wrap"><h1>How {BRAND} works</h1>
<p>We're a small, independent referral service based in San Bernardino County. We built this site to make it easier to find someone for tree work without calling a dozen companies.</p>
<ol><li>You fill out the <a href="contact.html">quote request form</a>.</li><li>We review it and share your job details and contact information with one or more independent tree service providers who serve your area.</li><li>Providers contact you directly to schedule an estimate or give a quote.</li><li>You decide who to hire, if anyone. Your agreement is directly with that provider.</li></ol>
<h2>What we are, and what we aren't</h2><ul><li>We're <strong>not</strong> a licensed contractor and we don't do tree work.</li><li>We don't guarantee any provider's work, price, license, or insurance. Please verify a license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> before hiring.</li><li>We may receive a fee from providers for referrals. It never costs you anything.</li><li>We don't post fake reviews or ratings.</li></ul>
<h2>Tree service companies</h2><p>Do you run a licensed, insured tree service in the Inland Empire and want more local jobs? <a href="contact.html?type=provider">Get in touch</a>.</p>{cta()}</main>""")

# CONTACT
form=f"""<form action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="hidden" name="_subject" value="New tree service quote request (IE Tree Quotes)">
<input type="hidden" name="_next" value="{BASE}/thank-you.html">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<label for="name">Your name *</label><input id="name" name="name" required>
<label for="phone">Phone *</label><input id="phone" name="phone" type="tel" required>
<label for="email">Email</label><input id="email" name="email" type="email">
<label for="city">City *</label><select id="city" name="city" required><option value="">Choose your city</option>{"".join(f"<option>{v[0]}</option>" for v in CITIES.values())}<option>Other Inland Empire city</option></select>
<label for="service">What do you need? *</label><select id="service" name="service" required><option value="">Choose a service</option>{"".join(f'<option value="{n}">{n}</option>' for s,n,d in SERVICES)}<option>Other / not sure</option><option>I'm a tree service provider</option></select>
<label for="timing">How soon?</label><select id="timing" name="timing"><option>Emergency (tree down / hazard)</option><option>Within 1-2 weeks</option><option selected>Within a month</option><option>Just getting prices</option></select>
<label for="details">Job details (tree type, rough height, number of trees, near house or power lines?)</label><textarea id="details" name="details"></textarea>
<label><input type="checkbox" name="consent" value="yes" required style="width:auto"> I agree that {BRAND} may share my request and contact info with independent local tree service providers so they can contact me about this job. *</label>
<p><button class="btn" type="submit">Send my request</button></p>
<p class="small">We'll use your information only to connect you with providers for this request. See our <a href="privacy.html">privacy policy</a>.</p></form>"""
page("contact.html", f"Get Free Tree Service Quotes | {BRAND}", "Request free quotes for tree removal, trimming, palm trimming, or stump grinding in the Inland Empire.",
f'<main class="wrap"><h1>Get free tree service quotes</h1><p>Fill out the form and we\'ll pass your request to independent local tree service providers. There\'s no cost and no obligation.</p><p class="note">Emergency? If a tree is on a power line or there\'s immediate danger, stay away and call 911 or your electric utility first.</p>{form}<p class="small">Prefer to call? {PHONE} (optional; the form is the fastest way to reach us).</p></main>')

page("thank-you.html", f"Thanks, we got your request | {BRAND}", "Thank you for your tree service request.",
 f"""<main class="wrap"><h1>Thanks! Your request was sent.</h1><p>We'll review it and pass it to local tree service providers who serve your area. They'll contact you directly. Please check each provider's license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> before hiring.</p><p><a href="index.html">Back to home</a></p></main>""")

page("privacy.html", f"Privacy Policy | {BRAND}", "Privacy policy for Inland Empire Tree Quotes.",
f"""<main class="wrap"><h1>Privacy policy</h1><p>Last updated {TODAY}.</p>
<p><strong>What we collect:</strong> the information you enter in our form (name, phone, email, city, and job details). Our form is processed by FormSubmit (formsubmit.co), which emails it to us. Our host (GitHub Pages) may log basic technical data such as IP addresses.</p>
<p><strong>How we use it:</strong> only to respond to your request and to share it with independent tree service providers in your area so they can contact you about your job. We don't sell your information to data brokers and we don't use it for unrelated marketing.</p>
<p><strong>Your choices:</strong> email {EMAIL} to ask us to delete your information or to stop sharing it. California residents may have additional rights under the CCPA/CPRA.</p>
<p><strong>Contact:</strong> {EMAIL}</p></main>""")

open("style.css","w").write(CSS)
urls=["","services.html","areas.html","how-it-works.html","contact.html","privacy.html"]+[f"areas/{k}.html" for k in CITIES]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(".nojekyll","w").write("")
print("built")
