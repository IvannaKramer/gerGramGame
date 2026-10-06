/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Drei Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 3].click();
    },
    'Artikel-Zwillinge': () => {
      const openC = $$('.mcard.open:not(.found)'), closed = $$('.mcard:not(.open)');
      if (openC.length >= 2) return;
      if (!openC.length) { closed[0] && closed[0].click(); return; }
      const o = openC[0], pic = o.querySelector('.pic').textContent, best = o.classList.contains('best');
      if (tmp++ % 4 === 0) { closed[closed.length - 1].click(); return; }
      const p = closed.find(c => c.classList.contains(best ? 'unb' : 'best') && c.querySelector('.pic').textContent === pic);
      p ? p.click() : errs.push('no partner for ' + pic);
    },
    'Ein oder eine?': () => { if ($('#gap') && !$('#gap').classList.contains('filled')) $$('.tile')[tmp++ % 3 === 0 ? 0 : (tmp % 2)].click(); },
    'Artikel-Jagd': () => {
      if ($('.wbtn.solved')) return;
      const s = $('#sentence').textContent; if (s !== word) { word = s; tries = 0; }
      if (!$('.wbtn.found')) {
        if ($$('.tile').some(t => !t.disabled)) errs.push('tiles active too early');
        const b = $$('.wbtn'); b[(b.length - 1 + tries++ * (b.length - 1)) % b.length].click(); return;
      }
      $$('.tile')[tmp++ % 3 === 0 ? 0 : (tmp % 2)].click();
    },
    'Neu oder bekannt?': () => { if ($('.lgap.cur:not(.filled)')) $$('.tile')[tmp++ % 5].click(); },
    'Wörterbuch-Profi': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const seq = ['', w, 'ein ' + w, 'xy ' + w, 'der Quatsch', 'der ' + w.toLowerCase(), 'die ' + w.toLowerCase(), 'das ' + w.toLowerCase(), 'Der ' + w, 'die  ' + w, ' das ' + w];
      if (tmp % 4 === 0 && tries === 2) { $('#lookup').click(); if ($('#dict').hidden) errs.push('no dict'); }
      if (tmp % 3 === 0 && tries === 0) tries = 8;
      inp.value = seq[Math.min(tries, 8) + (tries > 8 ? (tries - 8) % 3 : 0)];
      tries++; $('#check').click();
    }
  }
