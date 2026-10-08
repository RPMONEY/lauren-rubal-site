"""One signature element per program page, used by pages.py."""
import math


def sig_cycles():
    return """<figure class="sig sig-cycle"><figcaption><span class="eyebrow">At a glance</span><h3>A healthy cycle</h3></figcaption>
<div class="cyc-bar"><span class="c1" style="flex:5"></span><span class="c2" style="flex:8"></span><span class="c3" style="flex:2"></span><span class="c4" style="flex:13"></span></div>
<div class="cyc-key">
<div><i class="c1"></i><b>Period</b><span>Usually 3 to 7 days</span></div>
<div><i class="c2"></i><b>Follicular phase</b><span>Estrogen rises as an egg matures</span></div>
<div><i class="c3"></i><b>Ovulation</b><span>An egg is released</span></div>
<div><i class="c4"></i><b>Luteal phase</b><span>Progesterone rises, usually about 12 to 14 days</span></div>
</div>
<p class="sig-note">A typical adult cycle lasts 21 to 35 days. Most of the variation in cycle length comes before ovulation, which is why charting your own cycle is so revealing.</p></figure>"""


def sig_fertility():
    return """<figure class="sig sig-pair"><figcaption><span class="eyebrow">A complete evaluation</span><h3>Fertility involves both partners</h3></figcaption>
<div class="pair">
<div><b>Female factors</b><ul><li>Ovulation and cycle health, charted over time</li><li>Hormones and thyroid function</li><li>The uterus and fallopian tubes</li><li>Inflammation and nutrient status</li></ul></div>
<div><b>Male factors</b><ul><li>Semen analysis</li><li>Health history and medications</li><li>Lifestyle and environmental exposures</li></ul></div>
</div></figure>"""


def sig_hub():
    nodes = ["Chronic stress", "Sleep", "Fatigue", "Thyroid", "Heart health", "Mood"]
    cx, cy, rx, ry = 320, 200, 230, 150
    lines, dots = "", ""
    for i, n in enumerate(nodes):
        a = math.radians(-90 + i * 60)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        lines += f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}"/>'
        if abs(math.cos(a)) < .2:
            anchor, dx = "middle", 0
        elif math.cos(a) > 0:
            anchor, dx = "start", 16
        else:
            anchor, dx = "end", -16
        dy = -18 if math.sin(a) < -.9 else (34 if math.sin(a) > .9 else 7)
        dots += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7"/><text x="{x+dx:.0f}" y="{y+dy:.0f}" text-anchor="{anchor}">{n}</text>'
    return f"""<figure class="sig sig-hub"><figcaption><span class="eyebrow">How it connects</span><h3>Everything affects your hormones</h3></figcaption>
<svg viewBox="-70 0 780 420" role="img" aria-label="Chronic stress, sleep, fatigue, thyroid, heart health and mood all connect to your hormones"><g class="ln">{lines}</g>
<circle class="core" cx="{cx}" cy="{cy}" r="74"/><text class="core-t" x="{cx}" y="{cy-4}" text-anchor="middle">Your</text><text class="core-t" x="{cx}" y="{cy+24}" text-anchor="middle">hormones</text>
<g class="nd">{dots}</g></svg></figure>"""


SIGS = {"normalized-cycles": sig_cycles, "optimized-fertility": sig_fertility, "integrative-tools": sig_hub}
