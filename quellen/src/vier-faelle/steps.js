/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Fall-Detektiv': () => {
      const mk = $('#mk'); if (!mk || mk.classList.contains('solved')) return;
      tmp++;
      if (tmp % 2) $$('.tile')[tmp % 4].click();
      else document.dispatchEvent(new KeyboardEvent('keydown', { key: String(tmp % 4 + 1) }));
    },
    'Artikel-Dreher': () => {
      const sp = $('#spin'); if (!sp || sp.classList.contains('solved')) return;
      const key = $('#qtext').textContent; if (key !== word) { word = key; tries = 0; tmp++; }
      if (tries === 0 && tmp % 3 === 0) { tries++; $('#check').click(); if (!/Tippe zuerst/.test($('#bubble').textContent)) errs.push('leere Prüfung'); return; }
      tries++;
      if (tmp % 4 === 1) document.dispatchEvent(new KeyboardEvent('keydown', { key: String(tries % 4 + 1) })); else sp.click();
      $('#check').click();
    },
    'Frage-Lupe': () => {
      if ($('.chunk.good') || !$('.chunk')) return;
      const c = $$('.chunk');
      tmp++;
      if (tmp % 2) c[tmp % c.length].click();
      else document.dispatchEvent(new KeyboardEvent('keydown', { key: String(tmp % c.length + 1) }));
    },
    'Fall-Kästen': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 4].click();
    },
    'Wort-Verwandler': () => {
      const g = $('#gap'); if (!g || g.classList.contains('filled')) return;
      const f = $$('.form');
      tmp++;
      if (tmp % 2) f[tmp % f.length].click();
      else document.dispatchEvent(new KeyboardEvent('keydown', { key: String(tmp % f.length + 1) }));
    },
    'Fall-Profi': () => {
      const inp = $('#sentence input'); if (!inp || inp.readOnly) return;
      const key = $('#sentence').textContent + $('#base').textContent; if (key !== word) { word = key; tries = 0; tmp++; }
      const pill = $('#bubble .pill'), base = $('#base').textContent;
      if (tries === 0 && tmp % 4 === 0) { inp.value = ''; }                                  /* leere Prüfung */
      else if (tries === 0 && tmp % 4 === 1) { inp.value = base.split(' ')[1]; }             /* nur das Nomen */
      else if (tries <= 1 && tmp % 4 === 2) { inp.value = base.toUpperCase(); tries = 1; }   /* Großschreibung */
      else if (tries <= 2 && tmp % 2 === 0) { inp.value = base; }                            /* Grundform */
      else if (pill) inp.value = pill.textContent;                                           /* Lösung abschreiben */
      else inp.value = 'die Banane';
      tries++; $('#check').click();
    }
  }
