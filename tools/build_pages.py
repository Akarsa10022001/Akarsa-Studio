# -*- coding: utf-8 -*-
"""Build the SEO / AEO / GEO pages, sitemap, llms.txt and robots.txt.

Usage (from the site root):  python3 tools/build_pages.py
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import PAGES, INSIGHTS_HUB, SITE, TODAY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "29"  # asset cache-buster for styles/config
ARROW = '<svg viewBox="0 0 24 24"><path d="M7 17 17 7M9 7h8v8"/></svg>'
BOOKING = "https://calendly.com/beakarsa/15-minute-discovery-call"  # free 30-minute audit call; page.js opens it as a Calendly popup
CAL_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17 12h-5v5h5v-5zM16 1v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-1V1h-2zm3 18H5V8h14v11z"/></svg>'
MARK = '<svg class="mark" viewBox="110 60 400 400" aria-hidden="true"><rect x="110" y="60" width="400" height="400" rx="100" fill="url(#akg)"/><path transform="translate(13 -22)" fill="#e9dcc0" d="M300,122 L172,246 L243,250 A71,93 0 0 1 172,343 L172,396 A128,140 0 0 0 300,256 Z M313,256 L372,256 A75,87 0 0 0 447,343 L447,396 A134,140 0 0 1 313,256 Z"/></svg>'
ORG_ID = SITE + "/#organization"
BY_SLUG = {p["slug"]: p for p in PAGES}
BY_SLUG["insights/"] = INSIGHTS_HUB

def esc(s): return html.escape(s, quote=True)
def strip(s): return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()
def url(slug): return SITE + ("/" + slug if slug else "/")

# keep the OpenAI Ads pixel identical to the homepage's
_index = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
_m = re.search(r"  <!-- OpenAI Ads pixel.*?</script>\n", _index, re.S)
PIXEL = _m.group(0) if _m else ""

SERVICES_ORDER = ["social-media-marketing-agency-indore", "meta-ads-agency-indore", "google-ads-agency-indore", "reddit-ads-agency-india",
                  "chatgpt-ads-agency-india", "ugc-video-production-agency", "influencer-marketing-agency-indore", "branding-agency-indore",
                  "website-development-company-indore", "digital-marketing-agency-vijay-nagar-indore"]
GUIDES_ORDER = ["results", "insights/chatgpt-ads-india-guide", "insights/reddit-ads-cost-india", "insights/meta-ads-cost-india", "case-studies/meta-ads-30k-52-enquiries"]

ORG_NODE = {
    "@type": "Organization", "@id": ORG_ID, "name": "Akarsa Studio", "legalName": "Akarsa Studio Private Limited", "url": SITE + "/",
    "logo": SITE + "/icon-512.png", "telephone": "+91-8109801383",
    "address": {"@type": "PostalAddress", "streetAddress": "Office No. 702, Shagun Arcade, Main Rd, near Apna Sweets, PU 4, near Vijay Nagar Square, Vijay Nagar",
                "addressLocality": "Indore", "addressRegion": "Madhya Pradesh", "postalCode": "452010", "addressCountry": "IN"},
    "founder": {"@type": "Person", "name": "Ritik Sharma", "jobTitle": "Founder & Director"},
    "sameAs": ["https://www.instagram.com/akarsa_studio/", "https://www.youtube.com/@AkarsaStudio", "https://www.facebook.com/profile.php?id=61577404206425", "https://www.pinterest.com/beakarsa", "https://linktr.ee/Akarsa_Studio"],
}

def stamp(day): return f"{day}T09:00:00+05:30"  # Google wants full datetimes with a timezone (IST)

def crumbs(p):
    trail = [("Home", "")]
    k = p["kind"]
    if k == "service": trail.append(("Services", None))
    elif k == "case": trail.append(("Case studies", None))
    elif k == "article": trail.append(("Insights", "insights/"))
    trail.append((p["nav_label"] if k != "hub" else "Insights", p["slug"]))
    return trail

def schema(p):
    page_url = url(p["slug"])
    graph = [ORG_NODE]
    ptype = {"about": "AboutPage", "hub": "CollectionPage"}.get(p["kind"], "WebPage")
    graph.append({"@type": ptype, "@id": page_url + "#webpage", "url": page_url, "name": p["title"], "description": p["desc"], "inLanguage": "en-IN",
                  "isPartOf": {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Akarsa Studio"}, "about": {"@id": ORG_ID},
                  "dateModified": stamp(p.get("updated", (TODAY,))[0]), "primaryImageOfPage": SITE + "/og-image.jpg"})
    # Google requires "item" on every breadcrumb, so crumbs without their own page are left out
    linked = [(name, slug) for name, slug in crumbs(p) if slug is not None]
    items = [{"@type": "ListItem", "position": i, "name": name, "item": url(slug)} for i, (name, slug) in enumerate(linked, 1)]
    graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if p["kind"] == "service":
        graph.append({"@type": "Service", "name": p["h1"], "serviceType": p.get("service_type", p["h1"]), "description": strip(p["answer"]), "url": page_url,
                      "provider": {"@id": ORG_ID}, "areaServed": [{"@type": "City", "name": "Indore"}, {"@type": "Country", "name": "India"}]})
    if p["kind"] in ("article", "case"):
        graph.append({"@type": "Article", "headline": p["h1"][:110], "description": p["desc"], "image": SITE + "/og-image.jpg", "datePublished": stamp(p.get("published", TODAY)), "dateModified": stamp(p.get("updated", (TODAY,))[0]),
                      "author": {"@type": "Organization", "name": "Akarsa Studio", "url": SITE + "/"}, "publisher": {"@id": ORG_ID}, "mainEntityOfPage": page_url,
                      "citation": [s[1] for s in p.get("sources", [])]})
    if p.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

def head(p):
    page_url = url(p["slug"])
    og_type = "article" if p["kind"] in ("article", "case") else "website"
    return f'''<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8" />
{PIXEL}  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(p["title"])}</title>
  <meta name="description" content="{esc(p["desc"])}" />
  <link rel="canonical" href="{page_url}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="theme-color" content="#0e3b30" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:site_name" content="Akarsa Studio" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:url" content="{page_url}" />
  <meta property="og:title" content="{esc(p["title"])}" />
  <meta property="og:description" content="{esc(p["desc"])}" />
  <meta property="og:image" content="{SITE}/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(p["title"])}" />
  <meta name="twitter:description" content="{esc(p["desc"])}" />
  <meta name="twitter:image" content="{SITE}/og-image.jpg" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <script>document.documentElement.classList.add('js')</script>
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/open-sauce-one-latin-700-normal.woff2" crossorigin />
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/open-sauce-one-latin-400-normal.woff2" crossorigin />
  <link rel="stylesheet" href="/styles.css?v={V}" />
  <link rel="stylesheet" href="/page.css?v={V}" />
  <script type="application/ld+json">
{schema(p)}
  </script>
</head>
'''

NAV = f'''<body class="subpage">
  <svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><linearGradient id="akg" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#0e3b30"/><stop offset="1" stop-color="#0e3b30"/></linearGradient></defs></svg>
  <a class="skip" href="#main">Skip to content</a>
  <header class="nav" id="top">
    <div class="nav__bar">
      <a href="/" class="nav__logo" aria-label="Akarsa Studio home">{MARK}<span class="nav__word">AKARSA</span></a>
      <nav class="nav__links" aria-label="Primary">
        <a href="/#services">Services</a>
        <a href="/#work">Work</a>
        <a href="/results">Results</a>
        <a href="/reddit-ads-agency-india" class="nav__new">Reddit Ads</a>
        <a href="/chatgpt-ads-agency-india">ChatGPT Ads</a>
        <a href="/insights/">Insights</a>
        <a href="/about">About</a>
      </nav>
      <a class="nav__cta" data-book="nav" href="{BOOKING}">Book a call</a>
      <button class="nav__burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
    </div>
    <div class="nav__mobile">
      <a href="/">Home</a><a href="/#services">Services</a><a href="/results">Results</a><a href="/reddit-ads-agency-india">Reddit Ads</a><a href="/chatgpt-ads-agency-india">ChatGPT Ads</a><a href="/insights/">Insights</a><a href="/about">About</a>
      <a class="btn btn--dark" data-book="menu" href="{BOOKING}"><span class="btn__label">Book an intro call</span></a>
    </div>
  </header>
  <a class="wa-float wa-float--book is-in" data-book="float" href="{BOOKING}" aria-label="Book a 30-minute intro call">{CAL_ICON}<span class="wa-float__tip">Book an intro call</span></a>
'''

def footer_cols():
    svc = "".join(f'<a href="/{s}">{esc(BY_SLUG[s]["nav_label"])}</a>' for s in SERVICES_ORDER)
    gd = "".join(f'<a href="/{s}">{esc(BY_SLUG[s]["nav_label"])}</a>' for s in GUIDES_ORDER)
    return svc, gd

def footer():
    svc, gd = footer_cols()
    return f'''  <footer class="footer">
    <div class="container footer__top footer__top--wide">
      <div class="footer__intro">
        <h2 class="footer__tag">We don’t sell illusions. We engineer impact.</h2>
        <p class="footer__about">Akarsa Studio Private Limited is an AI-driven marketing agency based in Vijay Nagar, Indore, working with brands across India.</p>
      </div>
      <div class="footer__col footer__col--links"><span class="eyebrow eyebrow--dark">Services</span>{svc}</div>
      <div class="footer__col footer__col--links"><span class="eyebrow eyebrow--dark">Guides &amp; proof</span>{gd}<a href="/insights/">All insights</a><a href="/about">About Akarsa</a></div>
    </div>
    <div class="container footer__mid">
      <div class="footer__contact">
        <span class="eyebrow eyebrow--dark">Contact</span>
        <a class="footer__big" data-book="footer" href="{BOOKING}">Book an intro call →</a>
        <span class="footer__line" data-phone>+91 81098 01383</span>
        <a class="footer__line footer__addr" data-address href="https://www.google.com/maps/search/?api=1&amp;query=Akarsa%20Studio%20Shagun%20Arcade%20Vijay%20Nagar%20Indore">Office No. 702, Shagun Arcade, Main Rd, near Apna Sweets, PU 4, near Vijay Nagar Square, Vijay Nagar, Indore, Madhya Pradesh 452010</a>
      </div>
      <div class="footer__col footer__social"><span class="eyebrow eyebrow--dark">Follow us</span>
        <div class="socials">
          <a data-social="instagram" aria-label="Instagram" href="https://www.instagram.com/akarsa_studio/"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
          <a data-social="youtube" aria-label="YouTube" href="https://www.youtube.com/@AkarsaStudio"><svg viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3V9Z" fill="currentColor"/></svg></a>
          <a data-social="facebook" aria-label="Facebook" href="https://www.facebook.com/profile.php?id=61577404206425"><svg viewBox="0 0 24 24"><path d="M15 3h-2.5A3.5 3.5 0 0 0 9 6.5V10H6v4h3v7h4v-7h3l1-4h-4V7a1 1 0 0 1 1-1h2V3Z"/></svg></a>
          <a data-social="pinterest" aria-label="Pinterest" href="https://www.pinterest.com/beakarsa"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M11 8.5c2.8-1 5 .6 4.6 3.2-.3 2-2 3.3-3.6 2.6M12 11l-2.5 9.5"/></svg></a>
        </div>
      </div>
    </div>
    <div class="container footer__brand">
      <svg class="footer__mark" viewBox="110 60 400 400" aria-hidden="true"><rect x="110" y="60" width="400" height="400" rx="100" fill="url(#akg)"/><path transform="translate(13 -22)" fill="#e9dcc0" d="M300,122 L172,246 L243,250 A71,93 0 0 1 172,343 L172,396 A128,140 0 0 0 300,256 Z M313,256 L372,256 A75,87 0 0 0 447,343 L447,396 A134,140 0 0 1 313,256 Z"/></svg>
      <span class="footer__word">Akarsa</span>
    </div>
    <div class="container footer__bottom">
      <span>© <span data-year>2026</span> Akarsa Studio Private Limited. All rights reserved.</span>
      <a href="/privacy">Privacy Policy</a>
      <a href="#top" class="to-top">Back to top ↑</a>
    </div>
  </footer>
  <script src="/config.js?v={V}"></script>
  <script src="/page.js?v={V}"></script>
</body>
</html>
'''


CRUMB_ANCHORS = {"Services": "#services", "Case studies": "#work"}

def crumb_html(p):
    parts = []
    for name, slug in crumbs(p):
        if slug is None: parts.append(f'<a href="/{CRUMB_ANCHORS[name]}">{esc(name)}</a>')
        elif slug == p["slug"]: parts.append(f'<span aria-current="page">{esc(name)}</span>')
        else: parts.append(f'<a href="/{slug}">{esc(name)}</a>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<i>/</i>'.join(parts) + '</nav>'

def hero(p):
    btn2 = "" if p["kind"] == "article" else '<a class="ghost" href="#faq">Read the FAQs ↓</a>'
    iso, label = p.get("updated", (TODAY, "17 October 2026"))
    upd = f'<p class="phero__date">Updated <time datetime="{iso}">{label}</time> · By the Akarsa Studio team</p>' if p["kind"] in ("article", "case") else ""
    visual = p.get("visual", "")
    return f'''  <main class="page" id="main">
    <section class="phero{' phero--article' if not visual else ''}">
      <div class="container phero__grid">
        <div class="phero__text">
          {crumb_html(p)}
          <span class="pill">{esc(p["eyebrow"])}</span>
          <h1 class="phero__title">{esc(p["h1"])}</h1>
          <p class="phero__lead">{esc(p["lead"])}</p>
          {upd}
          <div class="answer"><span class="answer__label">Quick answer</span><p>{esc(p["answer"])}</p></div>
          <div class="phero__ctas">
            <a class="btn btn--dark" data-book="page-hero" href="{BOOKING}"><span class="btn__label">{esc(p.get("cta_label", "Book an intro call"))}</span><span class="btn__icon">{ARROW}</span></a>
            {btn2}
          </div>
        </div>
        {visual}
      </div>
    </section>
'''

def sections_html(p):
    out = []
    for i, (h2, body) in enumerate(p.get("sections", [])):
        sid = re.sub(r"[^a-z0-9]+", "-", strip(h2).lower()).strip("-")[:48]
        out.append(f'<section class="psec" id="{sid}"><div class="container psec__inner" data-in><h2 class="psec__h">{h2}</h2><div class="prose">{body}</div></div></section>')
    return "\n".join(out)

def cards_html(p):
    if not p.get("cards"): return ""
    palette = ["pink", "purple", "green", "orange", "stone", "white"]
    cards = "".join(f'<div class="kcard kcard--{palette[i % len(palette)]}" data-in><span class="kcard__n">{i+1:02d}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(p["cards"]))
    label = "What’s included" if p["kind"] == "service" else "Highlights"
    return f'<section class="psec"><div class="container"><div class="psec__head" data-in><span class="pill">{label}</span><h2 class="psec__h">Everything you get</h2></div><div class="kgrid">{cards}</div></div></section>'

def steps_html(p):
    if not p.get("steps"): return ""
    st = "".join(f'<li class="kstep" data-in><span>{i+1:02d}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for i, (t, d) in enumerate(p["steps"]))
    return f'<section class="psec"><div class="container"><div class="psec__head" data-in><span class="pill">How we work</span><h2 class="psec__h">Our process</h2></div><ol class="ksteps">{st}</ol></div></section>'

def proof_html(p):
    if p["kind"] not in ("service", "about"): return ""
    from content import PROOF_STATS
    st = "".join(f'<div class="kstat" data-in><strong>{esc(b)}</strong><span>{esc(l)}</span></div>' for b, l in PROOF_STATS)
    return f'<section class="psec psec--dark"><div class="container"><div class="psec__head" data-in><span class="pill">Proof, not promises</span><h2 class="psec__h">Results you can count</h2></div><div class="kstats">{st}</div></div></section>'

def faq_html(p):
    if not p.get("faqs"): return ""
    qs = "".join(f'<details class="qa2" data-in{" open" if i == 0 else ""}><summary><h3>{esc(q)}</h3><i></i></summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(p["faqs"]))
    return f'<section class="psec" id="faq"><div class="container psec__narrow"><div class="psec__head psec__head--center" data-in><span class="pill">FAQ</span><h2 class="psec__h">Frequently asked questions</h2></div><div class="qa2-list">{qs}</div></div></section>'

def related_html(p):
    rel = [BY_SLUG[s] for s in p.get("related", []) if s in BY_SLUG]
    if not rel: return ""
    items = "".join(f'<a class="rel" href="/{r["slug"]}" data-in><span class="rel__k">{esc(r["eyebrow"])}</span><strong>{esc(r["nav_label"])}</strong><span class="rel__d">{esc(r["desc"][:110].rsplit(" ", 1)[0])}…</span><span class="rel__go">{ARROW}</span></a>' for r in rel)
    return f'<section class="psec"><div class="container"><div class="psec__head" data-in><span class="pill">Keep exploring</span><h2 class="psec__h">Related</h2></div><div class="rels">{items}</div></div></section>'

def sources_html(p):
    if not p.get("sources"): return ""
    li = "".join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t, u in p["sources"])
    return f'<section class="psec psec--sources"><div class="container psec__narrow"><h2 class="psec__h psec__h--sm">Sources</h2><ol class="sources">{li}</ol><p class="src-note">Facts checked on 17 October 2026. Third-party benchmarks are estimates; your results depend on your industry, offer and creative.</p></div></section>'

def cta_html(p):
    return f'''<section class="psec"><div class="container"><div class="ctaband" data-in>
<h2>Ready to grow with Akarsa Studio?</h2><p>Book a 30-minute intro call. We’ll look at your marketing and tell you honestly what to fix first.</p>
<a class="btn btn--light" data-book="page-cta" href="{BOOKING}"><span class="btn__label">Book an intro call</span><span class="btn__icon">{ARROW}</span></a>
</div></div></section>
  </main>
'''

def article_body(p):
    toc = "".join(f'<li><a href="#{re.sub(r"[^a-z0-9]+", "-", strip(h).lower()).strip("-")[:48]}">{esc(strip(h))}</a></li>' for h, _ in p["sections"])
    tk = "".join(f"<li>{esc(t)}</li>" for t in p.get("takeaways", []))
    secs = "".join(f'<h2 id="{re.sub(r"[^a-z0-9]+", "-", strip(h).lower()).strip("-")[:48]}">{h}</h2>{b}' for h, b in p["sections"])
    return f'''<section class="psec"><div class="container art">
<aside class="art__toc"><span class="eyebrow eyebrow--muted">On this page</span><ol>{toc}<li><a href="#faq">FAQ</a></li></ol></aside>
<article class="prose prose--article">
<div class="takeaways"><span class="answer__label">Key takeaways</span><ul>{tk}</ul></div>
{secs}
<div class="authorbox"><img src="/icon-192.png" alt="" width="56" height="56" loading="lazy" /><div><strong>Akarsa Studio</strong><span>AI-driven marketing agency in Vijay Nagar, Indore. We run Meta, Google, Reddit and ChatGPT ads for brands across India. <a href="/about">About us</a></span></div></div>
</article></div></section>'''

def render(p):
    parts = [head(p), NAV, hero(p)]
    if p["kind"] == "article":
        parts += [article_body(p), faq_html(p), related_html(p), sources_html(p), cta_html(p)]
    else:
        parts += [sections_html(p), cards_html(p), steps_html(p), proof_html(p), faq_html(p), related_html(p), sources_html(p), cta_html(p)]
    parts.append(footer())
    return "\n".join(x for x in parts if x)

def render_hub(h):
    items = []
    for s in GUIDES_ORDER:
        g = BY_SLUG[s]
        items.append(f'<a class="rel rel--big" href="/{s}" data-in><span class="rel__k">{esc(g["eyebrow"])}</span><strong>{esc(g["h1"])}</strong><span class="rel__d">{esc(g["desc"])}</span><span class="rel__go">{ARROW}</span></a>')
    hub = dict(h, faqs=[], related=[], sources=[], wa="Hi Akarsa! I read your insights and want to talk about marketing.")
    body = f'<section class="psec"><div class="container"><div class="rels rels--2">{"".join(items)}</div></div></section>'
    return "\n".join([head(hub), NAV, hero(hub), body, cta_html(hub), footer()])

def build_404():
    """Branded page for unknown URLs. Vercel serves /404.html with a real 404 status; noindex keeps it out of search."""
    links = "".join(f'<a class="rel" href="/{s}"><span class="rel__k">{esc(BY_SLUG[s]["eyebrow"])}</span><strong>{esc(BY_SLUG[s]["nav_label"])}</strong><span class="rel__go">{ARROW}</span></a>'
                    for s in ["results", "meta-ads-agency-indore", "social-media-marketing-agency-indore", "about"])
    html_ = f'''<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8" />
{PIXEL}  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Page not found | Akarsa Studio</title>
  <meta name="robots" content="noindex, follow" />
  <meta name="theme-color" content="#0e3b30" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <script>document.documentElement.classList.add('js')</script>
  <link rel="stylesheet" href="/styles.css?v={V}" />
  <link rel="stylesheet" href="/page.css?v={V}" />
</head>
{NAV}  <main class="page" id="main">
    <section class="phero"><div class="container psec__narrow">
      <span class="pill">Error 404</span>
      <h1 class="phero__title">This page doesn’t exist.</h1>
      <p class="phero__lead">The link may be old or mistyped. Here’s where most people were heading.</p>
      <div class="phero__ctas"><a class="btn btn--dark" href="/"><span class="btn__label">Back to the homepage</span><span class="btn__icon">{ARROW}</span></a></div>
    </div></section>
    <section class="psec"><div class="container"><div class="rels">{links}</div></div></section>
  </main>
{footer()}'''
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(html_)

# ---------- security headers + caching (vercel.json) ----------
# Third parties the pages really use: GSAP/Lenis (exact versions, SRI-pinned in index.html), the OpenAI Ads pixel,
# and the Calendly booking popup. Anything else is refused by the browser.
CSP_SOURCES = {
    "default-src": ["'self'"],
    "script-src": ["'self'", "https://cdn.jsdelivr.net/npm/gsap@3.12.5/", "https://cdn.jsdelivr.net/npm/lenis@1.1.13/",
                   "https://bzrcdn.openai.com", "https://assets.calendly.com"],
    "style-src": ["'self'", "'unsafe-inline'", "https://assets.calendly.com"],
    "img-src": ["'self'", "data:", "https://bzr.openai.com", "https://assets.calendly.com"],
    "font-src": ["'self'"],
    "connect-src": ["'self'", "https://bzr.openai.com", "https://bzrcdn.openai.com"],
    "frame-src": ["https://calendly.com"],
    "frame-ancestors": ["'self'"],
    "base-uri": ["'self'"],
    "form-action": ["'self'"],
    "object-src": ["'none'"],
}

def inline_script_hashes():
    """sha256 of every inline executable script on every page, so CSP allows exactly these and nothing injected."""
    import base64, glob, hashlib
    hashes = set()
    for f in glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "*", "*.html")):
        for attrs, body in re.findall(r"<script([^>]*)>(.*?)</script>", open(f, encoding="utf-8").read(), re.S):
            if "src=" in attrs or "application/ld+json" in attrs:
                continue
            hashes.add("'sha256-" + base64.b64encode(hashlib.sha256(body.encode()).digest()).decode() + "'")
    return sorted(hashes)

def write_vercel_config():
    src = {k: list(v) for k, v in CSP_SOURCES.items()}
    src["script-src"] += inline_script_hashes()
    csp = "; ".join(f"{k} {' '.join(v)}" for k, v in src.items())
    cache = lambda v: [{"key": "Cache-Control", "value": v}]
    config = {
        "cleanUrls": True,
        "headers": [
            {"source": "/(.*)", "headers": [
                {"key": "Content-Security-Policy", "value": csp},
                {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains"},
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=(), usb=(), browsing-topics=()"},
                {"key": "Cross-Origin-Opener-Policy", "value": "same-origin-allow-popups"},
            ]},
            # later rules win: general first, most specific last
            {"source": "/(.*)\\.(png|jpg|svg|ico|webmanifest)", "headers": cache("public, max-age=86400, stale-while-revalidate=86400")},
            {"source": "/assets/(.*)", "headers": cache("public, max-age=2592000, stale-while-revalidate=86400")},
            {"source": "/(.*)\\.(css|js)", "headers": cache("public, max-age=2592000, stale-while-revalidate=86400")},  # always referenced with ?v=
            {"source": "/assets/fonts/(.*)", "headers": cache("public, max-age=31536000, immutable")},
            # public brand kit: logos, avatar and banners, readable from other sites (press, partners, profile uploads)
            {"source": "/assets/brand/(.*)", "headers": [{"key": "Access-Control-Allow-Origin", "value": "*"},
                                                         {"key": "Cross-Origin-Resource-Policy", "value": "cross-origin"}]},
        ],
    }
    open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8").write(json.dumps(config, indent=2, ensure_ascii=False) + "\n")

def write(slug, content):
    path = os.path.join(ROOT, (slug + "index.html") if slug.endswith("/") else (slug + ".html"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)
    return path

def build_sitemap():
    pri = {"service": "0.9", "article": "0.8", "case": "0.7", "about": "0.6", "hub": "0.6"}
    old = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    home_block = re.search(r"  <url>\s*<loc>https://www\.akarsaone\.xyz/</loc>.*?</url>", old, re.S).group(0)
    home_block = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{TODAY}</lastmod>", home_block, 1)
    urls = [home_block]
    for p in PAGES + [INSIGHTS_HUB]:
        urls.append(f'  <url>\n    <loc>{url(p["slug"])}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{pri[p["kind"]]}</priority>\n  </url>')
    urls.append(f'  <url>\n    <loc>{SITE}/privacy</loc>\n    <lastmod>2026-10-13</lastmod>\n    <changefreq>yearly</changefreq>\n    <priority>0.3</priority>\n  </url>')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(urls) + "\n</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)

FACTS = f"""- Legal name: Akarsa Studio Private Limited (brand: Akarsa, also written Ākarṣa)
- What: AI-driven, truth-seeking marketing agency — "where art meets intelligence"
- Founder: Ritik Sharma (Founder & Director, host of Akarsa Live)
- Address: Office No. 702, Shagun Arcade, Main Rd, near Apna Sweets, PU 4, near Vijay Nagar Square, Vijay Nagar, Indore, Madhya Pradesh 452010, India
- Phone/WhatsApp: +91 81098 01383
- 30-minute intro call (book online): {BOOKING}
- Office hours: Mon–Fri 11:00–19:30, Sat 12:00–15:30, Sun closed (IST)
- Website: https://www.akarsaone.xyz
- Services: social media marketing, UGC & short-form video, video editing & animation, influencer marketing, Meta ads, Google ads, YouTube ads, Reddit ads, ChatGPT ads, brand identity & logo design, graphic design, website development & management, AI marketing automation
- Offer: spend more than $1,000 on Reddit ads through Akarsa Studio and Reddit assigns a dedicated team from Reddit to the account, working alongside Akarsa to optimise and precisely target
- Clients: 20+ brands incl. Starbucks, Adidas, Decathlon, Burger Singh, Chirmi, The Duke's Table, Olympia Fitness Gym, The Korean Trends, Mayaram's Farm, Bake Affaire, Nomad Pizza, Kunafa Bytes, Lokal, Urban Theka, Kahani, Varenyam, Zhanna Events & Flowers, Fleuristry
- Results: Meta ads ₹30,000 → 52 enquiries; cost per enquiry ₹7,500 → ₹577 (≈13× lower). E-commerce client (RC toys), 6 Sep–7 Oct 2026: 196 purchases from ₹74,600, ₹381 per purchase, 3.7× average ROAS. International store: $419 → $1,149 (2.74× ROAS). Own lead campaigns (Meta API, Aug 2025–Oct 2026): ₹25,944 spent, 186 leads; best ₹28.68 and ₹47.76 per lead. Full data: https://www.akarsaone.xyz/results Akarsa One (AI business intelligence): 3× qualified leads
- Social: Instagram @akarsa_studio · YouTube @AkarsaStudio · Facebook · Pinterest /beakarsa"""

def build_llms():
    lines = ["# Akarsa Studio", "", "> Akarsa Studio (Akarsa Studio Private Limited) is an AI-driven marketing agency in Vijay Nagar, Indore, India. It runs social media, UGC/reels, influencer marketing, Meta, Google, YouTube, Reddit and ChatGPT ads, branding and website development for 20+ brands including Starbucks, Adidas and Decathlon.", "", "## Key facts", FACTS, "", "## Services"]
    for s in SERVICES_ORDER:
        p = BY_SLUG[s]; lines.append(f'- [{p["h1"]}]({url(s)}): {strip(p["answer"])}')
    lines += ["", "## Guides and proof"]
    for s in GUIDES_ORDER:
        p = BY_SLUG[s]; lines.append(f'- [{p["h1"]}]({url(s)}): {p["desc"]}')
    lines += ["", "## Company", f"- [About Akarsa Studio]({url('about')}): {BY_SLUG['about']['desc']}", f"- [Homepage]({SITE}/): Overview, work, services, process, FAQs and contact.", "", "## Optional", f"- [Full facts and FAQs for AI assistants]({SITE}/llms-full.txt)", ""]
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))
    full = ["# Akarsa Studio — full reference for AI assistants", "", "## Key facts", FACTS, ""]
    for p in [BY_SLUG[s] for s in SERVICES_ORDER + GUIDES_ORDER] + [BY_SLUG["about"]]:
        full += [f'## {p["h1"]}', f'URL: {url(p["slug"])}', "", strip(p["answer"]), ""]
        if p.get("takeaways"): full += ["Key takeaways:"] + [f"- {t}" for t in p["takeaways"]] + [""]
        for q, a in p.get("faqs", []): full += [f"Q: {q}", f"A: {a}", ""]
        if p.get("sources"): full += ["Sources:"] + [f"- {t}: {u}" for t, u in p["sources"]] + [""]
    open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(full))

ROBOTS = """# Akarsa Studio — all search engines and AI assistants are welcome to crawl this site.
User-agent: *
Allow: /

# AI search & assistant crawlers (explicitly allowed for GEO / AI answers)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /
User-agent: CCBot
Allow: /
User-agent: Meta-ExternalAgent
Allow: /

Sitemap: https://www.akarsaone.xyz/sitemap.xml
"""

if __name__ == "__main__":
    for p in PAGES:
        write(p["slug"], render(p))
    write("insights/", render_hub(INSIGHTS_HUB))
    build_sitemap(); build_llms(); build_404()
    write_vercel_config()  # last: hashes every inline script on every page, including index.html and privacy.html
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(ROBOTS)
    print(f"built {len(PAGES) + 1} pages + sitemap.xml, llms.txt, llms-full.txt, robots.txt")
