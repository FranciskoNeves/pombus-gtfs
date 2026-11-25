import hashlib, sys
delta_path, out_path = sys.argv[1], sys.argv[2]
d = open(delta_path, 'rb').read().decode('ascii')
lines = d.split('\n')
assert lines[-1] == '', 'delta sem newline final'
lines = lines[:-1]
hdr = lines[0]
assert hdr == 'shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled', 'header errado: ' + hdr

def fmt5(v, dec):
    neg = v < 0
    s = str(abs(v)).rjust(6, '0')
    return ('-' if neg else '') + s[:-5] + '.' + s[-5:][:dec]

def fmt1(v):
    neg = v < 0
    s = str(abs(v)).rjust(2, '0')
    return ('-' if neg else '') + s[:-1] + '.' + s[-1]

rows = [hdr]
prev = None
n = 0
for ln in lines[1:]:
    dtag = ''
    if '|D' in ln:
        i = ln.index('|D')
        dtag = ln[i+2:]
        ln = ln[:i]
    latD, lonD = (5, 5) if dtag == '' else (int(dtag[0]), int(dtag[1]))
    if ln.startswith('B|'):
        _, sid, a, b, c, e = ln.split('|')
        latE, lonE, seq, disE = int(a), int(b), int(c), int(e)
    else:
        parts = ln.split('|')
        dl, dn, dd = int(parts[0]), int(parts[1]), int(parts[2])
        seq = int(parts[3][1:]) if len(parts) > 3 and parts[3].startswith('S') else prev[3] + 1
        sid = prev[0]
        latE = prev[1] + dl; lonE = prev[2] + dn; disE = prev[3] + dd
    rows.append('%s,%s,%s,%d,%s' % (sid, fmt5(latE, latD), fmt5(lonE, lonD), seq, fmt1(disE)))
    prev = (sid, latE, lonE, seq, disE)
    n += 1

decoded = '\n'.join(rows) + '\n'
blob = ('blob %d\0' % len(decoded.encode())).encode() + decoded.encode()
got = hashlib.sha1(blob).hexdigest()
expect = "e338194011d10a84d05421ea02b958c5f5f1b252"
if got != expect:
    raise SystemExit('SHA MISMATCH: got %s expected %s' % (got, expect))
open(out_path, 'w', newline='').write(decoded)
print('OK blob-sha1=%s bytes=%d rows=%d' % (got, len(decoded.encode()), n + 1))
