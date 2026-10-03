/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Verlängerungs-Trick': () => {
      const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return;
      const st = $('#stretch');
      if (!st.disabled) { if (tmp++ % 3 === 0) $$('.tile')[0].click(); st.click(); return; }
      $$('.tile')[tmp++ % 2].click();
    },
    'Buchstaben-Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 6].click();
    },
    'Verlängerungs-Memory': () => {
      const openC = $$('.mcard.open:not(.found)'), closed = $$('.mcard:not(.open)');
      if (openC.length >= 2) return;
      if (!openC.length) { closed[0] && closed[0].click(); return; }
      const o = openC[0];
      if (tmp++ % 4 === 0) { closed[closed.length - 1].click(); return; }
      const p = closed.find(c => c.dataset.p === o.dataset.p);
      p ? p.click() : errs.push('no partner for ' + o.dataset.p);
    },
    'Welches Wort hilft?': () => {
      const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return;
      const opts = $$('.opt:not(:disabled)');
      if (opts.length) { opts[tmp++ % opts.length].click(); return; }
      const tiles = $$('.tile'); tiles.length && tiles[tmp++ % 2].click();
    },
    'Grundform-Trick': () => { const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return; $$('.tile')[tmp++ % 4].click(); },
    'Fehler-Detektiv': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      if ($('#form').hidden) { const h = $('.tok.hint') || $('.tok:not(:disabled)'); h && h.click(); tries = 0; return; }
      const pill = $('#bubble .pill');
      if (tries === 0) inp.value = $('.tok.found').textContent;
      else if (pill && tries >= 3) inp.value = (tmp++ % 3 === 0 && tries === 3) ? pill.textContent.toUpperCase() : pill.textContent;
      else inp.value = 'Abc' + tries;
      tries++; $('#check').click();
    }
  }
