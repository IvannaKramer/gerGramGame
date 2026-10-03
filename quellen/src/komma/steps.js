/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Komma-Klick': () => {
      if ($('#sentence').classList.contains('solved')) return;
      const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      /* jeder dritte Satz: gleich die leuchtenden bzw. von hinten alle Stellen; sonst erst „Kein Komma“ probieren */
      const gaps = [...$$('.cgap:not(.set)')].reverse();
      const all = tmp % 3 === 0 ? gaps.concat($('#none')) : [$('#none')].concat(gaps);
      all[tries++ % all.length].click();
    },
    'Bindewort-Jagd': () => {
      if ($('#sentence').classList.contains('solved')) return;
      const bs = $$('.wbtn'); const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      if (tmp % 3 === 0) { bs.find(b => ['weil', 'dass', 'wenn', 'als', 'ob'].includes(b.textContent)).click(); return; }
      if (tries === 0) { tries++; bs[bs.length - 1].click(); return; }
      bs[(tries++ - 1) % bs.length].click();
    },
    'Komma-Ampel': () => { if ($('#spot')) $$('.tile')[tmp++ % 3 === 0 ? 0 : (tmp % 2)].click(); },
    'Satz-Baumeister': () => {
      const chips = $$('.chip:not(.used)'); if (!chips.length) return;
      chips[tmp++ % chips.length].click();
    },
    'Regel-Sortierer': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 3].click();
    },
    'Komma-Meister': () => {
      if ($('#sentence').classList.contains('solved')) return;
      const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const hints = $$('.cgap.hint'), gaps = $$('.cgap');
      tries++;
      if (tries === 1 && tmp % 2) { gaps[0].click(); return; }          /* erst ein (meist falsches) Komma setzen */
      if (tries === 2 && tmp % 4 === 1) { gaps[0].click(); return; }     /* … und manchmal wieder wegnehmen */
      if (tries === 3 && tmp % 3 === 0) { gaps[gaps.length - 1].click(); return; }
      if (hints.length) { hints[0].click(); return; }
      $('#check').click();
    }
  }
