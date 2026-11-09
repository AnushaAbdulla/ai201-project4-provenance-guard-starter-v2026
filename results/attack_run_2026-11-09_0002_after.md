# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 00:02
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c4468034-0662-403e-bb9f-94a034915376` | unsure | 0.585 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `b9c4f1e4-2d45-425c-830d-9a7b1736327f` | unsure | 0.640 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `5e8a338b-03f1-42d1-bf80-d1ff7d3656df` | unsure | 0.522 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `a114a497-0734-4b94-a2b5-66aec00a39ea` | unsure | 0.639 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `d1635ac7-b002-47e0-86fc-d9140a71a117` | human | 0.660 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `238eec2f-8deb-4727-b343-c46775089f10` | unsure | 0.510 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b1ba37df-4b0a-4f99-8ad4-7ab0153a0c0a` | unsure | 0.563 | BROKE |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `163a93e3-81de-4e8c-b2f7-6ec7c3458de1` | unsure | 0.596 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `17056efc-5ea9-4174-aa63-fadc83f307a9` | ai | 0.925 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `eefceb68-df1a-43dd-8973-3f3efbf7dfa3` | unsure | 0.660 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `8dc3df18-1340-437d-b9aa-7d57c55a0cb8` | ai | 0.834 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `06c45085-8536-4e78-a46a-4b61577a1630` | unsure | 0.783 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `22dd4000-3917-434e-ab05-254eaf84c7de` | unsure | 0.782 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `ddbf2aee-664f-4935-8bd4-22bf70335623` | ai | 0.875 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `56d7e4df-21ce-4efd-b50b-de04ff11589a` | ai | 0.828 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `1acd1678-3317-40ed-95f5-f7804279fa01` | unsure | 0.774 | HELD |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f766a626-c579-462e-9cfd-1ad6e2fcdf39` | unsure | 0.590 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `903cc3bc-7069-44a1-bc01-07c9f10b4585` | human | 0.789 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `db4ff49b-f25f-485f-874d-28375fb7493a` | unsure | 0.584 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `06e24271-52b0-464a-8665-293237b1d77d` | unsure | 0.569 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 400 | `—` | — | — | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `211bdc74-0b25-434e-8801-644bd8b1dbbc` | unsure | 0.628 | HELD |
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
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
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
  "content_id": "c4468034-0662-403e-bb9f-94a034915376",
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
  "content_id": "b9c4f1e4-2d45-425c-830d-9a7b1736327f",
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
  "content_id": "5e8a338b-03f1-42d1-bf80-d1ff7d3656df",
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
  "content_id": "a114a497-0734-4b94-a2b5-66aec00a39ea",
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
  "content_id": "d1635ac7-b002-47e0-86fc-d9140a71a117",
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
  "content_id": "238eec2f-8deb-4727-b343-c46775089f10",
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
  "content_id": "b1ba37df-4b0a-4f99-8ad4-7ab0153a0c0a",
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
  "content_id": "163a93e3-81de-4e8c-b2f7-6ec7c3458de1",
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
  "content_id": "17056efc-5ea9-4174-aa63-fadc83f307a9",
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
  "content_id": "eefceb68-df1a-43dd-8973-3f3efbf7dfa3",
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
  "content_id": "8dc3df18-1340-437d-b9aa-7d57c55a0cb8",
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
  "content_id": "06c45085-8536-4e78-a46a-4b61577a1630",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7827,
  "model_score": 0.8051,
  "style_score": 0.7603,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
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
  "content_id": "22dd4000-3917-434e-ab05-254eaf84c7de",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7819,
  "model_score": 0.8329,
  "style_score": 0.7309,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
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
  "content_id": "ddbf2aee-664f-4935-8bd4-22bf70335623",
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
  "content_id": "56d7e4df-21ce-4efd-b50b-de04ff11589a",
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
  "content_id": "1acd1678-3317-40ed-95f5-f7804279fa01",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7742,
  "model_score": 0.8816,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with an AI tool. That happens a lot, and it isn't a judgement about you or your work. If you wrote it yourself, you don't need to do anything \u2014 but if you'd like a person to look at it, you can ask for a review using the content ID shown with this result.",
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
  "content_id": "f766a626-c579-462e-9cfd-1ad6e2fcdf39",
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
  "content_id": "903cc3bc-7069-44a1-bc01-07c9f10b4585",
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
  "content_id": "db4ff49b-f25f-485f-874d-28375fb7493a",
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
  "content_id": "06e24271-52b0-464a-8665-293237b1d77d",
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
  "content_id": "211bdc74-0b25-434e-8801-644bd8b1dbbc",
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

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
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

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
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

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
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

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
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

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
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
