/* ---------- Ziehen mit Maus, Finger oder Stift ---------- */
let drag = null, suppressClick = false;
function enableDrag(srcSel, tgtSel, onDrop) {
  document.addEventListener('pointerdown', e => {
    if (e.button !== 0 || state.busy || !gameOn()) return;
    const src = e.target.closest(srcSel);
    if (!src) return;
    audio();
    drag = { src, x0: e.clientX, y0: e.clientY, id: e.pointerId, moved: false, ghost: null, over: null };
    try { src.setPointerCapture(e.pointerId); } catch (_) {}
  });
  document.addEventListener('pointermove', e => {
    if (!drag || e.pointerId !== drag.id) return;
    const dx = e.clientX - drag.x0, dy = e.clientY - drag.y0;
    if (!drag.moved) {
      if (Math.hypot(dx, dy) < 10) return;
      drag.moved = true;
      const r = drag.src.getBoundingClientRect();
      const g = drag.src.cloneNode(true);
      g.classList.add('ghost');
      g.classList.remove('selected', 'drop-over', 'hint');
      g.setAttribute('aria-hidden', 'true');
      g.removeAttribute('data-id');
      g.style.cssText += `;left:${r.left}px;top:${r.top}px;width:${r.width}px;height:${r.height}px;right:auto;bottom:auto;`;
      document.body.appendChild(g);
      drag.ghost = g;
      drag.src.classList.add('dragging');
    }
    drag.ghost.style.transform = `translate(${dx}px, ${dy}px) rotate(3deg) scale(1.06)`;
    const under = document.elementFromPoint(e.clientX, e.clientY);
    const tgt = under ? under.closest(tgtSel) : null;
    if (tgt !== drag.over) {
      if (drag.over) drag.over.classList.remove('drop-over');
      if (tgt) tgt.classList.add('drop-over');
      drag.over = tgt;
    }
  });
  const end = (e, cancelled) => {
    if (!drag || e.pointerId !== drag.id) return;
    const d = drag; drag = null;
    if (!d.moved) return;
    suppressClick = true; setTimeout(() => { suppressClick = false; }, 80);
    d.src.classList.remove('dragging');
    if (d.over) d.over.classList.remove('drop-over');
    if (d.over && !cancelled) { d.ghost.remove(); onDrop(d.src, d.over); }
    else if (reduced || !d.ghost.animate) d.ghost.remove();
    else d.ghost.animate([{ transform: d.ghost.style.transform }, { transform: 'translate(0,0) rotate(0deg) scale(1)' }],
      { duration: 220, easing: 'ease-out' }).onfinish = () => d.ghost.remove();
  };
  document.addEventListener('pointerup', e => end(e, false));
  document.addEventListener('pointercancel', e => end(e, true));
}
