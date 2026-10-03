/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Punkt oder Strich?': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 2].click();
    },
    'Doppel-Werkstatt': () => { const s = $('#slot'); if (!s || s.classList.contains('filled')) return; $$('.tile')[tmp++ % 3 === 0 ? 0 : 1].click(); },
    'Langes i gesucht': () => {
      /* Karten der Reihe nach antippen: So werden auch Karten mit kurzem i erwischt und der Tipp-Pfad läuft. */
      const h = $('.scard.hint'); if (h) { h.click(); return; }
      const c = $('.scard:not(:disabled)'); c && c.click();
    },
    'Kurz-oder-lang-Entscheider': () => {
      const s = $('#slot'); if (!s || s.classList.contains('filled')) return;
      const h = $('.tile.hint'); if (h && tmp % 2) { tmp++; h.click(); return; }
      $$('.tile')[tmp++ % 2].click();
    },
    'Das verschwundene h': () => {
      const box = $('#letters'); if (box.classList.contains('locked')) return;
      if (box.dataset.w !== word) { word = box.dataset.w; tries = 0; }
      const h = $('.lt.hint'), n = $$('.lt:not(.h)').length;
      if (h) h.click();
      else if (tries > 0) { const on = $('.lt.h'); if (on) on.click(); $$('.lt:not(.h)')[(tries - 1) % (n - 1)].click(); }
      else if (tmp++ % 5 === 0) $$('.lt:not(.h)')[n - 1].click();   /* letzter Buchstabe: nur ein Hinweis, kein h */
      tries++; $('#check').click();
    },
    'Regel-Meister': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#sent').textContent; if (w !== word) { word = w; tries = 0; }
      const pill = $('#bubble .pill');
      if (tries === 0) inp.value = tmp++ % 2 ? 'k' : 'Xyz';
      else if (pill && tries >= 3) inp.value = (tmp++ % 3 === 0 && tries === 3) ? pill.textContent.toUpperCase() : pill.textContent;
      else inp.value = 'Abc' + tries;
      tries++; $('#check').click();
    }
  }
