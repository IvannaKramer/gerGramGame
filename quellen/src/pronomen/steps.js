/* Auto-Spieler für den Test: je Spieltitel eine Funktion, die alle 300 ms einen Schritt macht.
   Verfügbar: $, $$, errs, tmp, word, tries (frei benutzbare Zähler), solved(), done(). */
{
    'Pronomen-Körbe': () => {
      const sel = $('.word-card.selected');
      if (!sel) { const c = $('.word-card:not(.done):not(.vanish)'); c && c.click(); return; }
      $$('.basket')[tmp++ % 4].click();
    },
    'Pronomen-Lücke': () => { if ($('#gap') && !$('#gap').classList.contains('filled')) $$('.tile')[tmp++ % 4].click(); },
    'Pronomen-Memory': () => {
      const FORMS = { bin: 'ich', bist: 'du', ist: 'er', sind: 'wir', seid: 'ihr', habe: 'ich', hast: 'du', hat: 'er', haben: 'wir', habt: 'ihr',
                      sehe: 'ich', siehst: 'du', sieht: 'er', sehen: 'wir', seht: 'ihr' };
      const key = c => { const t = c.querySelector('.word').textContent; return c.classList.contains('sp') ? t : FORMS[t.split(' ')[1]]; };
      const openC = $$('.mcard.open:not(.found)'), closed = $$('.mcard:not(.open)');
      if (openC.length >= 2) return;
      if (!openC.length) { closed[0] && closed[0].click(); return; }
      const o = openC[0];
      if (tmp++ % 4 === 0) { closed[closed.length - 1].click(); return; }
      const p = closed.find(c => c.classList.contains('sp') !== o.classList.contains('sp') && key(c) === key(o));
      p ? p.click() : errs.push('no partner for ' + key(o));
    },
    'Wer ist gemeint?': () => { if ($('.opt') && !$('.opt.good')) $$('.opt')[tmp++ % 4].click(); },
    'Ersetz-Spiel': () => {
      if (!$('#next-box').hidden) { $('#next-btn').click(); return; }
      tmp++;
      if (!$('.np.selected')) {
        if (tmp % 9 === 0) { $$('.tile')[0].click(); return; }
        const keep = $$('.np').filter(b => !b.hasAttribute('aria-pressed')), tg = $$('.np[aria-pressed]');
        (tmp % 4 === 0 ? keep[tmp % keep.length] : tg[tmp % tg.length]).click();
        return;
      }
      $$('.tile')[tmp % 4].click();
    },
    'Pronomen-Profi': () => {
      const inp = $('#sentence input'); if (!inp || inp.readOnly) return;
      const w = $('#sentence').textContent; if (w !== word) { word = w; tries = 0; tmp++; }
      const pill = $('#bubble .pill');
      if (tmp % 4 === 0 && tries === 0) tries = 2;
      if (tries === 0) inp.value = '';
      else if (tries === 1) inp.value = 'xyz';
      else if (tries === 2) inp.value = 'Er';
      else if (tries === 3) inp.value = 'sie';
      else if (tries === 4) inp.value = 'ihm';
      else if (tries === 5) inp.value = 'es';
      else if (pill) inp.value = pill.textContent;
      else inp.value = ['Sie', 'ihn', 'ihr', 'ihnen', 'Es', 'er'][tries % 6];
      tries++; $('#check').click();
    }
  }
