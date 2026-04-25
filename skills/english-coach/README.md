# English Coach

English Coach is a Hermes skill for practical English learning: translation, word cards, pronunciation, correction, polishing, optional audio, and optional flashcard images.

- **Skill name:** `english-coach`
- **Formal name:** English Coach
- **Author:** Rac 🦝
- **Primary triggers:** `en:`, `zh:`, `word:`, `words:`, `say:`, `fix:`, `polish:`
- **Legacy aliases:** `lv:`, `level:`, `vocab:`, `pronounce:`

## Install

Copy this folder into a Hermes skills directory:

```bash
mkdir -p ~/.hermes/skills/openclaw-imports
cp -R skills/english-coach ~/.hermes/skills/openclaw-imports/english-coach
```

Required files:

```text
english-coach/SKILL.md
english-coach/references/cefr.md
english-coach/references/EFLLex_NLP4J
```

## Quick use

```text
word: plausible
words: paste an English paragraph here
say: how are you doing?
fix: I goed to store
en: 我想确认一下这个方案是否合理
zh: That sounds like a plausible explanation.
polish: Thanks for your help
```
