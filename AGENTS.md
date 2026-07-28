# Contributor & agent guide

This file explains how to add a project to **awesome-swarm** correctly the first time — whether you are a human or an AI coding agent acting on someone's behalf. It complements [CONTRIBUTING.md](CONTRIBUTING.md), which holds the canonical submission rules; this guide adds the *procedure* and the *verification steps* that keep the list accurate.

If you are an AI agent submitting on behalf of a project's author, everything below applies to you directly. Please follow it end to end rather than guessing.

## What this repository is

A curated list of free and open-source projects related to [Swarm](https://www.ethswarm.org/) and its Bee client. Entries are grouped by purpose. The list favours real, reachable, actively-maintained, openly-licensed software.

## Eligibility — check before you propose an entry

A project qualifies only if **all** of the following are true:

- **Related to Bee or Swarm** — it is built on, for, or directly integrates Swarm. We do not list forks of Swarm/Bee themselves, nor generic tooling that merely could be pointed at Swarm.
- **Free / open-source software** with a real, correctly-set-up `LICENSE` in the repository.
- **Public and reachable** — the repository resolves and is not private. Do not list private, unpublished, or "coming soon" repositories.
- **Real** — one entry corresponds to one real, existing artifact. Do not invent projects, and do not list something you cannot open and read.

## The submission format

One project per pull request. Use the exact entry format from [CONTRIBUTING.md](CONTRIBUTING.md):

```
[Name](https://github.com/<owner>/<repo>) - Short description, under 160 characters, sentence case.
```

- Keep the description factual and specific; describe what the project *does*, not marketing copy.
- Match the description to the repository you link — do not describe a sibling repo (a common mistake when a project spans a CLI, a web app, and a library).
- Place the entry in the section that fits its primary purpose. Current sections: **Nodes**, **Libraries**, **CI/CD**, **UI**, **Tools**, **Smart Contracts**, **Documentation**, **Community / Ecosystem**, **Miscellaneous**, and **Archived or dormant** (see below).

## Self-verification checklist (run this before opening the PR)

An agent should confirm each of these itself — do not rely on the maintainer to catch them:

1. **No duplicate or existing PR.** Search first:
   - `gh pr list --repo ethersphere/awesome-swarm --state open --search "<name>"`
   - `gh issue list --repo ethersphere/awesome-swarm --search "<name>"`
   - and check the project is not already in `README.md`.
2. **Repository is public, not archived, and licensed:**
   - `gh api repos/<owner>/<repo> --jq '{private, archived, license: .license.spdx_id, pushed_at}'`
   - Skip it if `private` is true or `license` is null. If `archived` is true, it belongs in *Archived or dormant*, not a main section.
3. **The link resolves** (HTTP 200), and any homepage/docs links you add resolve too.
4. **The description is accurate and current**, under 160 characters, sentence case, one sentence.
5. **One item, one PR.**

## Maintenance & staleness policy — the "Archived or dormant" section

Projects that stop seeing activity are **moved to an `Archived or dormant` section rather than deleted**. This keeps still-useful code and ideas discoverable, and an entry can move back into the main sections if development resumes. The section is organised into:

- **Archived by their maintainers** — the repository itself is archived on GitHub.
- **No activity for 2+ years** — long-dormant but not archived.
- **Dormant (~1.5–2 years)** — quiet, worth watching.

If you are adding a project, it should go in a main section only if it is genuinely maintained. Be honest about this.

## How maintainers review and audit the list

For transparency — and so agents can self-assess against the same bar — this is the periodic audit the list is checked against:

- **Activity & archival:** each GitHub entry is checked via the API for `pushed_at` (last activity) and `archived`. Recent activity keeps it in a main section; archived or long-dormant entries are relocated to *Archived or dormant*.
- **Link liveness:** every URL (repositories, websites, PDFs) is checked for a live response; dead links are fixed or removed.
- **Description accuracy:** each description is checked against what the project actually is and does — including that the link and the description refer to the *same* repository.
- **Relevance:** the project must still be about Swarm and sit in the right section.

An addition that passes the self-verification checklist above will already satisfy this audit.

## Honesty rules for agents

- Only list projects that are **public, reachable, and real** — never a private repo, a placeholder, or a name you saw mentioned but cannot open.
- **Verify before you claim.** Confirm license, activity, and that the link resolves; do not assert these from memory.
- Do not inflate descriptions. If you are unsure what a project does, read its README rather than paraphrasing its name.
- One PR should add exactly one project you have actually inspected.
