/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'ABC-Nachbarn': () => {
      if ($('.lt.gap.filled') || !$('.opt')) return;
      const o = $$('.opt:not(:disabled)'); if (!o.length) return;
      if (tmp++ % 2) o[0].click(); else document.dispatchEvent(new KeyboardEvent('keydown', { key: String($$('.opt').indexOf(o[o.length - 1]) + 1) }));
    },
    'ABC-Raupe': () => {
      if ($('#row').classList.contains('solved') || !$('.wcard')) return;
      const k = s => s.toLowerCase().replace(/ä/g, 'a').replace(/ö/g, 'o').replace(/ü/g, 'u');
      const now = $$('.wcard .w').map(w => w.textContent), want = now.slice().sort((a, b) => k(a) < k(b) ? -1 : 1);
      const id = want.join(); if (id !== word) { word = id; tries = 0; tmp++; }
      if (tries < tmp % 3) { tries++; $('#check').click(); if ($('#row').classList.contains('solved')) errs.push('falsche Reihe angenommen'); return; }
      const p = now.findIndex((w, i) => w !== want[i]);
      if (p < 0) { $('#check').click(); return; }
      const from = now.indexOf(want[p]);
      if (tmp % 2) { if (!$('.wcard.selected')) $$('.wcard')[from].click(); else $$('.wcard')[p].click(); }
      else { const c = $$('.wcard')[from]; c.focus(); c.dispatchEvent(new KeyboardEvent('keydown', { key: tmp % 4 ? 'ArrowLeft' : 'ArrowUp', bubbles: true })); }
    },
    'Was steht zuerst?': () => {
      if ($('#duo').classList.contains('solved') || !$('.pickw')) return;
      const p = $$('.pickw'), id = p.map(x => x.dataset.w).sort().join(); if (id !== word) { word = id; tries = 0; tmp++; }
      const first = p.map(x => x.dataset.w).sort()[0];
      const good = p.find(x => x.dataset.w === first), bad = p.find(x => x !== good);
      if (tries < tmp % 3) { tries++; bad.click(); if (tries === 2 && !$('.pickw.hint')) errs.push('kein Tipp'); return; }
      if (tmp % 2) good.click(); else document.dispatchEvent(new KeyboardEvent('keydown', { key: String(p.indexOf(good) + 1) }));
    },
    'Wo ist mein Platz?': () => {
      if ($('#list').classList.contains('solved') || !$('#new .word-card')) return;
      const g = $$('.gap:not(:disabled)'); if (!g.length) return;
      if (tmp % 7 === 0) $('#new .word-card').click();
      const h = $('.gap.hint');
      if (h) { h.click(); return; }
      if (tmp++ % 2) g[0].click(); else document.dispatchEvent(new KeyboardEvent('keydown', { key: String(+g[g.length - 1].dataset.g + 1) }));
    },
    'Leitwort-Detektiv': () => {
      if ($('#word').classList.length > 1) return;
      const o = $$('.wbtn:not(:disabled)'); if (!o.length) return;
      if (tmp++ % 2) o[0].click(); else document.dispatchEvent(new KeyboardEvent('keydown', { key: String($$('.wbtn').indexOf(o[o.length - 1]) + 1) }));
    },
    'Grundform-Profi': () => {
      const inp = $('#answer'); if (inp.readOnly) return;
      const w = $('#from').textContent; if (w !== word) { word = w; tries = 0; }
      const pill = $('#bubble .pill');
      if (tries === 0) { inp.value = ''; $('#check').click(); if (!/Schreibe zuerst/.test($('#bubble').textContent)) errs.push('leere Prüfung'); inp.value = 'xyz'; }
      else if (pill && tries >= 3) {
        const t = pill.textContent, up = t[0] === t[0].toUpperCase();
        inp.value = (tmp++ % 3 === 0 && tries === 3) ? (up ? t.toLowerCase() : t[0].toUpperCase() + t.slice(1)) : (tmp % 2 && up ? 'die ' + t : t);
      } else inp.value = 'abc' + tries;
      tries++; $('#check').click();
    }
  }
