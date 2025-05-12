# Git and GitHub

## What is Git?
* Git is a **distributed version control system** that helps developers track changes in their code, collaborate with others, and manage different versions of a project. It allows users to:
  + Keep a history of changes.
  + Work on different features using branches.
  + Merge code changes efficiently.

## What is a Repository?
* A **repository (repo)** is a storage location for a project that contains all its files, history, and version control information.
* Repositories can be **local** (stored on your computer) or **remote** (hosted on platforms like GitHub etc.). 

## What is GitHub?
* GitHub is a **web-based platform** that provides hosting for Git repositories. It offers features like:
  + Remote repository storage.
  + Collaboration tools (pull requests, issues, discussions).

## Concept of add, commit, and push
* Git follows a three-step process for saving changes:
1. **Add**: Moves changes from the working directory to the staging area.
2. **Commit**: Saves the staged changes to the local repository with a message.
3. **Push**: Uploads committed changes to a remote repository.

### 1. add
#### Example:
```bash
git add filename.txt  # Adds a specific file
git add .             # Adds all changed files in the current directory
```

### 2. commit
#### Example:
```bash
git commit -m "Added a new feature"
```

### push
#### Example:
```bash
git push origin main  # Pushes changes to the 'main' branch of the remote repo
```

## Workflow Example:
```bash
git add .                       # Stage all changes
git commit -m "Updated feature" # Commit changes locally
git push origin main            # Push changes to remote repository
```

## Exercise
* Make your own temporary repository on GitHub. Write some code at local, and then `git add`, `git commit`, `git push` to upload your change.



---



# Using private repository

* When using private repository in GitHub, take following procedure

## GitHub Classic Token: Private Repository Access Guide
###  Step 1: Create a Classic Personal Access Token (PAT)
1. Log in to GitHub and visit:  
   👉 https://github.com/settings/tokens
2. Click **"Generate new token (Classic)"**

###  Step 2: Clone the repository using HTTPS

```bash
git clone https://github.com/your-username/private-repo.git
```

- **Username**: Your GitHub username  
- **Password**: Paste the generated Classic Token

###  Step 3: Save your token to avoid repeated prompts

```bash
git config --global credential.helper store
```
* Your token will be stored in plain text in `~/.git-credentials`.  
* Use only on trusted machines.

###  Step 4: Development loop (standard Git usage)

```bash
git add .
git commit -m "your commit message"
git push origin main
```
