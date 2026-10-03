/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Signalwörter-Jagd': () => {
      const t = $('#target'); if (!t || t.classList.contains('filled')) return;
      const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const all = tmp % 2 ? [...$$('.tok'), $('#none')] : [$('#none'), ...$$('.tok')];
      all[tries++ % all.length].click();
    },
    'Zwei Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 2].click();
    },
    'Groß oder klein?': () => { if ($('#gap') && !$('#gap').classList.contains('filled')) $$('.tile')[tmp++ % 3 === 0 ? 0 : (tmp % 2)].click(); },
    'Fehler-Detektiv': () => {
      if ($('#sentence').classList.contains('solved') || !$('.tok')) return;
      const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const all = tmp % 2 ? [...$$('.tok')].reverse().concat($('#ok')) : [$('#ok'), ...$$('.tok')];
      all[tries++ % all.length].click();
    },
    'Adjektiv-Werkstatt': () => { if ($('#gap') && !$('#gap').classList.contains('filled')) $$('.tile')[tmp++ % 4].click(); },
    'Großschreib-Profi': () => {
      const ins = $$('#sentence input'); if (!ins.length || ins.every(i => i.readOnly)) return;
      const w = $$('.capl').map(c => c.textContent).join(' '); if (w !== word) { word = w; tries = 0; tmp++; }
      const open = ins.filter(i => !i.readOnly), capOf = i => i.parentNode.querySelector('.capl').textContent;
      const lower = i => capOf(i).toLowerCase(), upper = i => capOf(i)[0] + capOf(i).slice(1).toLowerCase();
      const pills = $$('#bubble .pill.gr, #bubble .pill.kl');
      const slow = tmp % 3 === 0;
      if (tries === 0) open.forEach(i => { i.value = ''; });
      else if (tries === 1) open.forEach(i => { i.value = 'xyz'; });
      else if (slow && tries < 5) open.forEach(i => { i.value = lower(i); });
      else if (slow && tries < 8) open.forEach(i => { i.value = upper(i); });
      else if (slow && pills.length === ins.length) ins.forEach((i, n) => { if (!i.readOnly) i.value = pills[n].textContent; });
      else open.forEach(i => { i.value = tries % 2 ? upper(i) : lower(i); });
      tries++; $('#check').click();
    }
  }
