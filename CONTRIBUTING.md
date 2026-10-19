# Contributing

Changes should make the tutor's next decision better: when to teach directly, when to wait for an attempt, how much a hint reveals, or what the learner's work actually establishes.

## Report a problem

Include the skill name, assistant or model if known, exact request, relevant reply, expected behavior, and a short explanation of the difference. Replace personal data with a small invented example. For premature solutions, preserve the wording that established the requested help level.

A failed example is useful even if it happens only once. Say how many times you tried it; do not turn one exchange into a general claim about a model or learner.

## Propose a change

Keep the change focused. Explain the concrete behavior it fixes and add or update a case in [behavioral-checks.md](docs/behavioral-checks.md) when relevant. Preserve direct explanation and production requests, valid alternative approaches, and the learner's control over assistance.

Each skill should work when copied on its own. Keep required instructions inside that skill's folder. Do not add mandatory accounts, private sources, model identities, or personal learner profiles. Each `SKILL.md` needs a folder-matching name and a precise description. Preserve its MIT notice.

Use plain language and concrete examples. Add a reference when it changes the tutor's decisions, rather than repeating a general manual. For a claim about educational effectiveness, link the supporting research and describe its population, task, and limits. A plausible instruction or one successful exchange does not establish a learning benefit.

Before opening a pull request:

1. Run `python scripts/validate.py` with Python 3.10 or later.
2. Try relevant behavioral cases in a fresh conversation if an assistant is available.
3. State what you actually tested, including model/host, assistance conditions, and any failures. If you only checked the files, say so.

The automated workflow checks structure and links. A maintainer still needs to judge whether an instruction is useful and whether a reported behavior supports the proposed fix.

## Scope and conduct

This collection covers five tutors and INDENGPT. Additional subjects or distribution formats can be discussed in an issue before a large change. Avoid adding personal records or a fixed learner-specific curriculum.

Follow the [code of conduct](CODE_OF_CONDUCT.md). Contributions are submitted under the repository's [MIT license](LICENSE).
