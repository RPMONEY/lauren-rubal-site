"""Generate Conditions & Care, the four program pages, For Patients, Contact and 404.
Shell (head, header, banner, footer) is taken from site/integrative-medicine.html.
Usage: python3 tools/pages.py site <BUILD>"""
import sys, os, re
SITE, BUILD = sys.argv[1], sys.argv[2]
src = open(os.path.join(SITE, "integrative-medicine.html")).read()
HEAD = src.split("<header class=\"site\">")[0]
HEADER = "<header class=\"site\">" + src.split("<header class=\"site\">")[1].split("</header>")[0] + "</header>"
COAST = "<section class=\"coast\">" + src.split("<section class=\"coast\">")[1].split("</section>")[0] + "</section>"
FOOTER = "<footer class=\"site\">" + src.split("<footer class=\"site\">")[1]
A = '<svg><use href="#arr"/></svg>'
TODO = lambda t: f'<span class="todo">[CONFIRM {t}]</span>'
PHONE = '<a href="tel:+19494156704">(949) 415-6704</a>'

def page(fname, title, desc, body, banner=True, ld=None):
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", HEAD)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', h)
    if ld:
        h = re.sub(r'<script type="application/ld\+json">.*?</script>', f'<script type="application/ld+json">{ld}</script>', h, flags=re.S)
    out = h + "\n" + HEADER + "\n" + body + "\n" + (COAST + "\n\n" if banner else "") + FOOTER
    out = re.sub(r"Build \d+", f"Build {BUILD}", out)
    open(os.path.join(SITE, fname), "w").write(out)
    print("wrote", fname)

def head_band(crumb, eyebrow, h1, lede=""):
    c = f'<p class="crumb">{crumb}</p>' if crumb else ""
    l = f"<p>{lede}</p>" if lede else ""
    return f'<section class="legal-head about-head"><div class="wrap">{c}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{l}</div></section>'

# ---------------------------------------------------------------- programs
PROGRAMS = [
 dict(slug="normalized-cycles", name="Normalized Cycles", img="im-gynecology.jpg",
  h1="Normalized <em>Cycles</em>",
  lede="Our Normalized Cycles program is designed to address a range of menstrual issues, including Polycystic Ovary Syndrome (PCOS), painful periods, Premenstrual Syndrome (PMS), and other menstrual irregularities.",
  intro="Your cycle is a vital sign. When periods are irregular, painful, heavy, or absent, it is usually a signal that something underneath deserves a closer look. This program focuses on understanding why your cycle is behaving the way it is, then building an individualized plan to restore a healthier rhythm.",
  addresses=["Polycystic Ovary Syndrome (PCOS)","Irregular or missed periods","Painful periods","Heavy or abnormal bleeding","Premenstrual Syndrome (PMS)","Uterine fibroids and polyps"],
  steps=[("i-clip","Detailed evaluation","Your cycle history, symptoms, hormones, and contributing factors such as inflammation and metabolic health."),
         ("i-doc","Cycle tracking","Learning to read your own cycle so patterns and changes are easy to see."),
         ("i-leaf","Integrative plan","Lifestyle, nutrition, and targeted support, with conventional treatment when it is the right tool."),
         ("i-people","Follow-up","Adjusting the plan as your cycle responds.")],
  row=("Integrative Gynecology", "Simply that a woman is not just her ovaries.", "You are a whole person. And so we must address and acknowledge your mental, emotional, spiritual, and physical state.")),
 dict(slug="optimized-fertility", name="Optimized Fertility &amp; Miscarriage Prevention", img="im-fertility.jpg",
  h1="Optimized <em>Fertility</em> &amp; Miscarriage Prevention",
  lede="Our Optimized Fertility &amp; Miscarriage Prevention program is specifically tailored for individuals and couples aiming to conceive, offering comprehensive support to enhance fertility and reduce the risk of miscarriage.",
  intro="Also known as Restorative Reproductive Medicine, this approach looks at understanding the reasons behind fertility issues using a detailed evaluation of your hormones, inflammation, nutrient status, microbiomes, gut, and environmental exposures.",
  addresses=["Difficulty conceiving","Recurrent pregnancy loss","Ovulation problems","Hormonal imbalances affecting fertility","Uterine factors such as fibroids or polyps","Preparing your body for pregnancy"],
  steps=[("i-clip","Root-cause evaluation","Hormones, inflammation, nutrient status, microbiomes, gut, and environmental exposures."),
         ("i-doc","A tailored plan","Supplements, hormone optimization, lifestyle changes, and potentially surgery to normalize structure and anatomy."),
         ("i-leaf","Close monitoring","Cycles monitored with ultrasounds and other methods, such as serial hormone levels."),
         ("i-heart","Ongoing support","A partnership through every cycle, adjusting as you go.")],
  row=("Integrative Fertility", "Understanding the reasons behind fertility issues.", "A tailored plan is created using supplements, hormone optimization, lifestyle changes, and potentially even surgeries to normalize structure &amp; anatomy. I also monitor your cycles closely with ultrasounds and other methods, such as serial hormone levels.")),
 dict(slug="hormone-transition", name="Hormone Transition", img="im-medicine.jpg",
  h1="Hormone <em>Transition</em>",
  lede="Our Hormone Transition program offers specialized support for individuals navigating significant hormonal changes during key life stages: adolescence, postpartum, and menopause.",
  intro="Hormonal transitions affect sleep, mood, energy, cycles, and long-term health. This program offers personalized, evidence-based support to help you understand what is changing and navigate each stage with clarity.",
  addresses=["Adolescent cycles and hormones","Postpartum hormonal changes","Perimenopause","Menopause","Sleep, mood, and energy changes tied to hormones"],
  steps=[("i-clip","Understanding the stage","A clear look at where you are hormonally and what you are experiencing."),
         ("i-doc","Personalized options","Lifestyle, nutritional, and medical options weighed against your goals and history."),
         ("i-leaf","Whole-person care","Attention to sleep, stress, and long-term health, not only symptoms."),
         ("i-people","Adjusting over time","Care that evolves as your body does.")],
  row=("Integrative Medicine", "Oriented to healing.", "It is medicine that is oriented to healing, to understanding we are more than our physical ailments. It seeks out all appropriate therapies, including conventional and alternative, and emphasizes the partnership between you and me.")),
 dict(slug="integrative-tools", name="Integrative Tools", img="mock-consult.jpg",
  h1="Integrative <em>Tools</em>",
  lede="Our Integrative Tools program is meticulously crafted to address a wide array of health concerns, including chronic stress, sleep disturbances, fatigue, thyroid imbalances, heart health, mood issues, and beyond.",
  intro="These are the factors that quietly shape hormonal and reproductive health. Integrative Tools is part of every program, and it can also be the focus of your care on its own.",
  addresses=["Chronic stress","Sleep disturbances","Fatigue","Thyroid imbalances","Heart health","Mood"],
  steps=[("i-clip","Comprehensive evaluation","Looking at how stress, sleep, thyroid, and metabolic health interact with your hormones."),
         ("i-leaf","Lifestyle and nutrition","Practical, individualized changes that fit your life."),
         ("i-doc","Targeted support","Supplements and conventional treatment chosen on the evidence."),
         ("i-people","Partnership","Time for follow-up, questions, and adjustment.")],
  row=("Integrative Medicine", "More than our physical ailments.", "It seeks out all appropriate therapies, including conventional and alternative, and emphasizes the partnership between you and me.")),
]

def program(p):
    others = [q for q in PROGRAMS if q["slug"] != p["slug"]]
    rel = "".join(f'<a class="rel" href="{q["slug"]}.html"><span class="eyebrow">Program</span><b>{q["name"]}</b><span class="more">Learn more {A}</span></a>' for q in others)
    addr = "".join(f"<li>{a}</li>" for a in p["addresses"])
    steps = "".join(f'<div class="s"><svg class="ico"><use href="#{i}"/></svg><div><b>{t}</b><p>{d}</p></div></div>' for i, t, d in p["steps"])
    rh, rlead, rbody = p["row"]
    body = f'''{head_band('<a href="conditions.html">Conditions &amp; Care</a> / ' + re.sub("<[^>]+>","",p["name"]), "Conditions &amp; Care", p["h1"], p["lede"])}

<section class="band" style="border-top:0"><div class="wrap two">
<div><span class="eyebrow">About this program</span><h2>What this program is for.</h2></div>
<div class="body"><p>{p["intro"]}</p>
<h3 class="list-h">What we address</h3><ul class="ticks">{addr}</ul>
<p style="margin-top:26px"><a class="btn btn-fill" href="contact.html">Request a Consultation {A}</a></p></div>
</div></section>

<section class="approach" style="border-bottom:0;padding-top:52px"><div class="wrap">
<span class="eyebrow">How it works</span>
<h2 class="lede-h" style="font-size:clamp(38px,3.2vw,52px);margin:14px 0 6px">Your care, step by step.</h2>
<div class="steps4">{steps}</div>
</div></section>

<section class="im-rows"><div class="wrap">
<div class="im-row">
<img src="img/{p["img"]}" alt="" loading="lazy">
<div><span class="eyebrow">The integrative difference</span><h2>{rh}</h2>
<p class="lead">{rlead}</p><p>{rbody}</p>
<p style="margin-top:22px"><a class="btn btn-line" href="integrative-medicine.html">What Is Integrative Medicine? {A}</a></p></div>
</div>
</div></section>

<section class="band tint"><div class="wrap">
<span class="eyebrow">Other programs</span>
<h2 class="lede-h">Explore more care.</h2>
<div class="rels">{rel}</div>
</div></section>
'''
    plain = re.sub("<[^>]+>", "", p["name"]).replace("&amp;", "&")
    page(p["slug"] + ".html", f"{plain} | Lauren Rubal, MD",
         re.sub("<[^>]+>", "", p["lede"]).replace('"', "'")[:300], body)

for p in PROGRAMS: program(p)

# ---------------------------------------------------------------- overview
idx = open(os.path.join(SITE, "index.html")).read()
cols = re.search(r'<div class="cols3">.*?</div>\n<div class="itools">.*?</div>\n(?=</div></section>)', idx, re.S).group(0)
page("conditions.html", "Conditions &amp; Care | Lauren Rubal, MD",
 "Integrative programs for cycles and PCOS, fertility and miscarriage prevention, hormone transitions, and the factors that shape hormonal health.",
 head_band("", "Conditions &amp; Care", "Expert care at <em>every</em> stage.", "Four integrative programs, each built around a detailed evaluation and a plan designed for you.") +
 f'<section class="conditions" style="padding-top:56px;padding-bottom:70px"><div class="wrap">{cols}</div></section>')

# ---------------------------------------------------------------- for patients
patients = f'''{head_band("", "For Patients", "Everything you need <em>before</em> your visit.", "New and existing patients, in person in San Juan Capistrano or by video. Se habla español.")}

<section class="band" style="border-top:0"><div class="wrap">
<span class="eyebrow">New patients</span>
<h2 class="lede-h">What to expect.</h2>
<div class="steps4">
<div class="s"><svg class="ico"><use href="#i-people"/></svg><div><b>A real consultation</b><p>Time to understand your history, your goals, and the reasons behind what you're experiencing.</p></div></div>
<div class="s"><svg class="ico"><use href="#i-clip"/></svg><div><b>Thorough evaluation</b><p>Targeted labs, imaging, and cycle tracking as appropriate.</p></div></div>
<div class="s"><svg class="ico"><use href="#i-doc"/></svg><div><b>Your plan</b><p>An individualized plan that includes lifestyle and nutritional optimization alongside medical care.</p></div></div>
<div class="s"><svg class="ico"><use href="#i-heart"/></svg><div><b>Monitored care</b><p>Follow-up through your cycles, adjusting as you go.</p></div></div>
</div>
</div></section>

<section class="band tint"><div class="wrap">
<div class="pt-grid">
<div class="pt-card"><span class="eyebrow">New patients</span><h3>Complete your intake forms</h3><p>Please complete your intake forms before your first visit. They're completed securely through our patient portal.</p><a class="btn btn-fill" href="#">Start Intake Forms {A}</a><p class="fine">{TODO("intake forms link and patient portal name")}</p></div>
<div class="pt-card"><span class="eyebrow">Existing patients</span><h3>Patient portal</h3><p>Message the office, view results, and manage appointments.</p><a class="btn btn-line" href="#">Log In to the Portal {A}</a><p class="fine">{TODO("portal login link")}</p></div>
<div class="pt-card"><span class="eyebrow">Virtual visits</span><h3>Enter the waiting room</h3><p>Have a video visit scheduled? Use the link below at your appointment time.</p><a class="btn btn-line" href="#">Virtual Waiting Room {A}</a><p class="fine">{TODO("virtual waiting room link")}</p></div>
</div>
</div></section>

<section class="band" style="border-top:0"><div class="wrap two">
<div><span class="eyebrow">Practical details</span><h2>Visits, payment &amp; policies.</h2></div>
<div class="faq">
<details open><summary>Where are visits held?</summary><p>In person at 31551 Camino Capistrano, Suite D, San Juan Capistrano, CA 92675, or by secure video visit. Dr. Rubal speaks English and Spanish.</p></details>
<details><summary>Do you accept insurance?</summary><p>{TODO("whether the practice is in-network, out-of-network or self-pay, and what patients should expect")}</p><p>If you are uninsured or not using insurance, you have the right to a <a href="good-faith-estimate.html">Good Faith Estimate</a> of expected charges.</p></details>
<details><summary>What should I bring to my first visit?</summary><p>Prior lab results, imaging reports, and any cycle tracking you've done, along with a list of current medications and supplements. {TODO("anything else the office asks new patients to bring")}</p></details>
<details><summary>What is your cancellation policy?</summary><p>{TODO("cancellation and no-show policy")}</p></details>
<details><summary>How do I reach the office?</summary><p>Call {PHONE}, or fax (949) 269-3263. For anything urgent, call 911.</p></details>
</div>
</div></section>
'''
page("patients.html", "For Patients | Lauren Rubal, MD",
 "Information for new and existing patients of Lauren Rubal, MD: what to expect, intake forms, patient portal, virtual visits, insurance and policies.", patients)

# ---------------------------------------------------------------- contact
MAPQ = "31551+Camino+Capistrano+Suite+D+San+Juan+Capistrano+CA+92675"
contact = f'''{head_band("", "Contact", "Request a <em>consultation.</em>", "In person in San Juan Capistrano or by video. Se habla español.")}

<section class="band" style="border-top:0"><div class="wrap contact-grid">
<div class="c-info">
<div class="c-block"><span class="eyebrow">Call the office</span><a class="c-big" href="tel:+19494156704">(949) 415-6704</a><p class="fine">Fax (949) 269-3263</p></div>
<div class="c-block"><span class="eyebrow">Visit</span><p class="c-addr">31551 Camino Capistrano, Suite D<br>San Juan Capistrano, CA 92675</p><a class="more" href="https://maps.google.com/?q={MAPQ}" target="_blank" rel="noopener">Get directions {A}</a></div>
<div class="c-block"><span class="eyebrow">Office hours</span><p>{TODO("office hours")}</p></div>
<div class="c-block"><span class="eyebrow">Virtual visits</span><p>Already scheduled? Visit <a href="patients.html">For Patients</a> to enter the virtual waiting room.</p></div>
</div>
<form class="req" action="CONTACT_FORM_ACTION_URL" method="post">
<h2>Send a request</h2>
<p class="fine" style="margin-top:6px">The office will contact you to schedule. Please don't include medical details in this form.</p>
<div class="row"><div><label for="fn">First name</label><input id="fn" name="first_name" autocomplete="given-name" required></div><div><label for="ln">Last name</label><input id="ln" name="last_name" autocomplete="family-name" required></div></div>
<div class="row"><div><label for="em">Email</label><input id="em" type="email" name="email" autocomplete="email" required></div><div><label for="ph">Phone</label><input id="ph" type="tel" name="phone" autocomplete="tel" required></div></div>
<div class="row"><div><label for="vt">Visit type</label><select id="vt" name="visit_type"><option>In person</option><option>Virtual</option><option>Either</option></select></div><div><label for="lg">Preferred language</label><select id="lg" name="language"><option>English</option><option>Español</option></select></div></div>
<label for="pr">Program of interest</label><select id="pr" name="program"><option value="">Choose one (optional)</option><option>Normalized Cycles</option><option>Optimized Fertility &amp; Miscarriage Prevention</option><option>Hormone Transition</option><option>Integrative Tools</option><option>Not sure yet</option></select>
<label class="check"><input type="checkbox" name="new_patient" checked> I'm a new patient</label>
<button class="btn btn-fill" type="submit">Send Request {A}</button>
<p class="fine">By submitting, you agree to be contacted about scheduling. See our <a href="privacy-policy.html">Privacy Policy</a>. For emergencies, call 911.</p>
</form>
</div></section>

<section class="map-band"><iframe loading="lazy" title="Map to the office" src="https://www.google.com/maps?q={MAPQ}&output=embed"></iframe></section>
'''
page("contact.html", "Contact &amp; Request a Consultation | Lauren Rubal, MD",
 "Request a consultation with Lauren Rubal, MD in San Juan Capistrano, CA. In-person and virtual visits. Call (949) 415-6704. Se habla español.", contact, banner=False)

# ---------------------------------------------------------------- 404
page("404.html", "Page not found | Lauren Rubal, MD", "The page you're looking for has moved.",
 head_band("", "Page not found", "This page has <em>moved.</em>", "Let's get you back on track.") +
 f'<section class="band" style="border-top:0;padding-top:40px"><div class="wrap"><p><a class="btn btn-fill" href="index.html">Back to Home {A}</a> &nbsp; <a class="btn btn-line" href="contact.html">Contact Us {A}</a></p></div></section>', banner=False)
