# Tutor Skills

Six agent skills for learning with an AI tutor: general study, mathematics, research, programming, AI engineering, and INDENGPT for stricter independent practice.

The tutors help you understand a topic, attempt the work, and repair the part that went wrong. They also answer direct questions directly. If you ask for an explanation or a complete solution, they provide it, while keeping that help separate from evidence of what you can do independently.

## Choose a skill

| Skill | Use it for | Try asking |
| --- | --- | --- |
| [General learning tutor](skills/general-learning-tutor/SKILL.md) | Studying a source, recall, comparing similar concepts, and later review | “Use general-learning-tutor to help me study these notes. Start with the distinction between the two concepts.” |
| [Math tutor](skills/math-tutor/SKILL.md) | Mathematical definitions, method selection, calculus, and proofs | “Use math-tutor. Check my proof and identify the first step that needs justification.” |
| [Research coach](skills/research-coach/SKILL.md) | Mathematical research, study design, computation, sources, and manuscript feedback | “Use research-coach. Does this conclusion follow from the experiment I described?” |
| [Programming tutor](skills/programming-tutor/SKILL.md) | Learning to write, explain, debug, test, and modify code | “Use programming-tutor. Here is my code and the output I expected. Help me locate the first mismatch.” |
| [AI engineering tutor](skills/ai-engineering-tutor/SKILL.md) | Moving from programming practice to reproducible ML experiments and AI applications | “Use ai-engineering-tutor. Help me choose a small project based on the Python I can currently write.” |
| [INDENGPT](skills/indengpt/SKILL.md) | Keeping the reasoning yours during a problem or study block | “Use INDENGPT for this problem. Give no hints unless I ask.” |

Start with the tutor closest to your goal. You do not need all six active at once. INDENGPT can work on its own or alongside a tutor; it changes how much help is given before an attempt.

## Get started

These are instruction files in the [Agent Skills format](https://agentskills.io/specification). They need an assistant that can read skill files. They do not require an API key, a paid course, or a particular model to read and use the instructions. Your chosen assistant may have its own access requirements.

### Install in Codex

Ask the built-in installer to install one folder from this repository, for example:

```text
Use $skill-installer to install skills/math-tutor from
https://github.com/Matt-xyl/tutor-skills
```

Then start a conversation with:

```text
Use $math-tutor. I am learning integration techniques.
Give me one problem to check whether I can choose the method myself.
```

You can also download or clone the repository and copy a complete skill folder into a skill location supported by your host. For current Codex local discovery, examples are `~/.agents/skills/math-tutor/` for your user or `.agents/skills/math-tutor/` in a project. Keep `SKILL.md` and the bundled license together. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery and installation behavior. If a new skill does not appear, restart Codex.

### Use another assistant

Use that assistant's documented Agent Skills installation method. If it cannot load skills, paste the selected `SKILL.md` into the conversation and ask it to follow the instructions for the current task. This is manual prompt use; it does not install a skill or guarantee that the assistant will follow every rule.

Read a skill before installing it. These folders contain instructions and a license; the repository's validation script is for maintainers and is not needed during tutoring.

## What a session looks like

In ordinary tutoring, you can bring your source, your attempt, or a question. The tutor uses what you already supplied and asks only for information that changes the next step. For new material, it teaches the missing idea. For familiar material, it can start with a problem and wait for your attempt.

Feedback usually identifies the first consequential gap and gives you a chance to repair it. A full critique, a worked solution, or a requested implementation can be useful too; the tutor should provide the help you asked for. Completing an assisted task and learning to do it independently are different outcomes, so a later fresh problem is needed when independence is what you want to check.

Under INDENGPT, hints come only when requested. “Give me the full solution to this one” permits the solution for that item. “Turn off INDENGPT for this session” ends that restriction for the study block. [More example requests](docs/examples.md) show these boundaries.

## Bring your own context

Tell the tutor your current goal and provide the relevant source or attempt. You can add a course rubric, preferred language, available time, or programming environment when it affects the work. There is no required learning-profile spreadsheet and no assumed curriculum.

The public skills are adapted from a personal tutoring collection maintained by [Matt-xyl](https://github.com/Matt-xyl). Personal study records, private document links, and assumptions about one learner's background were removed. This repository is maintained separately; it does not read or synchronize anyone's private learning records.

## What has been checked

The repository includes structural checks for the six skill folders, frontmatter, local links, bundled licenses, and accidental personal-context references. A set of [behavioral review cases](docs/behavioral-checks.md) describes what to check in an actual assistant session.

Structural validation does not show that a tutor improves learning. These prompts have not been established as an effective educational intervention, and different models may follow them differently. Claims about progress should come from the learner's actual work, including later independent performance when relevant. A source review and the limits of the design are recorded in [design notes](docs/design-notes.md).

## Contribute or report a problem

Open an issue with the skill name, a small anonymized example, and what should have happened. If the tutor reveals a solution too early, include the request that set the help level. Do not post private learning records, credentials, or unpublished research.

For changes, read [CONTRIBUTING.md](CONTRIBUTING.md). To run the local checks with Python 3.10 or later:

```sh
python scripts/validate.py
```

Maintained by Matt-xyl. Released under the [MIT license](LICENSE).
