# Session 2 — Getting Started with AI Coding Tools
One-page handout

Session: Getting Started with GitHub & Copilot (90 minutes)  
Goal: Help participants set up GitHub and GitHub Copilot, understand version-control basics, and generate their first AI-assisted code safely.

---

Quick agenda
- Recap: key takeaways from Session 1  
- Intro to GitHub & version control  
- Setting up your first repository  
- Installing & configuring GitHub Copilot  
- Hands-on project: your first AI-generated program  
- Privacy & licensing when working online  
- Q&A and troubleshooting time  

---

Learning objectives
- Create and push a repository to GitHub.
- Enable and configure GitHub Copilot inside VS Code.
- Use Copilot to scaffold and refine code.
- Explain how repo visibility and licensing affect data privacy and sharing. 

---

## Before we begin
Make sure you have:
- A GitHub account → [https://github.com/](https://github.com/)  
- VS Code installed and signed in with GitHub  
- Git installed (`git --version`)  
- (Optional) GitHub Copilot extension installed in VS Code  

---

## Hands-on lab (≈45 minutes)

1. **Create a new repo** on GitHub → name it `ai-coding-intro`.  
2. **Clone** it locally or open directly in VS Code via *Source Control → Clone Repository*.  
3. Create file hello.py and ask Copilot for a function to greet a name.  
4. Commit and push your work to the main branch. You can do this via the terminal with the following:
```
git add .
git commit -m "Add hello.py"
git push
```
Or this can be done using the VS Code IDE as follows - see image below:
1. Select the `+` for files you want to push.
2. add a commit message - this is a brief message explaining your change (If you want to do commit messages like a software engineer, take a look at this guide on semantic commit messages: https://www.conventionalcommits.org/en/v1.0.0/).
3. Click commit!
![alt text][def1]

[def1]: images/handout-vs-code-ide.png "Image of VS Code IDE"

### Making a new branch / pull request
You can make a new branch from the terminal with the command `git checkout -b <your_branch_name>`. 
Alternatively, using the IDE we can make a new branch by clicking the branch name:
![alt text][def2]

[def2]: images/vs-code-branch-option.png "Branch button"

Then, select `+ Create new branch...`

For making a PR, you can select the PR button on the IDE:
![alt text][def3]

[def3]: images/vs-code-pr-option.png "PR button"

OR go to the repository on github, go to the branch and make the PR from there. Good practice is to add a succinct title and a clear description. 