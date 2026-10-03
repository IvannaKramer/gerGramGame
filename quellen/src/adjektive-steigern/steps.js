/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Siegertreppchen': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      const st = $$('.step:not(.filled)');
      st.length && st[tmp++ % st.length].click();
    },
    'Wie oder als?': () => { if ($('.gap.filled')) return; $$('.tile')[tmp++ % 2].click(); },
    'Stufe gesucht': () => { if ($('.opt.right')) return; const b = $$('.opt:not(:disabled)'); b.length && b[tmp++ % b.length].click(); },
    'Stufen-Werkstatt': () => {
      if ($('#build').classList.contains('locked')) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; if (tmp++ % 5 === 0) { $('#check').click(); return; } }
      $$('.stem-tile')[tries % 2].click(); $$('.end-tile')[Math.floor(tries / 2) % 3].click();
      tries++; $('#check').click();
    },
    'Treppauf, treppab': () => {
      if ($('.gap.filled')) return;
      const w = $('#sentence').textContent; if (w !== word && !$('.gap.on')) { word = w; tries = 0; }
      $$('.lvl')[tries % 3].click(); tries++; $('#check').click();
    },
    'Steigerungs-Meister': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; }
      const pill = $('#bubble .pill');
      if (tries === 0) inp.value = tmp % 2 ? 'xyz' : $('#lbl .adj').textContent;
      else if (pill && tries >= 3) inp.value = (tmp++ % 3 === 0 && tries === 3) ? pill.textContent.toUpperCase() : (tmp % 2 ? 'am ' + pill.textContent : pill.textContent);
      else inp.value = 'abc' + tries;
      tries++; $('#check').click();
    }
  }
