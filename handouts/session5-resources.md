# Session 5 — Resources & Further Reading

This handout collects links and short notes to help you continue learning after the course.

---

## Tools & product docs
- GitHub Copilot: https://docs.github.com/en/copilot  
- Copilot Chat (if available in org): https://docs.github.com/en/copilot/copilot-chat  
- ChatGPT: https://chat.openai.com/ (use responsibly — avoid pasting secrets)  
- Codeium / TabNine / CodeWhisperer: vendor docs

---

## Testing & TDD
- pytest: https://docs.pytest.org/en/stable/  
- Test design checklist: assert meaningful behavior, cover edge cases, prefer small, deterministic tests.

---

## Linters & formatting
- black (code formatter): https://black.readthedocs.io/  
- ruff (fast linter): https://github.com/charliermarsh/ruff  
- isort (imports sorter): https://pycqa.github.io/isort/

---

## Pre-commit & automation
- pre-commit: https://pre-commit.com/  
- Example `.pre-commit-config.yaml` entries:
  - black, ruff, isort, end-of-file-fixer, check-ast

---

## Licensing & IP guidance
- Choose a License (overview): https://choosealicense.com/  
- SPDX license list: https://spdx.org/licenses/  
- Quick guide: permissive vs copyleft (MIT/Apache vs GPL/AGPL). When in doubt — escalate.

---

## Security & secrets
- Never paste credentials, private data, or proprietary info into public AI tools.  
- Use local/redacted prompts, or private enterprise models if available.

---

## Reading & policy
- Papers and policy summaries (selected):
  - Practical guide to using code generation tools safely (internal course reading list)  
  - “On the hazards of AI-generated code” — curated resources in repo `/resources`

---

## How to learn more (practical next steps)
1. Pick a small personal project. Add pytest coverage and pre-commit hooks.  
2. Try AI-assisted refactor in a branch, add tests before and after.  
3. Automate test runs in GitHub Actions and require PR checks.  
4. Document any AI usage and track lessons learned in project README.

---

If you'd like, I can:
- Convert any of these handouts into a single printable PDF / combined pack (one command to export with marp).  
- Produce a ready-to-run script that writes these files into `handouts/` in your local repo and commits them for you to push.

Which would you like next — script to write & commit these files, or the marp-cli commands to export PDFs locally?