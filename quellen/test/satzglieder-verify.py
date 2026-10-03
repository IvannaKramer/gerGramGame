import ast, re, sys, pathlib, itertools, collections
d = pathlib.Path(sys.argv[1])
cap = lambda s: s[0].upper() + s[1:]
sent = lambda p: cap(' '.join(p)) + '.'
def data(n):
    t = (d / f'g{n}.txt').read_text()
    m = re.search(r'const SENTENCES = (\[.*?\n\]);', t, re.S)
    return ast.literal_eval(m.group(1))
seen, errs = {}, []
for n in range(1, 7):
    D = data(n); print(f'\n== g{n}: {len(D)} Sätze'); cnt = collections.Counter()
    for row in D:
        parts = list(row[1:]) if n == 1 else list(row) if n in (3, 4) else list(row[0])
        s = sent(parts)
        if s in seen: errs.append(f'doppelt: {s}')
        seen[s] = n
        if ' ' in parts[1]: errs.append('Verb mehrteilig: ' + s)
        cnt[len(parts)] += 1; extra = ''
        if n == 2:
            allp = [sent(p) for p in itertools.permutations(parts)]
            valid = [sent(p) for p in itertools.permutations(parts) if p[1] == parts[1]]
            if row[1] not in valid: errs.append('richtig ungültig: ' + row[1])
            if row[1] == s: errs.append('richtig = Grundsatz')
            key = lambda x: sorted(x.lower().replace('.', '').split())
            extra = '\n     ✓ ' + row[1]
            for w in row[2:]:
                if w in valid: errs.append('falsch ist gültig: ' + w)
                if key(w) != key(s): errs.append('andere Wörter: ' + w)
                extra += f"\n     x {w}  [{'Verbstelle' if w in allp else 'zerrissen'}]"
        if n == 5:
            i = parts.index(row[1])
            if i < 2: errs.append('Start falsch ' + s)
            extra = '\n     → ' + sent([row[1], parts[1]] + [p for k, p in enumerate(parts) if k not in (1, i)])
        if n == 6:
            c = row[1]; W = ' '.join(parts).split(); vi = len(parts[0].split())
            if len(set(c)) != 6: errs.append('nicht 6 Karten: ' + s)
            r = [x for x in c if x in parts]; cnt[f'richtig{len(r)}'] += 1
            for x in c:
                g = x.split(); at = next((i for i in range(len(W) - len(g) + 1) if W[i:i + len(g)] == g), -1)
                if at < 0: errs.append('Karte nicht im Satz: ' + x)
                if parts[1] in g: errs.append('Karte mit Verb: ' + x)
                rest = [w for i, w in enumerate(W) if i != vi and not (at <= i < at + len(g))]
                extra += f"\n     {'✓' if x in parts else 'x'} {cap(x)} {W[vi]} {' '.join(rest)}."
        print(' ' + ' | '.join(p if i else cap(p) for i, p in enumerate(parts)) + '.' + extra)
    print(' Verteilung:', dict(cnt))
print('\nFEHLER:\n' + '\n'.join(errs) if errs else '\nkeine Fehler')
