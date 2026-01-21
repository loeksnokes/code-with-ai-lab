# Session 2 — Getting Started with AI Coding Tools
One-page handout

Duration: 60 minutes  
Purpose: Help participants 
- set up GitHub and GitHub Copilot, 
- understand version-control basics, and 
- generate their first AI-assisted code safely.

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
- Set up VS Code with AI coding extensions
- Understand how AI coding assistants work
- Write your first code with AI assistance
- Explore AI suggestions and learn to evaluate them critically

---

## Before we begin
Make sure you have:
- A GitHub account → [https://github.com/](https://github.com/)  
- VS Code installed and signed in with GitHub  
- Git installed (`git --version`)  
- (Optional) GitHub Copilot extension installed in VS Code  

---

## Hands-on lab

1. **Create a new repo** on GitHub → name it `ai-coding-intro`.  
2. **Clone** it locally or open directly in VS Code via *Source Control → Clone Repository*.  
3. Create file and ask Copilot for a function to generate the fibonacci numbers.  
4. Commit and push your work to the main branch. You can do this via the terminal with the following:
```
git add .
git commit -m "Add [file_name].py"
git push
```
Or this can be done using the VS Code IDE as follows - see image below:
1. Select the `+` for files you want to push.
2. add a commit message - this is a brief message explaining your change (If you want to do commit messages like a software engineer, take a look at this guide on semantic commit messages: https://www.conventionalcommits.org/en/v1.0.0/).
3. Click commit!
![alt text][def1]

[def1]: images/handout-vs-code-ide.png "Image of VS Code IDE"

See also
- Git FAQ (pull vs push, rebase, merge, WIP squashing): [Session 4 — Git FAQ](./session4-git-faq.md)