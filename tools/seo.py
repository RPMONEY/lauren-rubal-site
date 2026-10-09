"""SEO layer: titles, descriptions, canonical, Open Graph, JSON-LD, clean links,
image hints and sitemap.xml. Idempotent. Run after pages.py / legal.py:
    python3 tools/seo.py site
"""
import sys, os, re, json

SITE = sys.argv[1] if len(sys.argv) > 1 else "site"
BASE = "https://www.laurenrubalmd.com"
NAME = "Lauren Rubal, MD"
OG_IMG = BASE + "/img/og-image.jpg"

PRACTICE = {
    "@type": ["Physician", "MedicalClinic"],
    "@id": BASE + "/#practice",
    "name": NAME,
    "url": BASE + "/",
    "image": OG_IMG,
    "logo": BASE + "/img/lr-mark.png",
    "description": "Integrative reproductive endocrinology in San Juan Capistrano: fertility, "
                   "cycle health, recurrent miscarriage and hormone transitions.",
    "telephone": "+1-949-415-6704",
    "faxNumber": "+1-949-269-3263",
    "address": {"@type": "PostalAddress", "streetAddress": "31551 Camino Capistrano, Suite D",
                "addressLocality": "San Juan Capistrano", "addressRegion": "CA",
                "postalCode": "92675", "addressCountry": "US"},
    "areaServed": "Orange County, California",
    "availableLanguage": ["English", "Spanish"],
    "medicalSpecialty": ["Reproductive Endocrinology and Infertility",
                         "Obstetrics and Gynecology", "Integrative Medicine"],
}
DOCTOR = {
    "@type": "Person", "@id": BASE + "/about#lauren-rubal",
    "name": "Lauren Rubal", "honorificSuffix": "MD", "jobTitle": "Reproductive Endocrinologist",
    "image": BASE + "/img/dr-lauren-rubal.jpg", "url": BASE + "/about",
    "worksFor": {"@id": BASE + "/#practice"},
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "University of Southern California"},
}

# file: (path, title, description, page type, breadcrumb label or None, about)
P = {
 "index.html": ("/", "Integrative Fertility Doctor, Orange County | Lauren Rubal, MD",
   "USC-trained reproductive endocrinologist in San Juan Capistrano. Integrative care for fertility, irregular cycles, recurrent miscarriage and hormone transitions.",
   "WebPage", None, None),
 "about.html": ("/about", "About Dr. Lauren Rubal | Reproductive Endocrinologist, Orange County",
   "Meet Dr. Lauren Rubal, a USC-trained reproductive endocrinologist, double board certified in OB/GYN and Integrative Medicine, practicing in Orange County.",
   "AboutPage", "About Dr. Rubal", None),
 "integrative-medicine.html": ("/integrative-medicine", "Integrative Medicine for Fertility & Hormones | Lauren Rubal, MD",
   "What integrative medicine means in Dr. Rubal's practice: evidence-based conventional care plus carefully chosen complementary therapies, built around you.",
   "MedicalWebPage", "Integrative Medicine", "Integrative Medicine"),
 "conditions.html": ("/conditions", "Fertility, Cycle & Hormone Care, Orange County | Lauren Rubal, MD",
   "Integrative programs for irregular and painful cycles, fertility and miscarriage prevention, and hormone transitions, with Dr. Lauren Rubal in San Juan Capistrano.",
   "MedicalWebPage", "Conditions & Care", None),
 "normalized-cycles.html": ("/normalized-cycles", "Normalized Cycles: PCOS & Irregular Period Care | Lauren Rubal, MD",
   "Care for PCOS, endometriosis, painful or heavy periods, PMS and irregular cycles. Dr. Rubal looks for the cause, not just the symptoms.",
   "MedicalWebPage", "Normalized Cycles", "Menstrual disorders"),
 "optimized-fertility.html": ("/optimized-fertility", "Fertility & Recurrent Miscarriage Care | Lauren Rubal, MD",
   "Fertility and recurrent miscarriage care that evaluates both partners, monitors your cycles closely and builds an individualized plan. San Juan Capistrano.",
   "MedicalWebPage", "Optimized Fertility & Miscarriage Prevention", "Infertility"),
 "hormone-transition.html": ("/hormone-transition", "Hormone Transition: Postpartum & Menopause Care | Lauren Rubal, MD",
   "Support for the hormone shifts of adolescence, postpartum and perimenopause or menopause, with an integrative evaluation and an individualized plan.",
   "MedicalWebPage", "Hormone Transition", "Menopause"),
 "integrative-tools.html": ("/integrative-tools", "Integrative Tools: Stress, Sleep & Thyroid | Lauren Rubal, MD",
   "How stress, sleep, fatigue, thyroid, heart health and mood shape your hormones, and the integrative tools Dr. Rubal uses to address them.",
   "MedicalWebPage", "Integrative Tools", None),
 "patients.html": ("/patients", "For Patients: Intake Forms & Visit Info | Lauren Rubal, MD",
   "Intake forms, the patient portal, virtual visits and what to expect at your first appointment with Dr. Lauren Rubal in San Juan Capistrano.",
   "WebPage", "For Patients", None),
 "contact.html": ("/contact", "Request a Consultation | Lauren Rubal, MD, San Juan Capistrano",
   "Request a consultation with Dr. Lauren Rubal. In person in San Juan Capistrano or by video. Call (949) 415-6704. Se habla español.",
   "ContactPage", "Contact", None),
 "privacy-policy.html": ("/privacy-policy", None, None, "WebPage", "Privacy Policy", None),
 "notice-of-privacy-practices.html": ("/notice-of-privacy-practices", None, None, "WebPage", "Notice of Privacy Practices", None),
 "good-faith-estimate.html": ("/good-faith-estimate", None, None, "WebPage", "Good Faith Estimate", None),
 "terms-of-use.html": ("/terms-of-use", None, None, "WebPage", "Terms of Use", None),
 "accessibility.html": ("/accessibility", None, None, "WebPage", "Accessibility", None),
 "404.html": (None, None, None, None, None, None),
}
PARENT = {"normalized-cycles.html", "optimized-fertility.html", "hormone-transition.html", "integrative-tools.html"}

def esc(s): return s.replace("&", "&amp;").replace('"', "&quot;")

def ld_for(f, path, title, desc, ptype, crumb, about):
    url = BASE + path
    page = {"@type": ptype, "@id": url + "#webpage", "url": url, "name": title,
            "description": desc, "isPartOf": {"@id": BASE + "/#website"},
            "about": {"@id": BASE + "/#practice"}, "inLanguage": "en-US"}
    if ptype == "MedicalWebPage" and about:
        page["about"] = {"@type": "MedicalCondition" if about not in ("Integrative Medicine",) else "MedicalSpecialty", "name": about}
        page["reviewedBy"] = {"@id": BASE + "/about#lauren-rubal"}
    graph = [{"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": NAME,
              "publisher": {"@id": BASE + "/#practice"}}, PRACTICE, page]
    if f in ("index.html", "about.html"):
        graph.append(DOCTOR)
    if crumb:
        items = [("Home", BASE + "/")]
        if f in PARENT: items.append(("Conditions & Care", BASE + "/conditions"))
        items.append((crumb, url))
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))

def clean_links(h):
    h = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1) or ""}"', h)
    return re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1)}{m.group(2) or ""}"', h)

def images(h):
    def fix(m):
        tag = m.group(0)
        if "mark-ico" in tag: return tag
        if "loading=" not in tag: tag = tag.replace("<img ", '<img loading="lazy" decoding="async" ', 1)
        tag = tag.replace('alt="Dr. Lauren Rubal"', 'alt="Portrait of Dr. Lauren Rubal, reproductive endocrinologist"')
        return tag
    return re.sub(r"<img [^>]*>", fix, h)

urls = []
for f, (path, title, desc, ptype, crumb, about) in P.items():
    fp = os.path.join(SITE, f)
    if not os.path.exists(fp): continue
    h = open(fp).read()
    # strip any previous SEO block / tags
    h = re.sub(r"\n?<!-- seo -->.*?<!-- /seo -->", "", h, flags=re.S)
    h = re.sub(r'\n?<link rel="canonical"[^>]*>|\n?<meta (?:property="og:[^"]+"|name="twitter:[^"]+"|name="robots")[^>]*>', "", h)
    if title: h = re.sub(r"<title>.*?</title>", f"<title>{title.replace('&', '&amp;')}</title>", h, flags=re.S)
    if desc: h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', h)
    t = re.search(r"<title>(.*?)</title>", h, re.S).group(1).replace("&amp;", "&")
    d = (re.search(r'<meta name="description" content="([^"]*)"', h) or [None, ""])[1].replace("&amp;", "&").replace("&quot;", '"')
    if path is None:
        block = '<meta name="robots" content="noindex">'
        h = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", h, flags=re.S)
        # 404 is served at any depth, so asset paths must be root-absolute
        h = re.sub(r'(href|src)="(?!/|https?:|#|tel:|mailto:)((?:styles\.css|favicon|img/|fonts/)[^"]*)"', r'\1="/\2"', h)
    else:
        url = BASE + path
        block = "\n".join([
            f'<link rel="canonical" href="{url}">',
            '<meta property="og:type" content="website">',
            f'<meta property="og:site_name" content="{NAME}">',
            f'<meta property="og:title" content="{esc(t)}">',
            f'<meta property="og:description" content="{esc(d)}">',
            f'<meta property="og:url" content="{url}">',
            f'<meta property="og:image" content="{OG_IMG}">',
            '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
            '<meta property="og:locale" content="en_US">',
            '<meta name="twitter:card" content="summary_large_image">'])
        ld = f'<script type="application/ld+json">{ld_for(f, path, t, d, ptype, crumb, about)}</script>'
        if '<script type="application/ld+json">' in h:
            h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: ld, h, count=1, flags=re.S)
        else:
            h = h.replace("</head>", ld + "\n</head>", 1)
        urls.append(url)
    h = re.sub(r'(<meta name="description" content="[^"]*">)', lambda m: m.group(1) + "\n<!-- seo -->\n" + block + "\n<!-- /seo -->", h, count=1)
    h = images(clean_links(h))
    open(fp, "w").write(h)

prio = {"/": "1.0"}
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    p = u[len(BASE):]
    pr = prio.get(p, "0.3" if p in ("/privacy-policy", "/notice-of-privacy-practices", "/good-faith-estimate", "/terms-of-use", "/accessibility") else "0.8")
    sm.append(f"  <url><loc>{u}</loc><priority>{pr}</priority></url>")
sm.append("</urlset>")
open(os.path.join(SITE, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
print("seo: %d pages, sitemap %d urls" % (len(P), len(urls)))
