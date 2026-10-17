# VERIFY log: chanakya-neeti

## 2026-10-17 (branch docs/2026-10-17/version-1)
- Inventory (inventory.py): base is text/p00.md (Devanagari, `ID | text`). Other files: tools/parse_s1.py is the parser written in the extraction stage (kept as a record, not a source); reference/tools/check_extraction.py is the checker. No second edition, no raw/ folder (S1 licence forbids reposting). No questions needed; answers recorded here.
- Second edition: not available, skipped.
- Structure (structure_check.py): 17 chapters, 339 verse IDs, 794 lines, no flags. Numbering jumps/repeats are properties of S1, already in ISSUES.md.
- check_extraction.py: 0 errors, 4 warnings (double spaces inside source lines).
- word_check.py: 3,879 tokens (2,612 distinct); 1 stray character; 0 typo candidates; 93 verse lines outside 15-17 / 22-23 aksharas (metre.tsv, mostly longer metres and chapter 12).
- AI proofreading: 102 items in 2 packs (1 stray, 93 metre, 8 sample).
- AI proofreading done (2 agents, Fable): 13 proposals (10 error, 3 unsure) of 102 lines; sample 8 lines, 0 errors. All proposed readings exist in the ITRANS source, so none is a conversion error. text/ unchanged. Details in checks/PROOFREAD.md, checks/proposals.tsv, ISSUES.md.
- plan_work.py: 17 chunks, 339 units, about 0.1 million draft output tokens plus about the same for the independent review. Waiting for the owner's choice of parts.
- Owner decisions: pilot layers on chapters 1-2; apply the 10 AI 'error' proposals (done: 9 lines, checks/applied-corrections.tsv).
- Pilot layers (chapters 1-2, 37 verses, 76 lines): drafted by one agent per chapter (Fable), checked with check_chunk.py (0 errors), independently reviewed by a second agent per chapter (ch1: 7 issues, 1 error; ch2: 15 issues, 1 error, an invented variant reading), patches applied (22 in total), merged. All AI text is an unreviewed draft until a person reads it.
- The Sanskrit is one file (text/p00.md), and write_layers.py writes layer files only when every chapter of the file is merged. So the pilot layers are NOT in text/; a format-exact preview is in layers-work/pilot-preview/ (p00-sandhi.md, p00-hindi.md, p00-english.md, chapters 1-2 only).

## Layers finished (2026-10-17)
- Chapters 3-17 drafted (one agent per chapter, model Sonnet 5.5 for chapters 4-17), checked (check_chunk.py, 0 errors), independently reviewed (a second agent per chapter), patches applied (apply_review.py --add-source), manual items settled by hand and logged in layers-work/p00/chNN/manual_changes_1.txt, merged. The reviewers' proposed fixed renderings were appended to layers-work/GLOSSARY.md after each chapter, so later chapters used them and earlier ones may not.
- write_layers.py wrote text/p00-sandhi.md, p00-hindi.md, p00-english.md (794 lines each). work_status.py: 17 of 17 chunks written.
- check_extraction.py: 0 errors, 6 warnings (the 4 source double-space lines plus the same lines 526 and 576 repeated in the sandhi layer).
- Feed: build_feed.py made feed/chanakya-neeti-p00.epub (17 chapters, 794 lines, 0.4 MB), map.json and part txt; extract_book.py from the template read back 794 of 794 line numbers.
- All translation and word-split text is AI draft. Review was by another AI, not a person; neither compared against a printed edition. Do not call it verified.

## Parallel run merged from version-2 (2026-10-17)
Branch version-2 held an earlier, independent run of the same verify stage (structure and word checks identical, a separate AI proofreading pass with 14 proposals, and unreviewed pilot draft chunks). Its structure, word and plan files were identical to this branch's; its proofreading outputs are kept in checks/proofread-v2/ (proposals.tsv, PROOFREAD.md, pack outputs), and its differing proposals are listed in ISSUES.md. Its chapter 1 pilot draft (layers-work/p00/ch01/chunk1_out.json) was superseded by the reviewed and merged version from this branch; text/ was not changed by version-2.
