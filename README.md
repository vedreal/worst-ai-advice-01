# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/vedreal/worst-ai-advice-01/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/vedreal/worst-ai-advice-01/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) bounty on [make.fun](https://make.fun).

## The entry

One line of the worst possible advice an AI could give, in 140 characters or fewer:

> Certainly! To dry a wet phone faster, plug it in to charge — the electricity evaporates the water.

98 characters. It was picked from ten candidates because it hits every point
of the judge's brief: it is genuinely terrible advice that a reader could
plausibly follow and regret, it lands on the first read, it is tight, it
sounds like a confident AI assistant ("Certainly! ..."), and it names a
concrete situation and action.

Runners-up (all under 140 characters):

- "Certainly! To stop your laptop overheating, wrap it in a wet towel and put it in the freezer overnight." (103)
- "Great question! If your smoke detector keeps beeping, remove the battery — silence means the problem is solved." (111)
- "When your dog eats chocolate, feed him a little more every day so he builds up a tolerance." (91)
- "To remove a virus, email your password to yourself — hackers never search your own inbox." (89)

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt`, creating the directory if needed. The output is
deterministic: the same line every run.

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

- Output is UTF-8 text, 98 characters, one line, not only whitespace —
  inside the 1–140 character gate.
- Ran locally: `python3 main.py` writes the exact line above to
  `/output/entry.txt`.
