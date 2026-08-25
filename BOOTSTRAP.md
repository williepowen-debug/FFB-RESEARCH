# FFB Research Session Process

Use this as the standard boot-up and closeout path on any machine before and after repo work.

## Boot-up process

Goal: start every work session from a known-good repo state, with GitHub `main` treated as the
source of truth.

### Human boot-up

From a shell:

```bash
cd /home/willi/FFB-RESEARCH
git rev-parse --show-toplevel
git status -sb
git branch --show-current
git worktree list
git fetch origin --prune
git switch main
git pull --ff-only
git status -sb
git rev-parse HEAD
git rev-parse origin/main
```

Inspect before switching or pulling. If the initial status shows modified or untracked files, an
interrupted merge/rebase, detached `HEAD`, or unfinished feature work, preserve it and decide how
to resume or hand it off. Do not automatically stash, commit, reset, or delete it.

Expected source-of-truth invariant after synchronization:

```text
repository root = /home/willi/FFB-RESEARCH
current branch = main
## main...origin/main
HEAD = origin/main
no interrupted Git operation
```

If fetching or pulling fails because GitHub is unavailable, report that source-of-truth sync is
unverified. Local inspection may continue, but do not claim a complete boot or start publication.
Treat discovery, synchronization, and branch creation as separate gates: each gate must succeed
before running the next. Do not place failure-sensitive boot commands in a sequence that continues
after a failed fetch, pull, or verification.

### Agent boot-up

At the start of every Codex/LLM session in this repo, establish context in phases.

#### Phase 1: discover state without changing it

1. Confirm the repository root with `git rev-parse --show-toplevel` rather than relying only on the
   shell path.
2. Read the local `AGENTS.md` and `BOOTSTRAP.md` for initial safety rules.
3. Inspect `git status -sb`, `git branch --show-current`, and `git worktree list` before switching,
   pulling, or creating a branch.
4. Pause and preserve state when there is unrelated work, an interrupted Git operation, detached
   `HEAD`, an unfinished feature branch, or another worktree occupying the intended branch.

#### Phase 2: synchronize source of truth

5. When the checkout is safe, run `git fetch origin --prune`, switch to `main`, and pull with
   `--ff-only`.
6. Confirm a clean `git status -sb` and prove `git rev-parse HEAD` equals
   `git rev-parse origin/main`. A network failure or divergence is a pause condition, not a reason
   to merge, rebase, reset, or claim synchronization.

#### Phase 3: load current instructions and scope the task

7. Re-read any operating document changed by the pull, then read `README.md`, `SOURCE_POLICY.md`,
   and the relevant guide:
   - whole-team buildout: `TEAM_BUILD.md`;
   - record creation or edits: `schemas/README.md` and the nearest template in `templates/`;
   - schedule work: `league/schedule/README.md`;
   - script/catalog work: `scripts/README.md`;
   - Chargers work: ARCHITECT scopes first, then BOLT uses `.claude/agents/bolt.md` and
     `teams/AFC/West/Los-Angeles-Chargers/AGENTS.md`.
8. Classify the task before branching:
   - read-only inspection remains on clean, synchronized `main`;
   - substantive edits use a short-lived feature branch;
   - unfinished in-scope work resumes only after its branch and ownership are verified;
   - monitoring work loads `INTELLIGENCE_PIPELINE.md` and freezes assignments before collection.
9. Before creating a feature branch, confirm its proposed name is absent locally and remotely:

   ```bash
   git branch --list agent/<short-topic>
   git branch -r --list origin/agent/<short-topic>
   git switch -c agent/<short-topic>
   ```

10. State the relevant validation gate before editing. Protected `main` does not require a full
    validation run at every boot; run a baseline check when repository health is in doubt, local
    tooling is relevant, or the task changes schemas, validators, scripts, or generated files.
11. Preserve unrelated local changes. Completed validated tasks use standing Publish Closeout
    authorization unless the user opts out or limits publication.

### Recovery boot mode

An intentional unfinished feature branch is not a normal source-of-truth boot and should not be
silently abandoned. When the previous closeout left recoverable work:

1. Confirm the current changes and branch belong to the task the user wants to resume.
2. Read the previous closeout handoff and inspect `git status -sb`, `git diff --stat`, the branch
   upstream, any associated PR, and `git worktree list`.
3. Fetch remote references with `git fetch origin --prune` without switching branches.
4. Compare the feature branch's base with current `origin/main`, but do not automatically merge,
   rebase, reset, stash, commit, or discard work.
5. Resume only when ownership, scope, and the next validation step are clear. Otherwise report the
   branch and preserve it for deliberate handoff or cleanup.

Recovery mode must state that the checkout is not on synchronized `main`; it may continue the
verified unfinished task, but it may not claim a clean source-of-truth boot.

### Agent boot report

Use this compact report after startup:

```text
Role:
Repository root:
Branch:
GitHub sync:
Worktree:
Interrupted operations:
Other worktrees:
Task mode:
Feature branch:
Guides loaded:
Validation gate:
Risks / pause condition:
```

Suggested user prompt:

```text
Work in /home/willi/FFB-RESEARCH as ARCHITECT, the repo orchestration/build agent.
Use GitHub main as the source of truth. Run the boot-up process from BOOTSTRAP.md:
inspect state before changing it, fetch --prune, switch to main, pull --ff-only, prove local main
matches origin/main, then create a collision-free feature branch only if the task requires edits.
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
git status -sb
git fetch origin --prune
git switch main
git pull --ff-only
git branch --list agent/<short-topic>
git branch -r --list origin/agent/<short-topic>
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
  commits, pushes, opens a PR, merges to `main`, removes the merged task branch locally and
  remotely, prunes stale tracking references, and proves local `main` matches GitHub `main`.

## Standard Closeout

Use Standard Closeout whenever a session ends, including when work is incomplete, needs review,
has failed validation, or is not approved for publication yet.

For a read-only session that leaves synchronized `main` unchanged, use Standard Closeout and mark
publication `not applicable (read-only; no changes)`.

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

After the publish prerequisites are satisfied:

```bash
git status -sb
git add <intended files>
git commit -m "<clear commit message>"
git push -u origin <feature-branch>
```

Then open a PR from `<feature-branch>` into `main`, verify required checks and repository rules,
and merge the PR under standing authorization unless the user opted out or a pause condition
applies.

### Post-merge hygiene

Publication is not complete when the PR merges. ARCHITECT must return the checkout to this
post-merge invariant:

```text
current branch = main
local main = origin/main
worktree = clean
task branch absent locally
task branch absent remotely
temporary task artifacts absent
```

After the PR is merged, treat each group below as a gate. Stop immediately if PR verification,
switching, pulling, or commit equality fails; do not continue into branch deletion.

```bash
gh pr view <pr-number> --json state,mergedAt,mergeCommit
git switch main
git pull --ff-only
git fetch origin --prune
git status -sb
git rev-parse HEAD
git rev-parse origin/main
git worktree list
```

Require `state: MERGED`, a non-null merge commit, a clean `main`, and identical `HEAD` and
`origin/main` commits. Then classify the local task branch before deleting it:

```bash
git merge-base --is-ancestor <feature-branch> main
```

- Exit `0`: the branch tip is an ancestor of `main`; delete it with
  `git branch -d <feature-branch>`.
- Nonzero exit: do not delete yet. This may be a squash merge; run
  `git cherry main <feature-branch>`.
- If every `git cherry` line is marked `-`, or it emits no unique commit, the patch is represented
  in `main` and `git branch -D <feature-branch>` is allowed.
- If any line is marked `+`, preserve the branch and report the unique commit as a pause condition.

After safe local deletion, verify cleanup:

```bash
git branch --list <feature-branch>
git branch -r --list origin/<feature-branch>
git worktree list
```

Expected status and branch results:

```text
## main...origin/main
<no local task-branch match>
<no remote task-branch match>
```

The two `rev-parse` commands must report the same commit. GitHub is configured to delete merged PR
branches automatically; `git fetch origin --prune` removes the corresponding local tracking
reference. If the remote task branch still exists, verify the PR is merged before deleting that
specific branch with `git push origin --delete <feature-branch>`.

Inspect temporary files or task-specific worktrees created during the task and remove only those
whose contents are confirmed disposable. Never broaden per-task closeout into deletion of other
agents' branches or worktrees.

If the merge happens outside the agent session, the next session should start with the normal
boot-up process so the local machine pulls the new source-of-truth state.

### Publish Closeout report format

Use this compact handoff shape:

```text
Published:
PR:
Merged commit:
Validation:
Local main synced:
Task branch deleted locally:
Task branch deleted remotely:
Remote references pruned:
Worktree clean:
Remaining branches / worktrees:
Follow-up:
```

## Periodic repository hygiene

Keep repository-wide cleanup separate from per-task Publish Closeout. A periodic audit may list
merged remote branches, local branches whose upstream is gone, open PRs, and attached worktrees.
Before deleting anything, reconcile each branch with GitHub PR state and `main`; use patch
equivalence for squash-merged branches. Deleting successfully merged branches is covered by
standing authorization. Abandoned, unmerged, ambiguous, or unrelated branches and worktrees
require explicit user direction.

## Validation gates

Run the relevant checks before committing or handing off substantive repo changes:

```bash
python3 scripts/validate_schedule.py
python3 scripts/validate_intelligence.py
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
what changed, and what should happen next. A human Publish Closeout follows the same PR
verification, synchronized-main check, branch classification, and post-merge invariant above; do
not delete a squash-merged branch merely because its upstream was deleted.

## Interrupted or recovery closeout

If the session is interrupted, validation fails, or the repo is not in a publishable state:

1. Do not merge to `main`.
2. Leave changes on the feature branch.
3. Report the exact branch, changed files, validation failures, and next recommended command.
4. On the next session, use Recovery boot mode to verify the branch and continue or clean up
   deliberately.

## If a machine is out of date

Use this safe update path:

```bash
cd /home/willi/FFB-RESEARCH
git rev-parse --show-toplevel
git status -sb
git branch --show-current
git worktree list
git fetch origin --prune
git switch main
git pull --ff-only
git status -sb
git rev-parse HEAD
git rev-parse origin/main
```

Each step is a gate. If inspection finds unfinished work, or if fetch, switch, pull, or commit
equality fails, stop and inspect before merging, rebasing, overwriting, or deleting anything.
