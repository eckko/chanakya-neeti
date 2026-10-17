# VERIFY log: chanakya-neeti

- 2026-10-17 (branch docs/2026-10-17/version-2, from main after PR #1): inventory run. Base = text/p00.md (Devanagari, S1 Sanskrit Documents). `tools/parse_s1.py` is the extraction parser and `reference/tools/check_extraction.py` the checker: both kept, not text sources. No second edition available; `--compare` skipped.
- Structure check: 17 chapters, 339 verse IDs, 794 lines, no flags. Source has 344 verses; 5 repeated numbers merged under one ID (see ISSUES.md).
