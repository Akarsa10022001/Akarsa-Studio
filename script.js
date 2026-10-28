/* =========================================================
   AKARSA STUDIO — interactions & motion
   ========================================================= */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const cfg = window.AKARSA || {};
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  scrollTo(0, 0);
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isTouch = matchMedia('(hover: none)').matches;

  /* ---------------- config wiring ---------------- */
  /* ---------------- booking: free audit call on Calendly (popup; the booking page itself if the widget can't load) ---------------- */
  const bookingUrl = cfg.booking || '';
  let calendly = null;
  const loadCalendly = () => calendly || (calendly = new Promise((resolve, reject) => {
    const css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'https://assets.calendly.com/assets/external/widget.css';
    document.head.appendChild(css);
    const js = document.createElement('script');
    js.src = 'https://assets.calendly.com/assets/external/widget.js';
    js.onload = () => (window.Calendly ? resolve(window.Calendly) : reject());
    js.onerror = reject;
    document.head.appendChild(js);
  }));
  // pause smooth scrolling while the popup is open, resume once Calendly removes its overlay
  const holdScroll = () => {
    window.__lenis?.stop();
    const mo = new MutationObserver(() => {
      if (!document.querySelector('.calendly-overlay')) { window.__lenis?.start(); mo.disconnect(); }
    });
    mo.observe(document.body, { childList: true });
  };
  $$('[data-book]').forEach(a => {
    if (!bookingUrl) return;
    const u = new URL(bookingUrl);
    u.searchParams.set('utm_source', 'website');
    u.searchParams.set('utm_medium', a.dataset.book || 'cta');
    u.searchParams.set('utm_content', location.pathname);
    a.href = u.href;
    a.target = '_blank';
    a.rel = 'noopener';
    a.addEventListener('click', e => {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return; // modified clicks open the booking page in a new tab
      e.preventDefault();
      loadCalendly()
        .then(C => { C.initPopupWidget({ url: `${a.href}&hide_gdpr_banner=1` }); holdScroll(); })
        .catch(() => { location.href = a.href; });
    });
  });
  /* ---------------- enquiry form: qualify first, then offer a time on Calendly ---------------- */
  (() => {
    const form = $('.enq');
    if (!form || !bookingUrl) return;
    const err = $('.enq__err', form);
    form.addEventListener('submit', e => {
      e.preventDefault();
      if (!form.checkValidity()) { form.classList.add('is-invalid'); err.hidden = false; return; }
      err.hidden = true; form.classList.remove('is-invalid');
      const d = Object.fromEntries(new FormData(form));
      const u = new URL(bookingUrl);
      u.searchParams.set('utm_source', 'website');
      u.searchParams.set('utm_medium', 'enquiry');
      u.searchParams.set('utm_content', location.pathname);
      const answers = { a1: d.company, a2: d.sector, a3: d.budget, a4: (d.brief || '').trim() };
      const direct = new URL(u);
      direct.searchParams.set('name', d.name);
      direct.searchParams.set('email', d.email);
      Object.entries(answers).forEach(([k, v]) => v && direct.searchParams.set(k, v));
      loadCalendly()
        .then(C => { C.initPopupWidget({ url: `${u.href}&hide_gdpr_banner=1`, prefill: { name: d.name, email: d.email, customAnswers: answers } }); holdScroll(); })
        .catch(() => { location.href = direct.href; });
    });
  })();

  $$('[data-email]').forEach(a => { if (cfg.email) { a.href = `mailto:${cfg.email}`; a.textContent = cfg.email; } else a.remove(); });
  $$('[data-phone]').forEach(el => { if (cfg.phoneDisplay) el.textContent = cfg.phoneDisplay; else el.remove(); });
  $$('[data-address]').forEach(el => {
    if (!cfg.address) return el.remove();
    el.textContent = cfg.address;
    if (el.tagName === 'A') { el.href = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent('Akarsa Studio, ' + cfg.address)}`; el.target = '_blank'; el.rel = 'noopener'; }
  });
  $$('[data-social]').forEach(a => {
    const url = (cfg.socials || {})[a.dataset.social];
    if (url) { a.href = url; a.target = '_blank'; a.rel = 'noopener'; } else a.remove();
  });
  if (!$$('.socials a').length) $('.footer__social')?.remove();
  $$('[data-social-link]').forEach(a => {
    const url = (cfg.socials || {})[a.dataset.socialLink];
    if (url) a.href = url;
    a.target = '_blank';
    a.rel = 'noopener';
  });
  $$('[data-year]').forEach(el => (el.textContent = new Date().getFullYear()));


  /* ---------------- designed thumbnails (Akarsa poster style, crisp at any size) ---------------- */
  const GLYPH = 'M300,122 L172,246 L243,250 A71,93 0 0 1 172,343 L172,396 A128,140 0 0 0 300,256 Z M313,256 L372,256 A75,87 0 0 0 447,343 L447,396 A134,140 0 0 1 313,256 Z';
  const ICON = {
    play: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width=".8"><circle cx="12" cy="12" r="11"/><path d="M10 8v8l6-4z" fill="currentColor" stroke="none"/></svg>',
    mega: '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11v3a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1Z"/><path d="M15 9a3 3 0 0 1 0 6M18 6a7 7 0 0 1 0 12"/></svg>',
    heart: '<svg viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.5 3.4 5 6.9 5c2 0 3.4 1.1 4.1 2.3C11.7 6.1 13.1 5 15.1 5c3.5 0 5.7 3.5 4.4 6.8C17.5 16.4 12 21 12 21Z" fill="#fff"/></svg>',
    spark: '<svg viewBox="0 0 24 24"><path d="M12 1.5l2.6 7.9L22.5 12l-7.9 2.6L12 22.5l-2.6-7.9L1.5 12l7.9-2.6z" fill="#fff"/></svg>'
  };
  const PIC = {
    stat: (b, t) => `<div class="pp-stat"><b>${b}</b><span>${t}</span></div>`,
    list: items => `<ul class="pp-list">${items.map(([ok, t]) => `<li class="${ok ? 'ok' : ''}"><i>${ok ? '✓' : '–'}</i>${t}</li>`).join('')}</ul>`,
    glyph: () => `<div class="pp-glyph"><svg viewBox="110 60 400 400"><path fill="currentColor" d="${GLYPH}"/></svg></div>`,
    chart: () => '<svg class="pp-chart" viewBox="0 0 100 80" preserveAspectRatio="none"><polyline points="0,70 18,62 34,66 50,48 66,40 82,22 100,8" fill="none" stroke="currentColor" stroke-width="1.4" vector-effect="non-scaling-stroke"/></svg>',
    swatch: () => '<div class="pp-swatch"><b>Aa</b><div><i style="background:#0e3b30"></i><i style="background:#b39a62"></i><i style="background:#e9dcc0"></i><i style="background:#f7f2e6"></i></div></div>',
    shapes: () => '<svg class="pp-shapes" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1"><path d="M10 50h80M50 10v80" stroke-dasharray="2 3" opacity=".4"/><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="18" opacity=".6"/></svg>',
    playbar: () => `<div class="pp-play">${ICON.play}<div class="pp-bar"><i></i></div></div>`,
    cal: () => `<div class="pp-cal">${Array.from({ length: 28 }, (_, i) => `<i class="${[1, 4, 6, 9, 12, 14, 17, 20, 22, 25, 27].includes(i) ? 'on' : ''}"></i>`).join('')}</div>`,
    bars: (arr, t) => `<div class="pp-bars"><div>${arr.map(v => `<i style="height:${v}%"></i>`).join('')}</div><span>${t}</span></div>`,
    browser: () => `<div class="pp-browser"><div class="pp-browser__top"><i></i><i></i><i></i></div><div class="pp-browser__body"><span></span><span></span><span></span></div></div>`,
    chat: () => '<div class="pp-chat"><p>We launch in March.</p><p class="me">Who is the buyer?</p></div>',
    icon: k => `<div class="pp-icon">${ICON[k]}</div>`,
    arch: () => '<svg class="pp-line" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1"><path d="M14 92h72M24 92V34l26-18 26 18v58"/><path d="M34 92V58h32v34M34 44h32M50 16v76" opacity=".55"/><path d="M38 66h8M54 66h8M38 76h8M54 76h8" opacity=".55"/></svg>',
    gem: () => '<svg class="pp-line" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1"><path d="M28 30h44l14 16-36 40-36-40z"/><path d="M14 46h72M28 30l10 16 12-16 12 16 10-16M38 46l12 40 12-40" opacity=".6"/></svg>',
    materials: () => '<div class="pp-mat"><i style="background:linear-gradient(135deg,#f3eee3,#d8cfbd 55%,#efe9dc)"></i><i style="background:linear-gradient(135deg,#8a7244,#e9dcc0 50%,#a88c55)"></i><i style="background:linear-gradient(135deg,#0e3b30,#245c4c)"></i><i style="background:linear-gradient(135deg,#e6dcc4,#cbbd9b)"></i></div>'
  };
  // quiet plates in the brand palette: em = emerald, dp = deep emerald, cr = cream, st = stone
  const TONE = { em: ['#0e3b30', '#e9dcc0'], dp: ['#0a2e25', '#e9dcc0'], cr: ['#f7f2e6', '#0e3b30'], st: ['#e6dcc4', '#0e3b30'] };
  const POSTERS = {
    result: { t: 'em', top: 'Published result', bot: '3.7× return', pic: PIC.stat('196', 'purchases in 32 days') },
    truth: { t: 'cr', top: 'Principle 01', bot: 'Truth over illusion', pic: PIC.glyph() },
    ai: { t: 'st', top: 'Principle 02', bot: 'Taste leads', pic: PIC.glyph() },
    systems: { t: 'st', top: 'Principle 03', bot: 'Fewer, made well', pic: PIC.shapes() },
    brand: { t: 'cr', top: 'Identity', bot: 'The brand book', pic: PIC.swatch() },
    logo: { t: 'em', top: 'Identity', bot: 'Mark making', pic: PIC.shapes() },
    hook: { t: 'em', top: 'Film', bot: 'Shot with light', pic: PIC.playbar() },
    always: { t: 'cr', top: 'Social', bot: 'One consistent look', pic: PIC.cal() },
    cpl: { t: 'em', top: 'Performance', bot: '13× lower cost', pic: PIC.bars([100, 70, 46, 24, 8], 'Cost per enquiry') },
    one: { t: 'dp', top: 'Akarsa One', bot: 'Buyer intelligence', pic: PIC.browser() },
    data: { t: 'dp', top: 'Performance', bot: 'Measured in sales', pic: PIC.chart() },
    talk: { t: 'cr', top: 'Enquire', bot: 'Tell us more', pic: PIC.chat() },
    next: { t: 'em', top: 'New projects', bot: 'By enquiry', pic: PIC.glyph() },
    reel: { t: 'em', top: 'Film', bot: 'Brand film', pic: PIC.icon('play') },
    ad: { t: 'cr', top: 'Campaign', bot: 'Launch', pic: PIC.chart() },
    post: { t: 'st', top: 'Content', bot: 'Stills', pic: PIC.gem() },
    estate: { t: 'em', top: 'Real estate', bot: 'Light and space', pic: PIC.arch() },
    jewel: { t: 'cr', top: 'Fine jewellery', bot: 'Metal and stone', pic: PIC.gem() },
    film: { t: 'dp', top: 'Brand film', bot: 'Made with restraint', pic: PIC.icon('play') },
    materials: { t: 'cr', top: 'The studio', bot: 'Stone, metal, light', pic: PIC.materials() }
  };
  const buildPoster = (el, key) => {
    const p = POSTERS[key];
    if (!p) return el;
    const [bg, fg] = TONE[p.t];
    el.classList.add('poster', 'plate');
    el.style.setProperty('--pbg', bg);
    el.style.setProperty('--pfg', fg);
    el.innerHTML = `<span class="plate__top">${p.top}</span><div class="plate__pic">${p.pic}</div><b class="plate__bot">${p.bot}</b><svg class="plate__mark" viewBox="110 60 400 400" aria-hidden="true"><path fill="currentColor" d="${GLYPH}"/></svg>`;
    return el;
  };
  $$('[data-poster]').forEach(el => buildPoster(el, el.dataset.poster));

  /* ---------------- descriptive alt text (SEO + accessibility) ---------------- */
  const CLIENT_NAMES = { starbucks: 'Starbucks', adidas: 'Adidas', decathlon: 'Decathlon', 'olympia-gym': 'Olympia Fitness Gym', 'burger-singh': 'Burger Singh', 'dukes-table': 'The Duke’s Table', 'korean-trends': 'The Korean Trends', chirmi: 'Chirmi', 'mayarams-farm': 'Mayaram’s Farm', 'kunafa-bytes': 'Kunafa Bytes', lokal: 'Lokal', mudoven: 'Mudoven', 'urban-theka': 'Urban Theka', kahani: 'Kahani', '7th-heaven': '7th Heaven', varenyam: 'Varenyam', zhanna: 'Zhanna Events & Flowers', 'bake-affaire': 'Bake Affaire', 'nothing-before-coffee': 'Nothing Before Coffee', 'nomad-pizza': 'Nomad Pizza', 'crush-coffee': 'The Crush Coffee' };
  const IG_ALTS = { r01: 'Akarsa Studio “Ruko!” short-form reel', r02: 'Akarsa Studio reel: Your marketing is a lie', r03: 'Meta Ads case study: ₹30K turned into 52 enquiries', r04: 'Akarsa Studio reel: Posting is not growth, you need a system', r05: 'Akarsa Studio reel: Are Meta ads a waste of money?', r06: 'Akarsa Studio talking-head short-form video', r08: 'Fleuristry brand film by Akarsa Studio', r09: 'Akarsa Live with Ritik Sharma and Malhar Chaudhari', r10: 'Akarsa One AI business intelligence reel', r11: 'Akarsa Studio reel: Spent ₹40,000 and got zero clients?', r12: 'Akarsa Studio short film reel' };
  const altFor = src => {
    const key = (src.split('/').pop() || '').replace(/\.\w+$/, '');
    if (src.includes('/clients/reels/')) return `${CLIENT_NAMES[key] || 'Client'} social media reel by Akarsa Studio`;
    return IG_ALTS[key] || 'Akarsa Studio work';
  };

  /* ---------------- media slots ---------------- */
  $$('.media').forEach(m => {
    if (m.dataset.art) {
      m.insertAdjacentHTML('afterbegin', '<span class="art-layer"></span><span class="art-layer art-layer--2"></span><span class="art-shape"></span><span class="art-grain"></span>');
    }
    // floating phone-style reels over the art (one or more, separated by |)
    const reels = (m.dataset.reel || '').split('|').map(x => x.trim()).filter(Boolean);
    if (reels.length) {
      const wrap = document.createElement('div');
      wrap.className = `reels reels--${reels.length}`;
      reels.forEach(r => {
        if (r.startsWith('poster:')) {
          const d = document.createElement('div');
          d.className = 'reel reel--poster';
          wrap.appendChild(buildPoster(d, r.slice(7)));
          return;
        }
        const im = document.createElement('img');
        Object.assign(im, { className: 'reel', loading: 'lazy', decoding: 'async', alt: altFor(r) });
        im.src = r;
        wrap.appendChild(im);
      });
      m.appendChild(wrap);
    }
    const src = (m.dataset.src || '').trim();
    if (!src) return;
    const isVideo = /\.(mp4|webm|mov)$/i.test(src);
    const el = document.createElement(isVideo ? 'video' : 'img');
    if (isVideo) Object.assign(el, { muted: true, loop: true, autoplay: true, playsInline: true, preload: 'metadata' });
    else { el.loading = m.closest('.hero') ? 'eager' : 'lazy'; el.alt = m.closest('[aria-hidden="true"]') ? '' : altFor(src); el.decoding = 'async'; }
    el.addEventListener(isVideo ? 'loadeddata' : 'load', () => { el.classList.add('is-loaded'); m.classList.add('has-src'); }, { once: true });
    el.addEventListener('error', () => el.remove(), { once: true });
    el.src = src;
    m.appendChild(el);
  });

  // only animate art that's on screen (keeps the GPU calm)
  const io = new IntersectionObserver(es => es.forEach(e => e.target.classList.toggle('in-view', e.isIntersecting)), { rootMargin: '100px' });
  $$('.media[data-art]').forEach(m => io.observe(m));

  // the sticky footer is only painted once the end of the page is close (see .footer-gated in styles.css)
  const footer = $('.footer');
  const pageEnd = $('.page__end');
  if (footer && pageEnd) {
    const gateFooter = () => footer.classList.toggle('is-near', pageEnd.getBoundingClientRect().top < innerHeight * 2);
    gateFooter();
    addEventListener('scroll', gateFooter, { passive: true });
    addEventListener('resize', gateFooter);
  } else footer?.classList.add('is-near');

  /* ---------------- split text ---------------- */
  const split = el => {
    const words = el.textContent.trim().split(/\s+/);
    el.innerHTML = words.map(w => `<span class="w"><span>${w.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</span></span>`).join(' ');
    el.setAttribute('aria-label', words.join(' '));
  };
  $$('.split, .split-inline').forEach(split);

  /* ---------------- button label width (arrow swap) ---------------- */
  const measureButtons = () => $$('.btn').forEach(b => {
    const l = $('.btn__label', b);
    if (l) b.style.setProperty('--lw', `${l.offsetWidth}px`);
  });
  measureButtons();

  /* ---------------- no-GSAP fallback ---------------- */
  if (!window.gsap || !window.ScrollTrigger) {
    $('.loader')?.remove();
    document.body.classList.remove('is-loading');
    $$('.circled path').forEach(p => (p.style.strokeDashoffset = 0));
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  /* ---------------- smooth scroll (Lenis) ---------------- */
  let lenis = null;
  if (window.Lenis && !reduced) {
    lenis = new Lenis({ duration: 1.15, easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    lenis.stop();
    window.__lenis = lenis;
  }
  let velocity = 0;
  ScrollTrigger.create({ onUpdate: s => { velocity = s.getVelocity(); } });

  // anchor links
  $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const id = a.getAttribute('href');
    if (id.length < 2 && id !== '#top') return;
    const t = id === '#top' ? 0 : $(id);
    if (t === null) return;
    e.preventDefault();
    closeMenu();
    if (lenis) lenis.scrollTo(t, { offset: -90, duration: 1.6 });
    else window.scrollTo({ top: t === 0 ? 0 : t.getBoundingClientRect().top + scrollY - 90, behavior: 'smooth' });
  }));

  /* ---------------- mobile menu ---------------- */
  const nav = $('.nav');
  const burger = $('.nav__burger');
  function closeMenu() { nav.classList.remove('is-open'); burger?.setAttribute('aria-expanded', 'false'); }
  burger?.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(open));
  });

  /* ---------------- nav hide / show ---------------- */
  let lastY = 0;
  const waFloat = $('.wa-float');
  const onScroll = y => {
    const down = y > lastY && y > 200;
    if (!nav.classList.contains('is-open')) nav.classList.toggle('is-hidden', down);
    waFloat.classList.toggle('is-in', y > innerHeight * 0.8);
    lastY = y;
  };
  if (lenis) lenis.on('scroll', ({ scroll }) => onScroll(scroll));
  else addEventListener('scroll', () => onScroll(scrollY), { passive: true });

  /* ---------------- initial states (hidden behind loader) ---------------- */
  gsap.set('.nav', { yPercent: -160 });
  gsap.set('.hl__i', { yPercent: 110 });
  gsap.set('.hero__kicker', { autoAlpha: 0, y: 14 });
  gsap.set('.hero [data-pop]', { autoAlpha: 0, scale: 0.8, y: 20 });
  gsap.set('.np-card', { autoAlpha: 0, scale: 0.8, x: 40, y: 20 });
  gsap.set('.phone-wrap', { autoAlpha: 0, scale: 0.7, y: 40 });

  /* ---------------- loader ---------------- */
  const loader = $('.loader');
  const count = { v: 0 };
  const intro = gsap.timeline({ paused: true });

  const tlLoad = gsap.timeline({
    defaults: { ease: 'power4.out' },
    onComplete: () => {
      document.body.classList.remove('is-loading');
      lenis?.start();
      loader.remove();
      ScrollTrigger.refresh();
    }
  });
  let seen = false;
  try { seen = sessionStorage.getItem('akarsa-seen') === '1'; sessionStorage.setItem('akarsa-seen', '1'); } catch (e) { /* storage blocked */ }
  if (reduced || seen) {
    tlLoad.to(loader, { autoAlpha: 0, duration: reduced ? 0 : 0.35 }).add(() => intro.play());
  } else {
    tlLoad
      .to('.loader__word span', { yPercent: -110, duration: 0.7, stagger: 0.04 }, 0.05)
      .to('.loader__line i', { scaleX: 1, duration: 1, ease: 'power2.inOut' }, 0.05)
      .to(count, { v: 100, duration: 1, ease: 'power2.inOut', onUpdate: () => ($('.loader__count').textContent = Math.round(count.v)) }, 0.05)
      .to('.loader__word span', { yPercent: -220, duration: 0.5, stagger: 0.03, ease: 'power3.in' }, 1.05)
      .to('.loader__meta, .loader__line', { autoAlpha: 0, duration: 0.25 }, 1.05)
      .to(loader, { clipPath: 'inset(0 0 100% 0 round 0 0 48px 48px)', duration: 0.8, ease: 'expo.inOut' }, 1.3)
      .add(() => intro.play(), 1.6);
  }
  gsap.set('.loader__word span', { yPercent: 110 });

  /* ---------------- hero intro (spring pops like the reference) ---------------- */
  intro
    .to('.nav', { yPercent: 0, duration: 1, ease: 'expo.out' }, 0)
    .to('.hero__kicker', { autoAlpha: 1, y: 0, duration: 0.8, ease: 'back.out(2)' }, 0)
    .to('.hl__i', { yPercent: 0, duration: 1.1, stagger: 0.1, ease: 'expo.out' }, 0.05)
    .to('.pw--3', { autoAlpha: 1, scale: 1, y: 0, duration: 1, ease: 'back.out(1.4)' }, 0.35)
    .to('.pw--2', { autoAlpha: 1, scale: 1, y: 0, duration: 1, ease: 'back.out(1.4)' }, 0.45)
    .to('.pw--1', { autoAlpha: 1, scale: 1, y: 0, duration: 1, ease: 'back.out(1.6)' }, 0.55)
    .to('.hero__benefits [data-pop]', { autoAlpha: 1, scale: 1, y: 0, duration: 0.7, stagger: 0.1, ease: 'back.out(2)' }, 0.6)
    .to('.np-card', { autoAlpha: 1, scale: 1, x: 0, y: 0, duration: 0.8, ease: 'back.out(1.8)' }, 0.75)
    .to('.hero__cta [data-pop]', { autoAlpha: 1, scale: 1, y: 0, duration: 0.8, stagger: 0.1, ease: 'back.out(1.7)' }, 0.85);

  /* ---------------- ribbon text loop ---------------- */
  (() => {
    const path = $('#ribbonPath');
    const tp = $('.ribbon__tp');
    if (!path || !tp) return;
    const seq = 'UGC • SHORT-FORM • SOCIAL MEDIA • INFLUENCER MARKETING • META ADS • GOOGLE ADS • REDDIT ADS • CHATGPT ADS • YOUTUBE ADS • BRANDING • LOGO DESIGN • WEBSITES • ANIMATION • ';
    tp.textContent = seq;
    const seqLen = tp.getComputedTextLength() || 1500;
    const pathLen = path.getTotalLength();
    const reps = Math.ceil((pathLen + seqLen) / seqLen) + 1;
    tp.textContent = seq.repeat(reps);
    // redrawing text along a curve is the most expensive thing on the page: only while the hero is on screen, ~30fps on phones
    let off = 0, heroOn = true, skip = false;
    const coarse = matchMedia('(pointer: coarse)').matches;
    new IntersectionObserver(([e]) => { heroOn = e.isIntersecting; }).observe($('.hero'));
    gsap.ticker.add((t, dt) => {
      if (!heroOn) return;
      const boost = Math.min(Math.abs(velocity) / 300, 8);
      off = (off + (0.05 + boost * 0.05) * dt) % seqLen;
      if (coarse && (skip = !skip)) return;
      tp.setAttribute('startOffset', -off);
    });
  })();

  /* ---------------- hero stories ---------------- */
  (() => {
    const slides = $$('.stories__slide');
    const bars = $$('.stories__bars b');
    if (!slides.length) return;
    let i = 0;
    const play = () => {
      slides.forEach((s, k) => s.classList.toggle('is-active', k === i));
      bars.forEach((b, k) => gsap.set(b, { scaleX: k < i ? 1 : 0 }));
      gsap.to(bars[i], { scaleX: 1, duration: 4, ease: 'none', onComplete: () => { i = (i + 1) % slides.length; play(); } });
    };
    play();
  })();

  // looping tweens keep restyling their tracks every frame; stop them while they're off screen
  const pauseOffscreen = (el, tw) => new IntersectionObserver(([e]) => (e.isIntersecting ? tw.resume() : tw.pause())).observe(el);

  /* ---------------- platform marquee (reacts to scroll speed) ---------------- */
  // the second half of each marquee track is a visual duplicate for looping — hide it from assistive tech
  $$('.logos__track').forEach(track => {
    const kids = [...track.children];
    kids.slice(kids.length / 2).forEach(k => k.setAttribute('aria-hidden', 'true'));
  });
  $$('.logos__track').forEach((track, k) => {
    const rev = track.classList.contains('logos__track--b');
    const tw = rev
      ? gsap.fromTo(track, { xPercent: -50 }, { xPercent: 0, ease: 'none', duration: 40, repeat: -1 })
      : gsap.to(track, { xPercent: -50, ease: 'none', duration: 40, repeat: -1 });
    pauseOffscreen(track.parentElement, tw);
    let hover = false;
    track.addEventListener('mouseenter', () => (hover = true));
    track.addEventListener('mouseleave', () => (hover = false));
    gsap.ticker.add(() => {
      const target = hover ? 0.2 : 1 + Math.min(Math.abs(velocity) / 400, 6);
      tw.timeScale(gsap.utils.interpolate(tw.timeScale(), target, 0.08));
    });
  });

  /* ---------------- instagram feed marquee (pauses on hover) ---------------- */
  (() => {
    const track = $('.feed__track');
    if (!track) return;
    const tw = gsap.to(track, { xPercent: -50, ease: 'none', duration: 60, repeat: -1 });
    pauseOffscreen(track.parentElement, tw);
    let hover = false;
    track.addEventListener('mouseenter', () => (hover = true));
    track.addEventListener('mouseleave', () => (hover = false));
    gsap.ticker.add(() => {
      const target = hover ? 0.15 : 1 + Math.min(Math.abs(velocity) / 500, 4);
      tw.timeScale(gsap.utils.interpolate(tw.timeScale(), target, 0.06));
    });
  })();

  /* ---------------- result counters ---------------- */
  $$('[data-count]').forEach(el => {
    const end = +el.dataset.count;
    const o = { v: 0 };
    gsap.to(o, {
      v: end, duration: 1.6, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 85%' },
      onUpdate: () => (el.textContent = Math.round(o.v) + (el.dataset.suffix || ''))
    });
  });


  /* ---------------- process visuals ---------------- */
  $$('.viz-chat').forEach(v => gsap.from($$('.bub', v), { y: 14, autoAlpha: 0, scale: 0.9, transformOrigin: 'left bottom', duration: 0.6, stagger: 0.45, ease: 'back.out(2)', scrollTrigger: { trigger: v, start: 'top 85%' } }));
  $$('.viz-plan').forEach(v => gsap.from($$('span', v), { x: -16, autoAlpha: 0, duration: 0.5, stagger: 0.18, ease: 'back.out(2)', scrollTrigger: { trigger: v, start: 'top 85%' } }));
  $$('.viz-create').forEach(v => gsap.from($$('.poster', v), { y: 50, rotation: 0, autoAlpha: 0, duration: 0.9, stagger: 0.12, ease: 'back.out(1.6)', scrollTrigger: { trigger: v, start: 'top 85%' } }));
  $$('.viz-grow').forEach(v => {
    gsap.from($$('.viz-grow__bars i', v), { scaleY: 0, transformOrigin: 'bottom', duration: 0.9, stagger: 0.08, ease: 'power3.out', scrollTrigger: { trigger: v, start: 'top 85%' } });
    gsap.from($('.viz-grow__tag', v), { scale: 0.6, autoAlpha: 0, duration: 0.6, delay: 0.5, ease: 'back.out(2.2)', scrollTrigger: { trigger: v, start: 'top 85%' } });
  });
  /* ---------------- logo wall ---------------- */
  $$('.logo-wall').forEach(w => gsap.fromTo($$('.wt', w), { scale: 0.5, rotation: () => gsap.utils.random(-14, 14), autoAlpha: 0 }, { scale: 1, rotation: 0, autoAlpha: 1, duration: 0.8, stagger: { each: 0.05, from: 'random' }, ease: 'back.out(1.8)', clearProps: 'transform', scrollTrigger: { trigger: w, start: 'top 80%', once: true } }));

  /* ---------------- Reddit + ChatGPT ads section ---------------- */
  $$('.rd-post').forEach(p => gsap.from(p, { y: 30, rotation: -3, autoAlpha: 0, duration: 0.9, ease: 'back.out(1.6)', clearProps: 'transform', scrollTrigger: { trigger: p, start: 'top 88%' } }));
  $$('.gpt-chat').forEach(c => gsap.from($$('.gpt-chat > *', c), { y: 16, autoAlpha: 0, scale: 0.94, duration: 0.6, stagger: 0.5, ease: 'back.out(2)', clearProps: 'transform', scrollTrigger: { trigger: c, start: 'top 85%' } }));
  $$('.offer__list li, .adcard__points li').forEach(li => gsap.from(li, { x: -14, autoAlpha: 0, duration: 0.5, ease: 'power3.out', clearProps: 'transform', scrollTrigger: { trigger: li, start: 'top 92%' } }));

  /* ---------------- generic reveals ---------------- */
  $$('.split, .split-inline').forEach(el => {
    if (el.closest('.hero')) return;
    gsap.from($$('.w > span', el), {
      yPercent: 110, duration: 0.7, ease: 'expo.out', stagger: 0.025,
      scrollTrigger: { trigger: el, start: 'top 88%' }
    });
  });
  $$('[data-reveal]').forEach(el => {
    gsap.from(el, { y: 50, autoAlpha: 0, duration: 1.1, ease: 'expo.out', clearProps: 'transform', scrollTrigger: { trigger: el, start: 'top 90%' } });
  });
  $$('[data-pop]').forEach(el => {
    if (el.closest('.hero')) return;
    gsap.from(el, { scale: 0.8, y: 30, autoAlpha: 0, duration: 0.9, ease: 'back.out(1.9)', clearProps: 'transform', scrollTrigger: { trigger: el, start: 'top 92%' } });
  });

  /* ---------------- pain section: pinned, dark-mode flip, floating cards ---------------- */
  (() => {
    const sec = $('.pain__sticky');
    if (!sec) return;
    const cards = $$('.pain__card', sec);
    const maxO = Math.max(...cards.map(c => +getComputedStyle(c).getPropertyValue('--o') || 0));
    const dist = () => innerHeight + maxO + 420;
    const tl = gsap.timeline({
      scrollTrigger: { trigger: sec, start: 'top top', end: () => `+=${dist()}`, pin: true, scrub: 0.6, invalidateOnRefresh: true }
    });
    tl.to(sec, { backgroundColor: '#1C1917', duration: 0.1, ease: 'none' }, 0)
      .to('.pain__title', { color: '#F4F4F3', duration: 0.1, ease: 'none' }, 0);
    cards.forEach((c, k) => {
      const o = +getComputedStyle(c).getPropertyValue('--o') || 0;
      const speed = 1 + (k % 3) * 0.06;
      tl.fromTo(c, { y: o }, { y: () => o - dist() * speed, ease: 'none', duration: 1 }, 0);
    });
    tl.to(sec, { backgroundColor: '#F4F4F3', duration: 0.1, ease: 'none' }, 0.9)
      .to('.pain__title', { color: '#1C1917', duration: 0.1, ease: 'none' }, 0.9);
  })();

  /* ---------------- scribbles draw on scroll ---------------- */
  const draw = (path, trigger, start = 'top 80%', end = 'bottom 40%') => {
    const len = path.getTotalLength();
    gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
    gsap.to(path, { strokeDashoffset: 0, ease: 'none', scrollTrigger: { trigger, start, end, scrub: 0.8 } });
  };
  $$('.scribble path').forEach(p => draw(p, p.closest('svg'), 'top 85%', 'bottom 30%'));
  $$('.team__wave path').forEach(p => draw(p, '.team__row', 'top 85%', 'bottom 45%'));
  $$('.cta__scribble path').forEach(p => draw(p, '.cta', 'top 80%', 'center 50%'));
  $$('.footer__loop path').forEach(p => draw(p, '.footer', 'top 100%', 'bottom 100%'));

  /* stickers & sticker parallax */
  $$('.feature__media').forEach(m => {
    gsap.to($('.media', m), { yPercent: -6, ease: 'none', scrollTrigger: { trigger: m, start: 'top bottom', end: 'bottom top', scrub: true } });
    const st = $('.sticker', m);
    if (st) gsap.to(st, { y: -40, ease: 'none', scrollTrigger: { trigger: m, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* ---------------- ring of work ---------------- */
  (() => {
    const ring = $('.ring');
    if (!ring) return;
    const items = $$('.ring__item', ring);
    const layout = () => {
      const R = innerWidth < 900 ? 250 : 450;
      items.forEach((it, k) => {
        const a = (360 / items.length) * k;
        const rad = (a * Math.PI) / 180;
        gsap.set(it, { x: R * Math.sin(rad), y: -R * Math.cos(rad), rotation: a });
      });
    };
    layout();
    addEventListener('resize', layout);
    gsap.fromTo(ring, { rotate: -40 }, { rotate: 40, ease: 'none', scrollTrigger: { trigger: '.ring-sec', start: 'top bottom', end: 'bottom top', scrub: 0.6 } });
    gsap.from(items, { scale: 0, duration: 0.9, ease: 'back.out(1.6)', stagger: { each: 0.05, from: 'center' }, scrollTrigger: { trigger: '.ring-sec', start: 'top 70%' } });
  })();

  /* ---------------- services: darken folders as the next one slides over ---------------- */
  (() => {
    const svcs = $$('.svc');
    svcs.forEach((s, k) => {
      const next = svcs[k + 1];
      if (!next) return;
      const body = $('.svc__body', s);
      const shade = document.createElement('span');
      shade.className = 'svc__shade';
      body.appendChild(shade);
      gsap.to(shade, { opacity: 0.18, ease: 'none', scrollTrigger: { trigger: next, start: 'top bottom', end: 'top 120px', scrub: true } });
      gsap.to($('.svc__media .media', s), { scale: 1.08, ease: 'none', scrollTrigger: { trigger: next, start: 'top bottom', end: 'top 120px', scrub: true } });
    });
    svcs.forEach(s => {
      gsap.from($$('.chips li', s), { y: 16, autoAlpha: 0, stagger: 0.06, duration: 0.6, ease: 'back.out(2)', scrollTrigger: { trigger: s, start: 'top 70%' } });
    });
  })();

  /* ---------------- comparison cards fly in ---------------- */
  gsap.from('.cmp--other', { x: -120, y: 60, rotation: -10, autoAlpha: 0, duration: 1.2, ease: 'back.out(1.4)', scrollTrigger: { trigger: '.compare__cards', start: 'top 80%' } });
  gsap.from('.cmp--us', { x: 120, y: 80, rotation: 12, autoAlpha: 0, duration: 1.2, delay: 0.12, ease: 'back.out(1.4)', scrollTrigger: { trigger: '.compare__cards', start: 'top 80%' } });
  gsap.from('.cmp li', { x: -14, autoAlpha: 0, stagger: 0.05, duration: 0.5, delay: 0.5, ease: 'power3.out', scrollTrigger: { trigger: '.compare__cards', start: 'top 80%' } });

  /* ---------------- team roles pop along the wave ---------------- */
  gsap.from('.role', { y: 80, scale: 0.6, rotation: () => gsap.utils.random(-20, 20), autoAlpha: 0, duration: 1, ease: 'back.out(1.7)', stagger: 0.08, clearProps: 'transform', scrollTrigger: { trigger: '.team__row', start: 'top 80%' } });

  /* ---------------- footer reveal ---------------- */
  gsap.fromTo('.footer__brand', { yPercent: 40, autoAlpha: 0.2 }, { yPercent: 0, autoAlpha: 1, ease: 'none', scrollTrigger: { trigger: '.cta', start: 'bottom bottom', end: () => `+=${$('.footer').offsetHeight}`, scrub: true } });

  /* ---------------- pricing switch ---------------- */
  (() => {
    const sw = $('.switch');
    if (!sw) return;
    const fill = mode => {
      $$('.pricing [data-monthly]').forEach(el => {
        const v = el.getAttribute(`data-${mode}`) || '';
        if (el.tagName === 'UL') {
          el.innerHTML = '';
          v.split('|').forEach(t => {
            const li = document.createElement('li');
            li.innerHTML = '<i class="tick"></i>';
            li.append(t);
            el.appendChild(li);
          });
        } else {
          el.textContent = v;
        }
      });
    };
    fill('monthly');
    $$('button', sw).forEach(b => b.addEventListener('click', () => {
      const mode = b.dataset.plan;
      if (b.classList.contains('is-active')) return;
      $$('button', sw).forEach(x => { x.classList.toggle('is-active', x === b); x.setAttribute('aria-selected', String(x === b)); });
      sw.classList.toggle('is-project', mode === 'project');
      const targets = $$('.plan__head > *, .plan__list');
      gsap.to(targets, {
        y: -10, autoAlpha: 0, duration: 0.2, stagger: 0.02, ease: 'power2.in',
        onComplete: () => {
          fill(mode);
          gsap.fromTo(targets, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.5, stagger: 0.03, ease: 'back.out(2)' });
        }
      });
    }));
  })();

  /* ---------------- FAQ accordion ---------------- */
  $$('.qa').forEach(qa => {
    const q = $('.qa__q', qa);
    const a = $('.qa__a', qa);
    q.addEventListener('click', () => {
      const open = qa.classList.contains('is-open');
      $$('.qa.is-open').forEach(o => {
        if (o === qa) return;
        o.classList.remove('is-open');
        $('.qa__q', o).setAttribute('aria-expanded', 'false');
        gsap.fromTo($('.qa__a', o), { height: $('.qa__a', o).offsetHeight }, { height: 0, duration: 0.5, ease: 'power3.inOut' });
      });
      if (open) {
        gsap.fromTo(a, { height: a.offsetHeight }, { height: 0, duration: 0.5, ease: 'power3.inOut', onComplete: () => ScrollTrigger.refresh() });
        qa.classList.remove('is-open');
      } else {
        qa.classList.add('is-open');
        gsap.fromTo(a, { height: 0 }, { height: 'auto', duration: 0.6, ease: 'expo.out', onComplete: () => ScrollTrigger.refresh() });
      }
      q.setAttribute('aria-expanded', String(!open));
    });
  });

  /* ---------------- nav link scramble ---------------- */
  const glyphs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ*#%&@';
  $$('[data-scramble]').forEach(a => {
    const orig = a.textContent;
    let raf;
    a.addEventListener('mouseenter', () => {
      let f = 0;
      cancelAnimationFrame(raf);
      const step = () => {
        a.textContent = orig.split('').map((ch, k) => (k < f / 2 ? ch : glyphs[(Math.random() * glyphs.length) | 0])).join('');
        f++;
        if (f / 2 <= orig.length) raf = requestAnimationFrame(step); else a.textContent = orig;
      };
      step();
    });
  });

  /* ---------------- custom cursor ---------------- */
  if (!isTouch) {
    const cur = $('.cursor');
    const dot = $('.cursor__dot');
    const ring = $('.cursor__ring');
    const label = $('.cursor__label');
    let mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;
    addEventListener('mousemove', e => {
      mx = e.clientX; my = e.clientY;
      dot.style.transform = `translate(${mx}px,${my}px)`;
      const t = e.target;
      const lab = t.closest?.('[data-cursor]');
      cur.classList.toggle('is-label', !!lab);
      if (lab) label.textContent = lab.dataset.cursor;
      cur.classList.toggle('is-link', !lab && !!t.closest?.('a,button'));
      cur.classList.toggle('on-dark', !!t.closest?.('.cta__card,.plan--dark,.nav__bar,.nav__mobile') || document.querySelector('.pain__sticky')?.contains(t) && getComputedStyle($('.pain__sticky')).backgroundColor === 'rgb(28, 25, 23)');
    }, { passive: true });
    // only show the custom cursor while the pointer is actually over the page
    addEventListener('mousemove', () => cur.classList.add('is-active'), { passive: true });
    document.addEventListener('mouseout', e => { if (!e.relatedTarget) cur.classList.remove('is-active'); });
    addEventListener('blur', () => cur.classList.remove('is-active'));
    gsap.ticker.add(() => {
      rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18;
      ring.style.transform = `translate(${rx}px,${ry}px)`;
    });
  }

  /* ---------------- magnetic buttons ---------------- */
  if (!isTouch) {
    $$('.magnetic').forEach(el => {
      const xTo = gsap.quickTo(el, 'x', { duration: 0.6, ease: 'elastic.out(1,0.4)' });
      const yTo = gsap.quickTo(el, 'y', { duration: 0.6, ease: 'elastic.out(1,0.4)' });
      el.addEventListener('mousemove', e => {
        const r = el.getBoundingClientRect();
        xTo((e.clientX - (r.left + r.width / 2)) * 0.25);
        yTo((e.clientY - (r.top + r.height / 2)) * 0.35);
      });
      el.addEventListener('mouseleave', () => { xTo(0); yTo(0); });
    });
  }

  /* ---------------- 3D tilt on project cards ---------------- */
  if (!isTouch) {
    $$('.project, .belief__img, .reel-card').forEach(card => {
      const rx = gsap.quickTo(card, 'rotationX', { duration: 0.8, ease: 'power3.out' });
      const ry = gsap.quickTo(card, 'rotationY', { duration: 0.8, ease: 'power3.out' });
      gsap.set(card, { transformPerspective: 1000 });
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        rx(((e.clientY - r.top) / r.height - 0.5) * -6);
        ry(((e.clientX - r.left) / r.width - 0.5) * 6);
      });
      card.addEventListener('mouseleave', () => { rx(0); ry(0); });
    });
  }

  /* ---------------- refresh after fonts / resize ---------------- */
  document.fonts?.ready.then(() => { measureButtons(); ScrollTrigger.refresh(); });
  addEventListener('resize', () => measureButtons());
})();
