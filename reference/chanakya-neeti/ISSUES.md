# Issues: chanakya-neeti

| Line ID | Kind | What | Source(s) | Suggested check |
|---|---|---|---|---|
| 00.03.21 -> 00.03.31 | numbering | source numbering jumps from 03-21 to 03-31 (the 03-31 verse is marked "Ed. Sharma") | S1 | compare with a second edition |
| 00.04.17 | duplicate number | two verses numbered 04-17 in the source (second marked "Ed. Sharma"); kept under one ID as lines a-d | S1 | confirm verse boundary |
| 00.05.5 | duplicate number | two verses numbered 05-05 (first marked "Ed. Sharma"); lines a-d under one ID | S1 | confirm verse boundary |
| 00.08.13 | variant | source adds "(dayAsamaH )" after the verse number, a variant for dayAparaH; not in the text | S1 | decide variant handling |
| 00.13.4 | note | source marks it "(4.1)"; same verse as 00.04.1 | S1 | note duplicate across chapters |
| 00.13.10 -> 00.13.12 | numbering | no verse 13-11 in the source | S1 | check other edition |
| 00.15.2 | duplicate number | two verses numbered 15-02; lines a-d under one ID; no 15-03 | S1 | confirm verse boundary |
| 00.16.13 | duplicate number | two verses numbered 16-13; lines a-d under one ID | S1 | confirm verse boundary |
| 00.16.15 | duplicate number | two verses numbered 16-15; no 16-16 or 16-17 in the source | S1 | confirm verse boundary |
| 00.03.7b, 00.04.3b | text | hyphen inside a compound (वाक्य-शल्येन, सज्जन-संगतिः) as in source | S1 | proofreading |
| 00.07.13a, 00.10.18a, 00.11.3c, 00.12.16c, 00.15.17c, 00.17.21c | text | line ends in "-" (escaped hyphen in the source marks a compound split across lines); kept | S1 | proofreading |
| 00.02.11a, 00.12.2c, 00.12.10b, 00.13.9b | spacing | double or odd spaces inside the line, as in the source | S1 | proofreading |
| -- | translations | no Hindi or English translation sources found yet | -- | find licensed sources |
| 00.03.7b | spelling | अदृशं as typed in the source (adR^ishaM) | S1 | proofreading |
| 00.15.16a | markup | line ends with a backslash, copied from S1 (`roShA\`, a TeX line-join); the word continues on 00.15.16b | S1 | proposal in checks/proposals.tsv (hyphen); decide against a printed edition |
| 00.17.18a/b | repeat | दूरीकृताः appears at the end of 17.18a and again at the start of 17.18b in S1 itself (checked in the ITRANS file); the AI proposal (end 17.18a at कर्णतालै-, start 17.18b with र्दूरीकृताः, the edition's split-word convention) was applied at the owner's request | S1 | check printed edition |
| 00.06.14d, 00.09.5c, 00.09.14c, 00.11.18c, 00.11.18d, 00.12.3d, 00.12.10a, 00.12.15b, 00.16.1c | typo? | AI proofreading proposals (reading in S1 confirmed identical in the ITRANS file, so not a conversion error): dittography कुशिष्यशिष्य; शाशि for शशि; missing space before कुवस्त्रता; नाथं; धर्षन्ति/घर्षन्ति; पुरुषा/पुरुषाः; कर्दमाणि/कर्दमानि; अतिमभीरता/अतिगभीरता; युगला/युगलं | S1 | see checks/proposals.tsv; check printed edition |

## Verification summary (verify-vedic-book-reference, 2026-10-17)
- Ran: structure check (no flags), extraction checker (0 errors, 4 warnings), word checker (1 stray character, 0 typo candidates, 93 lines outside the usual akshara counts), AI proofreading of 102 lines (1 stray, 93 metre, 8 random sample lines).
- Proposals: 13 lines (10 error, 3 unsure), all in checks/proposals.tsv. The text in text/ is unchanged. The 8-line sample had 0 errors (too small for a rate).
- Not done: second edition comparison (none available); lines not flagged were not read by the AI. These are AI screens, not proof.

## Corrections applied (2026-10-17, owner asked to apply the AI 'error' proposals)
9 lines changed in text/p00.md (10 proposal rows; 15.16a was flagged twice): 00.06.14d, 00.09.5c, 00.09.14c, 00.12.3d, 00.12.15b, 00.15.16a, 00.16.1c, 00.17.18a, 00.17.18b. Before/after for each is in checks/applied-corrections.tsv. These are AI proposals, not checked against a printed edition. From now on text/p00.md differs from S1 at these lines. The 3 'unsure' lines (00.11.18c, 00.11.18d, 00.12.10a) are unchanged.
