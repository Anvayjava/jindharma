# Jindharma

Interactive study material on Jain Dharma, from Digambar sources, in English and Hindi.

## Pages
- [Karma Siddhant](karma-siddhant/) — the eight karmas, flow charts, and the 14 Gunasthanas
- [Tattvartha Sutra](tattvartha-sutra/) — chapters 1 and 8
- [Chhah Dhala](chhah-dhala/) — dhals 1 and 2
- [Samaysaar](samaysaar/) — gathas 1–16

## How the pages are made
`tattvartha-sutra/`, `chhah-dhala/` and `samaysaar/` are generated from the content files in `tools/content/`.
To add a chapter, dhal or adhikar: add its text and explanations to the matching file in `tools/content/`,
register the page in that file's `PAGES` list, and run:

```
python3 tools/build.py
```

Every verse or sutra is marked either "checked against a scanned edition" or "proofread pending".
`karma-siddhant/index.html` is a single hand-written file. New top-level topics go in the `TOPICS` list of the root `index.html`.
