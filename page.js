/* AKARSA — lightweight script for sub-pages (no heavy animation libraries) */
(() => {
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const cfg = window.AKARSA || {};

  // WhatsApp links (per-link message via data-wa-msg)
  const waBase = `https://wa.me/${(cfg.whatsapp || '918109801383').replace(/\D/g, '')}`;
  $$('[data-wa]').forEach(a => {
    const msg = a.dataset.waMsg || cfg.whatsappMessage || '';
    a.href = `${waBase}?text=${encodeURIComponent(msg)}`;
    a.target = '_blank';
    a.rel = 'noopener';
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
