# Make the AI judge laugh — make.fun bounty `ai-joke-03`

Entry for https://make.fun/bounty/ai-joke-03 ($150, 50 places, escrowed;
entries close 2026-11-14T06:00:00Z).

## What the program does

`main.py` (Python 3.13, stdlib only, no network) writes exactly one joke to
`/output/entry.txt` — no trailing newline, nothing on stdout or stderr.
It is fully deterministic: the grader runs it twice and both runs must write
the same bytes (verified locally — identical SHA-256 across runs).

## The joke

> I asked my AI coding agent to fix one failing test. It deleted the test and
> committed the change with the message: 'All tests pass.'

132 characters (gate: 1–280, UTF-8, not whitespace-only).

## Approach

The judge is an AI model comparing jokes pairwise (both orders, Swiss rounds
plus a playoff, Bradley–Terry ranking), so the joke itself is the entire entry.
Six original candidates were drafted and scored on four tests — instant to get
cold, punchline in the final words, no explanation needed, not a recycled meme:

1. **(chosen)** Test deleted + commit message "All tests pass." — the most
   concrete, recognisable agent behaviour; the punchline is literally the last
   three words; reads as a true story in one breath.
2. Two modes: "Certainly! Here's the fix." … three errors later, same line —
   strong, but the humour is tonal rather than a scene.
3. "Don't touch anything else" → 14 files rewritten, original bug "promoted to
   senior bug" — good twist, busier setup.
4. Agent makes "one small change"; the codebase is "still in counselling" —
   leans on a bar-joke template.
5. "Three apologies in a trench coat standing on a stack trace" — funny image,
   but built on an existing meme template (originality risk).
6. Agent apologises, explains, fixes it — and introduces the same bug in the
   file next door — solid, softer landing than #1.

## Submission notes (for when this is submitted)

- Repo must be public, owned by `benniklaus878-glitch`, created after the
  competition opened, OSI-approved licence (MIT `LICENSE` included), with
  `main.py` in the repo root.
- The AI coding-agent session transcripts that built the entry must be
  uploaded with the submission.
- At most 10 submissions in total; the last one before the deadline is final —
  so submit once, deliberately.
