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

My service takes a piece of writing and guesses whether a person or an AI
wrote it. Here's what happens to a submission:

1. It's sent to `POST /submit` in `app.py`. The rate limiter checks it first.
2. `app.py` checks the input. Bad input gets a `400` error and is logged.
   Good input gets a `content_id`.
3. `detector.py::model_signal` gives a `model_score` from 0 to 1, based on
   how predictable the text is to gpt2.
4. `stylometry.py::style_signal` gives a `style_score` from 0 to 1, based on
   sentence lengths, word variety and punctuation.
5. `scoring.py::combine_signals` turns the two scores into one.
6. `scoring.py::score_to_label` turns that score into a label a person can
   read.
7. `audit.py` saves everything to `logs/audit.jsonl`, and the result is sent
   back.

If the writer thinks the result is wrong, they send their `content_id` to
`POST /appeal`. That marks it `under_review` in the log.

**Input rules:** `text` needs at least 30 words and at most 20,000
characters. `creator_id` needs 1–100 characters. Breaking a rule gets a `400`
error (`invalid_json`, `missing_text`, `text_too_short`, `text_too_long` or
`missing_creator_id`).

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to gpt2, a small AI model.
The more predictable it is, the higher the score (closer to AI).

**Why that might differ between human and AI writing:** AI writes by picking
likely next words, so its writing is easy for another AI to predict. People's
writing is usually more surprising.

**What it can't see:** Who actually wrote it. Plain, simple writing is
predictable too, so people writing in a second language, or just writing
simply, get scored as AI. My plain human test got 0.91, which is higher than
my AI test (0.88). It also only reads the first ~300 words.

### Signal two — the style signal

**What it measures:** The shape of the text, not what it says. It looks at
three things:
- how much sentence lengths vary
- how many different words are used
- how much punctuation like `; : — ( ) ? !` is used

Low on each one means more AI-like. Each becomes a number from 0 to 1, and I
average them.

**Why that might differ between human and AI writing:** AI tends to write
even sentences, safe words and simple punctuation. People's writing is
messier.

**What it can't see:** It can't read. Typos, splitting sentences or adding
dashes change the score without changing who wrote it. It also scores plain
human writing as AI (0.82 on my test), which is the same mistake signal one
makes.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** I average the two scores. But to get the AI label, *both*
scores have to be at least 0.60. If either one is lower, the result can only
be "unsure". That way one signal alone can't accuse someone.

**The numbers:** (in `config.py`)

| Setting | Value |
|---|---|
| Model signal weight | 0.5 |
| Style signal weight | 0.5 |
| Each score needs at least this for an AI label | 0.60 |
| Human label: score at or below | 0.35 |
| AI label: score at or above | 0.75 |

I moved the AI cutoff up from 0.65 to 0.75, because wrongly accusing a writer
is worse than missing some AI.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

My formal human test got 0.49 from signal one and 0.05 from signal two. The
average is 0.27, so it's labelled human, which is right.

The case my rule can't fix is when both signals are wrong together. My plain
human test got 0.90 and 0.82. Both are over 0.60, so it's labelled AI (0.86).
Both signals make the same mistake, so combining them doesn't help.

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

All three labels can be reached. In my tests, clearly human text scored 0.20
(human), lightly edited AI scored 0.68 (unsure) and clearly AI text scored
0.90 (AI).

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

Someone who gets this label may have written every word. So it says "we
can't tell" instead of "this might be AI". It says this happens a lot, that
it isn't a judgement about them, and that they don't have to do anything. I
left out scores and words like "suspicious", because those sound like an
accusation.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

This is plain human writing. Both signals think it's AI, so it gets the AI
label. That's why I appealed it.

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

The original decision is still there. The appeal is added after it, with
status `under_review`.

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

- *What I asked for:* Help write out the steps and undestand the codebase
- *What came back:* A clean explanation of what was happening in each file
- *What I changed:* nothing

**Moment 2**

- *What I asked for:* Are my acceptance criteria good and is the work for this milestone done?
- *What came back:* feedback on what to change (not useful)
- *What I changed:* I liked my criteria so I kept them

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 100 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

A real writer submits a few times an hour. If they're fixing typos, maybe 5
times in a minute. 10 a minute and 100 a day is plenty for them.

A script trying to figure out my thresholds needs hundreds or thousands of
tries. At 100 a day, 1,000 tries would take 10 days.

The limit also stops the model from getting overloaded, since each check
takes a second or two.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

By `creator_id`. If there isn't one, by IP address.

The problem is that a script can just use a different `creator_id` every
time and never hit the limit. The attack set did this. If I ran this for
real, I'd add a limit per IP address too.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
$ python run_attacks.py --flood 15
15 submissions as 'flood_tester' against http://127.0.0.1:5000

400 400 400 400 400 400 400 400 400 400 429 429 429 429 429

5 of 15 were rate limited.
Wrote results/flood_2026-11-04_1846.md
```

The first 10 come back `400` because the flood text is too short (under 30
words). After 10, the limit kicks in and the rest get `429`. All 15 show up
in the log.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

I ran it on port 5001 because my Mac was using port 5000 for AirPlay. The
rate limit was 5 per minute at the time.

```bash
python run_attacks.py --set attack_set --url http://127.0.0.1:5001 --label before
```

**How I marked them.** BROKE means the attack got what it was going for:
- **evasion:** AI text didn't get the AI label ("unsure" counts as broke)
- **false_positive:** human writing got labelled AI
- **prompt_injection:** the text got the result it asked for
- **malformed:** the server crashed or gave a `500`
- **flood:** requests got past the limit

| Family | Attacks | Held | Broke |
|---|---|---|---|
| `evasion` | 10 | 2 | 8 |
| `false_positive` | 8 | 2 | 6 |
| `prompt_injection` | 6 | 5 | 1 |
| `malformed` | 20 | 20 | 0 |
| `flood_same_creator` | 12 | 12 | 0 |
| **Total** | **56** | **41** | **15** |

| ID | Family | Targeting | Status | Guess | model | style | combined | Verdict | Why |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.16 | 0.67 | 0.42 | **BROKE** | AI text not caught |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.59 | 0.13 | 0.36 | **BROKE** | AI text not caught |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.67 | 0.38 | 0.52 | **BROKE** | AI text not caught |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.61 | 0.67 | 0.64 | **BROKE** | AI text not caught |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.32 | 0.36 | 0.34 | **BROKE** | labelled human |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.57 | 0.45 | 0.51 | **BROKE** | AI text not caught |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.59 | 0.29 | 0.44 | **BROKE** | AI text not caught |
| EV08 | evasion | signal one: text below the token window | 400 | — | — | — | — | **HELD** | refused, too short |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.70 | 0.49 | 0.60 | **BROKE** | AI text not caught |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.98 | 0.87 | 0.92 | **HELD** | caught |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.62 | 0.70 | 0.66 | **HELD** | not accused |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.74 | 0.93 | 0.83 | **BROKE** | human labelled AI |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.81 | 0.76 | 0.78 | **BROKE** | human labelled AI |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.83 | 0.73 | 0.78 | **BROKE** | human labelled AI |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.80 | 0.95 | 0.87 | **BROKE** | human labelled AI |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.88 | 0.77 | 0.83 | **BROKE** | human labelled AI |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.88 | 0.67 | 0.77 | **BROKE** | human labelled AI |
| FP08 | false_positive | very short genuine human submission | 400 | — | — | — | — | **HELD** | not accused, but refused for being too short |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.46 | 0.36 | 0.41 | **HELD** | instruction did nothing |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.20 | 0.22 | 0.21 | **BROKE** | got the human label it wanted |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.59 | 0.24 | 0.42 | **HELD** | instruction did nothing |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.50 | 0.36 | 0.43 | **HELD** | labels can't be changed |
| PI05 | prompt_injection | attempt to inject into the audit log | 400 | — | — | — | — | **HELD** | refused, too short |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.56 | 0.70 | 0.63 | **HELD** | instruction did nothing |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | **HELD** | 400, no crash |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | **HELD** | 400, no crash |
| MF03 | malformed | text is control characters | 400 | — | — | — | — | **HELD** | 400, no crash |
| MF04 | malformed | text is only punctuation | 400 | — | — | — | — | **HELD** | 400, no crash |
| MF05 | malformed | text is a very long single word | 400 | — | — | — | — | **HELD** | 400, no crash |
| MF06 | malformed | text is emoji only | 400 | — | — | — | — | **HELD** | 400, no crash |
| MF07 | malformed | text is right-to-left script | 400 | — | — | — | — | **HELD** | 400, no crash |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ02 | malformed | no creator_id | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ05 | malformed | text is null | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | **HELD** | 400, no crash |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | — | — | **HELD** | 429, blocked before reaching my code |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | — | — | **HELD** | 429, blocked before reaching my code |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | **HELD** | 400, no crash |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | — | — | **HELD** | refused, too short |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | — | — | **HELD** | refused, too short |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | — | — | **HELD** | refused, too short |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | — | — | **HELD** | refused, too short |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | — | — | **HELD** | refused, too short |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | blocked by the limit |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | blocked by the limit |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | blocked by the limit |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | blocked by the limit |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | blocked by the limit |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | blocked by the limit |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | blocked by the limit |

**What the counts say.** Most problems are in two groups:
- **False positives:** 6 of 8 real writers got labelled AI. Both scores were
  above 0.60 every time, so my rule didn't help.
- **Evasion:** 8 of 10 got past. 7 landed in "unsure" and 1 (EV05) got
  labelled human.

Nothing crashed.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

I picked entries that show problems: 4 real writers labelled AI, 3 AI texts
that got through, the injection that got labelled human, and 3 rejected
requests (one too short, two rate limited).

```json
{"combined_score": 0.7827, "confidence": 0.7827, "content_id": "f6b443be-186a-47ab-936a-eb44f1f6cc24", "creator_id": "attacker_FP03", "guess": "ai", "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong — clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.", "model_score": 0.8051, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.7603, "text_sha256": "f876400f145c0cbc5c16df96a83f6229e8c50624fc35965309d7af61e78eb591", "timestamp": "2026-11-05T00:34:03+00:00", "truncated": false, "word_count": 83}
{"combined_score": 0.8746, "confidence": 0.8746, "content_id": "6d7f4d8c-5ef7-4bdb-ad9b-8e0fb680431b", "creator_id": "attacker_FP05", "guess": "ai", "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong — clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.", "model_score": 0.8005, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.9487, "text_sha256": "7545ded553421ccf87614ff03476af3a7201673a13c9b2fbeda5fb6865b6253d", "timestamp": "2026-11-05T00:34:04+00:00", "truncated": false, "word_count": 70}
{"combined_score": 0.8341, "confidence": 0.8341, "content_id": "9de7f64c-b5a2-493e-9be1-ab334f49c277", "creator_id": "attacker_FP02", "guess": "ai", "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong — clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.", "model_score": 0.7387, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.9296, "text_sha256": "631b8f514858e6565b1b9c6cd26b881a805685dd7cacb69bfc7d465c9e9c1874", "timestamp": "2026-11-05T00:34:03+00:00", "truncated": false, "word_count": 76}
{"combined_score": 0.7742, "confidence": 0.7742, "content_id": "71c255e3-7d56-4f71-b9a5-dbcb5ad58d51", "creator_id": "attacker_FP07", "guess": "ai", "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong — clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.", "model_score": 0.8816, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.6667, "text_sha256": "73509863f15b33de726aff73dada059e1ce22d201f4b758fb1fb99736b8be0f5", "timestamp": "2026-11-05T00:34:04+00:00", "truncated": false, "word_count": 59}
{"combined_score": 0.3399, "confidence": 0.6601, "content_id": "76268500-ab36-4d27-be9c-8b7cada66e40", "creator_id": "attacker_EV05", "guess": "human", "label": "We think this was probably written by a person.", "model_score": 0.3212, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.3587, "text_sha256": "a20f4a78c4a56779b7954a3c8a3d23379d39e2cfd71e7aa1d6bb687be407f3f5", "timestamp": "2026-11-05T00:34:03+00:00", "truncated": false, "word_count": 81}
{"combined_score": 0.4151, "confidence": 0.5849, "content_id": "493acfb4-44a8-4125-8679-1b557c738eca", "creator_id": "attacker_EV01", "guess": "unsure", "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything — but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.", "model_score": 0.1635, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.6667, "text_sha256": "c9c118b0916bad8afd0a8c469d4c1e2e566af634c9a3632121921d1d5835236b", "timestamp": "2026-11-05T00:34:03+00:00", "truncated": false, "word_count": 84}
{"combined_score": 0.2108, "confidence": 0.7892, "content_id": "2f491da0-5967-4121-aab3-82039f309fa6", "creator_id": "attacker_PI02", "guess": "human", "label": "We think this was probably written by a person.", "model_score": 0.2044, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.2173, "text_sha256": "61f8f3b0b0b9bcae0f3558ded6225d5fbed5ac3d5d76d004a5ddf4bd9dfb18df", "timestamp": "2026-11-05T00:34:04+00:00", "truncated": false, "word_count": 42}
{"combined_score": 0.5963, "confidence": 0.5963, "content_id": "d6b2b173-d058-42a2-97b5-5505c03b8641", "creator_id": "attacker_EV09", "guess": "unsure", "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything — but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.", "model_score": 0.7042, "rule": {"agreement_floor": 0.6, "ai_threshold": 0.75, "human_threshold": 0.35, "weight_model": 0.5, "weight_style": 0.5}, "status": "decided", "style_score": 0.4883, "text_sha256": "6a1df5493d488bb6ecf34ad402e25dd37bdb9eab8b4d15ada43d500d6ffde81e", "timestamp": "2026-11-05T00:34:03+00:00", "truncated": false, "word_count": 110}
{"creator_id": "attacker_FP08", "event": "rejected", "reason": "text_too_short", "status": "rejected", "timestamp": "2026-11-05T00:34:04+00:00"}
{"creator_id": "unknown", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-05T00:34:04+00:00"}
{"creator_id": "attacker_flood", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-05T00:34:04+00:00"}
```

What these show:
- All the wrongly accused writers had both scores above 0.60, so my rule
  didn't protect them.
- EV01 used typos to fool signal two, but it fooled signal one more (0.16).
- The `unknown` entry is RQ10 or RQ11. They had no `creator_id`, so they were
  limited by IP address and never reached my code.

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03:** someone writing carefully in their second language got labelled AI
(0.78). This is the same person I worried about in Milestone 1. They use
simple words and even sentences because they're being careful, and both
signals read that as AI (0.81 and 0.76). The label says it might be wrong and
lets them appeal, but it still tells them we don't think they wrote their own
work.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My writing labelled AI | ≤ 1 of 10 | 1/10 | 1/10 | 1/10 | MET |
| 2. AI scores at least 0.30 above human | gap ≥ 0.30 | 0.41 | 0.41 | 0.41 | MET |
| 3. All three labels show up | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 4. Appeals work, fake IDs refused | 10 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Bad input gets a 400 and is logged | 6 of 6 | 6/6 | 6/6 | 6/6 | MET |

I ran `python run_eval.py --label before --url http://127.0.0.1:5001` (port
5001 because AirPlay was using 5000). All five were met in all three runs.
The scores were exactly the same every run, because gpt2 gives the same
answer for the same text.

How I got each number:
1. 1 of my 10 pieces was labelled AI: the plain "I went to the store" one
   (0.87). 6 were unsure and 3 were human.
2. My 5 AI texts averaged 0.82 and my 5 own pieces averaged 0.41, a gap of
   0.41.
3. The 4 inputs got ai, unsure, unsure and human, so all three labels showed
   up.
4. 5 real appeals got `200` and `under_review` with 1 appeal in the log. 5
   fake IDs got `404` with nothing logged.
5. All 6 bad requests got a `400` with the right error, and each one was
   logged as `rejected`.

To test criteria 4 and 5, I added to `run_eval.py`. It now sends appeals
(`run_eval.py::run_appeals`), can send a body that isn't JSON, and checks
the log after each request.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

All of this is Run 1, from `results/run_2026-11-04_1957_before.md`, made by
`run_eval.py::main`.

**Criterion 1: my own and plain writing**

```json
[
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.5066,
    "model_score": 0.2667,
    "style_score": 0.7201,
    "combined_score": 0.4934,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "good afternoon, my name is bibble. I am the director of dog food in mi"
  },
  {
    "status": 200,
    "error": null,
    "guess": "human",
    "confidence": 0.7067,
    "model_score": 0.2193,
    "style_score": 0.3674,
    "combined_score": 0.2933,
    "label": "We think this was probably written by a person.",
    "logged_as": "decided:human",
    "sent": "sup my name is gregory. I like rap music and mediterranina food, like "
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.6981,
    "model_score": 0.4959,
    "style_score": 0.9002,
    "combined_score": 0.6981,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "In other news today, the democrats won the house and governor nominati"
  },
  {
    "status": 200,
    "error": null,
    "guess": "human",
    "confidence": 0.7403,
    "model_score": 0.2238,
    "style_score": 0.2956,
    "combined_score": 0.2597,
    "label": "We think this was probably written by a person.",
    "logged_as": "decided:human",
    "sent": "Exhibiting a growing sense of panic as screens lit up with rumors and "
  },
  {
    "status": 200,
    "error": null,
    "guess": "human",
    "confidence": 0.7123,
    "model_score": 0.5337,
    "style_score": 0.0418,
    "combined_score": 0.2877,
    "label": "We think this was probably written by a person.",
    "logged_as": "decided:human",
    "sent": "\u201cJon Ossoff running for president? No, no, you must be mistaken. He ju"
  },
  {
    "status": 200,
    "error": null,
    "guess": "ai",
    "confidence": 0.8715,
    "model_score": 0.8645,
    "style_score": 0.8785,
    "combined_score": 0.8715,
    "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
    "logged_as": "decided:ai",
    "sent": "I went to the store. I bought food. I like milk. I eat bread. I like t"
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.7014,
    "model_score": 0.5451,
    "style_score": 0.8576,
    "combined_score": 0.7014,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "I worked today. I work at a start up. I painted my nails. My nails are"
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.6112,
    "model_score": 0.5073,
    "style_score": 0.7151,
    "combined_score": 0.6112,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "I like coconut. I dont like coconut milk. i use coconut oil in my hair"
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.5023,
    "model_score": 0.3064,
    "style_score": 0.689,
    "combined_score": 0.4977,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "I like coffee. Pressed coffee is new for me I haven't had it yet. I li"
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.6538,
    "model_score": 0.5431,
    "style_score": 0.7645,
    "combined_score": 0.6538,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "I want to buy a new phone. I like the pink one. It is very expensive. "
  }
]
```

**Criterion 2: AI texts**

```json
[
  {
    "status": 200,
    "error": null,
    "guess": "ai",
    "confidence": 0.8298,
    "model_score": 0.8477,
    "style_score": 0.812,
    "combined_score": 0.8298,
    "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
    "logged_as": "decided:ai",
    "sent": "The implementation of the proposed framework requires careful consider"
  },
  {
    "status": 200,
    "error": null,
    "guess": "ai",
    "confidence": 0.7544,
    "model_score": 0.826,
    "style_score": 0.6829,
    "combined_score": 0.7544,
    "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
    "logged_as": "decided:ai",
    "sent": "Effective time management is essential for achieving success in both p"
  },
  {
    "status": 200,
    "error": null,
    "guess": "ai",
    "confidence": 0.7917,
    "model_score": 0.9267,
    "style_score": 0.6568,
    "combined_score": 0.7917,
    "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
    "logged_as": "decided:ai",
    "sent": "Climate change represents one of the most significant challenges facin"
  },
  {
    "status": 200,
    "error": null,
    "guess": "ai",
    "confidence": 0.8743,
    "model_score": 0.8643,
    "style_score": 0.8844,
    "combined_score": 0.8743,
    "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
    "logged_as": "decided:ai",
    "sent": "Social media has transformed the way people communicate and share info"
  },
  {
    "status": 200,
    "error": null,
    "guess": "ai",
    "confidence": 0.8451,
    "model_score": 0.9283,
    "style_score": 0.7618,
    "combined_score": 0.8451,
    "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
    "logged_as": "decided:ai",
    "sent": "Regular physical activity offers numerous benefits for both physical a"
  }
]
```

**Criterion 2: my own writing**

```json
[
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.5066,
    "model_score": 0.2667,
    "style_score": 0.7201,
    "combined_score": 0.4934,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "good afternoon, my name is bibble. I am the director of dog food in mi"
  },
  {
    "status": 200,
    "error": null,
    "guess": "human",
    "confidence": 0.7067,
    "model_score": 0.2193,
    "style_score": 0.3674,
    "combined_score": 0.2933,
    "label": "We think this was probably written by a person.",
    "logged_as": "decided:human",
    "sent": "sup my name is gregory. I like rap music and mediterranina food, like "
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.6981,
    "model_score": 0.4959,
    "style_score": 0.9002,
    "combined_score": 0.6981,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "In other news today, the democrats won the house and governor nominati"
  },
  {
    "status": 200,
    "error": null,
    "guess": "human",
    "confidence": 0.7403,
    "model_score": 0.2238,
    "style_score": 0.2956,
    "combined_score": 0.2597,
    "label": "We think this was probably written by a person.",
    "logged_as": "decided:human",
    "sent": "Exhibiting a growing sense of panic as screens lit up with rumors and "
  },
  {
    "status": 200,
    "error": null,
    "guess": "human",
    "confidence": 0.7123,
    "model_score": 0.5337,
    "style_score": 0.0418,
    "combined_score": 0.2877,
    "label": "We think this was probably written by a person.",
    "logged_as": "decided:human",
    "sent": "\u201cJon Ossoff running for president? No, no, you must be mistaken. He ju"
  }
]
```

**Criterion 3: label coverage**

```json
[
  {
    "status": 200,
    "error": null,
    "guess": "ai",
    "confidence": 0.8298,
    "model_score": 0.8477,
    "style_score": 0.812,
    "combined_score": 0.8298,
    "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
    "logged_as": "decided:ai",
    "sent": "The implementation of the proposed framework requires careful consider"
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.6805,
    "model_score": 0.7121,
    "style_score": 0.649,
    "combined_score": 0.6805,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "Getting a new framework off the ground takes some thought. You've got "
  },
  {
    "status": 200,
    "error": null,
    "guess": "unsure",
    "confidence": 0.5066,
    "model_score": 0.2667,
    "style_score": 0.7201,
    "combined_score": 0.4934,
    "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
    "logged_as": "decided:unsure",
    "sent": "good afternoon, my name is bibble. I am the director of dog food in mi"
  },
  {
    "status": 200,
    "error": null,
    "guess": "human",
    "confidence": 0.7067,
    "model_score": 0.2193,
    "style_score": 0.3674,
    "combined_score": 0.2933,
    "label": "We think this was probably written by a person.",
    "logged_as": "decided:human",
    "sent": "sup my name is gregory. I like rap music and mediterranina food, like "
  }
]
```

**Criterion 4: appeals** (made by `run_eval.py::run_appeals`)

```json
[
  {
    "kind": "real",
    "content_id": "7cb88847-4fb6-432e-b611-cf66cec9eae2",
    "appeal_status": 200,
    "reported_status": "under_review",
    "error": null,
    "appeal_entries_in_log": 1
  },
  {
    "kind": "real",
    "content_id": "1e240695-c7bd-4222-9a72-28438be8ed9b",
    "appeal_status": 200,
    "reported_status": "under_review",
    "error": null,
    "appeal_entries_in_log": 1
  },
  {
    "kind": "real",
    "content_id": "fea1228a-2a8b-4d41-babd-927ec8cb99f9",
    "appeal_status": 200,
    "reported_status": "under_review",
    "error": null,
    "appeal_entries_in_log": 1
  },
  {
    "kind": "real",
    "content_id": "d9a62a89-4bc0-4ac6-8562-ccdc79704edd",
    "appeal_status": 200,
    "reported_status": "under_review",
    "error": null,
    "appeal_entries_in_log": 1
  },
  {
    "kind": "real",
    "content_id": "f36d384c-0ee7-4536-ab8c-c102ce30ae10",
    "appeal_status": 200,
    "reported_status": "under_review",
    "error": null,
    "appeal_entries_in_log": 1
  },
  {
    "kind": "fake",
    "content_id": "84547cf0-cf3e-4d36-9f2a-9b066d98d8b4",
    "appeal_status": 404,
    "reported_status": null,
    "error": "unknown_content_id",
    "appeal_entries_in_log": 0
  },
  {
    "kind": "fake",
    "content_id": "0cf396bf-f3d3-4669-9cb3-98889cb92047",
    "appeal_status": 404,
    "reported_status": null,
    "error": "unknown_content_id",
    "appeal_entries_in_log": 0
  },
  {
    "kind": "fake",
    "content_id": "51bc9d9a-178a-4102-9eff-20b20db1d18e",
    "appeal_status": 404,
    "reported_status": null,
    "error": "unknown_content_id",
    "appeal_entries_in_log": 0
  },
  {
    "kind": "fake",
    "content_id": "2481e722-8278-4f96-8028-c3067ec77257",
    "appeal_status": 404,
    "reported_status": null,
    "error": "unknown_content_id",
    "appeal_entries_in_log": 0
  },
  {
    "kind": "fake",
    "content_id": "d015ebf8-bb50-41bd-944c-da439e42cc37",
    "appeal_status": 404,
    "reported_status": null,
    "error": "unknown_content_id",
    "appeal_entries_in_log": 0
  }
]
```

**Criterion 5: bad input**

```json
[
  {
    "status": 400,
    "error": "missing_text",
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "logged_as": "rejected:missing_text",
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "error": "text_too_short",
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "logged_as": "rejected:text_too_short",
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "error": "text_too_short",
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "logged_as": "rejected:text_too_short",
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "error": "text_too_short",
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "logged_as": "rejected:text_too_short",
    "sent": "This sentence is here to test the minimum length rule, and it has been"
  },
  {
    "status": 400,
    "error": "text_too_long",
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "logged_as": "rejected:text_too_long",
    "sent": "a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a "
  },
  {
    "status": 400,
    "error": "invalid_json",
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "logged_as": "rejected:invalid_json",
    "sent": "raw body: 'this is not json'"
  }
]
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
