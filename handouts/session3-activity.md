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

Activity B — Refactoring & Code Review (small groups) — 20 minutes
Objective: Use AI to remove duplication safely, review its suggestion critically, and produce a short review comment.

Steps
1. Open/extract the lab repo and navigate to:
   `/exercises/03-refactoring/`
2. Run the existing tests first to confirm they pass:
   - Create a venv, install deps, run `pytest -q`
3. Inspect `string_utils.py`:
   - Identify the duplicated logic in `shout()` and `whisper()`.
4. Ask an AI tool for a refactoring suggestion. If using AI:
   - Paste `string_utils.py` and ask it to remove duplication without changing behaviour.
   - Ask it to explain each change.
5. Review the suggestion critically before applying it:
   - Does it still handle `None`, empty strings and whitespace-only strings?
   - Is the result clearer, or just shorter?
6. Apply the refactor and run `pytest -q` — all tests should still pass.
7. Add at least one test for an edge case the existing tests do not cover (e.g. surrounding whitespace on `whisper`, mixed-case input).
8. Write a short review comment (2–4 sentences) as if reviewing a teammate's refactor:
   - Is behaviour preserved? What evidence (tests) supports that?
   - Any remaining concerns or suggested follow-ups?
9. Create a brief PR description documenting AI assistance.

Deliverable: one review comment (post in Teams chat) + PR description (post in Teams).

Success criteria
- Duplication is removed and all tests pass.
- Group can explain what the AI changed and why behaviour is preserved.
- Review comment cites test evidence or identifies a concern.

Facilitator hints
- If students lack GitHub push access, they can still create a branch locally and paste a zip or PR description into Teams.
- Keep time tight: stop coding at the timebox and ask groups to paste their PR description into chat even if they didn't fully push.