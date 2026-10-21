# Exercise 04 — Test-Driven Development: `calculate_grade`

## Goal

- Use TDD (red, green, refactor) to finish `calculate_grade(score)` in `calculate_grade.py`.
- Tests are provided; write minimal code to satisfy them iteratively, then add your own tests first.

## Instructions

1. Run `pytest -q` to see the failing tests (scores below 0 and above 100 should raise `ValueError`).
2. Make each failing test pass with the smallest change, running the tests after each one.
3. Write new tests for boundary scores (e.g. 59.9, 60, 89.9, 90) and invalid input, and watch each fail before fixing the code.
4. Refactor with all tests green.
