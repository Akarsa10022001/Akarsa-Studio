# -*- coding: utf-8 -*-
"""Content for the SEO / AEO / GEO landing pages and guides.

Every number here is either Akarsa's own data (Meta ads case: ₹30,000 -> 52 enquiries,
cost per enquiry ₹7,500 -> ₹577; Akarsa One: 3x qualified leads; 20+ brands) or a
third-party fact cited in the page's `sources`. Do not add claims without a source.
"""

import os
from functools import lru_cache

SITE = "https://www.akarsaone.xyz"
TODAY = "2026-10-17"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@lru_cache(None)
def img_size(src):
    """(width, height) of a site image, for width/height attributes; None if it can't be read."""
    try:
        from PIL import Image
        with Image.open(os.path.join(ROOT, src.lstrip("/"))) as im:
            return im.size
    except Exception:
        return None

# ---------- shared sources ----------
S_INC42 = ("Inc42 — OpenAI rolls out ChatGPT ads in India (27 Aug 2026)", "https://inc42.com/buzz/openai-rolls-out-chatgpt-ads-in-india/")
S_E4M = ("exchange4media — OpenAI rolls out ChatGPT Ads in India", "https://www.exchange4media.com/digital-news/openai-rolls-out-chatgpt-ads-in-india-157677.html")
S_CNBC = ("CNBC — OpenAI rolls out ads on select ChatGPT plans in India (28 Aug 2026)", "https://www.cnbc.com/2026/08/28/openai-strategy-india-anthropic-ipo.html")
S_OUTLOOK = ("Outlook Business — OpenAI rolls out ChatGPT ads in India, its second-largest market", "https://www.outlookbusiness.com/corporate/openai-rolls-out-chatgpt-ads-in-india-its-second-largest-market")
S_OPENAI = ("OpenAI — A milestone in expanding access to AI", "https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/")
S_ICECUBE = ("Icecube Digital — ChatGPT Ads in India: cost, setup & eligibility", "https://www.icecubedigital.in/blog/chatgpt-ads-india/")
S_UPGROWTH = ("upGrowth — ChatGPT Ads India 2026 guide", "https://upgrowth.in/chatgpt-ads-guide-india/")
S_SAMOSA = ("Social Samosa — Durgesh Kaushik breaks down Reddit's ad strategy (31 Jul 2025)", "https://www.socialsamosa.com/interviews/durgesh-kaushik-reddit-ad-strategy-9605595")
S_E4M_REDDIT = ("exchange4media — Why Reddit could be the next big playground for Indian brands", "https://www.exchange4media.com/marketing-news/why-reddit-could-be-the-next-big-playground-for-indian-brands-146277.html")
S_AIMERS = ("Aimers — Reddit Ads cost in 2026: CPC, CPM and budget benchmarks", "https://aimers.io/blog/reddit-ads-cost")
S_STACKMATIX = ("Stackmatix — Reddit Ads cost in 2026", "https://www.stackmatix.com/blog/reddit-ads-cost-guide-2026")
S_TRILOKANA = ("Trilokana — Reddit advertising cost in India: 2025 guide", "https://trilokana.com/blog/reddit-advertising-cost-in-india-2025-guide/")
S_OWL_IN = ("OwlClaw — Meta ads benchmarks India", "https://owlclaw.com/benchmarks/meta-ads-benchmarks-india")
S_SOTROS = ("Sotros Infotech — Paid social ads benchmarks India & Southeast Asia 2026", "https://sotrosinfotech.com/blog/paid-social-ads-benchmarks-india-southeast-asia-2026/")
S_VAIZLE = ("Vaizle — Facebook ads cost", "https://insights.vaizle.com/facebook-ads-cost/")
S_CASE_REEL = ("Akarsa Studio on Instagram — ₹30K → 52 enquiries breakdown", "https://www.instagram.com/akarsa_studio/reel/DeEImQ5OMDT/")

WA = "Hi Akarsa! I found you on your website and would like to talk about "

# ---------- reusable visuals ----------
def reels(paths, color="#1c1917", light=False, alts=None):
    cls = "media media--panel" + (" media--light" if light else "")
    alts = alts or [""] * len(paths)
    def wh(p):
        d = img_size(p)
        return f' width="{d[0]}" height="{d[1]}"' if d else ""
    imgs = "".join(f'<img class="reel" src="{p}" alt="{a}"{wh(p)} loading="eager" decoding="async" />' for p, a in zip(paths, alts))
    return f'<div class="pvisual"><div class="{cls}" style="--pc:{color}"><div class="reels reels--{len(paths)}">{imgs}</div></div></div>'

GPT_MOCK = '''<div class="pvisual pvisual--mock pvisual--dark"><div class="gpt-chat" aria-hidden="true">
  <p class="gpt-chat__q">Which gym in Indore has the best trainers?</p>
  <p class="gpt-chat__a">Here are a few well-reviewed options people recommend…</p>
  <div class="gpt-chat__ad"><span class="gpt-chat__label">Sponsored</span><strong>Your Brand</strong><span>Free trial session · Book on WhatsApp</span></div>
</div><span class="pvisual__chip">Ads appear below answers · labelled “Sponsored”</span></div>'''

REDDIT_MOCK = '''<div class="pvisual pvisual--mock pvisual--reddit"><div class="rd-post" aria-hidden="true">
  <div class="rd-post__votes"><svg viewBox="0 0 24 24"><path d="M12 4 4 13h5v7h6v-7h5z"/></svg><b>1.2k</b></div>
  <div class="rd-post__body"><div class="rd-post__meta"><span class="rd-post__sub"></span>r/IndianStartups · <em>Promoted</em></div>
  <p class="rd-post__title">Your brand, in front of the exact communities that buy.</p>
  <div class="rd-post__actions"><span>💬 86 comments</span><span class="rd-post__cta">Learn more</span></div></div>
</div><div class="offer offer--mini"><span class="offer__eyebrow">Reddit team offer</span><strong class="offer__big">$1,000+</strong><span class="offer__line">spend on Reddit ads = a <b>dedicated team from Reddit</b></span></div></div>'''

GOOGLE_MOCK = '''<div class="pvisual pvisual--mock"><div class="gad" aria-hidden="true">
  <div class="gad__bar"><span>marketing agency in indore</span><i></i></div>
  <div class="gad__res"><span class="gad__spon">Sponsored</span><span class="gad__url">www.yourbrand.in › services</span>
  <strong class="gad__title">Your Brand — Book a Free Consultation Today</strong>
  <p>Trusted by local customers. Fast response on WhatsApp. Call or visit our Vijay Nagar store.</p>
  <div class="gad__links"><span>Pricing</span><span>Reviews</span><span>Contact</span></div></div>
  <div class="gad__res gad__res--org"><span class="gad__url">www.competitor.com</span><strong class="gad__title">Organic result</strong><p>…</p></div>
</div><span class="pvisual__chip">Search ads · Performance Max · YouTube</span></div>'''

BROWSER_MOCK = '''<div class="pvisual pvisual--mock"><div class="bmock"><div class="bmock__bar"><i></i><i></i><i></i><span>akarsaone.xyz</span></div>
<img src="/og-image.jpg" alt="Akarsa Studio website homepage designed and built by Akarsa" width="1200" height="630" loading="eager" /></div>
<span class="pvisual__chip">Our own site — designed, built &amp; SEO-optimised in-house</span></div>'''

BRAND_MOCK = '''<div class="pvisual pvisual--mock"><div class="bboard" aria-hidden="true">
  <div class="bboard__mark"><svg viewBox="110 60 400 400"><rect x="110" y="60" width="400" height="400" rx="100" fill="url(#akg)"/><path fill="#fff" d="M300,122 L172,246 L243,250 A71,93 0 0 1 172,343 L172,396 A128,140 0 0 0 300,256 Z M313,256 L372,256 A75,87 0 0 0 447,343 L447,396 A134,140 0 0 1 313,256 Z"/></svg></div>
  <div class="bboard__type"><b>Aa</b><span>Open Sauce One<br/>Anton · Caveat</span></div>
  <div class="bboard__sw"><i style="--c:#1C1917">#1C1917</i><i style="--c:#FFA8F2">#FFA8F2</i><i style="--c:#AA94FF">#AA94FF</i><i style="--c:#9EF483">#9EF483</i></div>
  <p class="bboard__note">Our own identity system — mark, type and colour.</p>
</div></div>'''

ADDRESS_CARD = '''<div class="pvisual pvisual--mock"><div class="addr-card">
  <svg class="addr-card__mark" viewBox="110 60 400 400" aria-hidden="true"><rect x="110" y="60" width="400" height="400" rx="100" fill="url(#akg)"/><path fill="#fff" d="M300,122 L172,246 L243,250 A71,93 0 0 1 172,343 L172,396 A128,140 0 0 0 300,256 Z M313,256 L372,256 A75,87 0 0 0 447,343 L447,396 A134,140 0 0 1 313,256 Z"/></svg>
  <span class="addr-card__eyebrow">Visit the studio</span>
  <strong>Akarsa Studio</strong>
  <address>Office No. 702, Shagun Arcade, Main Rd,<br/>near Apna Sweets, PU 4, near Vijay Nagar Square,<br/>Vijay Nagar, Indore, Madhya Pradesh 452010</address>
  <p class="addr-card__hours">Mon–Fri 11:00 am – 7:30 pm · Sat 12:00 – 3:30 pm · Sun closed</p>
  <a class="addr-card__btn" href="https://www.google.com/maps/search/?api=1&amp;query=Akarsa%20Studio%20Shagun%20Arcade%20Vijay%20Nagar%20Indore%20452010" target="_blank" rel="noopener">Get directions ↗</a>
</div></div>'''

ABOUT_VISUAL = '''<div class="pvisual pvisual--mock"><div class="founder-card">
  <img src="/assets/founder/ritik-sharma.jpg" alt="Ritik Sharma, Founder &amp; Director of Akarsa Studio" width="256" height="256" loading="eager" />
  <strong>Ritik Sharma</strong><span>Founder &amp; Director · Host of Akarsa Live</span>
  <p>“We don’t sell illusions. We engineer impact.”</p>
</div></div>'''

# ---------- verified results: stat tiles + bar charts built as real tables ----------
# Numbers come from Meta Ads Manager (client exports) or Meta's API (our own accounts); keep the maths notes in sync.
def kpis(items):
    return f'<div class="rkpis{" rkpis--3" if len(items) == 3 else ""}">' + "".join(f'<div class="rkpi" data-in><strong>{v}</strong><span>{l}</span></div>' for v, l in items) + '</div>'

def bars(title, sub, col, rows, best=None):
    # rows: (label, value, shown, tooltip); bars scale from zero; `best` highlights one row, None = all accent
    top = max(r[1] for r in rows)
    trs = "".join(
        f'<tr tabindex="0" data-tip="{lab}|{tip}"><th scope="row">{lab}</th>'
        f'<td class="rchart__track"><span class="rbar{" rbar--top" if best is None or i == best else ""}" style="--w:{v / top * 100:.1f}%"></span></td>'
        f'<td class="rchart__val">{shown}</td></tr>'
        for i, (lab, v, shown, tip) in enumerate(rows))
    return (f'<figure class="rchart" data-in><figcaption><strong>{title}</strong><span>{sub}</span></figcaption>'
            f'<table><thead class="vh"><tr><th scope="col">Item</th><th scope="col">Bar</th><th scope="col">{col}</th></tr></thead><tbody>{trs}</tbody></table></figure>')

def vsource(text):
    return f'<p class="vsrc"><i aria-hidden="true"></i>{text}</p>'

# RC-toy e-commerce client, ads level, 6 Sep–7 Oct 2026, 7-day click (client's Ads Manager)
RC_ADS = [("Ad 1", 38, 15820, 416, 3.1, 138420, 2.1), ("Ad 2", 52, 17960, 345, 4.0, 162310, 1.8), ("Ad 3", 36, 13640, 379, 3.4, 119870, 2.0),
          ("Ad 4", 28, 9720, 347, 4.2, 96540, 1.6), ("Ad 5", 42, 17460, 416, 3.8, 141220, 1.9)]

def _rc_table():
    rows = "".join(f'<tr><th scope="row">{a}</th><td>{p}</td><td>₹{s_:,}</td><td>₹{c}</td><td>{r:.1f}×</td><td>{re_:,}</td><td>{f}</td></tr>' for a, p, s_, c, r, re_, f in RC_ADS)
    return ('<div class="rtable" data-in><table><thead><tr><th scope="col">Ad</th><th scope="col">Purchases</th><th scope="col">Amount spent</th><th scope="col">Cost per purchase</th>'
            '<th scope="col">Purchase ROAS</th><th scope="col">Reach</th><th scope="col">Frequency</th></tr></thead><tbody>' + rows +
            '</tbody><tfoot><tr><th scope="row">Total</th><td>196</td><td>₹74,600</td><td>₹381</td><td>3.7× total</td><td>—</td><td>1.9</td></tr></tfoot></table></div>')

RESULTS_VISUAL = '''<div class="pvisual pvisual--mock"><div class="rcard">
  <span class="rcard__eyebrow">E-commerce brand · 6 Sep–7 Oct 2026</span>
  <div class="rcard__stats"><div><strong>3.7×</strong><span>ROAS</span></div><div><strong>196</strong><span>purchases</span></div><div><strong>₹381</strong><span>per purchase</span></div></div>
  <div class="rcard__bars" aria-hidden="true">''' + "".join(f'<div><span>{a}</span><i style="--w:{r / 4.2 * 100:.0f}%"></i><b>{r:.1f}×</b></div>' for a, _, _, _, r, _, _ in RC_ADS) + '''</div>
  <span class="rcard__src">From Meta Ads Manager · 7-day click</span>
</div></div>'''

# Google reviews shown on the site: exact text from the Google Business Profile, all still live and 5 stars on 21 Oct 2026.
# Deliberately no Review/AggregateRating schema (Google treats a business's own review markup as self-serving).
# (name, what they hired us for, exact review text, avatar background, avatar letter colour)
GOOGLE_REVIEWS = [
    ("Bhaskar Gupta", "Restaurant franchise", "We wanted to expand our restaurant franchise, and Akarsa helped us improve our online presence and generate more franchise enquiries. Their content strategy has made a real difference for us.", "#FFA8F2", "#1C1917"),
    ("Gyandeep Parashar", "Real-estate firm", "I went to them for my real-estate firm, my firm has grew a lot since the time I have started working with them.", "#AA94FF", "#1C1917"),
    ("Deepak Dixit", "", "Best in town for marketing 🙌 👏", "#9EF483", "#1C1917"),
    ("Shashwat Mishra", "", "Great experience with akrarsa and team", "#FFA952", "#1C1917"),
    ("Shivam Baghel", "", "Spectacular.", "#1C1917", "#FFA8F2"),
]
GOOGLE_PROFILE = "https://g.page/r/CcurrO6xi-njEBM"

def google_reviews(attr="data-reveal", title=True):
    """Homepage review strip (pasted into index.html by hand). The first set is read by assistive tech; the loop copies are hidden."""
    def card(r, hidden):
        name, what, text, bg, fg = r
        hid = ' aria-hidden="true"' if hidden else ""
        return (f'<figure class="grev"{hid}>'
                f'<figcaption class="grev__who"><span class="grev__dp" style="--dp:{bg};--dpc:{fg}" aria-hidden="true">{name[0]}</span>'
                f'<span><strong>{name}</strong><span class="grev__meta">{(what + " · ") if what else ""}Google review</span></span></figcaption>'
                f'<div class="grev__stars" role="img" aria-label="Rated 5 out of 5 on Google">★★★★★</div>'
                f'<blockquote><p>{text}</p></blockquote></figure>')
    # four copies: each half of the track is two sets wide, so the loop never shows a gap on wide screens
    track = "".join(card(r, k > 0) for k in range(4) for r in GOOGLE_REVIEWS)
    head = "<strong>What clients say on Google</strong>" if title else ""
    return (f'<div class="greviews"><div class="greviews__head" {attr}>{head}'
            f'<a href="{GOOGLE_PROFILE}" target="_blank" rel="noopener">See all our reviews on Google →</a></div>'
            f'<div class="greviews__viewport" {attr}><div class="greviews__track">{track}</div></div></div>')

# ---------- shared blocks ----------
PROOF_STATS = [("₹577", "cost per enquiry on Meta ads — down from ₹7,500"), ("3.7×", "ROAS for an e-commerce brand — 196 purchases in 32 days"), ("3×", "qualified leads with Akarsa One, our AI business intelligence"), ("20+", "brands including Starbucks, Adidas & Decathlon")]

PAGES = []

def page(**kw):
    PAGES.append(kw)
    return kw

# =====================================================================
# 1. ChatGPT ads agency (commercial, blue-ocean)
# =====================================================================
page(
    slug="chatgpt-ads-agency-india", kind="service", group="Ads",
    title="ChatGPT Ads Agency in India | Akarsa Studio",
    desc="Run ChatGPT ads in India with Akarsa Studio, an AI-driven agency in Indore: strategy, setup, conversational ad copy, tracking and reporting.",
    nav_label="ChatGPT Ads",
    eyebrow="New · ChatGPT Ads", h1="ChatGPT Ads Agency in India",
    lead="Be the brand people see when they ask ChatGPT what to buy, where to go and who to hire.",
    answer="Akarsa Studio is an AI-driven marketing agency in Indore that plans, launches and optimises ChatGPT ads for Indian businesses. ChatGPT ads went live in India on 27 August 2026. They appear below answers for logged-in adults on the Free and Go plans, and self-serve buying starts at ₹725 a day.",
    visual=GPT_MOCK, wa=WA + "ChatGPT ads.", cta_label="Start ChatGPT ads",
    service_type="ChatGPT advertising",
    sections=[
        ("ChatGPT ads in India: the key facts", '''<div class="facts"><table>
<tr><th>Launched in India</th><td>27 August 2026 — India is OpenAI’s second-largest market</td></tr>
<tr><th>Who sees ads</th><td>Logged-in adults on the Free and Go plans. Plus, Pro, Business, Enterprise and Education stay ad-free</td></tr>
<tr><th>Where ads appear</th><td>Below ChatGPT’s answer when a relevant sponsored product or service exists — clearly labelled and visually separated</td></tr>
<tr><th>Self-serve buying</th><td>ChatGPT Ads Manager opened on 4 September 2026</td></tr>
<tr><th>Minimum budget</th><td>Daily budgets start at ₹725</td></tr>
<tr><th>Never shown</th><td>To users under 18, or next to sensitive topics such as mental health and politics</td></tr>
<tr><th>Your data</th><td>Advertisers get aggregate results (impressions, clicks) — never conversations, chat history or memories</td></tr>
<tr><th>Launch agency partners</th><td>WPP and Omnicom, on a non-exclusive basis</td></tr>
</table></div>
<p class="src-note">Sources: Inc42, exchange4media, Outlook Business — see the list at the end of this page.</p>'''),
        ("Why advertise on ChatGPT now", '''<p>People don’t scroll past ChatGPT answers — they ask a specific question and act on what they read. That makes every placement high-intent. Three numbers explain the opportunity:</p>
<ul class="ticks">
<li><b>Early window.</b> Only about 50 brands were expected to go live in India in the launch week, so auctions are far less crowded than Meta or Google.</li>
<li><b>Higher conversion.</b> Redseer estimates AI-native ad formats can deliver up to 4× the conversion rate of conventional search ads (as reported by Inc42).</li>
<li><b>Where budgets are heading.</b> Redseer expects conversational AI assistants to account for around 8% of digital advertising by 2030.</li>
</ul>
<p>OpenAI says ChatGPT Ads has already reached a $1 billion annualised revenue run rate with tens of thousands of advertisers worldwide. The brands that learn the format now will own the cheapest clicks while competition is still low.</p>'''),
    ],
    cards=[("Question mapping", "We find the questions your buyers actually ask ChatGPT — “best café near Vijay Nagar”, “gym with personal trainer in Indore” — and match offers to them."),
           ("Ads Manager setup", "Account, billing, campaign structure and budgets set up correctly from day one, starting from the ₹725/day minimum."),
           ("Conversational ad copy", "Ads written to answer a question, not shout a slogan — with an offer that makes the next step obvious."),
           ("Lead capture", "Landing pages or a WhatsApp flow built for the click, so enquiries reach you in seconds."),
           ("Tracking that proves ROI", "OpenAI Ads pixel and lead events (we already run it on this site) so every enquiry is measured."),
           ("Weekly optimisation", "We test placements, copy and offers every week and move budget to what converts.")],
    steps=[("Map the questions", "Research the conversations your customers have with AI."), ("Build the offer", "Write conversational ads and a fast landing or WhatsApp flow."), ("Launch small", "Start near the minimum budget and learn what converts."), ("Scale winners", "Move spend to the questions and copy that bring enquiries.")],
    faqs=[("Are ChatGPT ads available in India?", "Yes. OpenAI rolled out ChatGPT ads in India on 27 August 2026, and the self-serve ChatGPT Ads Manager opened to Indian businesses on 4 September 2026."),
          ("How much do ChatGPT ads cost in India?", "Daily budgets start at ₹725. What you actually pay per lead depends on your category, offer and targeting — we start close to the minimum, measure cost per enquiry, then scale what works."),
          ("Who sees ChatGPT ads?", "Logged-in adults on ChatGPT’s Free and Go plans. Users on Plus, Pro, Business, Enterprise and Education plans don’t see ads, and ads are never shown to anyone under 18."),
          ("Do ChatGPT ads change ChatGPT’s answers?", "No. OpenAI says ads don’t influence responses. They appear below the answer, clearly labelled and visually separated, and advertisers never get access to conversations."),
          ("Can a small business in Indore run ChatGPT ads?", "Yes. With self-serve buying from ₹725 a day, a café, gym, clinic or coaching centre can test ChatGPT ads without an enterprise budget. Local intent questions are often the cheapest to win."),
          ("Why use an agency for ChatGPT ads?", "The format is new, so most teams are still guessing. We bring conversational copywriting, offer design, lead tracking and weekly optimisation — and we already run performance campaigns on Meta, Google and Reddit.")],
    related=["reddit-ads-agency-india", "insights/chatgpt-ads-india-guide", "meta-ads-agency-indore", "google-ads-agency-indore"],
    sources=[S_INC42, S_E4M, S_OUTLOOK, S_CNBC, S_OPENAI],
)

# =====================================================================
# 2. Reddit ads agency (commercial, low competition, with offer)
# =====================================================================
page(
    slug="reddit-ads-agency-india", kind="service", group="Ads",
    title="Reddit Ads Agency in India | Akarsa Studio",
    desc="Reddit ads that reach the right communities. Spend $1,000+ on Reddit ads with us and Reddit assigns a dedicated team from Reddit to your brand.",
    nav_label="Reddit Ads",
    eyebrow="New · Reddit Ads", h1="Reddit Ads Agency in India",
    lead="Reach people inside the communities where they ask for recommendations — before your competitors do.",
    answer="Akarsa Studio runs Reddit ads for Indian and global brands from Indore, targeting by community, interest and conversation. Spend more than $1,000 on Reddit ads with us and Reddit assigns a dedicated team from Reddit itself, working alongside Akarsa to optimise and precisely target your campaigns.",
    visual=REDDIT_MOCK, wa=WA + "Reddit ads and the dedicated team from Reddit.", cta_label="Get your Reddit team",
    service_type="Reddit advertising",
    sections=[
        ("The offer: a dedicated team from Reddit at $1,000+", '''<div class="offer offer--wide"><span class="offer__eyebrow">Exclusive Reddit offer</span><strong class="offer__big">Spend $1,000+</strong>
<span class="offer__line">on Reddit ads with us and get a <b>dedicated team from Reddit</b></span>
<ul class="offer__list"><li><i class="tick"></i>Reddit’s own team assigned to your brand</li><li><i class="tick"></i>Working alongside the Akarsa team</li><li><i class="tick"></i>Sharper optimisation &amp; precise targeting</li></ul></div>
<p>When your Reddit ad spend with Akarsa crosses $1,000, Reddit assigns a dedicated team from Reddit to your account. They work hand in hand with us on targeting and optimisation, while we keep handling your strategy, Reddit-native creative, tracking and reporting.</p>'''),
        ("Why Reddit, and why now", '''<p>Reddit is different from every other ad platform: in the words of Reddit’s Durgesh Kaushik, “we are organised by interests, not social connections.” People join communities to ask questions and compare options — exactly the moment a brand wants to be present.</p>
<ul class="ticks">
<li><b>100,000+ active communities</b> worldwide, covering almost every niche a business sells into.</li>
<li><b>Built for India now:</b> Reddit has launched machine translation in Hindi and Bengali and introduced Reddit Answers in India.</li>
<li><b>Fast-growing outside the US:</b> Reddit’s international advertising revenue grew more than 80% year on year.</li>
<li><b>Wide open in India:</b> fewer than 10% of large consumer brands in India have activated formal Reddit campaigns, according to Gozoop’s India country head (via exchange4media).</li>
</ul>
<p>Low competition plus high-intent conversations is the combination that makes early Reddit advertisers win cheap attention.</p>'''),
        ("How Reddit ad targeting works", '''<p>Reddit lets you choose <b>where</b> and <b>to whom</b> your ads show:</p>
<ul class="ticks">
<li><b>Community targeting</b> — show ads in the subreddits your buyers read.</li>
<li><b>Interest targeting</b> — reach people by the topics they engage with.</li>
<li><b>Keyword and conversation targeting</b> — appear next to discussions about your category.</li>
<li><b>Location targeting</b> — focus spend on India, specific regions, or global markets.</li>
</ul>
<p>Reddit-native creative matters as much as targeting: ads that read like a helpful post outperform ads that read like a banner. That’s what our Reddit specialists write.</p>'''),
        ("What do Reddit ads cost?", '''<p>Reddit’s stated minimum is $5 a day. Third-party 2026 estimates put typical CPCs around $0.50–$2.50 and CPMs around $3–$9 globally, while one 2025 India guide reported roughly ₹8–₹20 per click. Your real numbers depend on the communities and offer — we forecast them during your audit. Read our full <a href="/insights/reddit-ads-cost-india">Reddit ads cost in India guide</a>.</p>'''),
    ],
    cards=[("Community research", "We map the subreddits, interests and conversations where your buyers already are."),
           ("Reddit-native creative", "Posts that sound like a helpful Redditor, not an ad — the single biggest driver of Reddit performance."),
           ("Precise targeting", "Community, interest, keyword and location targeting combined and tested."),
           ("Pixel & conversion tracking", "Reddit Pixel and conversion events set up so every lead and sale is measured."),
           ("Comment management", "We monitor and respond to comments on your promoted posts — Reddit audiences reward brands that engage."),
           ("Continuous optimisation", "Weekly tests on creative, communities and bids, with transparent reporting.")],
    steps=[("Audit", "Your goals, audience and the communities they use."), ("Create", "Reddit-native ads and landing pages."), ("Launch", "Tight targeting, conversion tracking live from day one."), ("Optimise", "Weekly improvements — with Reddit’s own team on board past $1,000.")],
    faqs=[("What do I get if I spend more than $1,000 on Reddit ads?", "A dedicated team from Reddit itself. When your Reddit ad spend with Akarsa crosses $1,000, Reddit assigns its own team to your account. They work alongside us on optimisation and precise targeting, while we handle community research, Reddit-native creative, tracking, comment management and weekly reporting."),
          ("Are Reddit ads worth it for Indian brands?", "Often, yes — especially for brands whose buyers research before purchasing. Fewer than 10% of large consumer brands in India run formal Reddit campaigns, so competition is low, and Reddit is investing in India with Hindi and Bengali machine translation."),
          ("How much do Reddit ads cost in India?", "Reddit’s minimum is $5 a day. Third-party estimates suggest typical CPCs of about $0.50–$2.50 globally, and one 2025 India guide reported around ₹8–₹20 per click. We forecast your costs during the audit."),
          ("Can Reddit ads target only Indian users?", "Yes. Reddit supports location targeting, so campaigns can focus on India, specific regions, or international markets if you sell globally."),
          ("Which businesses do best on Reddit?", "Tech and SaaS, gaming, D2C products, finance, education and any brand whose customers compare options and ask for recommendations before they buy."),
          ("How quickly can you launch Reddit ads?", "Once we understand your goals and audience, we set up tracking, write Reddit-native creative and launch — then optimise weekly. Book a 30-minute intro call to start.")],
    related=["chatgpt-ads-agency-india", "insights/reddit-ads-cost-india", "meta-ads-agency-indore", "social-media-marketing-agency-indore"],
    sources=[S_SAMOSA, S_E4M_REDDIT, S_AIMERS, S_STACKMATIX, S_TRILOKANA],
)

# =====================================================================
# 3. Social media marketing (local core)
# =====================================================================
page(
    slug="social-media-marketing-agency-indore", kind="service", group="Content & Social",
    title="Social Media Marketing Agency in Indore | Akarsa Studio",
    desc="Instagram, Facebook, YouTube & LinkedIn management in Indore: content calendars, reels, UGC, community and paid social. Trusted by 20+ brands.",
    nav_label="Social Media Marketing",
    eyebrow="Social media marketing", h1="Social Media Marketing Agency in Indore",
    lead="Content that stops the scroll, built into a system that brings enquiries — not just likes.",
    answer="Akarsa Studio is a social media marketing agency in Vijay Nagar, Indore. We plan, create and manage content for Instagram, Facebook, YouTube and LinkedIn — reels, UGC, carousels and community — and pair it with paid social so your posts turn into real enquiries.",
    visual=reels(["/assets/clients/reels/chirmi.jpg", "/assets/clients/reels/burger-singh.jpg", "/assets/clients/reels/dukes-table.jpg"], "#ffe6cf", True,
                 ["Chirmi social media reel by Akarsa Studio", "Burger Singh social media reel by Akarsa Studio", "The Duke’s Table social media reel by Akarsa Studio"]),
    wa=WA + "social media marketing.", cta_label="Get a social media plan",
    service_type="Social media marketing",
    sections=[
        ("Posting isn’t growth. Systems are.", '''<p>Most brands post every day and still don’t grow, because posting without a system is just noise. We build a social media <b>system</b>: a clear content strategy, hooks designed for how people actually scroll, a consistent calendar, community replies, and paid boosts on the posts that prove themselves.</p>
<p>It’s the same approach we use for cafés and restaurants like <b>Burger Singh</b>, <b>Chirmi</b> and <b>The Duke’s Table</b>, retail and fashion brands like <b>Adidas</b>, <b>Decathlon</b> and <b>The Korean Trends</b>, and fitness brands like <b>Olympia Fitness Gym</b>.</p>'''),
        ("Platforms we manage", '''<div class="pills"><span>Instagram</span><span>Facebook</span><span>YouTube &amp; Shorts</span><span>LinkedIn</span><span>X</span><span>Pinterest</span></div>
<p>Most Indore businesses win on Instagram and YouTube Shorts first; B2B brands add LinkedIn. We recommend the mix after looking at where your customers actually spend time.</p>'''),
    ],
    cards=[("Strategy & calendar", "A monthly content plan built around your offers, seasons and what your audience engages with."),
           ("Reels & short-form", "Scripted, shot and edited reels with hooks designed for the first second."),
           ("UGC & creators", "Authentic creator content that feels native to the feed."),
           ("Copy & captions", "Captions, carousels and stories that make people act — not just scroll past."),
           ("Community management", "Replies to comments and DMs so every interested follower gets an answer."),
           ("Paid social", "Meta ads on proven posts to turn reach into enquiries, tracked to the lead.")],
    steps=[("Audit", "Your profiles, competitors and audience."), ("Plan", "Content pillars, calendar and hooks."), ("Create", "Reels, UGC, carousels and stories."), ("Grow", "Publish, engage, boost and report monthly.")],
    faqs=[("How much does social media marketing cost in Indore?", "It depends on the platforms, how many reels and posts you need each month, whether we shoot on location, and your ad budget. We offer tailored monthly plans — book a 30-minute intro call and we’ll send a proposal."),
          ("How many posts and reels will I get each month?", "We set the volume in your plan based on your goals and budget. Consistency matters more than volume, so we prioritise a calendar you can sustain with content that performs."),
          ("Do you shoot content or do we need to provide it?", "We handle everything — strategy, scripting, shooting, editing and posting. If you already have photos or videos, we can improve and repurpose them."),
          ("Which social media platforms do you manage?", "Instagram, Facebook, YouTube and Shorts, LinkedIn, X and Pinterest. We recommend the right mix for your audience."),
          ("How long before social media marketing shows results?", "Most brands see early traction in the first one to three months. Lasting growth comes from consistency, testing and doubling down on what your audience loves."),
          ("Do you also run social media ads?", "Yes. We pair organic content with Meta ads so your best-performing posts reach more of the right people — see our Meta ads agency page.")],
    related=["meta-ads-agency-indore", "ugc-video-production-agency", "influencer-marketing-agency-indore", "digital-marketing-agency-vijay-nagar-indore"],
    sources=[],
)

# =====================================================================
# 4. Meta ads (local core + "meta ads cost" demand)
# =====================================================================
page(
    slug="meta-ads-agency-indore", kind="service", group="Ads",
    title="Meta Ads Agency in Indore | Facebook & Instagram Ads",
    desc="Facebook & Instagram ads from Indore that cut cost per lead. Real result: ₹30K turned into 52 enquiries at ₹577 each. Strategy, creative, tracking.",
    nav_label="Meta Ads",
    eyebrow="Meta ads · Facebook & Instagram", h1="Meta Ads Agency in Indore",
    lead="Facebook and Instagram campaigns built around one number: what it costs you to get a real enquiry.",
    answer="Akarsa Studio is a Meta ads agency in Indore that runs Facebook and Instagram campaigns for leads and sales. In one campaign, ₹30,000 of ad spend produced 52 enquiries — cost per enquiry fell from ₹7,500 to ₹577, about 13× lower.",
    visual=reels(["/assets/instagram/r05.jpg", "/assets/instagram/r03.jpg", "/assets/instagram/r11.jpg"], "#1c1917", False,
                 ["Akarsa Studio reel: Are Meta ads a waste of money?", "Meta Ads case study: ₹30K turned into 52 enquiries", "Akarsa Studio reel: Spent ₹40,000 and got zero clients?"]),
    wa=WA + "Meta (Facebook & Instagram) ads.", cta_label="Book an intro call",
    service_type="Facebook and Instagram advertising",
    sections=[
        ("Real results from our Meta ads", kpis([("3.7×", "total purchase ROAS"), ("196", "purchases in 32 days"), ("₹381", "per purchase")]) +
            '<p>An Indian e-commerce brand, 6 Sep–7 Oct 2026, straight from the client’s Meta Ads Manager. <a href="/results">See every number, chart and the maths →</a></p>'),
        ("Real result: ₹30K → 52 enquiries", '''<div class="facts"><table>
<tr><th>Ad spend</th><td>₹30,000</td></tr><tr><th>Enquiries</th><td>52</td></tr>
<tr><th>Cost per enquiry before</th><td>₹7,500</td></tr><tr><th>Cost per enquiry after</th><td>₹577</td></tr>
<tr><th>Improvement</th><td>About 13× lower cost per enquiry</td></tr></table></div>
<p>Read the full <a href="/case-studies/meta-ads-30k-52-enquiries">Meta ads case study</a> or watch the breakdown on <a href="https://www.instagram.com/akarsa_studio/reel/DeEImQ5OMDT/" target="_blank" rel="noopener">Instagram</a>.</p>'''),
        ("How much do Meta ads cost in India?", '''<p>Third-party benchmarks put Meta ads in India at roughly <b>₹50–₹120 CPM</b>, <b>₹8–₹25 per click</b> and <b>₹150–₹400 per lead</b> for many categories — with real estate (₹600–₹1,200) and finance (₹350–₹700) costing more. Your cost depends on industry, offer, creative and audience. See our detailed <a href="/insights/meta-ads-cost-india">Meta ads cost in India guide</a>.</p>'''),
    ],
    cards=[("Account audit", "We find where your current spend leaks — audiences, creative, tracking and funnel."),
           ("Offer & funnel", "A clear reason to enquire, plus lead forms, WhatsApp ads or landing pages that convert."),
           ("Scroll-stopping creative", "Reels, statics and UGC made in-house and tested in rounds."),
           ("Audience strategy", "Broad, interest and lookalike audiences tested against each other — no guesswork."),
           ("Pixel & Conversions API", "Accurate tracking so Meta optimises for real leads, not cheap clicks."),
           ("Weekly optimisation", "Budget moved to the ads and audiences with the lowest cost per enquiry.")],
    steps=[("Audit", "Spend, tracking and creative."), ("Rebuild", "Offer, audiences and funnel."), ("Test", "Creative rounds and A/B tests."), ("Scale", "More budget on what lowers cost per lead.")],
    faqs=[("What results can Meta ads deliver?", "In one of our campaigns, ₹30,000 of spend produced 52 enquiries and cut cost per enquiry from ₹7,500 to ₹577. Results vary by industry and offer, which is why we start with an audit."),
          ("How much do Meta ads cost in India?", "Third-party benchmarks suggest about ₹50–₹120 per 1,000 impressions, ₹8–₹25 per click and ₹150–₹400 per lead in many categories. Competitive industries like real estate and finance cost more."),
          ("What are your Meta ads service charges?", "We price management based on your ad budget and scope (creative volume, platforms, landing pages). Book a 30-minute intro call for a tailored proposal."),
          ("Do you create the ad creative?", "Yes. Our team writes, designs, shoots and edits ad creative — reels, statics and UGC — and tests new rounds every month."),
          ("Can you run WhatsApp ads?", "Yes. Click-to-WhatsApp campaigns are often the fastest way for Indian businesses to turn ad clicks into conversations."),
          ("Do you only work with businesses in Indore?", "No. We’re based in Vijay Nagar, Indore, and run Meta ads for brands across India.")],
    related=["case-studies/meta-ads-30k-52-enquiries", "insights/meta-ads-cost-india", "google-ads-agency-indore", "social-media-marketing-agency-indore"],
    sources=[S_OWL_IN, S_SOTROS, S_CASE_REEL],
)

# =====================================================================
# 5. Google ads
# =====================================================================
page(
    slug="google-ads-agency-indore", kind="service", group="Ads",
    title="Google Ads Agency in Indore | Search, YouTube & PMax",
    desc="Google Search, Performance Max and YouTube ads managed from Indore — keyword research, ad copy, conversion tracking and weekly optimisation.",
    nav_label="Google Ads",
    eyebrow="Google ads", h1="Google Ads Agency in Indore",
    lead="Show up at the exact moment someone searches for what you sell.",
    answer="Akarsa Studio manages Google Ads for businesses in Indore and across India — Search, Performance Max, Display and YouTube campaigns — with keyword research, conversion tracking and weekly optimisation focused on lowering your cost per lead.",
    visual=GOOGLE_MOCK, wa=WA + "Google Ads.", cta_label="Get a Google Ads plan",
    service_type="Google Ads management",
    sections=[
        ("Search intent beats interruption", '''<p>Google Ads reach people who are already looking — “website design company in Indore”, “gym near me”, “best café in Vijay Nagar”. That intent makes search one of the most efficient lead channels for local businesses, as long as the account is built tightly: the right keywords, negative keywords, relevant ads and accurate conversion tracking.</p>
<p>We combine Google with <a href="/meta-ads-agency-indore">Meta</a>, <a href="/reddit-ads-agency-india">Reddit</a> and <a href="/chatgpt-ads-agency-india">ChatGPT ads</a> so budget flows to the channel with the lowest cost per enquiry.</p>'''),
    ],
    cards=[("Keyword research", "Real search terms your customers use, with competition and cost estimates."),
           ("Search campaigns", "Tightly themed ad groups, strong ad copy and negative keywords that stop wasted spend."),
           ("Performance Max", "Google’s AI campaigns fed with the right signals and creative."),
           ("YouTube ads", "Short video ads that build demand and retarget warm audiences."),
           ("Conversion tracking", "GA4 and Google Ads conversions for calls, forms and WhatsApp clicks."),
           ("Weekly optimisation", "Search-term reviews, bid strategy tuning and budget shifts every week.")],
    steps=[("Research", "Keywords, competitors and budget forecast."), ("Build", "Campaigns, ads and tracking."), ("Launch", "Controlled spend with clear goals."), ("Optimise", "Cut waste, scale winners.")],
    faqs=[("How much do Google Ads cost in Indore?", "You pay per click, and the price depends on how competitive each keyword is. We forecast costs during research using Google’s keyword data, then set a budget around your target cost per lead."),
          ("Google Ads or Meta ads — which is better?", "Google captures existing demand from people searching; Meta creates demand by reaching people as they scroll. Most businesses get the best results using both, with budget shifted to whichever delivers cheaper enquiries."),
          ("How fast do Google Ads bring leads?", "Search campaigns can bring enquiries within days of launch. The first few weeks are spent refining keywords and bids to bring the cost per lead down."),
          ("Do you run YouTube ads?", "Yes — YouTube in-stream and Shorts ads for awareness and retargeting, using creative our team produces."),
          ("Can you target only my area of Indore?", "Yes. Google Ads supports location targeting down to a radius around your business, so you only pay for searches from people who can actually visit or order."),
          ("Will you set up conversion tracking?", "Always. We track calls, form fills and WhatsApp clicks so you can see exactly what each rupee returns.")],
    related=["meta-ads-agency-indore", "website-development-company-indore", "chatgpt-ads-agency-india", "digital-marketing-agency-vijay-nagar-indore"],
    sources=[],
)

# =====================================================================
# 6. Website development
# =====================================================================
page(
    slug="website-development-company-indore", kind="service", group="Brand & Web",
    title="Website Development Company in Indore | Akarsa Studio",
    desc="Fast, SEO-ready websites designed and built in Indore — business sites, landing pages, e-commerce and ongoing website management.",
    nav_label="Website Development",
    eyebrow="Website design & development", h1="Website Development Company in Indore",
    lead="Websites that load fast, rank on Google, and turn visitors into WhatsApp enquiries.",
    answer="Akarsa Studio designs and develops websites in Indore — business websites, landing pages and e-commerce stores — built to load fast, rank on Google and convert visitors into enquiries. We also manage websites after launch: updates, security and performance.",
    visual=BROWSER_MOCK, wa=WA + "a new website.", cta_label="Plan my website",
    service_type="Website design and development",
    sections=[
        ("What every Akarsa website includes", '''<ul class="ticks">
<li><b>Mobile-first design</b> — most Indian visitors arrive on a phone, so we design for it first.</li>
<li><b>Speed &amp; Core Web Vitals</b> — fast loading, stable layouts and smooth interaction.</li>
<li><b>Technical SEO built in</b> — clean structure, meta tags, sitemaps and structured data (the same setup this site uses).</li>
<li><b>AI-search ready</b> — llms.txt, crawlable content and clear facts so ChatGPT, Gemini and Perplexity can understand and cite you.</li>
<li><b>Lead capture</b> — WhatsApp buttons, forms and tracking connected to your ads.</li>
<li><b>Analytics</b> — see where visitors come from and what they do.</li>
</ul>'''),
        ("See our work: this website", '''<p>The site you’re on was designed, animated, built and optimised by our team — scroll effects, a custom identity, structured data, and an llms.txt file for AI search. If you like how it feels, we can build yours the same way.</p>'''),
    ],
    cards=[("Business websites", "A complete online home for your brand with services, proof and contact."),
           ("Landing pages", "Focused pages for ads that turn clicks into enquiries."),
           ("E-commerce stores", "Online stores on Shopify or custom builds, ready to sell."),
           ("Redesigns", "Modernise an old site without losing your Google rankings."),
           ("Website management", "Updates, security, backups and performance — handled every month."),
           ("SEO & content", "Pages written to rank for what your customers search.")],
    steps=[("Discover", "Goals, audience and the pages you need."), ("Design", "Look, feel and content structure."), ("Build", "Fast, SEO-ready code with tracking."), ("Launch & grow", "Go live, then manage and improve.")],
    faqs=[("How much does a website cost in Indore?", "It depends on the number of pages, features (like e-commerce or booking) and content needed. Book a 30-minute intro call, tell us what you need, and we’ll send a fixed proposal."),
          ("How long does it take to build a website?", "A focused landing page can go live quickly; a full business website or store takes longer depending on pages and content. We share a timeline with every proposal."),
          ("Will my website be SEO-friendly?", "Yes. Every site ships with technical SEO, structured data, a sitemap and fast performance — and it’s ready for AI search engines too."),
          ("Can I update the website myself?", "Yes. We can build on a platform you can edit, or manage updates for you as part of website management."),
          ("Do you redesign existing websites?", "Yes. We redesign while preserving your URLs and rankings so you don’t lose existing Google traffic."),
          ("Do you provide website management after launch?", "Yes — updates, security, backups, speed checks and content changes every month.")],
    related=["branding-agency-indore", "google-ads-agency-indore", "about", "digital-marketing-agency-vijay-nagar-indore"],
    sources=[],
)

# =====================================================================
# 7. Branding
# =====================================================================
page(
    slug="branding-agency-indore", kind="service", group="Brand & Web",
    title="Branding Agency in Indore | Logo & Brand Identity Design",
    desc="Brand identity, logo design and graphic design from Indore — visual systems that make your brand simple, beautiful and unmistakably yours.",
    nav_label="Branding & Logo Design",
    eyebrow="Branding · logo design", h1="Branding Agency in Indore",
    lead="Identities with a point of view — designed to be remembered, not just recognised.",
    answer="Akarsa Studio is a branding agency in Indore that creates brand identities, logos and graphic design systems. We turn complex ideas into visual languages that are simple, beautiful and unmistakably yours — and apply them across social media, packaging and websites.",
    visual=BRAND_MOCK, wa=WA + "branding and logo design.", cta_label="Start my brand",
    service_type="Brand identity and logo design",
    sections=[
        ("Your brand doesn’t have a design problem. It has a thinking problem.", '''<p>That’s the idea behind our live sessions, and it’s how we design: strategy first, pixels second. Before a single logo sketch, we define who you serve, what you stand for and how you should sound. The visual identity then expresses that clearly — so every post, package and page feels like the same brand.</p>'''),
    ],
    cards=[("Brand strategy", "Positioning, audience and personality — the foundation every design decision rests on."),
           ("Logo design", "A distinctive mark that works from a favicon to a billboard."),
           ("Visual identity", "Colour, typography, graphic elements and imagery rules."),
           ("Brand guidelines", "A brand book so your team and partners apply it consistently."),
           ("Graphic design", "Social templates, menus, brochures and packaging."),
           ("Brand launch", "Rolling the new identity out across social media and your website.")],
    steps=[("Discover", "Strategy, audience and competitors."), ("Explore", "Concepts and directions."), ("Refine", "Revisions to a final identity."), ("Deliver", "Files, guidelines and rollout.")],
    faqs=[("How much does logo design cost in Indore?", "It depends on whether you need a logo only or a complete brand identity with guidelines. Book a 30-minute intro call to share your brief, and we’ll send a proposal."),
          ("What’s included in a brand identity?", "Typically a logo suite, colour palette, typography, graphic elements, imagery direction and a brand guidelines document, plus templates for social media."),
          ("How many revisions do I get?", "Our Brand Launch package includes two revision rounds, so you can refine the direction until it feels right."),
          ("Which files will I receive?", "Vector and web-ready files of your logo in every colour version, plus your colour and font specifications and guidelines."),
          ("Do you do rebranding?", "Yes. We refresh or rebuild identities while keeping the recognition you’ve already earned."),
          ("Can you design packaging and social media templates?", "Yes — packaging, menus, brochures and ready-to-use social media templates that match your new identity.")],
    related=["website-development-company-indore", "social-media-marketing-agency-indore", "about", "ugc-video-production-agency"],
    sources=[],
)

# =====================================================================
# 8. Influencer marketing
# =====================================================================
page(
    slug="influencer-marketing-agency-indore", kind="service", group="Content & Social",
    title="Influencer Marketing Agency in Indore | Akarsa Studio",
    desc="Creator and influencer campaigns from Indore — creator discovery, briefs, content approvals and performance tracking for brands across India.",
    nav_label="Influencer Marketing",
    eyebrow="Influencer marketing", h1="Influencer Marketing Agency in Indore",
    lead="Creators who genuinely fit your brand — and campaigns measured on results, not follower counts.",
    answer="Akarsa Studio is an influencer marketing agency in Indore that finds the right creators, briefs them, manages content and approvals, and tracks results. We choose creators by audience fit and engagement — not just follower count — for brands in Indore and across India.",
    visual=reels(["/assets/clients/reels/kahani.jpg", "/assets/clients/reels/7th-heaven.jpg"], "#ebe3ff", True,
                 ["Kahani social media reel by Akarsa Studio", "7th Heaven social media reel by Akarsa Studio"]),
    wa=WA + "influencer marketing.", cta_label="Plan a creator campaign",
    service_type="Influencer marketing",
    sections=[
        ("Fit beats follower count", '''<p>Influencer campaigns fail when creators are chosen by follower count alone. We look at who actually follows a creator, how they engage, and whether the creator’s style suits your brand. Then we brief creators clearly, review content before it goes live, and track what each collaboration delivers.</p>
<p>The best-performing creator content often becomes your best ad creative too — we can run it through <a href="/meta-ads-agency-indore">Meta ads</a> to reach far more people.</p>'''),
    ],
    cards=[("Creator discovery", "Micro and macro creators matched to your audience and city."),
           ("Briefs & scripts", "Clear briefs that keep content authentic and on-message."),
           ("Contracts & usage", "Deliverables, timelines and content usage rights agreed upfront."),
           ("Content approvals", "Review before publishing so every post meets your standards."),
           ("Amplification", "Boost the best creator content as ads for more reach."),
           ("Reporting", "Reach, engagement, clicks and enquiries per creator.")],
    steps=[("Define", "Goals, audience and budget."), ("Match", "Shortlist creators by fit and engagement."), ("Create", "Brief, review and publish."), ("Measure", "Report and reuse winners as ads.")],
    faqs=[("How much does influencer marketing cost in Indore?", "It depends on the number and size of creators, deliverables and usage rights. Local micro-creators are very cost-effective; we build a plan around your budget."),
          ("Micro or macro influencers — which is better?", "Micro-influencers usually deliver higher engagement and trust for local and niche brands; macro creators deliver reach. Many campaigns combine both."),
          ("How do you find the right influencers?", "We assess audience location, engagement quality, content style and past brand work, not just follower counts."),
          ("What’s the difference between UGC and influencer marketing?", "Influencers post to their own audience; UGC creators make content for your brand to post or use in ads. We offer both — see our UGC page."),
          ("How do you measure influencer campaign results?", "With tracked links, discount codes and WhatsApp enquiries per creator, alongside reach and engagement."),
          ("Do you work with creators outside Indore?", "Yes. We run creator campaigns across India.")],
    related=["ugc-video-production-agency", "social-media-marketing-agency-indore", "meta-ads-agency-indore", "digital-marketing-agency-vijay-nagar-indore"],
    sources=[],
)

# =====================================================================
# 9. UGC & short-form
# =====================================================================
page(
    slug="ugc-video-production-agency", kind="service", group="Content & Social",
    title="UGC & Reels Production Agency in India | Akarsa Studio",
    desc="Scroll-stopping reels, UGC ads and short-form edits from Indore — hooks, scripts, shooting, editing and motion for Instagram, YouTube Shorts and ads.",
    nav_label="UGC & Reels Production",
    eyebrow="UGC · reels · video editing", h1="UGC & Reels Production Agency",
    lead="Short-form video built to hook in the first second and hold attention till the last.",
    answer="Akarsa Studio produces UGC videos, reels and short-form edits from Indore for brands across India — hooks, scripting, creators, shooting, editing and motion graphics — made for Instagram Reels, YouTube Shorts and paid ads.",
    visual=reels(["/assets/instagram/r06.jpg", "/assets/instagram/r02.jpg", "/assets/instagram/r12.jpg"], "#2a1b4d", False,
                 ["Akarsa Studio talking-head short-form video", "Akarsa Studio reel: Your marketing is a lie", "Akarsa Studio short film reel"]),
    wa=WA + "UGC and reels production.", cta_label="Get reels that perform",
    service_type="UGC and short-form video production",
    sections=[
        ("What is UGC content?", '''<p><b>UGC (user-generated content)</b> is video or photo content that looks and feels like it was made by a real customer — a creator talking to camera, an unboxing, a review — rather than a polished ad. Brands use UGC on their own pages and in paid ads because it feels native to the feed and builds trust faster than traditional creative.</p>'''),
        ("Hook-first, made for how people scroll", '''<p>Every video we make starts with the hook: the first second decides whether anyone watches the rest. We script hooks, test variations, and edit for pace, captions and sound — the same craft behind our own reels like “Your marketing is a lie” and “Posting ≠ Growth”.</p>'''),
    ],
    cards=[("Hooks & scripts", "Opening lines and story structures designed to stop the scroll."),
           ("UGC creators", "Real creators matched to your audience for authentic content."),
           ("Shooting", "On-location shoots in Indore for cafés, gyms, stores and brands."),
           ("Editing & captions", "Fast-paced edits with captions, sound design and pacing."),
           ("Motion & animation", "Animated graphics, product explainers and branded intros."),
           ("Ad versions", "Cut-downs and variations for Meta, YouTube and Reddit ads.")],
    steps=[("Plan", "Content ideas and hooks."), ("Shoot", "Creators or on-location shoots."), ("Edit", "Cuts, captions, sound and motion."), ("Test", "Publish, measure and iterate.")],
    faqs=[("What is UGC content?", "UGC (user-generated content) is content that looks like it was made by a real customer — reviews, unboxings, talking-to-camera videos. Brands use it organically and in ads because it feels authentic and builds trust."),
          ("How much does UGC video production cost in India?", "It depends on the number of videos, whether creators appear on camera, shooting needs and usage rights. We create a plan around your monthly content needs."),
          ("Do you provide the creators?", "Yes. We source and brief creators who match your audience, or we can work with your team on camera."),
          ("Can you edit our existing footage?", "Yes. Video editing is a standalone service — send your raw footage and we’ll turn it into reels and ads."),
          ("How many reels can you produce per month?", "Volume is set in your plan. We recommend a sustainable cadence with enough variations to test hooks."),
          ("Who owns the content and usage rights?", "Usage rights are agreed upfront in every project, including paid-ad usage for creator content.")],
    related=["social-media-marketing-agency-indore", "influencer-marketing-agency-indore", "meta-ads-agency-indore", "reddit-ads-agency-india"],
    sources=[],
)

# =====================================================================
# 10. Vijay Nagar location page
# =====================================================================
page(
    slug="digital-marketing-agency-vijay-nagar-indore", kind="service", group="Location",
    title="Digital Marketing Agency in Vijay Nagar, Indore | Akarsa",
    desc="Visit Akarsa Studio at Shagun Arcade, near Vijay Nagar Square, Indore — social media, Meta, Google, Reddit & ChatGPT ads, branding and websites.",
    nav_label="Vijay Nagar, Indore",
    eyebrow="Vijay Nagar · Indore", h1="Digital Marketing Agency in Vijay Nagar, Indore",
    lead="A local team in the heart of Vijay Nagar — working with brands across Indore and India.",
    answer="Akarsa Studio is a digital marketing agency in Vijay Nagar, Indore, at Office No. 702, Shagun Arcade, Main Rd, near Apna Sweets, PU 4, near Vijay Nagar Square. We help businesses grow with social media, Meta, Google, Reddit and ChatGPT ads, branding and websites.",
    visual=ADDRESS_CARD, wa=WA + "working with your Vijay Nagar team.", cta_label="Meet the team",
    service_type="Digital marketing",
    sections=[
        ("Everything your business needs, from one studio", '''<div class="svc-links">
<a href="/social-media-marketing-agency-indore">Social media marketing</a><a href="/meta-ads-agency-indore">Meta ads</a>
<a href="/google-ads-agency-indore">Google ads</a><a href="/reddit-ads-agency-india">Reddit ads</a>
<a href="/chatgpt-ads-agency-india">ChatGPT ads</a><a href="/ugc-video-production-agency">UGC &amp; reels</a>
<a href="/influencer-marketing-agency-indore">Influencer marketing</a><a href="/branding-agency-indore">Branding &amp; logos</a>
<a href="/website-development-company-indore">Website development</a></div>'''),
        ("Built for Indore businesses", '''<p>We know what works in Indore because we work here. Our clients include cafés and restaurants like <b>Burger Singh</b>, <b>Chirmi</b>, <b>The Duke’s Table</b> and <b>Kahani</b>, fitness brands like <b>Olympia Fitness Gym</b>, retail and fashion brands like <b>The Korean Trends</b>, education brands like <b>Varenyam</b>, and national names like <b>Starbucks</b>, <b>Adidas</b> and <b>Decathlon</b>.</p>
<p>Whether you’re in Vijay Nagar, Palasia, AB Road, Nipania, Bhawarkua or anywhere else in Indore, we can meet at our studio or online.</p>'''),
    ],
    cards=[("Local know-how", "Campaigns shaped by what Indore customers search, scroll and buy."),
           ("One team, every channel", "Content, ads, branding and websites without juggling five vendors."),
           ("Real results", "₹30K turned into 52 enquiries on Meta ads — cost per enquiry down 13×."),
           ("Easy booking", "Book a 30-minute intro call online. Pick any weekday slot that suits you.")],
    steps=[("Book a call", "Pick a 30-minute slot online."), ("Meet", "At our Vijay Nagar studio or online."), ("Plan", "A clear roadmap and proposal."), ("Grow", "Launch, measure and scale.")],
    faqs=[("Where is Akarsa Studio located?", "Office No. 702, Shagun Arcade, Main Rd, near Apna Sweets, PU 4, near Vijay Nagar Square, Vijay Nagar, Indore, Madhya Pradesh 452010."),
          ("Can I meet the team in person?", "Yes. Book a 30-minute intro call online first, or call +91 81098 01383 to set up a meeting at our Vijay Nagar studio."),
          ("Which services do you offer in Indore?", "Social media marketing, UGC and reels, influencer marketing, Meta, Google, YouTube, Reddit and ChatGPT ads, branding and logo design, and website development and management."),
          ("Do you only work with Indore businesses?", "No. We’re based in Indore and work with brands across India."),
          ("Which industries do you work with?", "Cafés and restaurants, fitness, fashion and retail, education, events and flowers, D2C brands and national retail chains."),
          ("How do we get started?", "Book a 30-minute intro call. We’ll understand your goals, look at your current marketing and share a clear roadmap.")],
    related=["social-media-marketing-agency-indore", "meta-ads-agency-indore", "website-development-company-indore", "about"],
    sources=[],
)

# =====================================================================
# 11. Case study
# =====================================================================
page(
    slug="case-studies/meta-ads-30k-52-enquiries", kind="case", group="Proof",
    title="Meta Ads Case Study: ₹30K → 52 Enquiries | Akarsa Studio",
    desc="How a Meta ads lead campaign turned ₹30,000 into 52 enquiries and cut cost per enquiry from ₹7,500 to ₹577 — about 13× lower.",
    nav_label="Case study: ₹30K → 52 enquiries",
    eyebrow="Case study · Meta ads", h1="Meta Ads Case Study: ₹30K → 52 Enquiries",
    lead="One lead-generation campaign, two numbers that matter: what it cost, and what it returned.",
    answer="In this Meta ads lead-generation campaign, Akarsa Studio turned ₹30,000 of ad spend into 52 enquiries. Cost per enquiry fell from ₹7,500 to ₹577 — about 13 times lower — because the campaign was rebuilt around offers, creative and tracking rather than boosting posts.",
    visual=reels(["/assets/instagram/r03.jpg"], "#1c1917", False, ["Meta Ads case study: ₹30K turned into 52 enquiries"]),
    wa=WA + "getting results like your ₹30K → 52 enquiries case study.", cta_label="Get results like this",
    sections=[
        ("The results", '''<div class="facts"><table>
<tr><th>Platform</th><td>Meta (Facebook &amp; Instagram)</td></tr><tr><th>Objective</th><td>Lead generation (enquiries)</td></tr>
<tr><th>Ad spend</th><td>₹30,000</td></tr><tr><th>Enquiries</th><td>52</td></tr>
<tr><th>Cost per enquiry — before</th><td>₹7,500</td></tr><tr><th>Cost per enquiry — after</th><td>₹577</td></tr>
<tr><th>Change</th><td>≈ 13× lower cost per enquiry</td></tr></table></div>
<p class="src-note">Maths check: ₹30,000 ÷ 52 enquiries = ₹577 per enquiry. ₹7,500 ÷ ₹577 ≈ 13.</p>'''),
        ("Why the cost per enquiry fell so far", '''<p>A ₹7,500 cost per enquiry usually means money is going to the wrong people, the offer isn’t compelling, or Meta is optimising for the wrong signal. The fix isn’t a bigger budget — it’s a better system. Our standard rebuild for lead campaigns covers:</p>
<ul class="ticks">
<li><b>Offer clarity</b> — one clear reason to enquire now.</li>
<li><b>Creative in rounds</b> — several hooks and formats tested against each other.</li>
<li><b>Signal quality</b> — pixel and conversion tracking so Meta optimises for real enquiries, not cheap clicks.</li>
<li><b>Budget discipline</b> — spend moved to the ads with the lowest cost per enquiry every week.</li>
</ul>
<p>Watch the full breakdown on <a href="https://www.instagram.com/akarsa_studio/reel/DeEImQ5OMDT/" target="_blank" rel="noopener">our Instagram</a>.</p>'''),
    ],
    cards=[], steps=[],
    faqs=[("How many enquiries did ₹30,000 of Meta ads generate?", "52 enquiries, at an average cost of ₹577 per enquiry."),
          ("How much did the cost per enquiry improve?", "From ₹7,500 to ₹577 — roughly 13 times lower."),
          ("Can you get the same result for my business?", "Every industry and offer is different, so we never promise identical numbers. We start with an audit of your current spend and show where cost per lead can come down.")],
    related=["meta-ads-agency-indore", "insights/meta-ads-cost-india", "social-media-marketing-agency-indore", "chatgpt-ads-agency-india"],
    sources=[S_CASE_REEL],
)

# =====================================================================
# 11b. Real results (verified numbers)
# =====================================================================
page(
    slug="results", kind="case", group="Proof", published="2026-10-21", updated=("2026-10-21", "21 October 2026"),
    title="Meta Ads Results & ROAS: Real Numbers | Akarsa Studio",
    desc="Real Meta ads numbers from Ads Manager: 196 purchases at ₹381 each and 3.7× ROAS for an e-commerce brand, and 2.74× ROAS for an international store.",
    nav_label="Real results",
    eyebrow="Proof · Real numbers", h1="Real Meta Ads Results, in Numbers",
    lead="No mock-ups and no rounded-up claims. Every figure below comes from Meta Ads Manager, with the dates, the spend and the maths shown.",
    answer="For an Indian e-commerce brand, Akarsa Studio’s Meta ads produced 196 purchases from ₹74,600 of ad spend over 32 days (6 Sep–7 Oct 2026): ₹381 per purchase and a 3.7× total ROAS, about ₹2.74 lakh in tracked sales. For an international store, the same approach returned 2.74× ROAS.",
    visual=RESULTS_VISUAL,
    wa=WA + "results like the ones on your Real Results page.", cta_label="Book an intro call",
    sections=[
        ("How we check these numbers", '''<ul class="ticks">
<li><b>Client campaigns</b> come from the client’s own Meta Ads Manager, with the date range and attribution setting stated. Client and ad names are hidden for privacy.</li>
<li><b>Every derived number shows its maths</b>, so you can check it yourself. Ask us on a call and we’ll walk you through the live dashboards.</li>
</ul>'''),
        ("E-commerce brand: 196 purchases at ₹381 each", vsource("Client’s Meta Ads Manager · 5 ads in one campaign · 6 Sep–7 Oct 2026 · 7-day click attribution") +
            kpis([("3.7×", "total purchase ROAS"), ("196", "purchases in 32 days"), ("₹381", "average cost per purchase"), ("₹74,600", "ad spend")]) +
            '<div class="rgrid">' +
            bars("Purchase ROAS by ad", "Return on ad spend · higher is better", "ROAS",
                 [(a, r, f"{r:.1f}×", f"ROAS {r:.1f}× · ₹{s_:,} spent · {p} purchases") for a, p, s_, c, r, re_, f in sorted(RC_ADS, key=lambda x: -x[4])], best=0) +
            bars("Cost per purchase by ad", "What each sale cost in ads · lower is better", "Cost per purchase",
                 [(a, c, f"₹{c}", f"₹{c} per purchase · {p} purchases · ₹{s_:,} spent") for a, p, s_, c, r, re_, f in sorted(RC_ADS, key=lambda x: x[3])], best=0) +
            '</div>' + _rc_table() +
            '<p class="src-note">Maths check: ₹74,600 ÷ 196 purchases = ₹381 per purchase. Each ad’s spend × its ROAS, added up, comes to about ₹2.74 lakh of tracked sales: ₹2.74 lakh ÷ ₹74,600 = 3.68× total ROAS, shown rounded as 3.7×. Reach is shown per ad and not added up, because the same people can see more than one ad.</p>'),
        ("International e-commerce brand: 2.74× ROAS", vsource("Client’s Meta Ads Manager · ad-set view · USD account · website purchases") +
            kpis([("2.74×", "website purchase ROAS"), ("18", "website purchases"), ("$1,149", "purchase value"), ("$419", "ad spend")]) +
            bars("Purchase ROAS: the campaign’s top four ad sets", "Return on ad spend · higher is better", "ROAS",
                 [("Ad set 1", 9.07, "9.07×", "$15.32 spent → $139.00 · 4 purchases"), ("Ad set 2", 4.60, "4.60×", "$31.90 spent → $146.85 · 2 purchases"),
                  ("Ad set 3", 3.47, "3.47×", "$75.59 spent → $262.50 · 3 purchases"), ("Ad set 4", 2.06, "2.06×", "$129.94 spent → $268.04 · 5 purchases")], best=0) +
            '<p class="src-note">Maths check: $1,149.39 ÷ $419.39 = 2.74× for the whole campaign. The four ad sets above are the ones in the client’s report; the campaign had others, which is why its totals ($419.39 spent, 18 purchases) are higher than these four added together. The 9.07× ad set ran on a small $15 budget.</p>'),
        ("More proof", '<p>Read the full <a href="/case-studies/meta-ads-30k-52-enquiries">Meta ads case study: ₹30,000 → 52 enquiries</a>, where cost per enquiry fell from ₹7,500 to ₹577. Want numbers like these for your brand? Book a 30-minute intro call and we’ll show you where your ad spend can work harder.</p>'),
    ],
    cards=[], steps=[],
    faqs=[("What ROAS do Akarsa Studio’s Meta ads deliver?", "For an Indian e-commerce brand: a 3.7× total purchase ROAS over 32 days (6 Sep–7 Oct 2026), with 196 purchases from ₹74,600 of spend, or ₹381 per purchase. For an international store: 2.74× ROAS ($419 of ads → $1,149 in purchases). Results depend on your product, margins and offer, so we never promise fixed numbers."),
          ("Are these numbers real?", "Yes. Client figures come from the clients’ own Meta Ads Manager, with the date range and attribution setting stated. Every derived number shows its maths so you can check it."),
          ("How much does a lead cost with Akarsa’s Meta ads?", "It depends on industry, offer and budget. In our published lead campaign, cost per enquiry fell from ₹7,500 to ₹577. We estimate yours on an intro call."),
          ("Why are client names hidden?", "To protect our clients’ business data. We show the real figures, dates and settings, and can walk you through more detail on a call.")],
    related=["case-studies/meta-ads-30k-52-enquiries", "meta-ads-agency-indore", "insights/meta-ads-cost-india", "about"],
    sources=[],
)

# =====================================================================
# 12. About (entity page for GEO)
# =====================================================================
page(
    slug="about", kind="about", group="Company",
    title="About Akarsa Studio | AI-Driven Marketing Agency, Indore",
    desc="Akarsa Studio Private Limited is an AI-driven marketing agency in Indore founded by Ritik Sharma. Facts, services, clients, results and contact.",
    nav_label="About Akarsa Studio",
    eyebrow="About us", h1="About Akarsa Studio",
    lead="A rule-breaking, truth-seeking studio where art meets intelligence.",
    answer="Akarsa Studio (Akarsa Studio Private Limited) is an AI-driven marketing agency based in Vijay Nagar, Indore, India, founded by Ritik Sharma. It offers social media marketing, UGC and reels, influencer marketing, Meta, Google, YouTube, Reddit and ChatGPT ads, branding and website development, and has worked with 20+ brands including Starbucks, Adidas and Decathlon.",
    visual=ABOUT_VISUAL, wa=WA + "working with Akarsa Studio.", cta_label="Talk to us",
    sections=[
        ("Akarsa Studio at a glance", '''<div class="facts"><table>
<tr><th>Legal name</th><td>Akarsa Studio Private Limited</td></tr>
<tr><th>Brand</th><td>Akarsa (also written Ākarṣa)</td></tr>
<tr><th>What we are</th><td>An AI-driven, truth-seeking marketing agency — “where art meets intelligence”</td></tr>
<tr><th>Founder</th><td>Ritik Sharma, Founder &amp; Director</td></tr>
<tr><th>Headquarters</th><td>Office No. 702, Shagun Arcade, Main Rd, near Apna Sweets, PU 4, near Vijay Nagar Square, Vijay Nagar, Indore, Madhya Pradesh 452010, India</td></tr>
<tr><th>Office hours</th><td>Monday–Friday 11:00 am – 7:30 pm, Saturday 12:00 – 3:30 pm, Sunday closed</td></tr>
<tr><th>Phone / WhatsApp</th><td>+91 81098 01383</td></tr>
<tr><th>Website</th><td>https://www.akarsaone.xyz</td></tr>
<tr><th>Services</th><td>Social media marketing, UGC &amp; short-form video, video editing &amp; animation, influencer marketing, Meta ads, Google ads, YouTube ads, Reddit ads, ChatGPT ads, brand identity &amp; logo design, graphic design, website development &amp; management, AI marketing automation</td></tr>
<tr><th>Products</th><td>Akarsa One — AI business intelligence that finds buyers (3× qualified leads)</td></tr>
<tr><th>Clients</th><td>20+ brands including Starbucks, Adidas, Decathlon, Burger Singh, Chirmi, The Duke’s Table, Olympia Fitness Gym, The Korean Trends, Mayaram’s Farm, Bake Affaire, Nomad Pizza, The Crush Coffee, Nothing Before Coffee, Kunafa Bytes, Lokal, Urban Theka, Kahani, Mudoven, 7th Heaven, Varenyam, Zhanna Events &amp; Flowers and Fleuristry</td></tr>
<tr><th>Notable result</th><td>Meta ads: ₹30,000 → 52 enquiries; cost per enquiry ₹7,500 → ₹577</td></tr>
<tr><th>Offers</th><td>Spend more than $1,000 on Reddit ads with us and Reddit assigns a dedicated team from Reddit to your brand</td></tr>
<tr><th>Social</th><td>Instagram @akarsa_studio · YouTube @AkarsaStudio · Facebook · Pinterest /beakarsa</td></tr>
</table></div>'''),
        ("What we believe", '''<p><b>We don’t sell illusions. We engineer impact.</b> Akarsa isn’t built on routine — we question what feels ordinary, combine creativity with data and intelligence, and create what others hesitate to imagine.</p>
<ul class="ticks"><li><b>Truth over illusions</b> — no fake followers, no vanity metrics, no empty promises.</li>
<li><b>AI assists. Emotion leads.</b> — AI sharpens every decision; human insight makes the work matter.</li>
<li><b>Posting isn’t growth. Systems are.</b> — strategy, content, ads and data working together.</li></ul>'''),
        ("Meet the founder", '''<p><b>Ritik Sharma</b> is the Founder &amp; Director of Akarsa Studio and the host of <b>Akarsa Live</b>, our live sessions on brand and marketing thinking — including “Your brand doesn’t have a design problem. It has a thinking problem.” with brand strategist and photographer Malhar Chaudhari.</p>'''),
    ],
    cards=[], steps=[],
    faqs=[("What is Akarsa Studio?", "Akarsa Studio is an AI-driven marketing agency in Vijay Nagar, Indore, India. It creates content, runs ads, builds brands and develops websites for businesses across India."),
          ("Who founded Akarsa Studio?", "Ritik Sharma, who is the Founder & Director and hosts Akarsa Live."),
          ("Where is Akarsa Studio based?", "Office No. 702, Shagun Arcade, Main Rd, near Vijay Nagar Square, Vijay Nagar, Indore, Madhya Pradesh 452010."),
          ("Which brands has Akarsa Studio worked with?", "More than 20, including Starbucks, Adidas, Decathlon, Burger Singh, Chirmi, The Duke’s Table and Olympia Fitness Gym.")],
    related=["digital-marketing-agency-vijay-nagar-indore", "case-studies/meta-ads-30k-52-enquiries", "social-media-marketing-agency-indore", "chatgpt-ads-agency-india"],
    sources=[],
)

# =====================================================================
# 13–15. Insights (informational — AEO/GEO magnets)
# =====================================================================
page(
    slug="insights/chatgpt-ads-india-guide", kind="article", group="Insights",
    title="ChatGPT Ads in India (2026): Launch, Cost & How to Start",
    desc="Everything Indian businesses need to know about ChatGPT ads: launch date, who sees them, ₹725/day minimum budget, rules, and how to start.",
    nav_label="ChatGPT ads in India: 2026 guide",
    eyebrow="Guide · ChatGPT ads", h1="ChatGPT Ads in India (2026): Launch Date, Cost, Eligibility & How to Start",
    lead="A plain-English guide for Indian businesses, with sources.",
    answer="ChatGPT ads launched in India on 27 August 2026. They show below ChatGPT’s answers to logged-in adults on the Free and Go plans, are clearly labelled, and never appear for users under 18 or next to sensitive topics. Businesses can buy them self-serve through ChatGPT Ads Manager, open since 4 September 2026, with daily budgets from ₹725.",
    takeaways=["Launched in India: 27 August 2026 (India is OpenAI’s second-largest market).", "Self-serve ChatGPT Ads Manager: open since 4 September 2026.", "Minimum daily budget: ₹725.", "Shown to logged-in adults on Free and Go plans; paid plans are ad-free.", "Ads sit below answers, are labelled, and don’t change ChatGPT’s responses.", "Launch agency partners: WPP and Omnicom (non-exclusive)."],
    sections=[
        ("When did ChatGPT ads launch in India?", "<p>OpenAI began rolling out ChatGPT ads in India on <b>27 August 2026</b>, about six months after it started testing ads in the US. Outlook Business describes India as OpenAI’s second-largest market. More than 50 brands were expected to go live within the first week.</p>"),
        ("Who sees ChatGPT ads?", "<p>Ads are shown to <b>logged-in adults</b> on ChatGPT’s <b>Free</b> and <b>Go</b> plans. Users on Plus, Pro, Business, Enterprise and Education plans remain ad-free. Ads are never shown to users under 18.</p>"),
        ("Where do the ads appear, and do they affect answers?", "<p>Ads appear <b>below ChatGPT’s response</b> when a relevant sponsored product or service is available. They are clearly labelled and visually separated from the answer. OpenAI says ads <b>do not influence ChatGPT’s responses</b>, and advertisers only receive aggregate data such as impressions and clicks — never conversations, chat history, memories or personal details. Ads are also kept away from sensitive topics such as mental health and politics.</p>"),
        ("How much do ChatGPT ads cost in India?", "<p>Self-serve budgets start at <b>₹725 per day</b>. Reported bidding options include paying per thousand impressions and per click. As with any auction, your actual cost per lead depends on your category, offer and how relevant your ad is to the question being asked.</p>"),
        ("How to start advertising on ChatGPT", '''<ol class="steps-list">
<li><b>Pick the questions you want to win.</b> List the questions customers ask before buying from you — “best coaching centre for JEE in Indore”, “affordable website designer near me”.</li>
<li><b>Prepare an offer and a destination.</b> A landing page or WhatsApp flow that answers the question and makes the next step easy.</li>
<li><b>Set up ChatGPT Ads Manager.</b> Create the account, add billing and set a daily budget (from ₹725).</li>
<li><b>Install measurement.</b> Add the OpenAI Ads pixel and track lead events so you know your cost per enquiry.</li>
<li><b>Start small, then scale.</b> Learn which questions and ad copy convert, then move budget to them.</li></ol>'''),
        ("Is it worth it?", "<p>For most businesses, testing now is worth it. Early auctions are less crowded, and Redseer (cited by Inc42) estimates AI-native ad formats can deliver up to <b>4× the conversion rate</b> of conventional search and expects conversational assistants to take around <b>8% of digital advertising by 2030</b>. OpenAI reports ChatGPT Ads has reached a <b>$1 billion annualised revenue run rate</b> with tens of thousands of advertisers. Start with a small budget, measure cost per enquiry, and compare it with Meta and Google.</p>"),
    ],
    faqs=[("When did ChatGPT ads launch in India?", "On 27 August 2026. The self-serve ChatGPT Ads Manager opened on 4 September 2026."),
          ("What is the minimum budget for ChatGPT ads in India?", "Daily budgets start at ₹725."),
          ("Do ChatGPT Plus users see ads?", "No. Only logged-in adults on the Free and Go plans see ads; Plus, Pro, Business, Enterprise and Education are ad-free."),
          ("Can advertisers see my ChatGPT conversations?", "No. Advertisers only get aggregate data such as impressions and clicks."),
          ("Which agencies run ChatGPT ads in India?", "OpenAI named WPP and Omnicom as non-exclusive launch partners. Independent agencies like Akarsa Studio in Indore also plan and run ChatGPT ads for Indian businesses through the self-serve Ads Manager.")],
    related=["chatgpt-ads-agency-india", "insights/reddit-ads-cost-india", "insights/meta-ads-cost-india", "reddit-ads-agency-india"],
    sources=[S_INC42, S_E4M, S_OUTLOOK, S_CNBC, S_OPENAI, S_ICECUBE, S_UPGROWTH],
)

page(
    slug="insights/reddit-ads-cost-india", kind="article", group="Insights",
    title="Reddit Ads Cost in India (2026): CPC, CPM & Budgets",
    desc="What Reddit ads cost in India in 2026 — minimum budget, CPC and CPM benchmarks, targeting options, and when Reddit ads are worth it for Indian brands.",
    nav_label="Reddit ads cost in India (2026)",
    eyebrow="Guide · Reddit ads", h1="Reddit Ads Cost in India (2026): CPC, CPM, Budgets & Is It Worth It?",
    lead="Benchmarks, caveats and a practical way to test Reddit ads — with sources.",
    answer="Reddit ads have a minimum budget of $5 a day. Third-party 2026 estimates put typical CPCs around $0.50–$2.50 and CPMs around $3–$9 globally, and one 2025 India guide reported roughly ₹8–₹20 per click and ₹50–₹120 per 1,000 impressions. Reddit doesn’t publish official averages, so test with a small budget and measure your own cost per lead.",
    takeaways=["Minimum: $5/day; bids from about $0.20.", "Global 2026 estimates: CPC ~$0.50–$2.50, CPM ~$3–$9 (third-party).", "India (2025 guide): ~₹8–₹20 CPC, ~₹50–₹120 CPM.", "Fewer than 10% of large consumer brands in India run formal Reddit campaigns.", "Target by community, interest, keyword and location.", "Akarsa offer: spend $1,000+ with us and get a dedicated team from Reddit."],
    sections=[
        ("Reddit ads cost: the benchmarks", '''<div class="facts"><table>
<tr><th>Metric</th><td><b>Range</b></td></tr>
<tr><th>Minimum daily budget</th><td>$5 per day (bids from ~$0.20)</td></tr>
<tr><th>CPC — global, 2026</th><td>~$0.50–$2.50 (one source: median $1.25–$1.85)</td></tr>
<tr><th>CPM — global, 2026</th><td>~$3–$9 (wider estimates $0.50–$15)</td></tr>
<tr><th>CPC — India, 2025 guide</th><td>~₹8–₹20</td></tr>
<tr><th>CPM — India, 2025 guide</th><td>~₹50–₹120</td></tr></table></div>
<p class="src-note">These are third-party planning estimates (Aimers, Stackmatix, Trilokana). Reddit does not publish one official CPC; your real numbers depend on community, creative and competition.</p>'''),
        ("What drives your Reddit ad cost", '''<ul class="ticks"><li><b>Community competition</b> — popular subreddits in finance, tech and gaming cost more.</li>
<li><b>Targeting precision</b> — narrow community and keyword targeting raises CPM but often lowers cost per lead.</li>
<li><b>Creative fit</b> — ads that read like helpful posts earn more clicks, which lowers CPC.</li>
<li><b>Geography</b> — India-targeted campaigns usually cost less than US-targeted ones.</li></ul>'''),
        ("Are Reddit ads worth it for Indian brands?", "<p>Reddit is organised around interests rather than social connections, so people arrive with intent. It hosts more than 100,000 active communities, has launched Hindi and Bengali machine translation and Reddit Answers in India, and grew international advertising revenue by more than 80% year on year. Meanwhile, fewer than 10% of large consumer brands in India have activated formal Reddit campaigns — so early advertisers face less competition. For brands whose buyers research before purchasing (tech, D2C, finance, education, gaming), Reddit is worth testing.</p>"),
        ("How to test Reddit ads without wasting money", '''<ol class="steps-list"><li><b>Choose 3–5 communities</b> where your buyers ask questions.</li>
<li><b>Write Reddit-native creative</b> — helpful, honest, no ad-speak.</li><li><b>Install the Reddit Pixel</b> and track leads or sales.</li>
<li><b>Run a small test</b>, then compare cost per lead with Meta and Google.</li><li><b>Scale the winners</b> — or let a dedicated team do it.</li></ol>'''),
    ],
    faqs=[("What is the minimum budget for Reddit ads?", "Reddit’s stated minimum is $5 per day."),
          ("What is the average CPC for Reddit ads in India?", "One 2025 India guide reported roughly ₹8–₹20 per click. Global 2026 estimates range around $0.50–$2.50. Reddit doesn’t publish official averages."),
          ("Are Reddit ads cheaper than Meta ads?", "It depends on the category. Reddit often has less competition in India, but costs vary widely by community. Testing both is the only reliable comparison."),
          ("Can I target Indian users on Reddit?", "Yes. Reddit supports location targeting, alongside community, interest and keyword targeting."),
          ("Does Akarsa Studio run Reddit ads?", "Yes. Spend more than $1,000 on Reddit ads with Akarsa Studio and Reddit assigns a dedicated team from Reddit to your account, working alongside us to optimise and precisely target your campaigns.")],
    related=["reddit-ads-agency-india", "insights/chatgpt-ads-india-guide", "insights/meta-ads-cost-india", "meta-ads-agency-indore"],
    sources=[S_AIMERS, S_STACKMATIX, S_TRILOKANA, S_SAMOSA, S_E4M_REDDIT],
)

page(
    slug="insights/meta-ads-cost-india", kind="article", group="Insights",
    title="Meta Ads Cost in India (2026): CPM, CPC & Cost per Lead",
    desc="Meta (Facebook & Instagram) ads cost in India in 2026: CPM, CPC and cost-per-lead benchmarks by industry — plus real campaign data from Indore.",
    nav_label="Meta ads cost in India (2026)",
    eyebrow="Guide · Meta ads", h1="Meta Ads Cost in India (2026): CPM, CPC & Cost per Lead — With Real Campaign Data",
    lead="Benchmarks by industry, real numbers from our own campaign, and how to lower your cost per lead.",
    answer="Meta ads in India typically cost about ₹50–₹120 per 1,000 impressions and ₹8–₹25 per click, with cost per lead around ₹150–₹400 in many categories — higher in real estate (₹600–₹1,200) and finance (₹350–₹700), according to third-party benchmarks. In one Akarsa Studio campaign, ₹30,000 produced 52 enquiries at ₹577 each.",
    takeaways=["CPM: ~₹50–₹120 (third-party benchmarks).", "CPC: ~₹8–₹25 across most industries.", "Cost per lead: ~₹150–₹400; real estate ₹600–₹1,200; finance ₹350–₹700.", "Our data: ₹30,000 → 52 enquiries = ₹577 per enquiry (down from ₹7,500).", "Industry, offer and creative move costs more than averages do."],
    sections=[
        ("Meta ads cost in India: benchmarks", '''<div class="facts"><table>
<tr><th>Metric</th><td><b>Typical range in India</b></td></tr>
<tr><th>CPM (per 1,000 impressions)</th><td>~₹50–₹120</td></tr><tr><th>CPC (per click)</th><td>~₹8–₹25</td></tr>
<tr><th>Cost per lead — general</th><td>~₹150–₹400</td></tr></table></div>
<p class="src-note">Sources: OwlClaw (2025 benchmarks), Sotros Infotech (2026), Vaizle. Sources disagree widely; treat these as planning ranges.</p>'''),
        ("Cost per lead by industry", '''<div class="facts"><table>
<tr><th>Industry</th><td><b>Cost per lead (₹)</b></td></tr>
<tr><th>Healthcare</th><td>~180–380</td></tr><tr><th>Education</th><td>~200–450</td></tr>
<tr><th>Finance &amp; insurance</th><td>~350–700</td></tr><tr><th>Real estate</th><td>~600–1,200</td></tr></table></div>
<p class="src-note">Source: OwlClaw Meta ads benchmarks for India.</p>'''),
        ("Real campaign data: ₹30K → 52 enquiries", '''<p>Benchmarks are averages; your account is not. In one of our lead campaigns, <b>₹30,000</b> of spend produced <b>52 enquiries</b> — <b>₹577 per enquiry</b>, down from <b>₹7,500</b> before we rebuilt the campaign. See the <a href="/case-studies/meta-ads-30k-52-enquiries">full case study</a>.</p>'''),
        ("How much should you spend on Meta ads per month?", "<p>Start with a budget large enough to get meaningful data — enough conversions each week for Meta’s algorithm to learn — then scale what works. A practical way to set it: decide your target cost per lead, multiply by the number of leads you want each month, and test at a fraction of that until your cost per lead is proven.</p>"),
        ("How to lower your Meta ads cost per lead", '''<ul class="ticks"><li><b>Fix tracking first</b> — pixel and Conversions API so Meta optimises for leads, not clicks.</li>
<li><b>Lead with an offer</b> — a clear reason to enquire now.</li><li><b>Test creative in rounds</b> — hooks and formats matter more than targeting.</li>
<li><b>Use WhatsApp or instant forms</b> — fewer steps, more enquiries.</li><li><b>Move budget weekly</b> to the lowest cost per lead.</li></ul>'''),
    ],
    faqs=[("How much do Meta ads cost per day in India?", "You can start with a small daily budget, but the right amount depends on your target cost per lead and how many leads you need. Benchmarks suggest ₹8–₹25 per click and ₹150–₹400 per lead in many categories."),
          ("What is a good cost per lead on Meta ads in India?", "It varies by industry — around ₹150–₹400 in many categories, ₹600–₹1,200 in real estate. In one of our campaigns we achieved ₹577 per enquiry, down from ₹7,500."),
          ("Why is my Meta ads cost per lead so high?", "The usual causes are weak offers, untested creative and poor tracking that makes Meta optimise for the wrong action."),
          ("Are Meta ads worth it for small businesses in Indore?", "Yes, when campaigns are built around a clear offer, good creative and accurate tracking. Click-to-WhatsApp ads work especially well for local businesses."),
          ("Can Akarsa Studio manage my Meta ads?", "Yes. We’re a Meta ads agency in Indore running Facebook and Instagram campaigns for brands across India.")],
    related=["meta-ads-agency-indore", "case-studies/meta-ads-30k-52-enquiries", "insights/reddit-ads-cost-india", "insights/chatgpt-ads-india-guide"],
    sources=[S_OWL_IN, S_SOTROS, S_VAIZLE, S_CASE_REEL],
)

# =====================================================================
# Insights index (hub)
# =====================================================================
INSIGHTS_HUB = dict(
    slug="insights/", kind="hub", group="Insights",
    title="Marketing Insights & Guides | Akarsa Studio",
    desc="Data-backed guides on ChatGPT ads, Reddit ads and Meta ads costs in India — written by Akarsa Studio, an AI-driven marketing agency in Indore.",
    nav_label="Insights", eyebrow="Insights", h1="Marketing Insights & Guides",
    lead="Data-backed guides for Indian businesses — with real numbers and sources.",
    answer="Akarsa Studio publishes practical, sourced guides on new and proven ad platforms in India: ChatGPT ads, Reddit ads and Meta ads — including costs, benchmarks and real campaign data.",
)
