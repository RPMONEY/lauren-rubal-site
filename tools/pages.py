"""Generate Conditions & Care, the four program pages, For Patients, Contact and 404.
Shell (head, header, banner, footer) is taken from site/integrative-medicine.html.
Usage: python3 tools/pages.py site <BUILD>"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigs import SIGS
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
# Each program page: title + patient question + editorial prose, sticky consult card,
# conditions list, when to be seen, evaluation steps, treatment options, quote, FAQ.
PROGRAMS = [
 dict(slug="normalized-cycles", name="Normalized Cycles", short="Normalized Cycles", talk="your cycles",
  quote="“My periods have always been like this. Is that just normal for me?”",
  intro=[
   "Many women are told that painful, heavy, or unpredictable periods are something to live with, or that the only answer is to suppress them. Dr. Rubal sees it differently. Your cycle is a window into your overall health, and when it is off, there is usually a reason worth finding.",
   "Cycle problems can come from many places: whether and how well you ovulate, the balance between estrogen and progesterone, thyroid function, insulin resistance, inflammation, or structural changes in the uterus such as fibroids or polyps. Two women with the same symptom can have very different causes, which is why care starts with understanding yours.",
   "Our Normalized Cycles program is designed to address a range of menstrual issues, including Polycystic Ovary Syndrome (PCOS), painful periods, Premenstrual Syndrome (PMS), and other menstrual irregularities. The goal is a healthier, more predictable cycle with fewer symptoms, and a stronger foundation for fertility whenever that time comes."],
  treat_h="What we treat",
  treat=[
   ("PCOS", "Irregular or absent ovulation, often with acne, excess hair growth, or insulin resistance. One of the most common causes of irregular cycles."),
   ("Endometriosis", "Tissue similar to the uterine lining growing outside the uterus, often causing painful periods, pelvic pain, or pain with intercourse, and sometimes affecting fertility."),
   ("Painful periods", "Cramping that disrupts school, work, or daily life is not something you simply have to push through."),
   ("PMS and PMDD", "Physical and emotional symptoms in the days before your period, from bloating and breast tenderness to irritability, anxiety, or low mood."),
   ("Heavy or prolonged bleeding", "Soaking through a pad or tampon every hour or two, passing large clots, or bleeding for more than seven days."),
   ("Irregular or missed periods", "Cycles that are unpredictable, very short or very long, or that stop altogether."),
   ("Fibroids and polyps", "Noncancerous growths in or on the uterus that can cause heavy bleeding, bleeding between periods, pressure, or difficulty conceiving.")],
  when=["Your periods regularly cause you to miss school, work, or plans",
        "You soak through a pad or tampon every one to two hours",
        "Your cycles are shorter than 21 days or longer than 35 days",
        "You have missed three or more periods in a row and are not pregnant",
        "You bleed between periods or after intercourse",
        "You've been told suppressing your cycle is your only option"],
  steps=[("A detailed history", "Your cycles, symptoms, health history and goals, in an unhurried first visit."),
         ("Cycle charting", "Learning to observe and record your own cycle, so patterns and ovulation become visible."),
         ("Targeted testing", "Hormone levels timed to your cycle, thyroid and metabolic testing, and pelvic ultrasound as appropriate."),
         ("Your plan", "Reviewed together, with time for questions, and adjusted as your cycle responds.")],
  tx=[("Restorative and lifestyle", ["Nutrition and metabolic support", "Sleep, stress and movement", "Targeted supplements where the evidence supports them"]),
      ("Medical and surgical", ["Cycle-timed hormone support", "Medication for specific conditions, such as insulin resistance", "Minimally invasive surgery for endometriosis, fibroids, or polyps when needed"])],
  pull=("Simply that a woman is not just her ovaries.", "Dr. Lauren Rubal"),
  faq=[("Do I have to go on birth control?", "Not necessarily. Dr. Rubal’s focus is finding and treating the underlying cause of your symptoms. She will walk you through all of your options so you can make an informed choice that fits your goals."),
       ("Can I come in if I’m not trying to get pregnant?", "Yes. Many patients come in simply to feel better and understand their bodies. A healthy cycle matters at every stage of life."),
       ("Do you see teenagers?", "Yes. Cycle concerns often begin in adolescence, and our <a href=\"hormone-transition.html\">Hormone Transition</a> program includes care for teens."),
       ("Are virtual visits available?", "Yes. Visits are available in person in San Juan Capistrano or by secure video.")]),

 dict(slug="optimized-fertility", name="Optimized Fertility &amp; Miscarriage Prevention", short="Fertility &amp; Miscarriage", talk="your fertility",
  quote="“We’ve been trying for a while. Is something wrong?”",
  intro=[
   "Not conceiving when you expected to, or losing a pregnancy, can feel isolating and overwhelming. Dr. Rubal practiced full-scope reproductive endocrinology and infertility for years, and she knows how many layers this diagnosis carries.",
   "When couples go to a fertility center, they may feel pressured to go directly to IVF. For some, it is not an option they are interested in, because of their beliefs, the cost, the hormones, or the procedures involved. Others have tried it without success. Our Optimized Fertility &amp; Miscarriage Prevention program offers a different starting point.",
   "Also known as Restorative Reproductive Medicine, it looks at understanding the reasons behind fertility issues using a detailed evaluation of your hormones, inflammation, nutrient status, microbiomes, gut, and environmental exposures. Hormonal medications are used judiciously, as one part of a broader plan, and your cycles are monitored closely to support your fertility month by month."],
  treat_h="Who this program helps",
  treat=[
   ("Difficulty conceiving", "Generally defined as not conceiving after 12 months of trying, or after 6 months if you are 35 or older. You don’t have to wait that long to ask questions."),
   ("Recurrent pregnancy loss", "Two or more pregnancy losses. A focused evaluation can identify contributing factors that may be addressed before the next pregnancy."),
   ("Ovulation problems", "Irregular, absent, or poorly supported ovulation, including ovulation problems related to PCOS or thyroid function."),
   ("Endometriosis and uterine factors", "Endometriosis, fibroids, polyps, and other structural factors that can affect conception and implantation."),
   ("Unexplained infertility", "When standard testing hasn’t provided an answer, a closer look at hormones, inflammation, and cycle health may reveal more."),
   ("Preparing for pregnancy", "Optimizing your health before you begin trying, so you start from the strongest possible foundation.")],
  when=["You’ve been trying for 12 months, or 6 months if you are 35 or older",
        "You’ve had two or more pregnancy losses",
        "Your cycles are irregular or you’re unsure whether you ovulate",
        "You have a known condition such as PCOS, endometriosis, or a thyroid disorder",
        "You want an alternative to IVF, or IVF hasn’t worked for you"],
  steps=[("Your full story", "Both partners’ health history, any prior testing and treatment, and what you want your path to look like."),
         ("Cycle charting and monitoring", "Tracking your cycle, with ultrasounds and serial hormone levels to see how ovulation and the uterine lining are working."),
         ("Root-cause testing", "Hormones, thyroid, inflammation, nutrient status and other factors, evaluation of the uterus and tubes, and a semen analysis for your partner when appropriate."),
         ("After pregnancy loss", "A focused evaluation that can include uterine, hormonal, genetic, blood-clotting and immune factors.")],
  tx=[("Restorative and lifestyle", ["Nutrition, lifestyle and metabolic optimization", "Targeted supplements where the evidence supports them", "Timing guided by your own charted cycle"]),
      ("Medical and surgical", ["Hormone optimization and ovulation support", "Treatment of thyroid and other contributing conditions", "Surgery to normalize structure and anatomy when needed"])],
  pull=("I also monitor your cycles closely with ultrasounds and other methods, such as serial hormone levels.", "Dr. Lauren Rubal"),
  faq=[("Do you offer IVF?", "Dr. Rubal’s practice focuses on restorative reproductive medicine, which works to identify and treat the underlying causes of infertility. She is happy to talk through every option with you, including IVF."),
       ("Should my partner be evaluated too?", "Yes, when appropriate. Fertility involves both partners, and a semen analysis is a standard part of a complete evaluation."),
       ("I’ve already had testing elsewhere. Will I need to repeat it?", "Bring your records. Dr. Rubal will review what has already been done and recommend additional testing only where it adds something."),
       ("Can I come in after a recent loss?", "Yes. Whether your loss was recent or some time ago, Dr. Rubal can help you understand what may have contributed and plan for what comes next.")]),

 dict(slug="hormone-transition", name="Hormone Transition", short="Hormone Transition", talk="hormone changes",
  quote="“I just don’t feel like myself anymore.”",
  intro=[
   "Hormones shift at predictable points in life, and those shifts can affect your cycle, sleep, mood, energy, skin, weight and long-term health. Too often, women are told these changes are simply part of growing up, having a baby, or getting older, and that there is little to do but wait them out.",
   "Our Hormone Transition program offers specialized support for individuals navigating significant hormonal changes during key life stages: adolescence, postpartum, and menopause. Dr. Rubal looks at what is changing, why, and what can help, using lifestyle, nutritional and medical options matched to your history and goals."],
  treat_h="Three key life stages", stages=["Teens", "After pregnancy", "Often 40s and beyond"],
  treat=[
   ("Adolescence", "The first years of menstruation are often irregular, but painful, very heavy, or absent periods deserve attention. Early signs of conditions such as PCOS or endometriosis often appear in the teen years, and a thoughtful evaluation can make a lasting difference."),
   ("Postpartum", "After pregnancy, hormones shift dramatically. Cycles may take time to return, especially while breastfeeding, and some women develop thyroid changes, mood changes, fatigue, or bleeding concerns that deserve a closer look."),
   ("Perimenopause and menopause", "Perimenopause can begin years before your final period, often in your 40s, bringing irregular cycles, hot flashes, night sweats, disrupted sleep, mood changes and vaginal dryness. Menopause is reached after 12 months without a period, and the years around it are an important time to protect long-term heart and bone health.")],
  when=["A teen’s periods haven’t started by age 15, or are extremely painful or heavy",
        "Your cycle hasn’t settled into a pattern months after having a baby",
        "Hot flashes, night sweats, or poor sleep are affecting daily life",
        "You notice heavy bleeding, bleeding between periods, or any bleeding after menopause",
        "Mood, energy, or weight have changed and no one has explained why"],
  steps=[("Understanding where you are", "Your stage of life, symptoms, cycle history and goals."),
         ("Targeted testing", "Hormone, thyroid and metabolic testing, and pelvic ultrasound when bleeding patterns change."),
         ("Options weighed together", "Lifestyle and nutrition, supplements, and hormone therapy when appropriate, considered against your health history."),
         ("Adjusting over time", "Transitions unfold over months and years, and your care evolves with them.")],
  tx=[("Restorative and lifestyle", ["Nutrition and metabolic support", "Sleep, stress and movement", "Targeted supplements where the evidence supports them"]),
      ("Medical", ["Hormone therapy when appropriate for your age and history", "Treatment of thyroid and other contributing conditions", "Evaluation and treatment of abnormal bleeding"])],
  pull=("It is medicine that is oriented to healing, to understanding we are more than our physical ailments.", "Dr. Lauren Rubal"),
  faq=[("Is hormone therapy safe?", "For many women, menopausal hormone therapy can be a safe and effective option. The right choice depends on your age, health history and symptoms, and Dr. Rubal will walk you through the benefits and risks for you specifically."),
       ("Are irregular periods normal in my 40s?", "Cycle changes are common in perimenopause. Heavy bleeding, bleeding between periods, or any bleeding after menopause should always be evaluated."),
       ("When should a teenager see a specialist?", "If periods haven’t started by 15, are severely painful or very heavy, or are still very irregular a few years after they begin."),
       ("Can you help if I’m breastfeeding?", "Yes. Treatment options are always chosen with breastfeeding in mind.")]),

 dict(slug="integrative-tools", name="Integrative Tools", short="Integrative Tools", talk="your whole health",
  quote="“My labs are normal, but I still don’t feel right.”",
  intro=[
   "Hormonal and reproductive health doesn’t exist in isolation. Chronic stress, poor sleep, fatigue, thyroid imbalances, heart health and mood all influence your hormones, and your hormones influence them in return.",
   "Our Integrative Tools program is meticulously crafted to address a wide array of health concerns, including chronic stress, sleep disturbances, fatigue, thyroid imbalances, heart health, mood issues, and beyond. It is part of every program we offer, and it can also be the focus of your care on its own."],
  treat_h="What we address",
  treat=[
   ("Chronic stress", "Ongoing stress affects stress hormones that can disrupt ovulation, cycle regularity, sleep and mood."),
   ("Sleep disturbances", "Trouble falling or staying asleep, often tied to hormonal shifts, stress, or night sweats."),
   ("Fatigue", "Persistent exhaustion can have identifiable contributors, from thyroid function and iron levels to blood sugar and hormonal changes."),
   ("Thyroid imbalances", "The thyroid influences cycles, fertility and pregnancy, and even subtle imbalances can matter."),
   ("Heart health", "Reproductive history, including PCOS, pregnancy complications and menopause, is closely linked to long-term cardiovascular health."),
   ("Mood", "Anxiety, low mood and irritability can rise and fall with hormonal changes, and deserve to be taken seriously.")],
  when=["You feel exhausted despite getting enough rest",
        "Stress or poor sleep is affecting your cycle or daily life",
        "You’ve been told your labs are normal but your symptoms persist",
        "You have a thyroid condition alongside cycle or fertility concerns",
        "You want a more complete look at your long-term health"],
  steps=[("A comprehensive evaluation", "How stress, sleep, thyroid, metabolic health and hormones interact in your body."),
         ("Targeted testing", "Thyroid, iron, metabolic and inflammatory markers, and others as appropriate."),
         ("Practical changes", "Nutrition, sleep, stress and movement, tailored to what fits your life."),
         ("Targeted support", "Supplements and conventional treatment, each chosen on the evidence and reviewed over time.")],
  tx=[("Restorative and lifestyle", ["Nutrition and metabolic support", "Sleep and stress-resilience strategies", "Movement suited to your health and goals"]),
      ("Medical", ["Targeted supplements where the evidence supports them", "Thyroid evaluation and treatment", "Conventional medication when indicated"])],
  pull=("You are a whole person. And so we must address and acknowledge your mental, emotional, spiritual, and physical state.", "Dr. Lauren Rubal"),
  faq=[("Do I need to be in another program to use Integrative Tools?", "No. Integrative Tools supports every program, and it can also be the focus of your care on its own."),
       ("Will Dr. Rubal replace my primary care physician?", "No. Dr. Rubal works alongside your primary care physician and any other specialists you see."),
       ("How do you decide which supplements to recommend?", "Supplements are recommended only where research supports them for your situation, with attention to quality, dosing and interactions with any medications.")]),
]

def program(p):
    others = [q for q in PROGRAMS if q["slug"] != p["slug"]]
    strip = "".join(f'<a href="{q["slug"]}.html">{q["name"]}</a>' for q in others)
    intro = "".join(f"<p>{x}</p>" for x in p["intro"])
    treat = "".join(f'<div class="dl-row"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in p["treat"])
    if p.get("stages"):
        line = "".join(f'<span><i></i>{s}</span>' for s in p["stages"])
        cols = "".join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in p["treat"])
        treat_block = f'<div class="life">{line}</div><div class="stages">{cols}</div>'
    else:
        treat_block = f'<dl class="cp-dl">{treat}</dl>'
    sig = SIGS.get(p["slug"], lambda: "")()
    when = "".join(f"<li>{w}</li>" for w in p["when"])
    steps = "".join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in p["steps"])
    tx = "".join(f'<div><h3>{h}</h3><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>" for h, items in p["tx"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in p["faq"])
    pq, pa = p["pull"]
    body = f'''<section class="cp"><div class="wrap cp-grid">
<article class="cp-main">
<p class="crumb"><a href="conditions.html">Conditions &amp; Care</a> / {re.sub("<[^>]+>","",p["short"])}</p>
<h1>{p["name"]}</h1>
<p class="cp-q">{p["quote"]}</p>
<div class="cp-intro">{intro}</div>
<p class="cp-mcta"><a class="btn btn-fill" href="contact.html">Request a Consultation {A}</a></p>

{sig}
<section class="cp-panel warm"><h2>{p["treat_h"]}</h2>
{treat_block}</section>

<blockquote class="cp-pull"><p>“{pq}”</p><cite>{pa}</cite></blockquote>

<section class="cp-panel dark"><h2>When to see a specialist</h2>
<p>It may be time to talk with Dr. Rubal if:</p>
<ul class="cp-when">{when}</ul></section>

<h2>How Dr. Rubal evaluates</h2>
<ol class="cp-steps">{steps}</ol>

<h2>Treatment may include</h2>
<div class="cp-tx">{tx}</div>
<p class="cp-note">Every plan is individualized. Not every patient needs every test or treatment.</p>

<h2>Common questions</h2>
<div class="faq cp-faq">{faq}</div>
</article>

<aside class="cp-card">
<div class="cp-who"><img src="img/dr-rubal-avatar.jpg" alt="Dr. Lauren Rubal" width="64" height="64"><div><b>Talk with Dr. Rubal about {p["talk"]}</b></div></div>
<ul>
<li>USC-trained Reproductive Endocrinologist</li>
<li>Double board certified, Integrative Medicine &amp; OB/GYN</li>
<li>In person in San Juan Capistrano or virtual</li>
<li>Se habla español</li>
</ul>
<a class="btn btn-fill" href="contact.html">Request a Consultation {A}</a>
<a class="cp-call" href="tel:+19494156704">Or call (949) 415-6704</a>
</aside>
</div></section>

<section class="cp-strip"><div class="wrap"><span class="eyebrow">Other programs</span><nav>{strip}<a href="integrative-medicine.html">What Is Integrative Medicine?</a></nav></div></section>
'''
    plain = re.sub("<[^>]+>", "", p["name"]).replace("&amp;", "&")
    desc = re.sub("<[^>]+>", "", p["intro"][0]).replace('"', "'")
    desc = desc if len(desc) < 300 else desc[:297].rsplit(" ", 1)[0] + "..."
    page(p["slug"] + ".html", f"{plain} | Lauren Rubal, MD", desc, body, banner=False)

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
