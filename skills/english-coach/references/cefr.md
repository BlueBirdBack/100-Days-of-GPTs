# CEFR Reference

## Data Source

**EFLLex** — 15,280 lemma–POS entries, A1–C1, from UCLouvain's CENTAL lab (LREC 2018). Chosen because Cambridge EVP has no bulk download and Oxford 3000/5000 is PDF-only. Source: <https://cental.uclouvain.be/cefrlex/efllex/>

**Data file:** `EFLLex_NLP4J` (TSV, same folder as this file)

**Key columns:** `word`, `tag` (NN/VB/JJ/RB), `level_freq@a1` through `level_freq@c1`, `total_freq@total`. Remaining ~100 columns are per-textbook breakdowns — ignore.

**Assigning a single level:** Use the lowest level where `level_freq > 0`. If spread across levels, report as range (e.g. "A2–B1") or peak. Ignore entries starting with `-` or containing `_` (NLP4J artifacts).

**Limitations:** No C2 data — estimate those. No definitions/IPA/examples — use Claude's knowledge. Does not disambiguate word senses or cover phrasal verbs / multi-word expressions.

## Output Format

Trigger: `lv: <word>` (aliases: `level:`, `ipa:`, `cefr:`)

---

**Word:** plausible
**CEFR:** B2 (Upper Intermediate)
**IPA:** /ˈplɔː.zɪ.bəl/ (UK) · /ˈplɑː.zə.bəl/ (US)

**Meaning:** Seems reasonable or likely to be true
**Synonyms:** possible (A1) · believable (B1) · likely (B1)

**Examples:**
1. "That sounds like a plausible explanation."
2. "Her excuse wasn't very plausible — I didn't believe her."
3. "It's plausible that he forgot, but I doubt it."

---

**Rules:**
- 3 synonyms, aim for A1–B1 level. If word is already A1–B1, synonyms at same or lower level.
- For polysemous words (e.g. "fair" = A1 adj / B2 noun), note the ambiguity.
- If not in EFLLex, estimate level without mentioning EFLLex.

## Levels

| Level | Name | Examples |
|-------|------|----------|
| A1 | Beginner | hello, water, eat, go, big |
| A2 | Elementary | restaurant, appointment, weather |
| B1 | Intermediate | decision, recommend, opportunity |
| B2 | Upper Intermediate | significant, consequence, perspective |
| C1 | Advanced | ubiquitous, paradigm, mitigate |
| C2 | Proficiency (no EFLLex data) | ephemeral, serendipity, perspicacious |

## HSK Correlation (approximate, contested)

| CEFR | HSK pre-2021 | HSK 3.0 |
|------|-------------|---------|
| A1 | 1 | 1–2 |
| A2 | 2–3 | 3–4 |
| B1 | 3–4 | 4–5 |
| B2 | 5 | 5–6 |
| C1 | 6 | 7–8 |
| C2 | Beyond 6 | 9 |
