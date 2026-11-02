"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

# Moving-average window for type_token_ratio, in words.
TTR_WINDOW = 50

# Punctuation that varies between writers: semicolons, colons, dashes,
# brackets, question and exclamation marks.
EXPRESSIVE_PUNCTUATION = ";:—–()?!"

# (AI-typical value, human-typical value) for each measure, set from the
# calibration inputs in Milestone 4. style_signal scales each onto 0–1 between
# these, so no measure wins just by having bigger numbers.
SCALE = {
    "spread": (0.20, 0.70),   # coefficient of variation of sentence length
    "ttr":    (0.75, 0.90),   # moving-average type-token ratio
    "punct":  (0.0, 5.0),     # expressive marks per 100 words
}


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    # One sentence has no spread to measure. 0.0 here; style_signal treats
    # it as "no evidence" rather than as perfectly even.
    if len(lengths) < 2:
        return 0.0
    # Coefficient of variation: stdev over mean, so long and short texts
    # compare. Higher means more varied, which points human.
    return round(statistics.stdev(lengths) / statistics.mean(lengths), 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    toks = words(text)
    if not toks:
        return 0.0
    # Plain TTR falls as text gets longer, so average it over a sliding
    # window instead (moving-average TTR). Short texts get plain TTR.
    if len(toks) <= TTR_WINDOW:
        return round(len(set(toks)) / len(toks), 4)
    ratios = [
        len(set(toks[i:i + TTR_WINDOW])) / TTR_WINDOW
        for i in range(len(toks) - TTR_WINDOW + 1)
    ]
    return round(sum(ratios) / len(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    toks = words(text)
    if not toks:
        return 0.0
    # Only the marks that vary between writers. Full stops and commas are
    # left out because everyone uses them.
    marks = sum(text.count(c) for c in EXPRESSIVE_PUNCTUATION)
    marks += len(re.findall(r"\s-\s|--", text))   # dashes typed as hyphens
    # Per 100 words. Higher means more varied punctuation, which points human.
    return round(100 * marks / len(toks), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    # Each measure points human when high, so each is flipped: its AI-typical
    # value maps to 1.0 and its human-typical value to 0.0, clamped between.
    def ai_ness(value, ai_end, human_end):
        return min(max((human_end - value) / (human_end - ai_end), 0.0), 1.0)

    lo, hi = SCALE["spread"]
    # One sentence has no spread, which is no evidence either way.
    spread = 0.5 if len(sentences(text)) < 2 else ai_ness(sentence_length_spread(text), lo, hi)
    lo, hi = SCALE["ttr"]
    ttr = ai_ness(type_token_ratio(text), lo, hi)
    lo, hi = SCALE["punct"]
    punct = ai_ness(punctuation_density(text), lo, hi)

    return round((spread + ttr + punct) / 3, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
