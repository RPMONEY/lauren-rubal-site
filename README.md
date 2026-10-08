# Lauren Rubal, MD website

Static site for laurenrubalmd.com. Hosted on Cloudflare Workers (static assets).

| Folder | What it is |
|---|---|
| `site/` | The finished website. This is what Cloudflare serves. |
| `tools/` | `pages.py` builds Conditions, program, For Patients, Contact and 404 pages. `legal.py` builds the legal pages. Both copy the header and footer from the hand-edited pages. |

Rebuild generated pages after changing the header or footer:

```
python3 tools/pages.py site <BUILD>
python3 tools/legal.py site <BUILD>
```

Deploy: `wrangler.jsonc` serves `site/`. Connect the repo to a Cloudflare Worker named `laurenrubalmd` and every push to `main` deploys.

## Open before launch
- Legal: legal entity name, office email, Privacy Officer, effective date, insurance vs self-pay
- For Patients: intake forms link, portal login link, virtual waiting room link, insurance answer, cancellation policy
- Contact: office hours; contact form and mailing list need a backend (form action URLs are placeholders)
- Photos: originals for the hero, coastline and integrative medicine images (current ones are cropped from mockups/screenshots)
