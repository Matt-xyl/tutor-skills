# Example requests

These are sample requests and expected boundaries, not transcripts of measured tutor performance. Use the skill names shown by your host after installation.

## Study a supplied source

```text
Use general-learning-tutor. Here are my course notes on correlation and
causation. Help me explain the distinction, then give me one fresh scenario.
Use these notes as the assessment scope.
```

The tutor should use the supplied source and teach what is missing. A same-session scenario can be practice; it should not be described as proof of long-term retention.

## Review a proof

```text
Use math-tutor. Check this proof, but do not replace it.
Identify only the first step that needs a justification.
```

The tutor should evaluate the actual route and locate the first material gap. If the proof is valid, it should accept it rather than invent a cosmetic objection.

## Debug your own code

```text
Use programming-tutor. I expected the loop to process every item, but the
last item is missing. Here is my code and a small input. Help me understand
the first mismatch, and let me try the fix.
```

The tutor can explain language behavior and the error locally. It should preserve the attempt and leave the requested repair to the learner.

## Request an implementation

```text
Use programming-tutor. Implement this file parser and test the three cases
below. I want a working implementation, not a lesson for this task.
```

The tutor should complete the stated implementation and verification using available tools. It should say what ran and keep supplied work separate from independent learning evidence.

## Review research claims

```text
Use research-coach. I changed two experimental settings at once and observed
a lower error. Does my conclusion about the first setting follow?
Review the inference; do not redesign the study yet.
```

The coach should address whether the evidence separates the two changes. It should stay within the inference review and avoid inventing results or a new research question.

## Plan a small ML experiment

```text
Use ai-engineering-tutor. I can write functions and read CSV files.
Help me choose one small classification project. Start with the target,
baseline, data split, and metric before selecting a model.
```

The tutor should check prerequisites relevant to that project and help make evaluation meaningful. A more complex model or polished interface is not enough to establish quality.

## Protect an independent attempt

```text
Use math-tutor and INDENGPT for this study block.
Give me one series-convergence problem. Do not name a test or include a hint.
```

After the attempt, a request can change the help level:

```text
Give me one minimal hint about the gap in my argument.
```

The response should contain one bounded cue, then wait. A later request can permit full help:

```text
Give me the full solution to this one. Keep INDENGPT active for the next item.
```

The solution is now permitted for that item. Future items in the block retain the restriction. To end the mode for the block:

```text
Turn off INDENGPT for this session and explain the topic directly.
```
