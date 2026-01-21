# Session 4 — Git FAQ (Quick Reference)

This handout captures Git essentials for the class: key terms (origin, main, local branches), pull vs push, how and when to merge, what rebase does, how to protect local work during pull, and what “squash WIP commits” means. Assume rebase-on-pull is NOT configured by default; we show how to opt in.

---

## Key Git terms (fast refresher)
- origin: The default name Git gives the remote copy of your repository on GitHub.
- main: The default primary branch (older repos may use master). It’s the branch you typically base work off and into which you merge PRs.
- Local branch: A branch that exists only on your machine until you publish it. Use local branches to isolate work, keep main clean, and open focused PRs.

Local branches — common commands
```zsh
# Create and switch to a new branch off main
git switch -c feature/my-change

# List branches (local) and show current branch (* indicates current)
git branch

# Publish your local branch to origin and set upstream
git push -u origin feature/my-change

# Switch back to main when needed
git switch main
```

Why use branches?
- Keep unrelated work separate and reviewable.
- Reduce conflicts by avoiding direct edits on main.
- Enable small, focused PRs with clear history.

## Pull vs Push
- git pull
  - Fetches remote changes and integrates them into your current branch.
  - By default, pull performs a merge; you can opt-in to rebase for a cleaner, linear history (see below).
- git push
  - Publishes your local commits to the remote branch.
  - Will be rejected if the remote has new commits you don’t have yet (non-fast-forward). First pull (rebase) then push.

Typical flow
```zsh
# Update your local branch with the latest upstream
# Option A (default behavior): merge
git pull

# Option B (recommended): rebase just for this pull
git pull --rebase

# After committing locally, publish your commits
git push
```

---

## What does rebase do?
Rebase “replays” your branch’s unique commits on top of another base (often origin/main), creating a clean, linear history.
- Copies your commits one by one, producing new commit IDs with the same changes but a new parent chain.
- Pros: linear history, easier review and bisecting; keeps your work at the tip.
- Caution: rewrites history—avoid rebasing commits others already rely on; if you do, push with --force-with-lease.

Turn on rebase-by-default (optional)
```zsh
# Enable rebase on pull for just this repo
git config --local pull.rebase true

# Or enable rebase on pull everywhere on your machine
git config --global pull.rebase true
```

Conflict handling during rebase
```zsh
# If conflicts occur
# 1) Edit files to resolve conflicts
# 2) Stage fixes
git add <files>
# 3) Continue or abort
git rebase --continue
# or
git rebase --abort
```

---

## Do I need to commit before pull to “protect” my work?
Short answer: No. Rebase requires a clean working tree and won’t overwrite uncommitted work—it will refuse to run until you handle it. You have three options:

1) Commit your WIP
- Guarantees your work is saved and rebase can proceed.
- Creates noisy commits (you can squash later).

2) Stash your changes (recommended if not ready to commit)
```zsh
git stash -u   # include untracked files
git pull       # (merges by default) — or use: git pull --rebase
git stash pop
```

3) Enable auto-stash for rebase
```zsh
# Repo-only
git config --local rebase.autoStash true
# Or globally
git config --global rebase.autoStash true
```

---

## How to do a merge (and when)
Merging integrates histories by creating a merge commit when needed (unlike rebase, which rewrites commit parents).

Keep a feature branch current by merging main
```zsh
# On your feature branch
git fetch origin
git merge origin/main   # may create a merge commit if diverged
# Resolve conflicts if any
git add <files>
git commit              # completes the merge if Git didn’t auto-commit
```

Integrate a feature into main (local example)
```zsh
git switch main
git fetch origin
git merge --no-ff your-feature  # optional --no-ff to force a merge commit
git push
```

When to prefer which:
- Rebase: keeping your local history clean while syncing with upstream; polishing commits before sharing.
- Merge: integrating shared work without rewriting history; preserving the explicit merge point.

PR options on GitHub:
- Create a merge commit: preserves commit sequence and the merge point.
- Squash and merge: combines PR commits into a single commit on main.
- Rebase and merge: replays PR commits onto main with no merge commit.

---

## What does “squash local WIP commits” mean?
Combine several small “work-in-progress” commits into one or a few meaningful commits before sharing a branch or opening a PR.

Interactive rebase (local cleanup)
```zsh
git fetch origin
git rebase -i origin/main
# In the editor: leave the first commit as "pick"; mark later WIP commits as "squash" or "fixup"; then write a clean message.

git push --force-with-lease   # only if you already pushed those commits
```

Alternative: let GitHub squash at merge time
- Reviewers choose “Squash and merge” in the PR. Your local branch still has multiple commits, but main gets a single, clean commit.

---

## Fixing a non-fast-forward push error
This happens when origin has new commits you don’t have locally.
```zsh
# Option A (merge):
git pull

# Option B (recommended):
git pull --rebase
git push
```
If you rebased already-pushed commits, update the remote safely:
```zsh
git push --force-with-lease
```

---

## Helpful settings you can enable
```zsh
# Pull rebases by default (set per repo or globally)
git config --local pull.rebase true
# or
git config --global pull.rebase true

# Optional: auto-stash during rebase (protects uncommitted work)
git config --local rebase.autoStash true
# or
git config --global rebase.autoStash true

# Optional: prefer fast-forward merges when possible
git config --local merge.ff only
```