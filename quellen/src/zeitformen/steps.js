/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Zeit-Sortierer': () => {
      if ($('#card').classList.contains('solved')) return;
      $$('.basket')[tmp++ % 4].click();
    },
    'Verb-Memory': () => {
      const P = { tanzen: 'er tanzte', weinen: 'er weinte', 'hören': 'er hörte', baden: 'er badete', 'träumen': 'er träumte', 'zählen': 'er zählte', schwimmen: 'er schwamm',
        rufen: 'er rief', reiten: 'er ritt', stehen: 'er stand', sitzen: 'er saß', liegen: 'er lag', denken: 'er dachte', frieren: 'er fror', graben: 'er grub' };
      const text = c => c.querySelector('.word').textContent;
      const openC = $$('.mcard.open:not(.found)'), closed = $$('.mcard:not(.open)');
      if (openC.length >= 2) return;
      if (!openC.length) { closed[0] && closed[0].click(); return; }
      const o = openC[0], gf = o.classList.contains('gf');
      if (tmp++ % 4 === 0) { closed[closed.length - 1].click(); return; }
      const want = gf ? P[text(o)] : Object.keys(P).find(k => P[k] === text(o));
      const p = closed.find(c => text(c) === want);
      p ? p.click() : errs.push('no partner for ' + text(o));
    },
    'Zwei-Teile-Detektiv': () => {
      if ($('#toks').classList.contains('solved')) return;
      const t = $('.tok:not(.hit):not(:disabled)'); t && t.click();
    },
    'Zeitmaschine': () => {
      if ($('#outcard').classList.contains('arrived')) return;
      const o = $('.opt:not(:disabled)'); o && o.click();
    },
    'Perfekt-Baukasten': () => {
      const b = (tmp++ % 2 ? $('#parts button:not(:disabled)') : null) || $('#kit button:not(:disabled)'); b && b.click();
    },
    'Verb-Meister': () => {
      const a = $('#a1'), b = $('#a2'); if (a.readOnly && b.readOnly) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const set = (el, v) => { if (!el.readOnly) el.value = v; };
      const pt = $('#bubble .pill.pt'), pf = $('#bubble .pill.pf');
      if (tries === 0) { set(a, 'xyz'); set(b, tmp % 2 ? 'hat xyz' : ''); if (tmp % 2 === 0) tries = -2; }
      else if (tries < 0) { set(b, 'ist abc'); tries = 0; }
      else if (pt && pf && tries >= 3) {
        const mode = tries === 3 ? tmp % 4 : 9;
        set(a, mode === 1 ? pt.textContent.toUpperCase() : pt.textContent);
        set(b, mode === 2 ? pf.textContent.split(' ')[1] : mode === 3 ? (pf.textContent.startsWith('hat') ? 'ist ' : 'hat ') + pf.textContent.split(' ')[1] : pf.textContent);
      }
      else { set(a, 'abc' + tries); set(b, 'hat abc' + tries); }
      tries++; $('#check').click();
    }
  }
