# Exercise 01 — Intro: Function generation and testing (Python)

## Goal

- Use AI assistance to generate a function that formats a friendly greeting.
- Learn how to review, run, and test AI-generated code.

## Instructions

### Setup local environment

Create one Python virtual environment, named `.venv`, **in the repository root**
and install the dependencies using the following steps, unless you have done
this already. All later exercises and activities reuse this environment:

#### macOS and Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Windows (cmd)

```bash
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

Check your installation by running `pytest`

### Implement the code

1. Open `starter.py` in VS Code.
2. Use Copilot (or another AI tool) to suggest a function
   `greet(name: str) -> str` that returns `"Hello, <name>!"`.
3. Review the suggestion, accept or edit.
4. Run tests again and ensure they pass. If they fail, inspect errors and fix.

## Files

- starter.py: starter file with TODO
- test_greet.py: tests for the function
- requirements.txt — pytest
