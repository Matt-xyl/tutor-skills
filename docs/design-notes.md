# Design notes and sources

Reviewed October 20, 2026. These notes explain choices made for the first public edition. They are a source review, not a claim that the repository has attracted contributors or improved anyone's learning.

## Make the first visit useful

GitHub describes a README as a place to explain a project's purpose, usefulness, getting started, support, and maintenance. The front page therefore starts with the six skills, their uses, an installation example, and what a session does. Longer examples and review cases sit in separate files. Internal links use relative paths so they remain useful in a downloaded copy. [GitHub: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

## Explain reuse and contributions

GitHub's community profile checks for files such as a README, license, contribution guidelines, and code of conduct. This edition includes those files, two focused issue templates, and a pull request template. Reporting instructions ask for a small anonymized example so a tutoring failure can be discussed without publishing a learner's records. [GitHub: Community profiles](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)

The repository uses MIT as selected by its maintainer. Each independently installable skill contains the license notice so it remains available when the folder is copied without the repository root. The license provides broad reuse permission with notice requirements and a warranty disclaimer. [Choose a License: MIT](https://choosealicense.com/licenses/mit/)

## Keep each skill portable and discoverable

The Agent Skills specification requires a `SKILL.md` with YAML frontmatter. The skill name must match its folder, and its description should explain the capability and when it applies. Each public skill is self-contained, has a focused description, and requires no private sources or sibling skills. A tutor implements its own independence boundary when that is requested, so installing INDENGPT separately is optional. [Agent Skills specification](https://agentskills.io/specification)

OpenAI's documentation describes local skill discovery, explicit and implicit invocation, and installation from other repositories. The README uses that documented local path and installer workflow. This repository distributes source skill folders; it does not claim a plugin-directory listing or verification on every compatible host. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)

## Adapt the teaching rules for another learner

The source collection was written for one person's study and research. This edition keeps the decision rules that can transfer: teach missing prerequisites, allow independent attempts, diagnose the first meaningful gap, honor direct requests, and distinguish assisted completion from later independent work. It removes personal diagnostic scores, schedules, private links, assumed experience, and a particular research model.

The five tutors have distinct scopes. The research coach remains oriented toward mathematical research rather than claiming expertise in every empirical design. The AI engineering tutor gives a prerequisite-based project ladder without tying it to one person's course choices or career expectations. None requires the learner to recreate the maintainer's profile.

## Keep validation claims narrow

The Python validator checks the expected skill set, frontmatter, bundled licenses, relative file links, and common markers of accidentally copied personal context. GitHub Actions runs the same checks. This catches packaging mistakes; it does not establish instruction-following reliability, educational effectiveness, or exhaustive removal of sensitive information.

The behavioral cases cover boundaries likely to fail, including premature solutions, missing prerequisites, valid proofs, narrow review requests, and explicit overrides. The [October 20 pilot](results/2026-10-20.md) records actual assistant responses across all six skills, with its model-provenance and review limitations. No independent multi-model evaluation or learner outcome study was run.

Research on individual teaching practices would not by itself validate their combination in these prompts. Review intervals, task counts, hint levels, and progress criteria should be treated as practical choices and adjusted to the learner, source, and course requirements. Claims of effectiveness require evidence beyond a well-written repository.
