/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Umlaut-Zauber': () => { const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return; $$('.tile')[tmp++ % 2].click(); },
    'Wortfamilien-Suche': () => {
      const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return;
      const opts = $$('.opt:not(:disabled)');
      if (opts.length) { opts[tmp++ % opts.length].click(); return; }
      const tiles = $$('.tile'); tiles.length && tiles[tmp++ % 2].click();
    },
    'Merkwort-Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 2].click();
    },
    'Lücken-Blitz': () => { const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return; $$('.tile')[tmp++ % 4].click(); },
    'Familien-Treffen': () => {
      const open = $$('.fcard:not(:disabled)'); if (!open.length) return;
      open[tmp++ % open.length].click();
    },
    'Schreib-Profi': () => {
      const inp = $('#answer'); if (inp.readOnly) { tries = 0; return; }
      const pill = $('#bubble .pill');
      if (pill && tries >= 3) inp.value = (tmp++ % 3 === 0 && tries === 3) ? pill.textContent.toUpperCase() : pill.textContent;
      else inp.value = 'Abc' + tries;
      tries++; $('#check').click();
    }
  }
