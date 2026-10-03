(() => {
  const errs = []; window.addEventListener('error', e => errs.push(e.message));
  const mode = (location.hash.match(/start|game|play/) || ['play'])[0];
  const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
  const solved = () => parseInt($('#progress-text').textContent);
  const done = () => $('#screen-done').classList.contains('active');
  const G = document.title.split(':')[0];
  if (mode === 'start') return;
  $('#start-btn').click();
  let steps = 0, tmp = 0, word = '', tries = 0;
  const report = () => { document.title = 'RESULT ' + JSON.stringify({ G, done: done(), solved: solved(), score: $('#score').textContent,
    stars: $$('.big-stars .star-on').length, review: $$('.review li').length, note: ($('.done-text.soft') || {}).textContent, errs }); };
  const STEP = /*STEPS*/;
  const iv = setInterval(() => {
    steps++;
    if (done() || steps > 4000 || (mode === 'game' && solved() >= 3 && steps % 9 === 0)) { clearInterval(iv); report(); return; }
    try { STEP[G](); } catch (e) { errs.push('step: ' + e.message); clearInterval(iv); report(); }
  }, 300);
})();
