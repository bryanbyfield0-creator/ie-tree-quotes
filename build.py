"""Static site generator for the IE lead-gen sites.
Site-specific copy, cities, services, guides and settings live in content.py (same folder).
This file is identical across the tree and junk sites; edit content.py for copy changes.
Run: python3 build.py
"""
import os, json, datetime, html as _html
import content as C

BASE, BRAND, SHORT = C.BASE, C.BRAND, C.SHORT_BRAND
TODAY = datetime.date.today().isoformat()
YEAR = datetime.date.today().year
PHOTOS = C.PHOTOS
CITIES = C.CITIES
SERVICES = C.SERVICES
GUIDES = C.GUIDES

def esc(s): return _html.escape(s, quote=True)

def img(key, rel="", cls="photo", lazy=True):
    src,w,h,alt,*_ = PHOTOS[key]
    la = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img class="{cls}" src="{rel}{src}" width="{w}" height="{h}" alt="{esc(alt)}"{la}>'

def hidden_fields():
    return f"""<input type="hidden" name="_subject" value="{esc(C.FORM_SUBJECT)}">
<input type="hidden" name="_next" value="{BASE}/thank-you.html">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">"""

ORG = {"@type":"Organization","@id":BASE+"/#org","name":BRAND,"url":BASE+"/","email":C.EMAIL,
       "description":C.ORG_DESCRIPTION}
def area_list(keys=None):
    keys = keys or list(CITIES)
    return [{"@type":"City","name":f"{CITIES[k]['name']}, CA"} for k in keys]

def breadcrumb_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":f"{BASE}/{u}"} for i,(n,u) in enumerate(items)]}

def faq_ld(faq):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":_strip(a)}} for q,a in faq]}

def _strip(s):
    import re
    return re.sub(r"<[^>]+>","",s)

def faq_html(faq):
    return "".join(f"<h3>{q}</h3><p>{a}</p>" for q,a in faq)

def sources_html(srcs):
    if not srcs: return ""
    return '<h2>Sources</h2><ul class="sources">'+"".join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{esc(t)}</a></li>' for t,u in srcs)+f'</ul><p class="small">Rules and programs change. Confirm details with the city, county, or agency before relying on them. Checked {C.FACTS_CHECKED}.</p>'

def crumbs(items, rel):
    parts=[f'<a href="{rel}index.html">Home</a>']+[f'<a href="{rel}{u}">{esc(n)}</a>' for n,u in items[:-1]]+[f'<span>{esc(items[-1][0])}</span>']
    return '<nav class="crumbs" aria-label="Breadcrumb">'+" › ".join(parts)+'</nav>'

PAGES=[]
def page(path, title, desc, body, schemas=(), mcta=True):
    assert len(title) <= 70, (path, len(title), title)
    assert 70 <= len(desc) <= 165, (path, len(desc), desc)
    PAGES.append((path,title,desc))
    depth = path.count("/")
    rel = "../"*depth
    canon = f"{BASE}/{path}".replace("index.html","")
    body_cls = ' class="has-mcta"' if mcta else ""
    mcta_href = "#quote" if path == "index.html" else f"{rel}contact.html"
    mcta_html = f'<div class="mobile-cta"><a href="{mcta_href}">Get free quotes</a></div>' if mcta else ""
    credits = ", ".join(dict.fromkeys(f'<a href="{v[5]}" rel="nofollow">{v[4]}</a> ({v[6]})' for v in PHOTOS.values()))
    sch = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas if s)
    verif = f'<meta name="google-site-verification" content="{C.GOOGLE_VERIFICATION}" />' if C.GOOGLE_VERIFICATION else ""
    robots = '<meta name="robots" content="noindex, follow">' if path == "thank-you.html" else ""
    og_img = f"{BASE}/{PHOTOS['hero'][0]}"
    guide_links = " · ".join(f'<a href="{rel}guides/{g["slug"]}.html">{esc(g["nav"])}</a>' for g in GUIDES)
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{verif}
{robots}<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:site_name" content="{esc(BRAND)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:image" content="{og_img}"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{rel}style.css">{sch}</head><body{body_cls}>
<header><div class="wrap"><a class="brand" href="{rel}index.html">{C.EMOJI} {BRAND}</a>
<nav aria-label="Main"><a href="{rel}services.html">Services</a><a href="{rel}areas.html">Service Areas</a><a href="{rel}guides/index.html">Guides</a><a href="{rel}how-it-works.html">How It Works</a><a class="nav-cta" href="{rel}contact.html">Get Quotes</a></nav></div></header>
{body}
<footer><div class="wrap"><p>{C.FOOTER_DISCLOSURE.replace('{rel}',rel)}</p>
<p><a href="{rel}services.html">Services</a> · <a href="{rel}areas.html">Service Areas</a> · <a href="{rel}guides/index.html">Guides</a> · <a href="{rel}how-it-works.html">How It Works</a> · <a href="{rel}privacy.html">Privacy</a> · <a href="{rel}contact.html">Contact</a></p>
<p class="small"><strong>Guides:</strong> {guide_links}</p>
<p class="small">{getattr(C,'SISTER_SITE','')}</p>
<p class="small">© {YEAR} {BRAND}. {C.FOOTER_AREA}</p>
<p class="credits">Photos: {credits}, used under free licenses. People shown are not affiliated with this site. <a href="{rel}privacy.html#photos">Photo credits</a></p></div></footer>
{mcta_html}
</body></html>"""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path,"w").write(html)

def cta(rel=""):
    return f'<p><a class="btn" href="{rel}contact.html">{C.CTA_TEXT}</a></p>'

CITY_OPTS = "".join(f"<option>{v['name']}</option>" for v in CITIES.values()) + "<option>Other Inland Empire city</option>"
SVC_OPTS = "".join(f'<option value="{n}">{n}</option>' for s,n,d in SERVICES) + "<option>Other / not sure</option>"
CONSENT = f"I agree that {BRAND} may share my request and contact info with independent local {C.PROVIDER_NOUN} providers so they can contact me about this job. *"

def quick_form(rel=""):
    return f"""<div class="quote-card" id="quote"><h2>Get free quotes</h2><p class="small">Takes about 30 seconds. Free, no obligation.</p>
<form action="{C.FORM_ACTION}" method="POST">
{hidden_fields()}
<input type="hidden" name="form" value="Homepage quick form">
<div class="row"><div><label for="q-name">Your name *</label><input id="q-name" name="name" autocomplete="name" required></div>
<div><label for="q-phone">Phone *</label><input id="q-phone" name="phone" type="tel" autocomplete="tel" required></div></div>
<div class="row"><div><label for="q-city">City *</label><select id="q-city" name="city" required><option value="">Choose your city</option>{CITY_OPTS}</select></div>
<div><label for="q-service">Service *</label><select id="q-service" name="service" required><option value="">Choose a service</option>{SVC_OPTS}</select></div></div>
<label for="q-details">{C.QUICK_DETAILS_LABEL}</label><textarea id="q-details" name="details" placeholder="{esc(C.QUICK_DETAILS_PLACEHOLDER)}"></textarea>
<label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>{CONSENT}</span></label>
<p style="margin:.7rem 0 .2rem"><button class="btn btn-block" type="submit">Get my free quotes</button></p>
<p class="small">Want to add email, timing, or more details? Use the <a href="{rel}contact.html">full request form</a>. See our <a href="{rel}privacy.html">privacy policy</a>.</p></form></div>"""

def service_ld(name, desc, keys=None, url=None):
    return {"@context":"https://schema.org","@type":"Service","serviceType":name,"name":name,"description":desc,
            "provider":ORG,"areaServed":area_list(keys),"url":url or BASE+"/"}

def city_link(name, rel=""):
    slug = name.lower().replace(" ","-")
    return f'<a href="{rel}{slug}.html">{name}</a>' if slug in CITIES else name

# ---------- HOME ----------
svc_cards="".join(f'<div class="card"><h3>{n}</h3><p>{d}</p><a href="services.html#{s}">More about {n.lower()}</a></div>' for s,n,d in SERVICES)
city_links="".join(f'<li><a href="areas/{k}.html">{C.CITY_LINK_TEXT.format(city=v["name"])}</a></li>' for k,v in CITIES.items())
guide_cards="".join(f'<div class="card"><h3><a href="guides/{g["slug"]}.html">{g["h1"]}</a></h3><p>{g["blurb"]}</p></div>' for g in GUIDES)
home_ld=[{"@context":"https://schema.org","@type":"WebSite","name":BRAND,"url":BASE+"/"},
         dict({"@context":"https://schema.org"},**ORG),
         service_ld(C.SERVICE_TYPE, C.ORG_DESCRIPTION),
         faq_ld(C.HOME_FAQ)]
page("index.html", C.HOME_TITLE, C.HOME_DESC,
f"""<section class="hero">{img("hero", cls="hero-bg", lazy=False)}<div class="wrap"><div>{C.HERO_HTML}</div>
{quick_form()}</div></section>
<main class="wrap">
<p class="note">{C.HOME_DISCLOSURE}</p>
<h2>{C.HOME_SERVICES_H2}</h2><div class="grid">{svc_cards}</div>
<div class="split"><div>{C.HOME_HOW_HTML}
{cta()}</div>{img(C.HOME_SPLIT_IMG)}</div>
<h2>Cities we cover</h2><ul class="cities">{city_links}</ul>
<h2>Homeowner guides</h2><div class="grid">{guide_cards}</div>
<h2>{C.TIPS_H2}</h2>{C.TIPS_HTML}
<h2>Frequently asked questions</h2>{faq_html(C.HOME_FAQ)}{cta()}</main>""", home_ld)

# ---------- SERVICES ----------
svc_html="".join((f'<section id="{s}" class="svc">{img(C.SVC_IMG[s])}<div>' if s in C.SVC_IMG else f'<section id="{s}"><div>')+f'<h2>{n}</h2><p>{d}</p><p><a href="contact.html?service={s}">Get {n.lower()} quotes</a></p></div></section>' for s,n,d in SERVICES)
svc_city="".join(f'<li><a href="areas/{k}.html">{v["name"]}</a></li>' for k,v in CITIES.items())
page("services.html", C.SERVICES_TITLE, C.SERVICES_DESC,
f'<main class="wrap">{crumbs([("Services","services.html")],"")}<h1>{C.SERVICES_H1}</h1><p>{C.SERVICES_INTRO}</p>{svc_html}<p class="note">{C.SERVICES_NOTE}</p>{C.SERVICES_EXTRA}<h2>Find a provider in your city</h2><ul class="cities">{svc_city}</ul>{cta()}</main>',
[breadcrumb_ld([("Home",""),("Services","services.html")])]+[service_ld(n,d,url=f"{BASE}/services.html#{s}") for s,n,d in SERVICES])

# ---------- AREAS ----------
area_items="".join(f'<li><a href="areas/{k}.html">{v["name"]}</a> <span class="small">({v["county"]} County)</span></li>' for k,v in CITIES.items())
page("areas.html", C.AREAS_TITLE, C.AREAS_DESC,
f'<main class="wrap">{crumbs([("Service Areas","areas.html")],"")}<h1>Service areas</h1><p>We take requests from these Inland Empire communities in San Bernardino and Riverside counties. If your city isn\'t listed, send a request anyway and we\'ll try to find a provider nearby.</p><ul class="cities">{area_items}</ul>{cta()}</main>',
[breadcrumb_ld([("Home",""),("Service Areas","areas.html")])])

# ---------- CITY PAGES ----------
for k,c in CITIES.items():
    name=c["name"]
    svc_list="".join(f'<li><a href="../services.html#{s}"><strong>{n}</strong></a>: {C.CITY_SVC_LINE(s,n,c)}</li>' for s,n,d in SERVICES)
    near="".join(f"<li>{city_link(x)}</li>" for x in c["nearby"])
    local="".join(f"<h2>{h}</h2>{b}" for h,b in c["local"])
    rg=[g for g in GUIDES if k in g.get("cities",[]) or g.get("all_cities")]
    rg_html="".join(f'<li><a href="../guides/{g["slug"]}.html">{g["h1"]}</a></li>' for g in rg)
    faq=c["faq"]+C.CITY_FAQ_COMMON(c)
    schemas=[service_ld(f"{C.SERVICE_TYPE} in {name}, CA", f"Free referral service connecting {name} residents with independent local {C.PROVIDER_NOUN} providers.", [k], f"{BASE}/areas/{k}.html"),
             faq_ld(faq), breadcrumb_ld([("Home",""),("Service Areas","areas.html"),(name,f"areas/{k}.html")])]
    page(f"areas/{k}.html", C.CITY_TITLE(c), C.CITY_DESC(c),
f"""<main class="wrap">{crumbs([("Service Areas","areas.html"),(name,f"areas/{k}.html")],"../")}<h1>{C.CITY_H1(c)}</h1>
<p>{c["intro"]}</p>
<p>Send us one request and we'll pass it to independent {C.PROVIDER_NOUN} providers who work in {name}. It's free, and you don't have to hire anyone.</p>
{cta("../")}
{local}
<h2>{C.CITY_JOBS_H2.format(city=name)}</h2><ul>{svc_list}</ul>
{('<h2>Helpful guides</h2><ul>'+rg_html+'</ul>') if rg_html else ''}
<h2>Nearby areas we cover</h2><ul class="cities">{near}</ul>
<h2>{name} FAQ</h2>{faq_html(faq)}
<p class="note">{BRAND} is a referral service, not a {C.COMPANY_NOUN}. Independent providers do all the work.</p>{cta("../")}
{sources_html(c.get("sources",[]))}</main>""", schemas)

# ---------- GUIDES ----------
gi="".join(f'<div class="card"><h2 class="h3"><a href="{g["slug"]}.html">{g["h1"]}</a></h2><p>{g["blurb"]}</p></div>' for g in GUIDES)
page("guides/index.html", C.GUIDES_TITLE, C.GUIDES_DESC,
f'<main class="wrap">{crumbs([("Guides","guides/index.html")],"../")}<h1>Homeowner guides</h1><p>{C.GUIDES_INTRO}</p><div class="grid">{gi}</div>{cta("../")}</main>',
[breadcrumb_ld([("Home",""),("Guides","guides/index.html")])])
for g in GUIDES:
    others="".join(f'<li><a href="{o["slug"]}.html">{o["h1"]}</a></li>' for o in GUIDES if o is not g)
    cl="".join(f'<li><a href="../areas/{k}.html">{CITIES[k]["name"]}</a></li>' for k in (g.get("cities") or list(CITIES))[:18])
    art={"@context":"https://schema.org","@type":"Article","headline":g["h1"],"description":g["desc"],"datePublished":C.GUIDES_PUBLISHED,"dateModified":TODAY,
         "author":ORG,"publisher":ORG,"mainEntityOfPage":f"{BASE}/guides/{g['slug']}.html","image":f"{BASE}/{PHOTOS[g.get('img','hero')][0]}"}
    schemas=[art, breadcrumb_ld([("Home",""),("Guides","guides/index.html"),(g["nav"],f"guides/{g['slug']}.html")])]
    if g.get("faq"): schemas.append(faq_ld(g["faq"]))
    page(f"guides/{g['slug']}.html", g["title"], g["desc"],
f"""<main class="wrap guide">{crumbs([("Guides","guides/index.html"),(g["nav"],f"guides/{g['slug']}.html")],"../")}<h1>{g["h1"]}</h1>
<p class="small">Updated {C.FACTS_CHECKED}. General information, not legal advice.</p>
{img(g["img"], rel="../") if g.get("img") else ""}
{g["body"]}
{('<h2>Common questions</h2>'+faq_html(g["faq"])) if g.get("faq") else ''}
{cta("../")}
<h2>Get quotes in your city</h2><ul class="cities">{cl}</ul>
<h2>More guides</h2><ul>{others}</ul>
{sources_html(g.get("sources",[]))}</main>""", schemas)

# ---------- HOW IT WORKS / CONTACT / THANKS / PRIVACY ----------
page("how-it-works.html", C.HOW_TITLE, C.HOW_DESC, f'<main class="wrap">{crumbs([("How It Works","how-it-works.html")],"")}{C.HOW_BODY}{cta()}</main>',
     [breadcrumb_ld([("Home",""),("How It Works","how-it-works.html")])])

form=f"""<form action="{C.FORM_ACTION}" method="POST">
{hidden_fields()}
<label for="name">Your name *</label><input id="name" name="name" autocomplete="name" required>
<label for="phone">Phone *</label><input id="phone" name="phone" type="tel" autocomplete="tel" required>
<label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email">
<label for="city">City *</label><select id="city" name="city" required><option value="">Choose your city</option>{CITY_OPTS}</select>
<label for="service">What do you need? *</label><select id="service" name="service" required><option value="">Choose a service</option>{SVC_OPTS}<option>I'm a {C.PROVIDER_NOUN} provider</option></select>
{C.CONTACT_EXTRA_FIELDS}
<label for="details">{C.CONTACT_DETAILS_LABEL}</label><textarea id="details" name="details"></textarea>
<label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>{CONSENT}</span></label>
<p><button class="btn" type="submit">Send my request</button></p>
<p class="small">We'll use your information only to connect you with providers for this request. See our <a href="privacy.html">privacy policy</a>.</p></form>"""
page("contact.html", C.CONTACT_TITLE, C.CONTACT_DESC,
f'<main class="wrap"><h1>{C.CONTACT_H1}</h1><p>Fill out the form and we\'ll pass your request to independent local {C.PROVIDER_NOUN} providers. There\'s no cost and no obligation.</p><p class="note">{C.CONTACT_NOTE}</p>{form}</main>', mcta=False)

page("thank-you.html", f"Thanks, we got your request | {SHORT}", f"Thank you for your {C.PROVIDER_NOUN} request. Local providers who serve your area will contact you directly.",
 f'<main class="wrap"><h1>Thanks! Your request was sent.</h1><p>{C.THANKS_TEXT}</p><p><a href="index.html">Back to home</a> · <a href="guides/index.html">Read our guides</a></p></main>', mcta=False)

page("privacy.html", f"Privacy Policy | {SHORT}", f"Privacy policy for {BRAND}: what we collect through our quote form, how it's shared with providers, and your choices.",
f"""<main class="wrap"><h1>Privacy policy</h1><p>Last updated {TODAY}.</p>
<p><strong>What we collect:</strong> the information you enter in our form (name, phone, email, city, and job details). Our form is processed by FormSubmit (formsubmit.co), which emails it to us. Our host (GitHub Pages) may log basic technical data such as IP addresses.</p>
<p><strong>How we use it:</strong> only to respond to your request and to share it with independent {C.PROVIDER_NOUN} providers in your area so they can contact you about your job. We don't sell your information to data brokers and we don't use it for unrelated marketing.</p>
<p><strong>Your choices:</strong> email {C.EMAIL} to ask us to delete your information or to stop sharing it. California residents may have additional rights under the CCPA/CPRA.</p>
<p><strong>Contact:</strong> {C.EMAIL}</p>
<h2 id="photos">Photo credits</h2><p>Photos on this site are stock photos used under free licenses that allow commercial use without attribution. We credit the photographers anyway. The people shown are not affiliated with {BRAND} or with any provider we refer you to.</p>
<ul>{"".join(f'<li>{v[3]}: photo by <a href="{v[5]}" rel="nofollow">{v[4]}</a> on <a href="{v[7]}" rel="nofollow">{v[6]}</a> ({v[8]})</li>' for v in PHOTOS.values())}</ul></main>""")

# ---------- STATIC FILES ----------
open("style.css","w").write(C.CSS)
urls=[p for p,_,_ in PAGES if p!="thank-you.html"]
prio=lambda p: "1.0" if p=="index.html" else ("0.8" if p.startswith("areas/") or p.startswith("guides/") or p in("services.html","contact.html") else "0.5")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}/{p.replace('index.html','')}</loc><lastmod>{TODAY}</lastmod><priority>{prio(p)}</priority></url>\n" for p in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\n\nSitemap: {BASE}/sitemap.xml\n")
open(".nojekyll","w").write("")
if C.INDEXNOW_KEY:
    open(f"{C.INDEXNOW_KEY}.txt","w").write(C.INDEXNOW_KEY)
open("urls.txt","w").write("\n".join(f"{BASE}/{p.replace('index.html','')}" for p in urls)+"\n")
# uniqueness checks
ts=[t for _,t,_ in PAGES]; ds=[d for _,_,d in PAGES]
dup_t={t for t in ts if ts.count(t)>1}; dup_d={d for d in ds if ds.count(d)>1}
assert not dup_t, dup_t
assert not dup_d, dup_d
print(f"built {len(PAGES)} pages")
