# Session 3 Quick Handout — Debugging, Collaboration & Responsible Use

Session goals
- Diagnose and fix bugs using tests + AI-assisted suggestions.
- Create and review PRs using a clear checklist.
- Apply basic license/IP checks and document AI usage.

Essential commands
- Create branch: git checkout -b fix/short-description
- Stage & commit: git add . && git commit -m "Fix: describe change"
- Push branch: git push -u origin <branch-name>
- Run tests: pytest -q
- Create PR: use GitHub web: New pull request → select branch → add description

Testing & debugging checklist
1. Reproduce the failing test locally (copy error & stack trace).  
2. Run `pytest -q` and note failing test name.  
3. Inspect minimal relevant code and tests.  
4. Ask AI for hypotheses including failing output & code snippet.  
5. Implement the smallest change, run tests, repeat.

PR & Code Review checklist
- Does code include tests and do they pass?  
- Are variable and function names clear?  
- Is there unnecessary code duplication?  
- Are there any large pasted blocks that require a license check?  
- Does the PR description state whether AI assisted and how?

IP & licensing quick rules
- Search for long matches (unique lines) on the web/GitHub.  
- If you find matching code, check license; permissive (MIT/Apache) often OK, copyleft (GPL) may impose obligations.  
- Record AI usage in the PR description and add an inline comment in code for significant AI contributions.

How to document AI use (recommended PR template snippet)
- AI assistance: [none / Copilot / ChatGPT / other]  
- What AI did: (e.g., suggested initial implementation of average(), suggested tests)  
- Human review: (brief summary of manual changes and tests added)

If you cannot open a PR
- Paste your branch name and the PR description into the Teams chat and a TA/instructor will create the PR for you.

Mini-Projects:
In `exercises/mini-projects` we have proposed some projects for the attendees to do. Choose which project you'd like to do and follow the instructions in the README.md.
Instructors will be available to help troubleshoot any issues.
 

Links & resources
- Lab exercises for this session: code-with-ai-lab/exercises/02-debugging and /03-license-check  
- Copilot docs: https://docs.github.com/en/copilot/getting-started-with-github-copilot  
- GitHub PRs: https://docs.github.com/en/pull-requests