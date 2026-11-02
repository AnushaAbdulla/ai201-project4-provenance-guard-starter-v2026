# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Few false positives on human writing

Of 10 pieces of human writing, at most 1 is labelled high-confidence AI, in
every one of the three trials. Five are pieces I wrote myself. The other five
are plain, simple human writing: short sentences and common words, the style
both signals are blind to.

**Why this target:** Wrongly accusing a real writer costs them far more than a
missed AI text costs the site. I include the plain-style pieces on purpose,
because that's who my Milestone 1 trace showed getting accused. A test of only
my own writing would hide that failure.

---

## 2. Clearly-AI and clearly-human text score far apart

The average `combined_score` of 5 clearly AI texts is at least 0.30 higher
than the average of 5 clearly human texts, in every trial.

**Why this target:** My labels are 0.35 and 0.75 apart. If the two kinds of
text don't land at least 0.30 apart, the thresholds are just sorting noise. A
gap that size means the signals are actually separating the two.

---

## 3. Every label is reachable

Every trial produces each of the three labels (high-confidence human, unsure,
high-confidence AI) at least once across my scenario inputs.

**Why this target:** An unreachable label is a silent bug. The config notes
warn that a stub style signal makes "human" impossible to reach. If a label
never appears, the score ranges have a gap.

---

## 4. Every appeal is recorded, and bad ones are refused

5 of 5 appeals on a real `content_id` return `200` with
`status: "under_review"`, and each adds exactly one appeal entry to the log.
5 of 5 appeals on a made-up `content_id` return `404` and add no appeal entry.

**Why this target:** The appeal is the only thing between a wrong accusation
and nothing at all, so it has to work every time, not most of the time. The
made-up-ID half catches the silent-typo failure that RUNNING.md warns about.

---

## 5. Bad input is refused cleanly and leaves a trace

I send 6 malformed requests: missing `text`, an empty string, whitespace only,
29 words, 20,001 characters, and a body that isn't JSON. All 6 return `400`
with the error code listed in the README, none return `500`, and each leaves a
`rejected` entry in the log.

**Why this target:** A crash on malformed input is one of the most common real
failures, and the attack set will try it. The log requirement is there because
a refused request that leaves no trace is an attack I'd never find.

---


<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
