/* AKARSA — lightweight script for sub-pages (no heavy animation libraries) */
(() => {
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const cfg = window.AKARSA || {};

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
  $$('[data-social]').forEach(a => { const u = (cfg.socials || {})[a.dataset.social]; if (u) a.href = u; a.target = '_blank'; a.rel = 'noopener'; });
  $$('[data-year]').forEach(el => (el.textContent = new Date().getFullYear()));

  // highlight the current page in the nav
  $$('.nav__links a').forEach(a => { if (a.getAttribute('href') === location.pathname) a.setAttribute('aria-current', 'page'); });

  // mobile menu
  const nav = document.querySelector('.nav');
  const burger = document.querySelector('.nav__burger');
  burger?.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(open));
  });
  $$('.nav__mobile a').forEach(a => a.addEventListener('click', () => nav.classList.remove('is-open')));

  // hide nav on scroll down, show on scroll up
  let lastY = scrollY;
  addEventListener('scroll', () => {
    const y = scrollY;
    if (!nav.classList.contains('is-open')) nav.classList.toggle('is-hidden', y > lastY && y > 200);
    lastY = y;
  }, { passive: true });

  // reveal on scroll
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('[data-in]').forEach((el, i) => { el.style.transitionDelay = `${(i % 4) * 60}ms`; io.observe(el); });
})();
