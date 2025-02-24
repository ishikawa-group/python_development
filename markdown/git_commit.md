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
