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

## Layer drafts: open choices for a human (2026-10-17)
| Where | Kind | Note |
|---|---|---|
| 00.03.19 | translation | "army" vs "dominion" |
| 00.04.1, 00.04.14 | translation | first "eva" (nidhanameva) and "tu" left unrendered; wording is a human choice |
| 00.11.18 | low confidence | lines c-d syntax unclear; flags dharṣantyaho and nāthaṃ rest on form and sense only (alternative naṣṭaṃ noted, a guess) |
| 00.12.2 | low confidence | line c has 10 syllables, a word may be missing; the source line has a double space (the token src carries a leading space as a harmless workaround, reviewed) |
| 00.05.5, 00.09.14, 00.16.13, 00.16.15 | grouping | two danda-closed verses printed under one number, kept as one unit as printed (a-b and c-d); a human may split them |
| 00.13.11, 00.15.3, 00.16.16-17 | numbering | absent in the source, so absent in the layers |
| 00.17.6, 00.17.13 | note | vā flag removed in 17.6; 17.13 is elliptical and the reading is uncertain |
| many | text_flags | possible-typo suggestions in the layers rest on form and sense only; none is checked against a printed edition |

## Second AI proofreading run (branch version-2, merged here 2026-10-17)
A parallel run of the verify stage (another AI pass over the same 102 lines) is kept in checks/proofread-v2/. Its agreeing proposals duplicate the rows above. It differs in these lines, none applied and none checked against a printed edition:
| Line | Run 1 (applied or listed above) | Run 2 (checks/proofread-v2/proposals.tsv) |
|---|---|---|
| 00.12.10a | unsure | error: कर्दमाणि -> कर्दमानि |
| 00.12.3d | error (applied) | unsure |
| 00.12.16c | not flagged | unsure: valirditisuto |
| 00.17.16a | not flagged | unsure: 28-matra Arya line |
| 00.17.18c | not flagged | error: गण्डयुग्म vs गण्डयुग |
| 00.11.18d | unsure | not flagged |
Check these against a printed edition. Run 2's random sample read 8 lines with 1 error (too small for a rate).
