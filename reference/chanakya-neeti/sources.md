# Sources: chanakya-neeti

| ID | Name | URL | Edition / editor / year | Script | Licence | Covers | Fetched how | Quality note | Role |
|---|---|---|---|---|---|---|---|---|---|
| S1 | Sanskrit Documents, Chanakya Niti (chANakyanItisort), processed and proofread by Sunder Hattangadi | https://sanskritdocuments.org/doc_z_misc_major_works/chANakyanItisort.itx (also .pdf and .html at the same path) | Chanakya Niti Darpana; some verses marked "Ed. Sharma"; 17 sections | ITRANS (.itx), Devanagari (.pdf, .html) | file header: prepared by volunteers, for personal study and research; not to be copied or reposted for promotion or commercial purpose without permission. Raw file therefore not committed | 17 chapters per the page | Owner downloaded the .itx and attached it to the chat (shell gets 403 from sanskritdocuments.org). Parsed by tools/parse_s1.py. sha256 6ed3542dadb9b6cca7ff0f4e87284f3904ecd6e09bb5c30cb56641649f2fd41f, 853 lines; the original is not stored in the repo (see licence) | ITRANS typed and proofread by volunteer; 17 sections, 344 verses; some verses marked Ed. Sharma | primary |

## Notes
- Reach test (2026-10-17): the shell reaches GitHub only. sanskritdocuments.org, gretil, sa.wikisource.org and archive.org all returned 403. GitHub search is limited to the session's repo.
- Web search for other typed Devanagari sources found only app/site copies (vedapath.app); not used, no stated edition or licence.
- Conversion: ITRANS to Devanagari with indic_transliteration; \\- (escaped hyphen) became "-"; anusvara written .n in the source stays as ं (not changed to a nasal).
- Hindi and English translations: none found yet. Candidates on the Sanskrit Documents index page link archive.org scans (Chanakya Neeti Darpan, Mihirchandra Sharma); those are scans and need OCR and a licence check.
