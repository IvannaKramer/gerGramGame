/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Kurz oder lang?': () => {
      const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return;
      if (tmp % 7 === 0 && !$('#listen').hidden) $('#listen').click();
      $$('.pickbtn')[tmp++ % 2].click();
    },
    'Drei Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      const lb = $('#bubble .listen'); if (lb && tmp % 5 === 0) lb.click();
      $$('.basket')[tmp++ % 3].click();
    },
    'Verlängerungs-Zauber': () => {
      const slot = $('#slot'); if (!slot || slot.classList.contains('filled')) return;
      const st = $('#stretch');
      if (!st.disabled) { if (tmp++ % 3 === 0) $$('.tile')[0].click(); st.click(); return; }
      if (tmp % 4 === 0 && !$('#listen').hidden) $('#listen').click();
      $$('.tile')[tmp++ % 3].click();
    },
    'Lücken-Geschichte': () => { if (!$('.sl.now')) return; $$('.tile')[tmp++ % 3].click(); },
    'Wortfamilien-Werkstatt': () => {
      const rows = $$('.frow:not(.ok)'); if (!rows.length) return;
      if (tries++ % 5 === 0) { $('#check').click(); return; }   /* auch mit leeren Lücken prüfen */
      const empty = rows.filter(r => !r.querySelector('.opt[aria-pressed="true"]'));
      if (empty.length) { const h = empty[0].querySelector('.opt.hint'), o = empty[0].querySelectorAll('.opt'); (h || o[Math.floor(Math.random() * 3)]).click(); return; }
      $('#check').click();
    },
    'Schreib-Meister': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#mark').textContent; if (w !== word) { word = w; tries = 0; }
      const pill = $('#bubble .pill');
      if (tries === 0) inp.value = 'Xyz';
      else if (tries === 1) inp.value = $('#mark').innerHTML.replace(/<i.*<\/i>/, 'ss');
      else if (pill && tries >= 3) inp.value = (tmp++ % 3 === 0 && tries === 3) ? pill.textContent.toUpperCase() : pill.textContent;
      else inp.value = 'Abc' + tries;
      tries++; $('#check').click();
    }
  }
