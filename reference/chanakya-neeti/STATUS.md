# Status: chanakya-neeti

Updated: 2026-10-17 on branch docs/2026-10-17/version-1. Base source: S1.

| Part | Chapter | Sanskrit verses (source) | Sanskrit IDs | Source | Hindi | English | Check | Notes |
|---|---|---|---|---|---|---|---|---|
| 00 | 01 | 17 | 17 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 02 | 20 | 20 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 03 | 22 | 22 | S1 | AI draft | AI draft | 0 errors | extracted; source numbering jumps 21 -> 31 |
| 00 | 04 | 20 | 19 | S1 | AI draft | AI draft | 0 errors | extracted; number 17 used twice (merged under 00.04.17) |
| 00 | 05 | 24 | 23 | S1 | AI draft | AI draft | 0 errors | extracted; number 5 used twice (merged under 00.05.5) |
| 00 | 06 | 22 | 22 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 07 | 21 | 21 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 08 | 23 | 23 | S1 | AI draft | AI draft | 0 errors | extracted; verse 13 carries a variant note in the source |
| 00 | 09 | 14 | 14 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 10 | 20 | 20 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 11 | 18 | 18 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 12 | 23 | 23 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 13 | 20 | 20 | S1 | AI draft | AI draft | 0 errors | extracted; verse 4 marked (4.1); numbering jumps 10 -> 12 |
| 00 | 14 | 20 | 20 | S1 | AI draft | AI draft | 0 errors | extracted;  |
| 00 | 15 | 19 | 18 | S1 | AI draft | AI draft | 0 errors | extracted; number 2 used twice; jumps 2 -> 4 |
| 00 | 16 | 20 | 18 | S1 | AI draft | AI draft | 0 errors | extracted; numbers 13 and 15 used twice; jumps 15 -> 18 |
| 00 | 17 | 21 | 21 | S1 | AI draft | AI draft | 0 errors | extracted;  |

All chapters are in text/p00.md (794 lines). Checker: 0 errors, 6 warnings (double spaces inside source lines and the same lines in the sandhi layer, see ISSUES.md). Verse IDs: 339 (344 verses in the source; the 5 repeated numbers are merged).

## Next
- A person reads the three layers (text/p00-sandhi.md, -hindi.md, -english.md); every unit is an AI draft that an independent AI reviewed.
- Verification against a printed edition (second source), including the 3 'unsure' lines.
- Quiz: start /quiz-advanced-cdn with feed/chanakya-neeti-p00.epub (kind verse-study).

## Verification (2026-10-17)
Structure, word and AI proofreading checks done (see VERIFY.md, ISSUES.md). Layers (sandhi, Hindi, English): all 17 chapters drafted by Sonnet/Fable agents, checked with check_chunk.py, independently reviewed by a second agent, patched, merged and written to text/p00-sandhi.md, -hindi.md, -english.md (794 lines each, IDs identical to p00.md). They are AI drafts no person has read. The EPUB feed is in feed/ (794 line numbers read back by the real extractor). Open choices are in ISSUES.md.
