# VERIFY log: chanakya-neeti

- 2026-10-17 (branch docs/2026-10-17/version-2, from main after PR #1): inventory run. Base = text/p00.md (Devanagari, S1 Sanskrit Documents). `tools/parse_s1.py` is the extraction parser and `reference/tools/check_extraction.py` the checker: both kept, not text sources. No second edition available; `--compare` skipped.
- Structure check: 17 chapters, 339 verse IDs, 794 lines, no flags. Source has 344 verses; 5 repeated numbers merged under one ID (see ISSUES.md).
- Word check: 3879 tokens; 1 stray character (00.15.16a, trailing backslash); 0 typo candidates; 93 verse lines outside 15-17 / 22-23 aksharas (metre.tsv; mostly other regular metres). Second edition: not available, skipped.
- AI proofreading (2 packs, 102 items: 1 stray, 93 metre, 8 random sample lines): 14 proposals (9 error, 5 unsure incl. duplicates of the stray line) in checks/proposals.tsv. Random sample: 8 ordinary lines read, 1 with an error (12.5%; sample far too small for an error rate). text/ NOT changed.
- plan_work: 17 chunks, 339 units, about 0.1M draft tokens (+ same for review). Waiting for the owner to choose scope for word split / Hindi / English layers.
