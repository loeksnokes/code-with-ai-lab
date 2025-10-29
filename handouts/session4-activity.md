# Session 4 — Activities (Refactoring)

Total time: 25 minutes (hands-on refactor) + optional CI inspection.

---

## Activity — Safe refactor (25 minutes)
Goal: use AI to propose a small refactor, implement it safely, and add tests to preserve behavior.

Steps
1. Open exercise:
   ```
   cd exercises/04-refactoring
   ```
2. Run tests:
   ```
   python -m venv .venv && source .venv/bin/activate
   pip install -r ../../requirements.txt
   pytest -q
   ```
3. Inspect `string_utils.py`. Identify duplicated logic.
4. Prompt AI for a small refactor suggestion (paste only the duplicated functions).
   - Ask for a one-function extraction and edge-case tests.
5. Implement the helper function and replace duplicated code.
6. Add/modify tests under `test_string_utils.py` to ensure identical behavior.
7. Commit & push:
   ```
   git checkout -b feat/refactor-string-utils
   git add .
   git commit -m "Refactor: extract normalize_str helper; added tests"
   git push -u origin feat/refactor-string-utils
   ```
8. Open a PR with a clear description and AI assistance note.

Success criteria
- All tests pass locally after refactor.
- PR contains a short rationale and AI summary.

---

## Facilitator tips
- Encourage tiny commits so reversion is easy.
- Coaches should verify the tests exercise behavior meaningfully.
- If students cannot push, they should zip their branch directory and post it in Teams.
