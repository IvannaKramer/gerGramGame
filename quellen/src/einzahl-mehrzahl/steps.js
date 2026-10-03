/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Mehrzahl-Memory': () => {
      const openC = $$('.mcard.open:not(.found)'), closed = $$('.mcard:not(.open)');
      if (openC.length >= 2) return;
      if (!openC.length) { closed[0] && closed[0].click(); return; }
      const o = openC[0], pic = o.querySelector('.pic').textContent, ez = o.classList.contains('ez');
      if (tmp++ % 4 === 0) { closed[closed.length - 1].click(); return; }
      const want = ez ? pic + pic : pic.slice(0, pic.length / 2);
      const p = closed.find(c => c.classList.contains(ez ? 'mz' : 'ez') && c.querySelector('.pic').textContent === want);
      p ? p.click() : errs.push('no partner for ' + pic);
    },
    'Eins oder viele?': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 2].click();
    },
    'Ballon-Mehrzahl': () => { const b = $('.balloon:not(:disabled):not(.pop):not(.away)'); b && b.click(); },
    'Endungs-Werkstatt': () => { if (!$('#slot') || $('#slot').classList.contains('filled')) return; $$('.tile')[tmp++ % 5].click(); },
    'Umlaut-Zauber': () => {
      if ($('#spell').classList.contains('locked')) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; }
      $$('button.lt.on').forEach(b => b.click());
      const can = $$('button.lt');
      if (tries > 0) { const b = $$('button.lt')[(tries - 1) % can.length]; b.click(); }
      tries++; $('#check').click();
    },
    'Mehrzahl-Meister': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; }
      const pill = $('#bubble .pill.mz');
      if (tries === 0) inp.value = 'Xyz';
      else if (pill && tries >= 3) inp.value = (tmp++ % 3 === 0 && tries === 3) ? pill.textContent.slice(4).toLowerCase() : (tmp % 2 ? pill.textContent : pill.textContent.slice(4));
      else inp.value = 'Abc' + tries;
      tries++; $('#check').click();
    }
  }
