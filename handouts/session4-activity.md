# Session 4 — Activities (Test-Driven Development)

Total time: 25 minutes (hands-on TDD) + optional CI inspection.

---

## Activity — Red, green, refactor with `calculate_grade` (25 minutes)
Goal: use tests to drive a fix, using AI as a helper while you stay in control of each red-green step.

Steps
1. Open exercise:
   ```
   cd exercises/04-tdd
   ```
2. Run tests and see them fail (red):
   ```
   source ../../.venv/bin/activate   # shared env from exercise 01 (Windows: ..\..\.venv\Scripts\activate.bat)
   pytest -q
   ```
   Two tests fail: `test_calculate_grade_below_0` and `test_calculate_grade_above_100`.
3. Read the failing tests and the docstring in `calculate_grade.py`. What behavior is the test asking for?
4. Make the first failing test pass (green) with the smallest possible change. If using AI:
   - Paste the failing test and `calculate_grade.py`.
   - Ask for the minimal change only, not a rewrite.
5. Run `pytest -q`, then repeat step 4 for the second failing test.
6. Write new tests first, one at a time, and watch each fail before fixing:
   - Boundary scores: 0, 59.9, 60, 70, 80, 89.9, 90, 100.
   - Invalid input types, e.g. `None` or `"90"`. Decide what behavior you want first.
7. Refactor with all tests green. Keep the tests unchanged while you tidy the code.
8. Commit & push:
   ```
   git switch -c feat/tdd-calculate-grade
   git add .
   git commit -m "Validate score range in calculate_grade; add boundary tests"
   git push -u origin feat/tdd-calculate-grade
   ```
9. Open a PR with a clear description and AI assistance note.

Success criteria
- All tests pass locally, including at least three new tests you wrote before fixing the code.
- Commit history shows tests added before or alongside the fix.
- PR contains a short rationale and AI summary.

---

## Facilitator tips
- Encourage tiny commits so reversion is easy.
- Coaches should verify the tests exercise behavior meaningfully.
- If students cannot push, they should zip their branch directory and post it in Teams.
