"""Patient reviews: homepage swipe row, one review per program page, rating line on Contact.
All quotes are VERBATIM from Google (excerpts joined with … only). Idempotent.
Run after pages.py:  python3 tools/reviews.py site"""
import sys, os, re, html

SITE = sys.argv[1] if len(sys.argv) > 1 else "site"
GOOGLE = "https://search.google.com/local/reviews?placeid=ChIJt-kVQfrh3IAR_8WU7rNMutk"
RATING, COUNT = "5.0", 43  # update to match Google

HOME = [
 ("Jenny T.", "From the first appointment, Dr. Rubal told us she had a lot of hope for us. Her belief in the possible, deep dive into root causes, and integrative western approach led us to get pregnant 7 months later (something we questioned many times if it was even possible for us!)."),
 ("Elle T.", "She walked me through one of the most difficult circumstances of my life and did so with a great amount of compassion and expertise. I felt truly cared for and well taken care of physically, emotionally, and spiritually. She has a gift."),
 ("Michelle H.", "Dr. Rubal told me more on our first meeting than multiple Reproductive Endocrinologists combined. I’ve been on a fertility journey for 5 years with multiple failed IUI’s and IVF’s, and by far this has been the most positive Doctors experience I’ve encountered."),
 ("Venetia M.", "My experience working with Dr. Rubal has been wonderful. She is caring, understanding, generous with her time and knowledgeable. It's very easy to get in touch with her and her office. I've never worked with a doctor that's so compassionate and wants you to genuinely reach your goals."),
 ("Claudia Q.", "She took the time to know us, both me and my husband, and asked us a lot of questions to get to any underlying causes of our recurrent miscarriages. No other doctor has spent that kind of time with us. Every time we saw her, we walked away with a lot more knowledge and hope."),
 ("Julia J.", "We traveled to see her after seeing 2 previous REI's who did not recognize our goals or provide holistic treatment options - we were successful after 2 months! She picked up on subtle details they had completely overlooked. She truly evaluates you as an entire person - not just a clinical case."),
]
PAGES = {
 "optimized-fertility.html": ("Angela C.", "After struggling with infertility for 8 years and experiencing a failed IVF cycle, I came to Dr. Rubal feeling discouraged and searching for answers. From the very beginning, she truly listened to my concerns and took the time to investigate the root causes affecting my health and fertility."),
 "normalized-cycles.html": ("Emelee L.", "She made me a priority and took my symptoms/biomarkers very seriously! I am happy to say that I am on my way to feeling like myself again."),
 "integrative-tools.html": ("Chelsea H.", "She is so compassionate, kind, generous with her knowledge and time. And, she is brilliant - that goes without saying! Her care is tailored, holistic, flexible and effective!"),
}
IM_PAGE = ("The Stroms", "Being a busy wife, mom, and doctor myself, experiencing Dr. Rubal's comprehensive, compassionate, accessible, and evidence-based practice has been an incredible blessing.")

STARS = '<span class="rv-stars" aria-label="5 out of 5 stars">★★★★★</span>'
A = '<svg><use href="#arr"/></svg>'
def card(name, q, cls="rv-card"):
    return f'<figure class="{cls}">{STARS}<blockquote>“{html.escape(q, quote=False)}”</blockquote><figcaption>{html.escape(name)} · Google review</figcaption></figure>'
def score():
    return f'<div class="rv-score"><b>{RATING}</b>{STARS}<span>{COUNT} reviews on Google</span><a class="more" href="{GOOGLE}" target="_blank" rel="noopener">Read all reviews {A}</a></div>'

SUM = f'<p class="rv-sum">{STARS}<b>{RATING}</b><span>{COUNT} reviews on Google</span></p>'
HOME_HTML = (f'<section class="reviews" aria-labelledby="rv-h"><div class="wrap"><div class="rv-head"><div><span class="eyebrow">Patient reviews</span>'
  f'<h2 id="rv-h">In their own <em>words.</em></h2>{SUM}</div>{score()}</div>'
  f'<div class="rv-track" tabindex="0" aria-label="Patient reviews, scroll for more">{"".join(card(n, q) for n, q in HOME)}</div>'
  f'<div class="rv-foot"><a class="more" href="{GOOGLE}" target="_blank" rel="noopener">Read all reviews {A}</a>'
  '<div class="rv-nav"><button type="button" data-d="-1" aria-label="Previous reviews">←</button><button type="button" data-d="1" aria-label="Next reviews">→</button></div></div>'
  '<script>(function(){var t=document.querySelector(".rv-track");document.querySelectorAll(".rv-nav button").forEach(function(b){b.addEventListener("click",function(){var c=t.querySelector(".rv-card");t.scrollBy({left:(c.offsetWidth+16)*b.dataset.d,behavior:"smooth"})})})})();</script>'
  '</div></section>')
LINE = (f'<p class="rv-line"><a href="{GOOGLE}" target="_blank" rel="noopener">{STARS}<b>{RATING}</b><span>{COUNT} reviews on Google</span></a></p>')

def put(fp, marker, block, anchor, before=True):
    h = open(fp).read()
    h = re.sub(rf"<!-- {marker} -->.*?<!-- /{marker} -->\n?", "", h, flags=re.S)
    i = h.find(anchor)
    if i < 0: print("anchor missing", fp, anchor[:30]); return
    if not before: i += len(anchor)
    h = h[:i] + f"<!-- {marker} -->{block}<!-- /{marker} -->\n" + h[i:]
    open(fp, "w").write(h)

put(os.path.join(SITE, "index.html"), "reviews", HOME_HTML, '<section class="coast">')
for f, (n, q) in PAGES.items():
    fp = os.path.join(SITE, f)
    m = re.search(r'<p class="cp-note">.*?</p>', open(fp).read(), re.S)  # after "Treatment may include"
    put(fp, "review", card(n, q, "rv-card rv-one"), m.group(0), before=False)
# Integrative Medicine page: no review (removed at Ryan's request)
h = open(os.path.join(SITE, "integrative-medicine.html")).read()
open(os.path.join(SITE, "integrative-medicine.html"), "w").write(re.sub(r"<!-- review -->.*?<!-- /review -->\n?", "", h, flags=re.S))
ct = os.path.join(SITE, "contact.html")
put(ct, "rvline", LINE, re.search(r'<form class="req"[^>]*>', open(ct).read()).group(0), before=False)
print("reviews placed")
