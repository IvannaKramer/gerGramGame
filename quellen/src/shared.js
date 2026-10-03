(() => {
'use strict';

/* ================= Daten: Hier kann die Lehrkraft die Wörter ändern ================= */
/*DATA*/

const PRAISE = ['Richtig!','Super!','Klasse!','Genau!','Prima!','Toll gemacht!','Stark!'];
const RETRY = [
  'Fast! Probier es noch einmal.',
  'Hmm, das passt noch nicht. Sprich das Wort mal laut.',
  'Guter Versuch! Was klingt besser?',
  'Nicht schlimm! Versuch es gleich noch einmal.'
];

/* ================= Hilfen ================= */
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
const reduced = !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
let lastPick = {};
const pick = (arr, key) => { let v; do { v = arr[Math.floor(Math.random() * arr.length)]; } while (arr.length > 1 && v === lastPick[key]); lastPick[key] = v; return v; };
const pairLi = w => `<li><span>${w.ez} →</span> <b>${w.mz}</b></li>`;

const STAR_PATH = 'M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z';
const starSVG = (on, style = '') => `<svg viewBox="0 0 24 24" class="${on ? 'star-on' : 'star-off'}" style="${style}" aria-hidden="true"><path d="${STAR_PATH}" stroke-width="1.6" stroke-linejoin="round"/></svg>`;
const starsRow = n => `<span class="stars" role="img" aria-label="${n} von 3 Sternen">${[0,1,2].map(i => starSVG(i < n)).join('')}</span>`;

function owlSVG(id = '', mood = '') {
  return `<svg class="owl ${mood}" ${id ? `id="${id}"` : ''} viewBox="0 0 120 120" aria-hidden="true">
    <path d="M30 42 L32 12 L52 30 Z" fill="var(--owl)"/>
    <path d="M90 42 L88 12 L68 30 Z" fill="var(--owl)"/>
    <ellipse cx="60" cy="66" rx="40" ry="44" fill="var(--owl)"/>
    <ellipse cx="25" cy="76" rx="9" ry="21" fill="var(--owl-wing)" transform="rotate(14 25 76)"/>
    <ellipse cx="95" cy="76" rx="9" ry="21" fill="var(--owl-wing)" transform="rotate(-14 95 76)"/>
    <ellipse cx="60" cy="84" rx="25" ry="24" fill="var(--owl-belly)"/>
    <path d="M50 80 q4 4 8 0 M62 80 q4 4 8 0 M56 90 q4 4 8 0" fill="none" stroke="var(--owl)" stroke-width="2" stroke-linecap="round" opacity=".45"/>
    <circle cx="44" cy="52" r="16" fill="#fff"/><circle cx="76" cy="52" r="16" fill="#fff"/>
    <g class="eyes-open"><circle cx="46" cy="54" r="7.5" fill="#22304A"/><circle cx="78" cy="54" r="7.5" fill="#22304A"/>
      <circle cx="48.5" cy="51.5" r="2.4" fill="#fff"/><circle cx="80.5" cy="51.5" r="2.4" fill="#fff"/></g>
    <g class="eyes-happy" fill="none" stroke="#22304A" stroke-width="4.5" stroke-linecap="round"><path d="M36 56 Q44 45 52 56"/><path d="M68 56 Q76 45 84 56"/></g>
    <path d="M54 63 L66 63 L60 73 Z" fill="#FFB627" stroke="#D98E00" stroke-width="1.5" stroke-linejoin="round"/>
    <ellipse cx="48" cy="109" rx="7" ry="4" fill="#FFB627"/><ellipse cx="72" cy="109" rx="7" ry="4" fill="#FFB627"/>
  </svg>`;
}
$$('[data-owl]').forEach(slot => { slot.outerHTML = owlSVG(slot.dataset.owlId || ''); });

/* ================= Fortschritt (lokal im Browser) ================= */
const KEY = '/*SLUG*/-' + GAME.id + '-v1';
const fresh = () => ({ stars: 0, best: 0, sound: true });
function load() {
  try {
    const p = JSON.parse(localStorage.getItem(KEY)) || {};
    return { stars: Math.max(0, Math.min(3, p.stars | 0)), best: Math.max(0, p.best | 0), sound: p.sound !== false };
  } catch (e) { return fresh(); }
}
function save() { try { localStorage.setItem(KEY, JSON.stringify(progress)); } catch (e) { /* ohne Speicher weiterspielen */ } }
let progress = load();

/* ================= Ton (erzeugt, keine Dateien) ================= */
let actx = null;
function audio() {
  if (!progress.sound) return null;
  try {
    if (!actx) { const AC = window.AudioContext || window.webkitAudioContext; if (!AC) return null; actx = new AC(); }
    if (actx.state === 'suspended') actx.resume();
  } catch (e) { return null; }
  return actx;
}
function tone(f, at, dur, type = 'sine', vol = .12) {
  const a = audio(); if (!a) return;
  const o = a.createOscillator(), g = a.createGain(), t = a.currentTime + at;
  o.type = type; o.frequency.value = f;
  g.gain.setValueAtTime(.0001, t);
  g.gain.exponentialRampToValueAtTime(vol, t + .02);
  g.gain.exponentialRampToValueAtTime(.0001, t + dur);
  o.connect(g); g.connect(a.destination); o.start(t); o.stop(t + dur + .05);
}
const sfx = {
  pick: () => tone(740, 0, .08, 'sine', .05),
  success: () => { tone(784, 0, .16, 'triangle', .13); tone(1175, .09, .26, 'triangle', .13); },
  fanfare: () => { [523, 659, 784, 1047].forEach((f, i) => tone(f, i * .12, .3, 'triangle', .12)); tone(1319, .52, .7, 'sine', .08); }
};
function renderSound() {
  $$('.sound-btn').forEach(b => {
    b.setAttribute('aria-pressed', String(progress.sound));
    b.setAttribute('aria-label', progress.sound ? 'Ton ausschalten' : 'Ton einschalten');
    b.innerHTML = progress.sound
      ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/><path d="M19 6a8.5 8.5 0 0 1 0 12"/></svg>'
      : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9z"/><path d="M17 9l5 6M22 9l-5 6"/></svg>';
  });
}
$$('.sound-btn').forEach(b => b.addEventListener('click', () => { progress.sound = !progress.sound; save(); renderSound(); if (progress.sound) sfx.pick(); }));
renderSound();

/* ================= Bildschirme ================= */
function show(name) {
  $$('.screen').forEach(s => s.classList.toggle('active', s.id === 'screen-' + name));
  window.scrollTo(0, 0);
}
const gameOn = () => $('#screen-game').classList.contains('active');

function renderStart() {
  const tally = $('#tally');
  tally.hidden = progress.best === 0;
  tally.innerHTML = `${starsRow(progress.stars)}<span>Dein Rekord: ${progress.best} Punkte</span>`;
  $('#start-btn').textContent = progress.best > 0 ? 'Nochmal spielen' : 'Spiel starten';
}
$('#start-btn').addEventListener('click', () => { audio(); startGame(); });

const resetBtn = $('#reset');
let resetTimer = null;
resetBtn.addEventListener('click', () => {
  if (!resetBtn.classList.contains('warn')) {
    resetBtn.classList.add('warn');
    resetBtn.textContent = 'Wirklich löschen? Nochmal tippen.';
    resetTimer = setTimeout(() => { resetBtn.classList.remove('warn'); resetBtn.textContent = 'Fortschritt löschen'; }, 3500);
    return;
  }
  clearTimeout(resetTimer);
  progress = { ...fresh(), sound: progress.sound }; save();
  resetBtn.classList.remove('warn'); resetBtn.textContent = 'Fortschritt gelöscht';
  setTimeout(() => { resetBtn.textContent = 'Fortschritt löschen'; }, 2000);
  renderStart();
});

/* ================= Spielstand, Punkte, Eule ================= */
const state = { score: 0, mistakes: 0, solved: 0, total: 0, busy: false, timers: [] };
function later(fn, ms) {
  const id = setTimeout(() => { state.timers = state.timers.filter(t => t !== id); fn(); }, ms);
  state.timers.push(id);
}
function resetState(total) {
  state.timers.forEach(clearTimeout);
  Object.assign(state, { score: 0, mistakes: 0, solved: 0, total, busy: false, timers: [] });
  const segs = $('#segs');
  segs.style.gridTemplateColumns = `repeat(${total},1fr)`;
  segs.innerHTML = '<span class="seg"></span>'.repeat(total);
  updateHud();
}
function updateHud() {
  $('#progress-text').textContent = `${state.solved} von ${state.total} geschafft`;
  $$('#segs .seg').forEach((s, i) => s.classList.toggle('on', i < state.solved));
  $('#score').textContent = `${state.score} Punkte`;
}
function say(html, mood = 'idle') {
  $('#bubble').innerHTML = html;
  const owl = $('#coach-owl');
  owl.classList.remove('happy', 'think');
  if (mood !== 'idle') { void owl.getBoundingClientRect(); owl.classList.add(mood); }
}
/* Richtig: 10 Punkte beim ersten Versuch, sonst 5 */
function solve(item, el, color) {
  const pts = item.misses === 0 ? 10 : 5;
  item.done = true;
  state.score += pts; state.solved++;
  updateHud(); sfx.success();
  if (el) {
    const r = el.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
    burst(x, y, color); floatPoints('+' + pts, x, y);
  }
}
/* Falsch: kein Fehler-Ton, nur ein Wackeln. Gibt true zurück, wenn jetzt ein Tipp dran ist. */
function miss(item, el) {
  item.misses++; state.mistakes++;
  wobble(el);
  return item.misses >= 2;
}
$('#home').addEventListener('click', () => { state.timers.forEach(clearTimeout); state.timers = []; state.busy = false; renderStart(); show('start'); });

/* ================= Animationen ================= */
function wobble(el) {
  if (reduced || !el || !el.animate) return;
  el.animate([{ rotate: '0deg' }, { rotate: '-5deg' }, { rotate: '5deg' }, { rotate: '-3deg' }, { rotate: '2deg' }, { rotate: '0deg' }],
    { duration: 480, easing: 'ease-in-out' });
}
const fx = $('#fx');
const cssVar = v => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
function burst(x, y, color) {
  if (reduced) return;
  const col = cssVar('--' + color), sun = cssVar('--sun');
  for (let i = 0; i < 14; i++) {
    const s = document.createElement('span');
    s.className = 'spark' + (i % 3 === 0 ? ' star' : '');
    s.style.left = x + 'px'; s.style.top = y + 'px';
    s.style.background = i % 3 === 0 ? sun : col;
    fx.appendChild(s);
    const ang = (i / 14) * Math.PI * 2 + Math.random() * .4, dist = 60 + Math.random() * 50;
    s.animate([{ transform: 'translate(0,0) scale(1)', opacity: 1 },
               { transform: `translate(${Math.cos(ang) * dist}px, ${Math.sin(ang) * dist}px) scale(.3)`, opacity: 0 }],
      { duration: 650, easing: 'cubic-bezier(.2,.8,.3,1)' }).onfinish = () => s.remove();
  }
}
function floatPoints(txt, x, y) {
  const p = document.createElement('span');
  p.className = 'pts'; p.textContent = txt;
  p.style.left = x + 'px'; p.style.top = y + 'px';
  fx.appendChild(p);
  if (reduced) { setTimeout(() => p.remove(), 700); return; }
  p.animate([{ transform: 'translate(-50%,-50%)', opacity: 0 }, { transform: 'translate(-50%,-110%)', opacity: 1, offset: .25 },
             { transform: 'translate(-50%,-260%)', opacity: 0 }], { duration: 900, easing: 'ease-out' }).onfinish = () => p.remove();
}
let confettiRun = 0;
function confetti() {
  if (reduced) return;
  const run = ++confettiRun;
  const c = $('#confetti'), ctx = c.getContext('2d');
  const W = innerWidth, H = innerHeight, dpr = Math.min(2, window.devicePixelRatio || 1);
  c.width = W * dpr; c.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const cols = ['--der', '--die', '--das', '--sun'].map(cssVar).concat('#8B5CF6');
  const parts = [];
  for (let i = 0; i < 170; i++) {
    const left = i % 2 === 0;
    parts.push({ x: left ? -10 : W + 10, y: H * .6 + Math.random() * H * .2,
      vx: (left ? 1 : -1) * (3 + Math.random() * 9), vy: -(9 + Math.random() * 12),
      s: 8 + Math.random() * 8, r: Math.random() * 6.28, vr: (Math.random() - .5) * .35,
      c: cols[i % cols.length], star: Math.random() < .25, wob: Math.random() * 6.28 });
  }
  const drawStar = (r) => {
    ctx.beginPath();
    for (let k = 0; k < 10; k++) {
      const rad = k % 2 ? r * .45 : r, ang = -Math.PI / 2 + k * Math.PI / 5;
      ctx.lineTo(Math.cos(ang) * rad, Math.sin(ang) * rad);
    }
    ctx.closePath(); ctx.fill();
  };
  c.style.display = 'block';
  const t0 = performance.now();
  (function frame(t) {
    if (run !== confettiRun) return;
    const el = t - t0;
    ctx.clearRect(0, 0, W, H);
    ctx.globalAlpha = el > 3000 ? Math.max(0, 1 - (el - 3000) / 900) : 1;
    for (const p of parts) {
      p.vy += .32; p.vx *= .99; p.vy *= .99; p.x += p.vx; p.y += p.vy; p.r += p.vr; p.wob += .12;
      ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.r); ctx.fillStyle = p.c;
      if (p.star) drawStar(p.s * .75);
      else { const h = p.s * .6 * Math.abs(Math.cos(p.wob)) + 1; ctx.fillRect(-p.s / 2, -h / 2, p.s, h); }
      ctx.restore();
    }
    if (el < 3900) requestAnimationFrame(frame);
    else { ctx.clearRect(0, 0, W, H); c.style.display = 'none'; }
  })(t0);
}

/* ================= Geschafft ================= */
function finish() {
  const t = state.total, m = state.mistakes;
  const stars = GAME.stars ? GAME.stars() : (m <= Math.round(t * .1) ? 3 : m <= Math.round(t * .4) ? 2 : 1);
  const record = progress.best > 0 && state.score > progress.best;
  progress.stars = Math.max(progress.stars, stars);
  progress.best = Math.max(progress.best, state.score);
  save();

  let note;
  if (GAME.note) note = GAME.note(stars);
  else if (m === 0) note = 'Kein einziger Fehlversuch. Stark!';
  else if (stars === 3) note = m === 1 ? 'Nur ein Fehlversuch. Super!' : `Nur ${m} Fehlversuche. Super!`;
  else if (stars === 2) note = `Du hattest ${m} Fehlversuche. Spiel nochmal, dann holst du 3 Sterne!`;
  else note = `Du hattest ${m} Fehlversuche. Übung macht den Meister – spiel ruhig nochmal!`;

  const nextBtn = GAME.next
    ? `<a class="btn btn-primary" href="${GAME.next.href}">Nächstes Spiel: ${GAME.next.title}</a>`
    : '<a class="btn btn-primary" href="index.html">Alle Spiele ansehen</a>';
  $('#done-card').innerHTML = `
    ${owlSVG('', 'happy')}
    <h2 class="done-title" id="done-title" tabindex="-1">Geschafft!</h2>
    <div class="big-stars" role="img" aria-label="${stars} von 3 Sternen">
      ${[0, 1, 2].map(i => starSVG(i < stars, `animation-delay:${.25 + i * .22}s`)).join('')}
    </div>
    ${record ? '<p class="record-badge">Neuer Rekord!</p>' : ''}
    <p class="done-text">Du hast alle ${t} ${GAME.unit || 'Wörter'} geschafft und <b>${state.score} Punkte</b> gesammelt.</p>
    <p class="done-text soft">${note}</p>
    <h3 class="review-lead">Alle Lösungen zum Nachlesen</h3>
    ${GAME.review()}
    <div class="actions">${nextBtn}
      <button class="btn btn-secondary" data-act="again">Nochmal spielen</button>
      <button class="btn btn-secondary" data-act="home">Zur Startseite</button></div>`;
  show('done');
  $('#done-title').focus({ preventScroll: true });
  sfx.fanfare();
  confetti();
}
$('#done-card').addEventListener('click', e => {
  const b = e.target.closest('[data-act]');
  if (!b) return;
  confettiRun++; $('#confetti').style.display = 'none';
  if (b.dataset.act === 'again') startGame(); else { renderStart(); show('start'); }
});

/*GAME*/

/* ---------- Los geht's ---------- */
renderStart();
})();
