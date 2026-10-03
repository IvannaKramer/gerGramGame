/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Satz-Zug': () => {
      if ($('#train').classList.contains('solved') || !$('.wagon')) return;
      const key = $('#pic').textContent; if (key !== word) { word = key; tries = 0; tmp++; }
      if (tries < tmp % 3) { tries++; $('#check').click(); return; }           /* absichtlich falsch prüfen */
      const v = $('.wagon.vb');
      if (v.dataset.pos !== '1') {
        if (tmp % 2) { if (!$('.wagon.selected')) v.click(); else $('.wagon[data-pos="1"]').click(); }
        else { v.focus(); v.dispatchEvent(new KeyboardEvent('keydown', { key: v.dataset.pos === '0' ? 'ArrowRight' : 'ArrowLeft', bubbles: true })); }
        return;
      }
      $('#check').click();
    },
    'Welcher Satz stimmt?': () => {
      if ($('.opt.good')) return;
      const o = $$('.opt:not(:disabled)'); if (!o.length) return;
      if (tmp++ % 2) o[0].click(); else document.dispatchEvent(new KeyboardEvent('keydown', { key: String(+o[o.length - 1].dataset.i + 1) }));
    },
    'Satzglieder zählen': () => {
      if ($('#base .chip.vb') && !$('.num.hint')) return;
      if (tmp % 5 === 0 && !$('#again').hidden) $('#again').click();
      $$('.num')[tmp++ % 4].click();
    },
    'Satz-Schere': () => {
      if (!$('.gap')) return;
      const KNOWN = { 'Die Ärztin hilft dem kranken Kind.': [0, 1, 2], 'Meine Oma strickt warme Socken.': [1, 2], 'Der Mond leuchtet in der Nacht hell.': [1, 2, 5] };
      const key = $$('#cut .w').map(w => w.textContent).join(' '); if (key !== word) { word = key; tries = 0; }
      const hints = $$('.gap.hint');
      if (hints.length) { hints[0].click(); return; }
      if (KNOWN[key] && tries === 0) { tries = 9; KNOWN[key].forEach(i => $(`.gap[data-i="${i}"]`).click()); return; }
      if (tries === 0) { $('#check').click(); if (!/Setze zuerst/.test($('#bubble').textContent)) errs.push('leere Prüfung'); }
      if (tries === 1) $('.gap').click();
      tries++; $('#check').click();
    },
    'Neuer Satzanfang': () => {
      if ($('#build .chip')) return;
      const key = $('#base').textContent; if (key !== word) { word = key; tries = 0; tmp++; }
      const free = () => $$('#tiles .wtile:not(.used)');
      const put = t => { const b = free().find(x => x.textContent.toLowerCase() === t.toLowerCase()); if (!b) { errs.push('kein Wort ' + t); return; } b.click(); };
      const clear = () => { let n = 0; while ($('#build .wtile') && n++ < 30) $('#build .wtile').click(); };
      const start = $('#build .start').textContent.toLowerCase().split(' ');
      const base = key.slice(0, -1).split(' ');
      const at = base.findIndex((_, i) => start.every((w, k) => (base[i + k] || '').toLowerCase() === w));
      const rest = base.filter((_, i) => i < at || i >= at + start.length);
      let want;
      if (tmp % 4 === 0 && tries < 2) { if (tries === 0) $('#check').click(); want = rest; }      /* falsch: Verb nicht vorn */
      else {
        const pills = $$('#bubble .pill');
        if (pills.length > 1) want = pills.map(p => p.textContent).join(' ').split(' ');           /* Tipp ablesen */
        else { const sub = tries === 0 ? 1 : 2; want = [rest[sub], ...rest.slice(0, sub), ...rest.slice(sub + 1)]; }
      }
      clear(); want.forEach(put);
      tries++; $('#check').click();
    },
    'Satzanfang-Profi': () => {
      if ($('.cand.good') || !$('.cand')) return;
      const KNOWN = { 'Der freche Papagei ruft den ganzen Vormittag lustige Wörter.': ['den ganzen Vormittag', 'lustige Wörter'],
        'Der alte Fischer repariert vor dem Sturm sein kaputtes Netz.': ['vor dem Sturm', 'sein kaputtes Netz'] };
      const key = $('#base').textContent; if (key !== word) { word = key; tries = 0; }
      const text = c => c.firstChild.textContent;
      if (KNOWN[key] && tries === 0) { tries = 9; $$('.cand').filter(c => KNOWN[key].includes(text(c))).forEach(c => c.click()); return; }
      const hints = $$('.cand.hint');
      if (hints.length) { hints[0].click(); return; }
      if (tries === 0) { $('#check').click(); if (!/Wähle zuerst/.test($('#bubble').textContent)) errs.push('leere Prüfung'); $$('.cand')[0].click(); document.dispatchEvent(new KeyboardEvent('keydown', { key: '2' })); }
      tries++; $('#check').click();
    }
  }
