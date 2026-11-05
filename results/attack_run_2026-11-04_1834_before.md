# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 18:34
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56** — marked by hand: see README, Attack Run — Before

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `493acfb4-44a8-4125-8679-1b557c738eca` | unsure | 0.585 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c83c9e40-2918-437b-9c53-721dbb7e9a57` | unsure | 0.640 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `6bbe8387-01bb-4094-ab7f-48bac65d6069` | unsure | 0.522 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `29b70753-f38f-4df9-8061-68303f5cc50d` | unsure | 0.639 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `76268500-ab36-4d27-be9c-8b7cada66e40` | human | 0.660 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `53f5622b-53fe-4688-baf7-c5f4c7809a01` | unsure | 0.510 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `f0629d22-e1d5-4bc9-a377-7b0b1f97b8ca` | unsure | 0.563 | BROKE |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d6b2b173-d058-42a2-97b5-5505c03b8641` | unsure | 0.596 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0a880a7d-7d68-4518-90ad-5f43432c7b80` | ai | 0.925 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c24aea57-e6e0-4f77-a656-beb657412b36` | unsure | 0.660 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `9de7f64c-b5a2-493e-9be1-ab334f49c277` | ai | 0.834 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f6b443be-186a-47ab-936a-eb44f1f6cc24` | ai | 0.783 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `29af42e0-23de-475e-8cfd-27bd2d0d9a41` | ai | 0.782 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `6d7f4d8c-5ef7-4bdb-ad9b-8e0fb680431b` | ai | 0.875 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `26411c0e-b26e-45a0-b7b8-c598704ea5fc` | ai | 0.828 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `71c255e3-7d56-4f71-b9a5-dbcb5ad58d51` | ai | 0.774 | BROKE |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ae074e53-d83a-4a38-802b-dbcb8664b773` | unsure | 0.590 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2f491da0-5967-4121-aab3-82039f309fa6` | human | 0.789 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `0465d02d-18af-44d7-af54-1bf134b08bc9` | unsure | 0.584 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `1748bc13-e98a-4406-b294-f3f28c8f4548` | unsure | 0.569 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 400 | `—` | — | — | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `90f32d8b-4383-4ba6-a38e-00f03dee1453` | unsure | 0.628 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "493acfb4-44a8-4125-8679-1b557c738eca",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5849,
  "model_score": 0.1635,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c83c9e40-2918-437b-9c53-721dbb7e9a57",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.6397,
  "model_score": 0.5943,
  "style_score": 0.1262,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "6bbe8387-01bb-4094-ab7f-48bac65d6069",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5224,
  "model_score": 0.6662,
  "style_score": 0.3786,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "29b70753-f38f-4df9-8061-68303f5cc50d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6391,
  "model_score": 0.6114,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "76268500-ab36-4d27-be9c-8b7cada66e40",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.6601,
  "model_score": 0.3212,
  "style_score": 0.3587,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "53f5622b-53fe-4688-baf7-c5f4c7809a01",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5099,
  "model_score": 0.5727,
  "style_score": 0.4471,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "f0629d22-e1d5-4bc9-a377-7b0b1f97b8ca",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5629,
  "model_score": 0.5862,
  "style_score": 0.288,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "d6b2b173-d058-42a2-97b5-5505c03b8641",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5963,
  "model_score": 0.7042,
  "style_score": 0.4883,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "0a880a7d-7d68-4518-90ad-5f43432c7b80",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9249,
  "model_score": 0.9792,
  "style_score": 0.8707,
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c24aea57-e6e0-4f77-a656-beb657412b36",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6603,
  "model_score": 0.6175,
  "style_score": 0.7032,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "9de7f64c-b5a2-493e-9be1-ab334f49c277",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.8341,
  "model_score": 0.7387,
  "style_score": 0.9296,
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "f6b443be-186a-47ab-936a-eb44f1f6cc24",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7827,
  "model_score": 0.8051,
  "style_score": 0.7603,
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "29af42e0-23de-475e-8cfd-27bd2d0d9a41",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7819,
  "model_score": 0.8329,
  "style_score": 0.7309,
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "6d7f4d8c-5ef7-4bdb-ad9b-8e0fb680431b",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8746,
  "model_score": 0.8005,
  "style_score": 0.9487,
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "26411c0e-b26e-45a0-b7b8-c598704ea5fc",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.8276,
  "model_score": 0.8814,
  "style_score": 0.7739,
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "71c255e3-7d56-4f71-b9a5-dbcb5ad58d51",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7742,
  "model_score": 0.8816,
  "style_score": 0.6667,
  "label": "This text has a lot in common with writing produced by AI tools, so we think it may not have been written by a person. This is an automatic guess and it can be wrong \u2014 clear, simple writing is sometimes mistaken for AI. If you wrote this yourself, you can ask a person to review it using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ae074e53-d83a-4a38-802b-dbcb8664b773",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5897,
  "model_score": 0.4625,
  "style_score": 0.3582,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "2f491da0-5967-4121-aab3-82039f309fa6",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.7892,
  "model_score": 0.2044,
  "style_score": 0.2173,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "0465d02d-18af-44d7-af54-1bf134b08bc9",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5839,
  "model_score": 0.5943,
  "style_score": 0.2379,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "1748bc13-e98a-4406-b294-f3f28c8f4548",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5686,
  "model_score": 0.4998,
  "style_score": 0.363,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_PI05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "90f32d8b-4383-4ba6-a38e-00f03dee1453",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6279,
  "model_score": 0.5583,
  "style_score": 0.6975,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
