#!/usr/bin/env python3
"""Parse S1 (chANakyanItisort.itx, ITRANS) into text/p00.md.

usage: parse_s1.py SOURCE.itx OUTDIR
Every Sanskrit character comes from the source through indic_transliteration;
nothing is corrected. Anomalies are printed for ISSUES.md.
"""
import re, sys, unicodedata
from pathlib import Path
from indic_transliteration import sanscript as S

src, out = Path(sys.argv[1]), Path(sys.argv[2])
raw = src.read_text(encoding="utf8").splitlines()
body = raw[raw.index(r"\begin{document}") + 1:]
END = re.compile(r"\|\|\s*(\d+)\\-(\d+)\s*(\(.*?\))?\s*$")
verses, cur, notes, seen_end = [], [], [], False
for ln in body:
    if "iti chANakyanItidarpaNaH" in ln:
        seen_end = True
    if seen_end:
        break
    s = ln.strip()
    if not s or s.startswith("\\") or s.startswith("##") or s.startswith("%"):
        continue
    mark = re.search(r"##(.*?)##", s)
    if mark:
        s = re.sub(r"\s*##.*?##", "", s).strip()
    m = END.search(s)
    cur.append(s)
    if m:
        cur[-1] = END.sub("||", s).rstrip()
        note = mark.group(1) if mark else None
        if m.group(3):
            note = (note + " " if note else "") + m.group(3)
        verses.append((int(m.group(1)), int(m.group(2)), cur, note))
        cur = []
if cur:
    print("LEFTOVER lines:", cur)

def dev(t):
    t = t.replace("\\-", "-")
    t = re.sub(r"\|\|", "", t)
    t = re.sub(r"\|", "", t)
    t = S.transliterate(t, S.ITRANS, S.DEVANAGARI)
    t = t.replace("", "॥").replace("", "।")
    return unicodedata.normalize("NFC", t)

merged = []
for ch, v, ls, note in verses:
    if merged and merged[-1][0] == ch and merged[-1][1] == v:
        print(f"DUPLICATE 00.{ch:02d}.{v}: number repeated in source; lines kept under one ID with continuing letters")
        merged[-1][2].extend(ls)
        merged[-1][4] += 1
    else:
        merged.append([ch, v, list(ls), note, 1])
lines, counts, prev = [], {}, {}
for ch, v, ls, note, n in merged:
    if ch in prev and v != prev[ch] + 1:
        print(f"NUMBERING ch{ch:02d}: {prev[ch]} -> {v}")
    elif ch not in prev and v != 1:
        print(f"NUMBERING ch{ch:02d} starts at {v}")
    prev[ch] = v
    counts[ch] = counts.get(ch, 0) + n
    if note:
        print(f"NOTE 00.{ch:02d}.{v}: marked '{note}' in source")
    for i, l in enumerate(ls):
        letter = chr(97 + i) if len(ls) > 1 else ""
        lines.append((ch, f"00.{ch:02d}.{v}{letter} | {dev(l)}"))
out.mkdir(parents=True, exist_ok=True)
(out / "p00.md").write_text("\n".join(l for _, l in lines) + "\n", encoding="utf8")
print("verses per chapter:", counts, "total", sum(counts.values()), "lines", len(lines))
