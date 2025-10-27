Exercise 01 — Intro: Function generation and testing (Python)

Goal
- Use AI assistance to generate a function that formats a friendly greeting.
- Learn how to review, run, and test AI-generated code.

Instructions
1. Open `starter.py` in VS Code.
2. Use Copilot (or another AI tool) to suggest a function `greet(name: str) -> str` that returns `"Hello, <name>!"`.
3. Review the suggestion, accept or edit, then run `python -m pytest` to execute tests.

Files
- starter.py — starter file with TODO
- test_greet.py — tests for the function
- requirements.txt — pytest

Run locally
- Create a Python virtual environment: `python -m venv .venv && source .venv/bin/activate` (or Windows equivalent)
- Install deps: `pip install -r requirements.txt`
- Run tests: `pytest -q`
