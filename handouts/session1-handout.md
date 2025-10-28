# Session 1 — Introduction to AI-Assisted Coding
One-page handout

Session: Introduction (60 minutes)  
Goal: Ground everyone in what AI-assisted coding is, the main tools, and the safe/responsible practices we will use.

Quick agenda
- Welcome & course overview  
- What AI-assisted coding is + examples  
- Tools & environments we will use  
- Responsible use and IP/licensing overview  
- Short hands-on warmup

Learning objectives
- Explain the role of AI assistants in coding workflows.
- Demonstrate how to run the starter exercise and test harness.
- Describe basic IP/licensing concerns for AI-generated code.

Before the session (if not done already)
- Install VS Code: https://code.visualstudio.com/  
- (Optional) Install GitHub Desktop: https://desktop.github.com/  
- Ensure you can open Microsoft Teams and your camera/mic work.

Warmup steps (in-class; 15 minutes)
1. Clone or download the lab repo:
   - `git clone https://github.com/loeksnokes/code-with-ai-lab.git`
   - OR download the ZIP from the repo page and extract.
2. Open `/exercises/01-intro-python` in VS Code.
3. Create and activate a virtual environment:
   - `python -m venv .venv` then:
     - macOS/Linux: `source .venv/bin/activate`
     - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
4. Install test deps:
   - `pip install -r requirements.txt`
5. Run the tests:
   - `pytest -q`
6. Use an AI assistant (Copilot, ChatGPT, etc.) to suggest an implementation for `greet(name)` in `starter.py`. Review, edit if necessary, and run tests again.

Responsible-use reminders
- Do not paste proprietary data into public AI tools.  
- Review any suggestion—run tests, check edge cases.  
- If using generated code, search for matches and check licenses for non-trivial code.

Resources & links
- Course materials: (code-with-ai-materials repo)  
- Lab exercises: (code-with-ai-lab repo)  
- GitHub Copilot docs: https://docs.github.com/en/copilot/getting-started-with-github-copilot  
- Quick GitHub start: https://docs.github.com/en/get-started/quickstart/hello-world

Need help?
- Course contacts: KE Hub (KEhub@newton.ac.uk), Collin Bleak (cb211@st-andrews.ac.uk), George Tyler (grlt20@bath.ac.uk)