# 🧠 Git Collaboration Exercise — Shared Dataset Challenge

## 🎯 Objective
This exercise aims to help you practice real-world Git collaboration workflows:
- Creating branches and commits
- Making pull requests
- Resolving merge conflicts
- Working collaboratively on a shared dataset and codebase

---

## 📘 Scenario

You are part of a **data science team** maintaining a shared dataset and preprocessing script.  
Your task is to:
1. Add your data to the shared CSV file.
2. Add one line of code to the Python script that processes the dataset.
3. Open a Pull Request (PR) to contribute your changes.

> ⚠️ Since everyone will edit the same files, **merge conflicts are expected**.  
> Resolving them correctly is part of the challenge!

---

## 📂 Repository structure

README.md
1-git.md
2-exo.md
3-frost_app_challenge_intro.md

crash-test/
dataset.csv
preprocess.py


## 🧩 Instructions

1. Add your github username to this google document so the teacher can add you as a collaborator to the repo:

https://docs.google.com/document/d/1LMmGRbgk8etWKchOmu3ba-pqWMZIMrRFS-GILj9D7vE/edit?usp=sharing

1. Clone the repository to your local machine:

Type the command into your terminal. If you're using windows, use Git Bash or WSL2.

```bash
git clone https://github.com/virgilus/git-crash-test.git
cd git-crash-test
```

1. Create a new branch which is named after you, so replace `<your-github-username>` with your actual GitHub username:

```bash
git checkout -b <your-github-username>
```

4. Edit the dataset

Add a new line to crash-test/dataset.csv with your own data.
Example:

```bash
echo "4,YourName,24,85" >> crash-test/dataset.csv
```

But you can also open the file in a text editor and add your line manually.

1. Edit the script

Open crash-test/preprocess.py and add one extra line of code (for example, a statistic or message).

Example:

```python
# Added by YourName
print("Average score:", df["score"].mean())
```

Commit your changes:

```bash
git add .
git commit -m "Adds my data and code"
```

Push your branch. The first time you do this, you may need to set the upstream branch. Follow what the terminal suggests which will be something like `git push --set-upstream origin <your-github-username>`.

Once you configured the upstream branch, you can just use `git push` to push directly on the branch.

```bash
git push
```

Go on the GitHub website and open a Pull Request from your branch to the main repository's main branch.

## ⚔️ Merge Conflicts

If your PR cannot be merged automatically, you will see a merge conflict message.

To fix it. Go back to your terminal and switch to the default branch named main:

```bash
git checkout main
```

Then pull the latest version of the main branch:

```bash
git pull
```

Switch back to your branch:

```bash
git checkout <your-github-username>
```
Merge the main branch into your branch:

```bash
git merge main
```

Open the folder in a IDE like VSCode to see the conflicted files. They will be marked with conflict markers (<<<<<<<, =======, >>>>>>>).
Edit the files to resolve the conflicts. Keep the changes you want and remove the conflict markers.

Commit your resolution:

```bash
git add .
git commit -m "Resolve merge conflict"
git push
```

Go back to the GitHub website and update your PR — it should now merge cleanly.

✅ Completion Criteria

Your contribution is considered successful if:

- Your name appears correctly in data/dataset.csv

- Your code line is added to scripts/preprocess.py

- You have resolved any merge conflicts successfully

- Your Pull Request is merged into the main repository

🧠 Tips

- Use git status often to track changes.

- Read conflict markers carefully when resolving conflicts.

- Communicate with your teammates if you’re unsure how to merge.

- Don’t worry if you break something — this repo is meant for experimentation!