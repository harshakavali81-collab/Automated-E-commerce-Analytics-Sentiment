# Sentiment model card — v1 deterministic rules baseline

## Purpose
Classify short English review text as positive, neutral or negative in a fully offline educational demo.

## Implementation
The scorer uses a small, manually curated word lexicon. Positive words add +1 and negative words -1. Negation words in the preceding two tokens flip a matched sentiment word. Sum above zero is positive, below zero negative, exactly zero neutral.

## Training data
**None.** This is a lexicon heuristic, not a trained transformer or a supervised machine learning model. All default review examples are synthetic.

## Evaluation
Automated tests check a small set of authored examples, positive/negative/neutral behavior, case normalization and negation. These tests **do not produce a statistical accuracy, precision, recall, or F1 score on independently labeled real-world reviews**.

## Risks and limitations
- Ignores sarcasm, subtle context, spelling variations, emojis, aspect-based opinions and non-English content.
- May misclassify negations, repeated terms and product-specific meanings.
- Review-selection biases, incentivized reviews and missing reviews are not controlled.
- Must not be interpreted as verified customer satisfaction, a moderation score, or a measure of all customers.

## Improvement path
Obtain a lawful, privacy-reviewed, representative labeled dataset. Split before modeling; report macro-F1, class-wise precision/recall, calibration/abstention coverage, and slice metrics. Compare the lexicon against a TF-IDF baseline and a contextual language model. Document the data's license, collection period, geographic coverage and language mix before deploying.
