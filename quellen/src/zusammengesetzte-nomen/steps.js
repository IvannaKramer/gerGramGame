/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Wörter-Puzzle': () => {
      const l = $('#left .pc:not(.done)'); if (!l) return;
      if (!l.classList.contains('selected')) { l.click(); return; }
      const rs = $$('#right .pc:not(.done)');
      const good = rs.find(r => r.dataset.id === l.dataset.id), bad = rs.find(r => r.dataset.id !== l.dataset.id);
      if (!good) { errs.push('no partner'); return; }
      /* jedes dritte Wort: erst zweimal falsch (Tipp-Pfad), dann richtig */
      if (l.dataset.id !== word) { word = l.dataset.id; tries = 0; tmp++; }
      if (tmp % 3 === 0 && tries < 2 && bad) { tries++; bad.click(); return; }
      if (tries === 2 && !good.classList.contains('hint')) errs.push('no hint glow');
      good.click();
    },
    'Wort-Schere': () => {
      if ($('.bench').classList.contains('locked')) return;
      const w = $$('.ltr').map(b => b.textContent).join(''); if (w !== word) { word = w; tries = 0; tmp++; }
      const ls = $$('.ltr');
      if (tries === 0) { tries++; $('#check').click(); return; }                 /* ohne Schere */
      if (tries === 1) { tries++; ls[0].click(); $('#mv-right').click(); $('#check').click(); return; }
      if (tries === 2) { tries++; $('#mv-left').click(); $('#mv-left').click(); $('#check').click(); return; }
      const h = $('.ltr.hint'); if (!h) { errs.push('no hint letter'); return; }
      tries++; h.click(); $('#check').click();
    },
    'Artikel-Chef': () => {
      if ($('#aslot').classList.contains('filled')) return;
      const w = $('.result').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const h = $('.art-btn.hint');
      if (h) { h.click(); return; }
      $$('.art-btn')[(tmp + tries++) % 3].click();
    },
    'Wörter-Baukasten': () => {
      const a = $('#aslot'); if (a && a.classList.contains('filled')) return;
      const h = $('.tile.hint'); if (h) { h.click(); return; }
      const ts = $$('.tile');
      ts[tmp++ % ts.length].click();
    },
    'Wort-Dreher': () => {
      if ($('.built') || $('.dslot.full')) return;
      const h = $('.tile.hint'); if (h) { h.click(); return; }
      const ts = $$('.tile:not(.used)'); if (!ts.length) return;
      ts[tmp++ % ts.length].click();
    },
    'Profi-Werkstatt': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const pill = $('#bubble .pill');
      if (tries === 0) inp.value = 'Xyz';
      else if (pill && tries >= 4) {
        const sol = pill.textContent, noun = sol.slice(4), art = sol.slice(0, 3);
        const other = ['der', 'die', 'das'].find(x => x !== art);
        if (tries === 4 && tmp % 3 === 0) inp.value = art + ' ' + noun.toLowerCase();
        else if (tries === 4 && tmp % 3 === 1) inp.value = other + ' ' + noun;
        else inp.value = sol;
      }
      else inp.value = 'der Abc' + tries;
      tries++; $('#check').click();
    }
  }
