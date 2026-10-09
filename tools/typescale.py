"""Strip scattered font-size declarations from styles.css and append one type scale.
Exempt: logo mark, USC badge, SVG diagram text, icon pseudo-elements. Run once; idempotent."""
import re
P='site/styles.css'
css=open(P).read()
MARK='/* ===== TYPE SCALE'
if MARK in css: css=css[:css.index(MARK)].rstrip()+'\n'
EXEMPT=('.mark','.usc','.sig-hub','::after','::before')
def fix(m):
    sel,body=m.group(1),m.group(2)
    if sel.strip().startswith('@') or any(e in sel for e in EXEMPT): return m.group(0)
    nb=re.sub(r'\s*font-size:[^;}]+;?','',body)
    return sel+'{'+nb+'}'
css=re.sub(r'([^{}]+)\{([^{}]*)\}',fix,css)
css+=open('tools/typescale.css').read()
open(P,'w').write(css)
