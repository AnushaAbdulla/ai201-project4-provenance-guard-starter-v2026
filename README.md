# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

**Input rules for `/submit`:** `text` must be 30+ words and at most 20,000 characters; `creator_id` must be 1–100 characters.
**Bad input gets a `400`** with one of `invalid_json`, `missing_text`, `text_too_short`, `text_too_long`, `missing_creator_id` (or `503 detector_unavailable` if the model won't load), and every refusal is logged as `rejected`.



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

### Signal two — the style signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Average the two signals, equally weighted. An AI label also
needs *both* signals to lean AI on their own: if either one is below the
agreement floor, the score is capped just under the AI threshold, so it can
land in "unsure" but never in "AI". One signal alone can't produce an
accusation. When they disagree in the other direction (one says human), the
average already pulls the score toward the middle, and I leave that alone,
because two methods disagreeing *is* uncertainty.

**The numbers:** (in `config.py`)

| Setting | Value |
|---|---|
| `WEIGHT_MODEL_SIGNAL` | 0.5 |
| `WEIGHT_STYLE_SIGNAL` | 0.5 |
| `AGREEMENT_FLOOR` (each signal must reach this for an AI label) | 0.60 |
| `HUMAN_THRESHOLD` (at or below → high-confidence human) | 0.35 |
| `AI_THRESHOLD` (at or above → high-confidence AI) | 0.75 |

The AI threshold sits at 0.75, not the starter's 0.65, so the unsure band
is wider on the AI side: a wrong accusation costs a writer more than a
missed detection costs the site.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

Formal human writing: a dense paragraph about a municipal permit dispute, with
semicolons, a colon, dashes, and sentences from 4 to 40+ words. Signal one gave
it **0.487** (the rare legal vocabulary surprised gpt2, so it was unsure).
Signal two gave it **0.050** (very uneven sentences, varied vocabulary, lots
of expressive punctuation). The average is **0.269**, below the human
threshold, so it's labelled human. The rule did what I want here: when one
signal is unsure and the other is confident it's human, the writer isn't
pushed toward an accusation.

The case my rule *can't* fix is the one where the signals agree and are both
wrong. Plain human writing (short sentences, common words, no semicolons or
dashes) scored **0.896** on signal one and **0.822** on signal two, so it
passes the agreement floor and lands at **0.859**, which is high-confidence AI.
Both blind spots hit the same writer, so no weighting of these two signals
separates them from clearly-AI text (0.896). That is the false positive I
traced in Milestone 1, and criterion 1 is where it will show up.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | above 0.35, below 0.75 | We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything — but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result. |
| high-confidence AI | 0.75 – 1.00 | This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong — clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result. |

All three are reachable. From my test inputs: clearly human text scored 0.20
(human), lightly edited AI scored 0.68 (unsure), and clearly AI text scored
0.90 (AI).

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The person reading it may have written every word, so it says "we can't
tell" about *us*, not "this might be AI" about *them*. It says outright that
this result is common and isn't a judgement, and that a writer who wrote it
themselves doesn't need to do anything. A review is offered as an option, not
demanded. I didn't use the word "suspicious", any score, or "AI-generated"
on its own, because those all read as an accusation with a hedge attached.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

This is plain human writing, the false positive from Milestone 1. Both
signals read it as AI, so it gets the AI label. That's why it's the one I
appeal.

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I moved to this city two years ago. At first it was hard for me. I did not know many people and my English was not very good. Now I have a job and some friends. I think the most important thing is to be patient. Every day I learn something new. My manager is kind and helps me when I have a problem. I want to study more next year.", "creator_id": "writer-42"}'
```

```json
{
  "combined_score": 0.8589,
  "confidence": 0.8589,
  "content_id": "f4b4b712-20e8-4f3a-9295-a43859f5efeb",
  "creator_id": "writer-42",
  "guess": "ai",
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "model_score": 0.8958,
  "status": "decided",
  "style_score": 0.822,
  "truncated": false
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "f4b4b712-20e8-4f3a-9295-a43859f5efeb", "reasoning": "I wrote this myself about my first two years here. English is my second language, so I keep my sentences simple on purpose."}'
```

```json
{
  "appealed_at": "2026-11-02T23:41:04+00:00",
  "content_id": "f4b4b712-20e8-4f3a-9295-a43859f5efeb",
  "message": "Thanks \u2014 your appeal is recorded and a person will review it. The original result isn't final while that happens.",
  "original_guess": "ai",
  "original_label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "status": "under_review"
}
```

**What the log shows afterwards**

The original decision is still there, unchanged, with the appeal appended
after it, now `under_review`.

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.8589,
      "content_id": "f4b4b712-20e8-4f3a-9295-a43859f5efeb",
      "creator_id": "writer-42",
      "guess": "ai",
      "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
      "model_score": 0.8958,
      "status": "decided",
      "style_score": 0.822,
      "timestamp": "2026-11-02T23:40:55+00:00"
    },
    {
      "content_id": "f4b4b712-20e8-4f3a-9295-a43859f5efeb",
      "creator_id": "writer-42",
      "event": "appeal",
      "reasoning": "I wrote this myself about my first two years here. English is my second language, so I keep my sentences simple on purpose.",
      "status": "under_review",
      "timestamp": "2026-11-02T23:41:04+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
