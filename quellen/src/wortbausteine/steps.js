/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Baustein-Detektiv': () => {
      const b = $$('.blk'); if (!b.length || b[0].classList.contains('on')) return;
      b[tmp++ % b.length].click();
    },
    'Wortfamilien-Häuser': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.house')[tmp++ % 3].click();
    },
    'Groß oder klein?': () => {
      const s = $('#slot'); if (!s || s.classList.contains('filled')) return;
      $$('.case')[Math.floor(tmp++ / 2) % 2].click();
    },
    'Baustein-Werkstatt': () => { if (!$('#slot') || $('#slot').classList.contains('filled')) return; $$('.tile')[tmp++ % 4].click(); },
    'Vorsilben-Lücke': () => {
      const g = $('#gap'); if (!g || g.classList.contains('filled')) return;
      const o = $$('.opt:not(:disabled)'); o[tmp++ % o.length].click();
    },
    'Nomen-Meister': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; }
      const pill = $('#bubble .pill.sol');
      if (tries === 0) inp.value = 'Xyz';
      else if (pill && tries >= 3) inp.value = (tmp++ % 3 === 0 && tries === 3) ? pill.textContent.slice(4).toLowerCase() : (tmp % 2 ? pill.textContent : pill.textContent.slice(4));
      else inp.value = 'Abc' + tries;
      tries++; $('#check').click();
    }
  }
