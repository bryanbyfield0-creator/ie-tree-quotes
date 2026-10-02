# Inland Empire Tree Quotes: lead site #1 (tree service)
- Live: https://bryanbyfield0-creator.github.io/ie-tree-quotes/ (GitHub Pages, repo bryanbyfield0-creator/ie-tree-quotes, deployed Oct 1, 2026 with the box's existing gh login)
- Rebuild: `python3 build.py`, then `git commit -am ... && git push` (Pages redeploys in about 1–2 minutes)
- Form: FormSubmit -> bryanbyfield0@gmail.com. **Not active yet:** the first submission triggers a FormSubmit "Activate form" email to Bryan, and he must click it. Until then, leads are not delivered. Not tested, because submitting a third-party form needs Bryan's OK.

## Why tree service (tree removal + palm trimming)
High ticket ($300 trims to $1,000–$5,000+ removals). Urgent demand from Santa Ana wind and storm damage. Recurring palm trimming (palms are everywhere in the IE). Foothill fire-season brush and dead-tree clearance. A large pool of small local operators who buy leads. Fewer national franchises than junk removal or pest control, and less scam saturation than garage-door repair. Search volume not measured (no keyword tool access); based on judgment.

## Google indexing next steps (need Bryan's Google login)
1. Google Search Console -> Add property -> URL prefix `https://bryanbyfield0-creator.github.io/ie-tree-quotes/`. Verify with the HTML-file method: download the google*.html file, give it to the agent, and the agent commits it to the repo root.
2. Submit the sitemap: `sitemap.xml`. Use URL Inspection -> "Request indexing" for the home page and the 8 city pages.
3. Optional: Bing Webmaster Tools (can import from GSC).
4. Long term: a custom domain (would cost money, so not bought). On a github.io subdomain, ranking will be slower and the site can't easily be "rented" with a domain transfer.

## v2 design (Oct 1, 2026)
- Photos in `img/` (self-hosted, optimized JPGs), credited in the footer and on privacy.html#photos. Defined in `PHOTOS` in build.py.
  - arborist-pruning-tree.jpg: Dmytro Glazunov, Unsplash (https://unsplash.com/photos/oqYrgDrs9Xk), Unsplash License
  - tree-removal-climber.jpg: Dmytro Glazunov, Unsplash (https://unsplash.com/photos/Bwn-wVh4OfY), Unsplash License, cropped
  - palm-tree-trimming.jpg: Emilio Sánchez Hernández, Pexels (https://www.pexels.com/photo/a-palm-tree-in-a-city-16738703/), Pexels License, cropped
- Homepage hero has the quick quote form (#quote). It posts to `FORM_ACTION` (the hashed FormSubmit endpoint) with the same hidden fields as contact.html (`hidden_fields()`), plus a `form=Homepage quick form` field so you can tell the two forms apart.
- Mobile (<=640px): the nav is one horizontally scrollable row (the Get Quotes pill is hidden there), and a sticky "Get free quotes" bar sits at the bottom (not on contact or thank-you). The body gets bottom padding.
- build.py now always writes the hashed form action. The old build wrote the raw email address, so don't revert that.
