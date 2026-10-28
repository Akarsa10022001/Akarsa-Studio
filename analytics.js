/* Akarsa Studio: measurement.
   Google Analytics 4 (G-FXH0GL55FH) and Meta Pixel (1749830945647617).
   Google runs in consent mode: until a visitor accepts, it sends cookieless pings only.
   The Meta Pixel loads only after a visitor accepts. No form contents are ever sent. */
(() => {
  const GA = 'G-FXH0GL55FH';
  const PIXEL = '1749830945647617';
  const KEY = 'akarsa-consent';
  const read = () => { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
  const save = v => { try { localStorage.setItem(KEY, v); } catch (e) {} };

  /* ---------- Google: consent mode first, then the tag ---------- */
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };
  const choice = read();
  const granted = choice === 'yes';
  gtag('consent', 'default', {
    analytics_storage: granted ? 'granted' : 'denied',
    ad_storage: granted ? 'granted' : 'denied',
    ad_user_data: granted ? 'granted' : 'denied',
    ad_personalization: granted ? 'granted' : 'denied',
    wait_for_update: 300
  });
  gtag('js', new Date());
  gtag('config', GA, { anonymize_ip: true });
  const g = document.createElement('script');
  g.async = true;
  g.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA;
  document.head.appendChild(g);

  /* ---------- Meta Pixel, only with consent ---------- */
  let fbReady = false;
  const loadPixel = () => {
    if (fbReady) return;
    fbReady = true;
    !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', PIXEL);
    fbq('track', 'PageView');
  };
  if (granted) loadPixel();

  /* one call that reaches both, with no personal data */
  const track = (gaName, params = {}, fbName, fbParams) => {
    try { gtag('event', gaName, params); } catch (e) {}
    if (fbName && window.fbq) { try { fbq('track', fbName, fbParams || {}); } catch (e) {} }
  };
  window.akarsaTrack = track;

  /* ---------- consent bar ---------- */
  const bar = () => {
    if (read()) return;
    const el = document.createElement('div');
    el.className = 'consent';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', 'Cookie choice');
    el.innerHTML = '<p>We use cookies to understand which pages and films help people, and to measure our own ads. <a href="/privacy">Privacy</a></p><div class="consent__btns"><button type="button" class="consent__no">Decline</button><button type="button" class="consent__yes">Accept</button></div>';
    document.body.appendChild(el);
    requestAnimationFrame(() => el.classList.add('is-in'));
    const close = v => {
      save(v);
      if (v === 'yes') {
        gtag('consent', 'update', { analytics_storage: 'granted', ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted' });
        loadPixel();
      }
      el.classList.remove('is-in');
      setTimeout(() => el.remove(), 500);
    };
    el.querySelector('.consent__yes').addEventListener('click', () => close('yes'));
    el.querySelector('.consent__no').addEventListener('click', () => close('no'));
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bar); else bar();

  /* ---------- what we measure ---------- */
  // enquiry form: sector and budget band only, never names or emails
  document.addEventListener('submit', e => {
    const f = e.target;
    if (!f.matches || !f.matches('form.enq') || !f.checkValidity()) return;
    const sector = f.sector?.value || '', budget = (f.querySelector('input[name="budget"]:checked') || {}).value || '';
    track('generate_lead', { form: 'enquiry', sector, budget_band: budget }, 'Lead', { content_category: sector });
  }, true);

  // a call booked in the Calendly popup
  addEventListener('message', e => {
    if (!/calendly\.com$/.test((() => { try { return new URL(e.origin).hostname; } catch (x) { return ''; } })())) return;
    if (e.data && e.data.event === 'calendly.event_scheduled') track('book_call', { method: 'calendly' }, 'Schedule');
  });

  // films, email, phone, WhatsApp and social clicks
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-yt], a[href]');
    if (!t) return;
    if (t.dataset.yt) { track('video_play', { video_title: t.dataset.title || t.dataset.yt }, 'ViewContent', { content_name: t.dataset.title || '' }); return; }
    const h = t.getAttribute('href') || '';
    if (h.startsWith('mailto:')) track('contact_email', {}, 'Contact');
    else if (h.startsWith('tel:')) track('contact_phone', {}, 'Contact');
    else if (/wa\.me|whatsapp/.test(h)) track('contact_whatsapp', {}, 'Contact');
    else if (/instagram|youtube|facebook|pinterest|linkedin|x\.com/.test(h)) track('social_click', { network: (h.match(/instagram|youtube|facebook|pinterest|linkedin|x\.com/) || [''])[0] });
    else if (h === '#enquire' || h.endsWith('/#enquire')) track('enquire_click', { from: t.textContent.trim().slice(0, 40) });
  }, true);
})();
