/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Nomen oder kein Nomen?': () => {
      const t = $$($('#step1').hidden ? '#step2 .tile' : '#step1 .tile');
      t[tmp++ % t.length].click();
    },
    'Groß oder klein?': () => { $$('.tile')[tmp++ % 2].click(); },
    'Nomen-Jagd': () => {
      const b = $$('.w:not(.found)');
      if (b.length) b[tmp++ % b.length].click();
    },
    'Wortarten-Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 3].click();
    },
    'Wortfamilien-Detektiv': () => {
      const b = $$('.fcard:not(:disabled)');
      if (b.length) b[tmp++ % b.length].click();
    },
    'Großschreib-Profi': () => {
      if ($('#sent').classList.contains('solved')) return;
      const w = $('#sent').textContent.toLowerCase(); if (w !== word) { word = w; tries = 0; }
      const hints = $$('.w.hint');
      if (hints.length) hints.forEach(b => b.click());
      else if (tries === 1) $('.w').click();
      tries++; $('#check').click();
    }
  }
