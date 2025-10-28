# Session 4 — Advanced Workflows (Refactoring, Test Generation & CI)

Duration: 90 minutes  
Purpose: reference for safe refactoring with AI, generating and validating tests, and using automation to maintain quality.

---

## Learning objectives
- Perform small, test-backed refactors safely.  
- Use AI to propose tests and evaluate them critically.  
- Add simple CI and pre-commit checks to catch regressions early.

---

## Refactor checklist (use before you change code)
1. Ensure baseline tests exist and run:
   - `pytest -q`
2. Add extra tests for uncovered behavior (if coverage is low).
3. Create a feature branch:
   - `git checkout -b feat/refactor-<short>`
4. Make small, atomic changes (one logical change per commit).
5. Run tests & linters locally after each commit:
   - `pytest -q`
   - `ruff check .` or `flake8 .` (if configured)
   - `black --check .` (if configured)
6. Write a clear PR description describing refactor intent and AI assistance.

---

## AI-assisted refactoring pattern
- Step 1: Ask AI for a minimal refactor suggestion (paste duplicative functions only).  
- Step 2: Request rationale and possible edge cases impacted by refactor.  
- Step 3: Implement suggested extraction or consolidation manually (do not accept a full automated rewrite blindly).  
- Step 4: Add tests to verify behavior remains the same.  
- Step 5: Run tests and add minimal documentation in PR.

Prompt example:
```
Given these two functions, suggest a small refactor to remove duplication while preserving behavior.
Function A: ...
Function B: ...
Also list edge cases I should test.
```

---

## Test generation with AI — best practice
- Provide AI with:
  - Function signature and docstring.
  - Examples of expected return values.
- Ask for:
  - A small set (4–8) of pytest-style tests including edge cases.
- Review each generated test:
  - Is the assertion correct?
  - Does it exercise meaningful behavior?
  - Does it duplicate existing tests?
- Add selected tests incrementally to the repo and run them.

Example request:
```
Generate 6 pytest tests for is_prime(n) covering small primes, composites and edge cases.
```

---

## Automation & CI quick guide
- Add GitHub Actions to run tests on PRs (see `.github/workflows/python-tests.yml`).
- Use `pre-commit` hooks locally:
  - Configure `.pre-commit-config.yaml` with `black`, `ruff`, `isort`.
  - Install locally: `pip install pre-commit && pre-commit install`.
- CI tips:
  - Run `pytest -q` as the core check.
  - Add a job step for linters to fail fast.
  - Optionally add a license-scan or dependency-safety step.

---

## Practical commands
- Run tests: `pytest -q`
- Install pre-commit & run once: `pre-commit run --all-files`
- Create branch: `git checkout -b feat/refactor-strings`
- Commit & push: `git add . && git commit -m "Refactor: extract helper; add tests" && git push -u origin feat/refactor-strings`

---

## When to avoid AI-driven large refactors
- Project has low or no tests.  
- Code touches security or cryptography.  
- Unclear licensing provenance of suggestions.  
- When code performance or concurrency guarantees are critical.

---

## Quick sample: refactoring string_utils
Before: two functions with identical pre-checks (strip/empty).  
Refactor idea:
- Extract `normalize_str(s)` helper that returns `""` or stripped text.
- Use helper in both `shout` and `whisper`.
Add tests to ensure identical behavior post-change.

---

## Resources & links
- pre-commit: https://pre-commit.com/  
- black, ruff, isort docs  
- GitHub Actions docs: https://docs.github.com/actions
