/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Proben-Lupe': () => { if ($('#gap') && !$('#gap').classList.contains('filled')) $$('.tile')[tmp++ % 3 === 0 ? 0 : (tmp % 2)].click(); },
    'Zwei Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 2].click();
    },
    'Komma-Wächter': () => {
      if ($('#sentence').classList.contains('solved')) return;
      const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; }
      const all = [...$$('.cgap')].reverse().concat($('#none'), $('#none'));
      all[tries++ % all.length].click();
    },
    'Wort-Detektiv': () => { if ($('#gap') && !$('#gap').classList.contains('filled')) $$('.tile')[tmp++ % 4].click(); },
    'Lücken-Geschichten': () => {
      if (!$('.lgap.cur')) return;
      tmp++;
      if (tmp % 7 === 0) { $('#lupe').click(); if (!/Probe/.test($('#bubble').textContent)) errs.push('no probe'); return; }
      if (tmp % 5 === 0) { const g = $$('.lgap:not(.filled)'); g[g.length - 1].click(); return; }
      $$('.tile')[tmp % 2].click();
    },
    'Schreib-Profi': () => {
      const ins = $$('#sentence input'); if (!ins.length || ins.every(i => i.readOnly)) return;
      const w = $('#sentence').textContent + ins.length; if (w !== word) { word = w; tries = 0; tmp++; }
      const pills = $$('#bubble .pill');
      if (tmp % 3 === 0 && tries === 0) { tries = 3; }
      if (tries === 0) ins.forEach(i => { if (!i.readOnly) i.value = ''; });
      else if (tries === 1) ins.forEach(i => { if (!i.readOnly) i.value = 'das'; });
      else if (tries === 2) ins.forEach(i => { if (!i.readOnly) i.value = 'dass'; });
      else if (tries === 3) ins.forEach(i => { if (!i.readOnly) i.value = 'Dass'; });
      else if (tries === 4) ins.forEach(i => { if (!i.readOnly) i.value = 'Das'; });
      else if (tries === 5) ins.forEach(i => { if (!i.readOnly) i.value = 'daß'; });
      else if (pills.length === ins.length) ins.forEach((i, n) => { if (!i.readOnly) i.value = pills[n].textContent; });
      else ins.forEach(i => { if (!i.readOnly) i.value = tries % 2 ? 'das' : 'dass'; });
      tries++; $('#check').click();
    }
  }
