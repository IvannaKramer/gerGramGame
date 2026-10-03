/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Rede-Finder': () => { if ($('#sentence').classList.contains('solved')) return; $$('.chunk')[tmp++ % 3 === 0 ? 0 : 1].click(); },
    'Zeichen-Helfer': () => { if (!$('.slot.cur')) return; $$('.key')[tmp++ % 4].click(); },
    'Satz-Puzzle': () => {
      const p = $$('.piece:not(.used)'); if (!p.length) return;
      if ($$('.piece').length !== 5) errs.push('pieces ' + $$('.piece').length);
      p[tmp++ % p.length].click();
    },
    'Zeichen-Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 4].click();
    },
    'Satz-Detektiv': () => {
      if ($('.opt.good')) return;
      if ($$('.opt').length !== 3) errs.push('opts');
      const o = $$('.opt:not(.off)'); o[tmp++ % o.length].click();
    },
    'Satzzeichen-Setzer': () => {
      const box = $('#sentence'); if (box.classList.contains('solved')) return;
      const w = box.textContent.replace(/[„“:,]/g, ''); if (w !== word) { word = w; tries = 0; }
      const key = ch => $(`.key[data-ch="${ch}"]`).click();
      if (tries === 0) { $('#check').click(); key('„'); $('.slot').click(); key('“'); key(':'); key(','); }
      else if (tries === 2) { $('#clear').click(); $$('.slot')[1].click(); key(','); }
      else if (tries >= 3) {
        const sol = $('#bubble .sol'); if (!sol || !/So ist es richtig/.test($('#bubble').textContent)) { errs.push('no solution shown'); return; }
        const sig = ['']; let n = 0, inR = false, cw = '';
        const fl = () => { if (cw) { n++; cw = ''; sig[n] = ''; } };
        for (const ch of sol.textContent) {
          if (ch === '„') { fl(); sig[n] += ch; inR = true; } else if (ch === '“') { fl(); sig[n] += ch; inR = false; }
          else if (!inR && (ch === ':' || ch === ',')) { fl(); sig[n] += ch; } else if (ch === ' ') fl(); else cw += ch;
        }
        fl();
        const slots = $$('.slot'); if (slots.length !== sig.length) { errs.push('slots ' + slots.length + '/' + sig.length); return; }
        slots.forEach((s, i) => { s.click(); $('#clear').click(); [...sig[i]].forEach(key); });
      }
      tries++; $('#check').click();
    }
  }
