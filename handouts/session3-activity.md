# Session 3 Activities — Detailed Instructions

Total time: 20 minutes (two parallel activities) — choose A or B or do both as time allows.

Activity Debugging (individual or pairs) — 20 minutes
Objective: Fix the intentional bug, add a test, and prepare a PR description.

Steps
1. Open/extract the lab repo and navigate to:
   `/exercises/02-debugging/`
2. Reproduce failing tests:
   - Create a venv, install deps, run `pytest -q`
3. Diagnose:
   - Read the failing test & stack trace.
   - Open `buggy_calc.py`.
4. Use an AI tool or manual inspection to propose a fix. If using AI:
   - Paste failing output + minimal function into the model prompt.
   - Ask for a minimal fix and a new test to cover the edge-case.
5. Implement fix and add at least one new test in the same folder.
6. Run `pytest -q` — all tests should pass.
7. Create a branch and commit:
   - git checkout -b fix/average-bug
   - git add .
   - git commit -m "Fix: use float division in average(); add test for floats"
   - git push -u origin fix/average-bug
8. Prepare a short PR description (paste into Teams if you cannot open PR):
   - What changed (1-2 lines)
   - Tests added
   - Whether AI assisted (and how)

Deliverable: branch pushed + PR description posted to Teams.

Success criteria
- Tests pass locally.
- Branch contains a clear commit history.
- PR description includes AI usage note.

Activity B — License & Code Review (small groups) — 20 minutes
Objective: Practice license detection and produce a short review comment.

Steps
1. Open `/exercises/03-license-check/`
2. Imagine an AI suggested a helper function (you will paste a provided example snippet into a temp file).
3. Search for matching code:
   - Use a web search (quote a unique string) and GitHub code search for matches.
4. If a match is found:
   - Identify license on matching source.
   - Decide whether the snippet's inclusion has implications (e.g., copyleft).
5. Write a short review comment (2–4 sentences) addressing:
   - Is the snippet OK to keep? If not, what action is needed?
   - If OK, what attribution or documentation is recommended?
6. Create a brief PR description documenting AI assistance.

Deliverable: one review comment (post in Teams chat) + PR description (post in Teams).

Success criteria
- Group demonstrates an ability to search & find matches.
- Comment correctly identifies license implications or recommends escalation.

Facilitator hints
- If students lack GitHub push access, they can still create a branch locally and paste a zip or PR description into Teams.
- Keep time tight: stop coding at the timebox and ask groups to paste their PR description into chat even if they didn't fully push.