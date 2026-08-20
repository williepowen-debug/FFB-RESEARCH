# FFB Research Session Process

Use this as the standard boot-up and closeout path on any machine before and after repo work.

## Boot-up process

Goal: start every work session from a known-good repo state, with GitHub `main` treated as the
source of truth.

### Human boot-up

From a shell:

```bash
cd /home/willi/FFB-RESEARCH
git switch main
git pull --ff-only
git status -sb
```

Expected clean state:

```text
## main...origin/main
```

If `git status -sb` shows modified files, stop and decide whether that local work should be
committed, stashed, or intentionally kept before pulling or switching branches.

### Agent boot-up

At the start of every Codex/LLM session in this repo, establish context in this order:

1. Confirm the working directory is `/home/willi/FFB-RESEARCH`.
2. Read `BOOTSTRAP.md`, `AGENTS.md`, `README.md`, and `SOURCE_POLICY.md`.
3. Confirm the branch and cleanliness with `git status -sb`.
4. If the user wants source-of-truth work, switch to `main` and run `git pull --ff-only`.
5. Create a feature branch before substantive edits unless the user explicitly wants direct `main`
   inspection only.
6. Identify the task domain and read the relevant guide:
   - whole-team buildout: `TEAM_BUILD.md`;
   - record creation or edits: `schemas/README.md` and the nearest template in `templates/`;
   - schedule work: `league/schedule/README.md`;
   - script/catalog work: `scripts/README.md`;
   - Chargers work: ARCHITECT scopes first, then BOLT uses `.claude/agents/bolt.md` and
     `teams/AFC/West/Los-Angeles-Chargers/AGENTS.md`.
7. Preserve unrelated local changes. Completed validated tasks use the standing Publish Closeout
   authorization unless the user opts out or limits publication.

Suggested user prompt:

```text
Work in /home/willi/FFB-RESEARCH as ARCHITECT, the repo orchestration/build agent.
Use GitHub main as the source of truth. Run the boot-up process from BOOTSTRAP.md:
switch to main, pull --ff-only, confirm status, then create a feature branch for this task.
Read AGENTS.md before editing. Route Chargers-specific research to BOLT only after repo state
and scope are clear. Use Standard Closeout when stopping. After successful validation, use the
standing Publish Closeout workflow unless I explicitly opt out or limit publication.
```

## Source-of-truth model

Treat GitHub `main` as the source of truth.

- Start new work from an up-to-date local `main`.
- Do substantive work on a short-lived feature branch.
- Merge completed work into `main` through GitHub.
- On every machine, return to `main` and pull before starting the next task.

Normal new-work flow:

```bash
git switch main
git pull --ff-only
git switch -c agent/<short-topic>
```

Use a branch name that describes the work, for example:

```bash
git switch -c agent/bengals-core-research
```

## Agent routing

- General repo work: use ARCHITECT, defined in `.claude/agents/architect.md`, and root `AGENTS.md`.
- Team buildout: use `TEAM_BUILD.md`.
- Chargers work: ARCHITECT scopes the task first; then use BOLT, defined in
  `.claude/agents/bolt.md`, and the Chargers-local guide at
  `teams/AFC/West/Los-Angeles-Chargers/AGENTS.md`.
- Schedule work: use `league/schedule/README.md` and validate with `scripts/validate_schedule.py`.
- Schema or catalog work: use `schemas/README.md` and `scripts/README.md`.

## Closeout model

Goal: end every work session with the repo in an explainable state. For completed validated tasks,
publishing to GitHub `main` is the default closeout under the repository's standing authorization.

Use two closeout tiers:

- **Standard Closeout** — always run before stopping. It reports status, validation, and next
  action, but does not publish.
- **Publish Closeout** — the default for completed validated work unless the user opts out. It
  commits, pushes, opens a PR, merges to `main`, deletes the merged task branch, and resyncs local
  `main`.

## Standard Closeout

Use Standard Closeout whenever a session ends, including when work is incomplete, needs review,
has failed validation, or is not approved for publication yet.

Before stopping work, ARCHITECT should:

1. Review the worktree with `git status -sb`.
2. Review the user-facing change set with `git diff --stat` and, when needed, `git diff`.
3. Regenerate generated files only when the work requires it. Never hand-edit `catalog.jsonl`.
4. Run the relevant validation gate.
5. Report any failures with the exact command and the unresolved cause.
6. State whether changes are uncommitted, committed locally, pushed, or merged.
7. State the branch name and whether it is ahead/behind its remote.
8. State the recommended next action.
9. State whether standing Publish Closeout applies or whether a pause condition prevents it.

### Standard Closeout report format

Use this compact handoff shape:

```text
Branch:
Repo state:
Changed:
Validation:
Not done / risks:
Recommended next action:
Publication / pause condition:
```

## Publish Closeout

Use Publish Closeout when work is complete and validated unless the user explicitly opts out or
limits publication for the task.

Publish Closeout is the source-of-truth path:

```text
feature branch -> push -> PR into main -> merge PR -> local main pulls merged GitHub main
```

### Publish prerequisites

Before publishing:

1. Confirm the current branch is a feature branch, not `main`.
2. Confirm the worktree contains only intended changes.
3. Run the relevant validation gate.
4. Confirm the commit message and PR scope are clear.
5. Confirm standing authorization applies and the user has not opted out or limited publication.

### Publish sequence

After approval:

```bash
git status -sb
git add <intended files>
git commit -m "<clear commit message>"
git push -u origin <feature-branch>
```

Then open a PR from `<feature-branch>` into `main`, verify checks/review expectations, and merge
the PR into `main` when approved.

Delete the remote feature branch as part of the successful merge, then delete the local feature
branch after switching away from it. Do not delete an unmerged branch under standing authorization.

After the PR is merged:

```bash
git switch main
git pull --ff-only
git status -sb
```

Expected final local state:

```text
## main...origin/main
```

If the merge happens outside the agent session, the next session should start with the normal
boot-up process so the local machine pulls the new source-of-truth state.

### Publish Closeout report format

Use this compact handoff shape:

```text
Published:
PR:
Merged to main:
Local main synced:
Validation:
Follow-up:
```

## Validation gates

Run the relevant checks before committing or handing off substantive repo changes:

```bash
python3 scripts/validate_schedule.py
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
python3 scripts/generate_catalog.py --check
git diff --check
```

Do not manually edit `catalog.jsonl`; regenerate it with `scripts/generate_catalog.py`.

For docs-only changes, the minimum closeout gate is:

```bash
python3 scripts/validate_repository.py
git diff --check
```

## Human closeout

Before ending a local work session:

```bash
git status -sb
git diff --stat
```

If work is complete and validated, either ask the agent to commit/push/PR or do it manually. If
work is intentionally unfinished, leave a note in the conversation or issue describing the branch,
what changed, and what should happen next.

## Interrupted or recovery closeout

If the session is interrupted, validation fails, or the repo is not in a publishable state:

1. Do not merge to `main`.
2. Leave changes on the feature branch.
3. Report the exact branch, changed files, validation failures, and next recommended command.
4. On the next session, boot up normally, inspect the branch, and continue or clean up deliberately.

## If a machine is out of date

Use this safe update path:

```bash
cd /home/willi/FFB-RESEARCH
git status -sb
git switch main
git pull --ff-only
```

If `git pull --ff-only` fails, the local branch has diverged or has local work. Stop and inspect
before merging, rebasing, or overwriting anything.
