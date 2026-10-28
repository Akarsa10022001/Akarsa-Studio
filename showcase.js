/* Akarsa Studio: film rail, film player and the 3D monogram.
   Runs on its own, without GSAP, so the work always shows. */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- film player (YouTube, no cookies) ---------- */
  let box;
  const openFilm = (id, title) => {
    if (!box) {
      box = document.createElement('div');
      box.className = 'player';
      box.setAttribute('role', 'dialog');
      box.setAttribute('aria-modal', 'true');
      box.innerHTML = '<button class="player__x" aria-label="Close film">×</button><div class="player__frame"></div><p class="player__cap"></p>';
      document.body.appendChild(box);
      box.addEventListener('click', e => { if (e.target === box || e.target.closest('.player__x')) closeFilm(); });
      addEventListener('keydown', e => { if (e.key === 'Escape') closeFilm(); });
    }
    $('.player__frame', box).innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&playsinline=1&rel=0&modestbranding=1&loop=1&playlist=${id}" title="${title}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>`;
    $('.player__cap', box).textContent = title;
    box.classList.add('is-open');
    document.documentElement.classList.add('is-playing');
    $('.player__x', box).focus();
  };
  const closeFilm = () => {
    if (!box) return;
    box.classList.remove('is-open');
    document.documentElement.classList.remove('is-playing');
    $('.player__frame', box).innerHTML = '';
  };
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-yt]');
    if (!t) return;
    e.preventDefault();
    openFilm(t.dataset.yt, t.dataset.title || 'Akarsa Studio film');
  });

  /* ---------- film rail: arrows, drag and 3D tilt ---------- */
  $$('.films').forEach(wrap => {
    const rail = $('.films__rail', wrap);
    const step = () => (rail.querySelector('.film')?.offsetWidth || 300) + 24;
    $('.films__prev', wrap)?.addEventListener('click', () => rail.scrollBy({ left: -step() * 2, behavior: 'smooth' }));
    $('.films__next', wrap)?.addEventListener('click', () => rail.scrollBy({ left: step() * 2, behavior: 'smooth' }));
    if (reduce) return;
    $$('.film', rail).forEach(card => {
      card.addEventListener('pointermove', e => {
        if (e.pointerType !== 'mouse') return;
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        card.style.setProperty('--rx', `${(-y * 8).toFixed(2)}deg`);
        card.style.setProperty('--ry', `${(x * 10).toFixed(2)}deg`);
        card.style.setProperty('--gx', `${((x + 0.5) * 100).toFixed(0)}%`);
      });
      card.addEventListener('pointerleave', () => { card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg'); });
    });
  });

  /* ---------- count-up numbers ---------- */
  const nums = $$('[data-to]');
  if (nums.length) {
    const run = el => {
      const to = parseFloat(el.dataset.to), dec = (el.dataset.to.split('.')[1] || '').length, suf = el.dataset.suf || '';
      if (reduce) { el.textContent = to.toFixed(dec) + suf; return; }
      const t0 = performance.now(), d = 1400;
      const tick = t => { const k = Math.min(1, (t - t0) / d), v = to * (1 - Math.pow(1 - k, 3)); el.textContent = v.toFixed(dec) + suf; if (k < 1) requestAnimationFrame(tick); };
      requestAnimationFrame(tick);
    };
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } }), { threshold: 0.6 });
    nums.forEach(n => io.observe(n));
  }

  /* ---------- dashboard bars grow when seen ---------- */
  $$('.dash').forEach(d => new IntersectionObserver(([e], o) => { if (e.isIntersecting) { d.classList.add('go'); o.disconnect(); } }, { threshold: 0.4 }).observe(d));

  /* ---------- 3D monogram (three.js, loaded only when it comes into view) ---------- */
  const stage = $('.glyph3d');
  if (!stage) return;
  const canTry = (() => { try { const c = document.createElement('canvas'); return !!(c.getContext('webgl2') || c.getContext('webgl')); } catch (e) { return false; } })();
  if (!canTry) return;
  const GLYPH = 'M300,122 L172,246 L243,250 A71,93 0 0 1 172,343 L172,396 A128,140 0 0 0 300,256 Z M313,256 L372,256 A75,87 0 0 0 447,343 L447,396 A134,140 0 0 1 313,256 Z';

  const build = () => {
    const THREE = window.THREE;
    if (!THREE) return;
    const canvas = document.createElement('canvas');
    canvas.className = 'glyph3d__canvas';
    canvas.setAttribute('aria-hidden', 'true');
    stage.prepend(canvas);
    const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.15;
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(30, 1, 1, 5000);
    camera.position.set(0, 0, 900);

    // a soft studio to reflect in: cream walls and a few warm light strips
    const pm = new THREE.PMREMGenerator(renderer);
    const room = new THREE.Scene();
    room.add(new THREE.Mesh(new THREE.BoxGeometry(60, 60, 60), new THREE.MeshBasicMaterial({ color: 0x2a2418, side: THREE.BackSide })));
    const strip = (w, h, x, y, z, ry, c) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ color: c, side: THREE.DoubleSide })); m.position.set(x, y, z); m.rotation.y = ry; room.add(m); };
    strip(40, 6, 0, 22, -20, 0, 0xfff1d6);
    strip(6, 40, -26, 0, 0, Math.PI / 2, 0xffe2b0);
    strip(6, 30, 26, -4, 6, -Math.PI / 2, 0xf7f2e6);
    strip(30, 3, 0, -24, 10, 0, 0xb39a62);
    scene.environment = pm.fromScene(room, 0.03).texture;

    // trace the SVG monogram into shapes
    const svgNS = 'http://www.w3.org/2000/svg';
    const shapes = GLYPH.split(/(?=M)/).map(d => {
      const p = document.createElementNS(svgNS, 'path');
      p.setAttribute('d', d.trim());
      const len = p.getTotalLength(), n = 220, pts = [];
      for (let i = 0; i < n; i++) { const q = p.getPointAtLength((i / n) * len); pts.push(new THREE.Vector2(q.x - 310, -(q.y - 259))); }
      return new THREE.Shape(pts);
    });
    const geo = new THREE.ExtrudeGeometry(shapes, { depth: 46, bevelEnabled: true, bevelThickness: 7, bevelSize: 4, bevelSegments: 6, curveSegments: 4 });
    geo.center();
    const gold = new THREE.MeshPhysicalMaterial({ color: 0xd4b277, metalness: 1, roughness: 0.24, clearcoat: 0.4, clearcoatRoughness: 0.2 });
    const mesh = new THREE.Mesh(geo, gold);
    scene.add(mesh);
    const key = new THREE.DirectionalLight(0xfff3dc, 1.2); key.position.set(300, 400, 600); scene.add(key);

    let w = 0, h = 0;
    const size = () => { const r = stage.getBoundingClientRect(); if (r.width === w && r.height === h) return; w = r.width; h = r.height; renderer.setSize(w, h, false); camera.aspect = w / h; camera.position.z = 900 / Math.min(1, camera.aspect * 1.05); camera.updateProjectionMatrix(); };
    let mx = 0, my = 0, live = false, raf = 0, t0 = performance.now();
    stage.addEventListener('pointermove', e => { const r = stage.getBoundingClientRect(); mx = (e.clientX - r.left) / r.width - 0.5; my = (e.clientY - r.top) / r.height - 0.5; });
    stage.addEventListener('pointerleave', () => { mx = my = 0; });
    const frame = t => {
      size();
      const s = (t - t0) / 1000;
      mesh.rotation.y += ((reduce ? 0.25 : Math.sin(s * 0.45) * 0.55) + mx * 0.8 - mesh.rotation.y) * 0.06;
      mesh.rotation.x += (my * 0.4 + 0.05 - mesh.rotation.x) * 0.06;
      mesh.position.y = reduce ? 0 : Math.sin(s * 0.9) * 6;
      renderer.render(scene, camera);
      if (live) raf = requestAnimationFrame(frame);
    };
    new IntersectionObserver(([e]) => { live = e.isIntersecting; cancelAnimationFrame(raf); if (live) raf = requestAnimationFrame(frame); }).observe(stage);
    stage.classList.add('is-3d');
  };

  const io3 = new IntersectionObserver(([e]) => {
    if (!e.isIntersecting) return;
    io3.disconnect();
    if (window.THREE) return build();
    const s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/npm/three@0.149.0/build/three.min.js';
    s.onload = build;
    document.head.appendChild(s);
  }, { rootMargin: '400px' });
  io3.observe(stage);
})();
