# Session 4 — Advanced Workflows (Test-Driven Development, Test Generation & CI)

Duration: 60 minutes  
Purpose: reference for test-driven development (TDD) with AI, generating and validating tests, and using automation to maintain quality, and basic concepts of continuous integration (CI).

---

## Learning objectives
- Use the red, green, refactor cycle to drive code changes from tests.  
- Use AI to propose tests and evaluate them critically.  
- Learn to implement simple CI.

---

## TDD checklist (use before you change code)
1. Run the existing tests and note which fail (red):
   - `pytest -q`
2. Create a feature branch:
   - `git checkout -b feat/tdd-<short>`
3. Write or pick one failing test that describes the behavior you want.
4. Write the smallest change that makes it pass (green).
5. Refactor with the tests green; run tests after each change:
   - `pytest -q`
6. Make small, atomic commits (one logical change per commit).
7. Write a clear PR description describing intent and AI assistance.

---

## AI-assisted TDD pattern
- Step 1: Paste the failing test and the function, and ask AI for the minimal change only.  
- Step 2: Request rationale and possible edge cases the test does not cover.  
- Step 3: Implement the change yourself (do not accept a full automated rewrite blindly).  
- Step 4: Write each new test first and watch it fail before fixing the code.  
- Step 5: Run tests and add minimal documentation in PR.

Prompt example:
```
Here is a failing test and the function under test.
Suggest the smallest change that makes the test pass without breaking the others.
Also list edge cases I should write tests for next.
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
Generate 6 pytest tests for calculate_grade(score) covering grade boundaries and out-of-range scores.
```

---

## What are plugins?

A plugin is a distributable package that extends an AI agents functionality.

There are many different types of plugin for various tasks, such as:

- **Custom agents** — Specialized AI assistants.
- **Skills** — Discrete callable capabilities.
- **Hooks** — Event handlers that intercept agent behavior.
- **Model Context Protocol configurations** — Configurations that describe how an agent integrates with external tools.

---

## Why should I use plugins?

Plugins provide the following benefits:

- Reusability across projects.
- Team standardization of configurations.
- Share domain expertise (for example, by providing the skills of a Python expert, or a Docker expert).
- Encapsulate complex MCP server setups.

---

## How to install plugins

You can install plugins from:

- A marketplace
- A repository
- A local path

A marketplace is a location where developers can publish, discover, install, and manage plugins. It's a bit like an app store—but for plugins. Examples of marketplaces include:

- [copilot-plugins](https://github.com/github/copilot-plugins)
- [awesome-copilot](https://github.com/github/awesome-copilot)
- [claude-code-plugins](https://github.com/anthropics/claude-code)
- [claudeforge-marketplace](https://github.com/claudeforge/marketplace)

---

## When to avoid AI-driven large refactors
- Project has low or no tests.  
- Code touches security or cryptography.  
- Unclear licensing provenance of suggestions.  
- When code performance or concurrency guarantees are critical.

---

## Quick sample: TDD with calculate_grade
Red: `test_calculate_grade_below_0` and `test_calculate_grade_above_100` fail because no error is raised.  
Green: add the smallest check, e.g. raise `ValueError` when `score < 0 or score > 100`.  
Next: write a failing test for a boundary (e.g. 89.9 is a `B`), fix, then refactor with tests green.

---

## Resources & links
- pre-commit: https://pre-commit.com/  
- black, ruff, isort docs  
- GitHub Actions docs: https://docs.github.com/actions
