# Ontario Floor Joist Span Selector (OBC Table 9.23.4.2.-A)

Maximum floor joist spans from OBC 2024 Table 9.23.4.2.-A for the two species groups Ontario builders actually buy — SPF and Douglas Fir–Larch, No. 1/No. 2 — across all five joist sizes, three spacings and the table's three restraint conditions (strapping, bridging, strapping + bridging). Includes a reverse mode: give it the span you need, it returns the smallest joist that works.

**Live web tool:** https://dust2engineering.github.io/ontario-floor-joist-span-selector/web/

## How it works

- Look up a span by species, size, spacing and restraint condition — the restraint condition matters: it changes the answer by up to half a metre.
- Or enter a required span and get the smallest joist in the table that covers it at your spacing and restraint.
- The table's load basis is residential floor live load (Note (1) to the table); joists must also satisfy the vibration criterion of 9.23.4.2.(2).

## Data in this repository

- `joist-span-table.json` — the full verified subset as machine-readable JSON, with the load-basis note and provenance.
- Read from the official BC Publications span tables (the NBC-harmonized Table A-1, counterpart of OBC Table 9.23.4.2.-A) and spot-checked cell-for-cell against OBC 2024 reproductions — every checked value matched. Other grades and species groups in the source table are outside this verified subset and are not included.

## Command line

```bash
python3 joist_spans.py --species SPF --size 38x184 --spacing 400 --restraint B
```

## Worked examples

- [example-lookup.txt](examples/example-lookup.txt)
- [example-reverse.txt](examples/example-reverse.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Structural. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
