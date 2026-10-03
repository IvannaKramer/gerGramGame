/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done().
   Die Schritte probieren der Reihe nach alle Möglichkeiten aus. So laufen richtige und falsche Antworten und die Tipps. */
{
    'Subjekt oder Prädikat?': () => {
      const c = $('.word-card:not(.done):not(.vanish)'); if (!c) return;
      if (tmp % 7 === 3 && !$('.word-card.selected') && !$('.basket.selected')) { tmp++; $$('.basket')[0].click(); c.click(); return; }   /* erst Korb, dann Karte */
      if (!$('.word-card.selected')) { c.click(); return; }
      $$('.basket')[(tmp++ >> 1) % 2].click();
    },
    'Farb-Markierer': () => {
      const b = $$('#sent .blk:not(.on)'); if (!b.length) return;
      b[tmp++ % b.length].click();
    },
    'Frag die Eule': () => {
      const o = $$('.opt:not(:disabled)'); if (!o.length) return;
      if (tmp % 4 === 0) document.dispatchEvent(new KeyboardEvent('keydown', { key: String(tmp % 3 + 1) })); else o[tmp % o.length].click();
      tmp++;
    },
    'Vier Farben': () => {
      const b = $('#sent .blk:not(.on)'); if (!b) return;
      if (!$('#sent .blk.selected')) {
        if (tmp % 3 === 0) document.dispatchEvent(new KeyboardEvent('keydown', { key: String(tmp % 4 + 1) }));   /* erst Stift, dann Satzglied */
        tmp++; b.click(); return;
      }
      const h = $('.pen.hint'); if (h && tmp % 2) { tmp++; h.click(); return; }
      $$('.pen')[tmp++ % 4].click();
    },
    'Satz-Bauplan': () => {
      const cards = $$('#pile .blk'), sel = $('#pile .blk.selected');
      if (sel) { const s = sel.classList.contains('hint') ? $('.slot.hint') : $$('.slot:not(.good)').find(x => !x.querySelector('.sl-b').textContent); if (!s) { errs.push('kein freies Feld'); return; } s.click(); return; }
      if (cards.length) {
        if (tmp % 11 === 5) { tmp++; $('#check').click(); if (!/Lege zuerst/.test($('#bubble').textContent)) errs.push('leere Prüfung'); return; }
        ($('#pile .blk.hint') || cards[tmp++ % cards.length]).click(); return;
      }
      if (tmp % 9 === 4 && $('.slot:not(.good)')) { tmp++; $('.slot:not(.good)').click(); return; }   /* Karte zurückholen */
      $('#check').click();
    },
    'Fehler-Detektiv': () => {
      if ($('#fix').hidden) { const b = $$('#sent .blk'), h = $('#sent .blk.hint'); if ($('#sent .blk.fixed')) return; (h || b[tmp % b.length]).click(); tmp++; return; }
      const h = $('#fix .pen.hint'); if (h) { h.click(); return; }
      if (tmp % 2) $$('#fix .pen')[tmp % 6].click(); else document.dispatchEvent(new KeyboardEvent('keydown', { key: String(tmp % 6 + 1) }));
      tmp++;
    }
  }
