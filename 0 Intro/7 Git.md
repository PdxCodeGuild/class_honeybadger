
# 7 Git

## 7.1 Version Control & Git

Version control is software that enables us to keep track of changes to files. This helps us retrieve older versions of code and undo mistakes. It also allows multiple developers to work on a project simultaneously. It can be used with any type of file, but is ordinarily used for source code. [Git](https://git-scm.com/) is one popular form of version control, others include [SVN](https://subversion.apache.org/) and [Mercurial](https://www.mercurial-scm.org/).

Git calls the directory it tracks changes in a **repository**. Git stores timestamped snapshots of the state of the repository called **commits**:

    commit 6aeba8f3f2c386e4dc97fd3e0b8fbfee8d751ac5
    Author: David Selassie <david@pdxcodeguild.com>
    Date:   Tue Mar 29 16:29:27 2016 -0700

Each commit has a globally unique **hash**, an author, a timestamp, a description of what changed, and a **parent** commit. Each commit stores the exact changes made to the files from the last commit. Commits build on top of each other to form a **history**, the full record of all snapshots of a project. The most recent commit is called the *HEAD*.

    Time --->
    C1 - C2 - C3 - C4
                    |
                    HEAD


## 7.2 Configuration and Status


### .gitignore

The `.gitignore` file is a special file at the top level of your repository that lists all files that should not be added to the history. These can include things like API keys, libraries, database passwords, user-specific configuration files, etc.

```
secrets.py
.idea
.DS_Store
```


### Set Your Username & Email

- `git config --global user.name "Your Name"`
- `git config --global user.email you@email.com`

### Set Connections to Remote Repositories

- `git remote add <remote_name> <repo_url>` adds a new remote repository with the given name
- `git remote rm <remote_name>` removes a remote repository
- `git remote set-url <remote_name> <repo_url>` updates the url of the remote repository with the given name


### Getting Information

- `git diff` shows the difference between files and the last commit
- `git diff --cached` shows the difference between staged files and the last commit
- `git status` shows the current branch, current commit, staged files, changed files, and untracked files
- `git log` shows a history of commits


## 7.1 Creating a Repository

There are two ways of creating a repository

- `git init` initializes the current folder as a repository. One must then add a remote repo in order to push.
- `git clone <repo_url>` creates a local repository in the current folder, which is automatically connected to the remote repository.


## 7.2 Staging and Committing

Git has a staging area for files to be added to before they're committed to the history.


- `git add <path>` adds a file or folder of files to staging
- `git add .` adds all updated files to staging
- `git commit` commits staged changes to the history and opens a text editor for a commit message
- `git commit -a` add and commit in one line
- `git commit -m "<commit_message>"` commit with the given message


- `git rm --cached <file>` `git reset <file>` removes a file from staging
- `git diff` shows the difference between files and the last commit
- `git diff --cached` shows the difference between staged files and the last commit
- `git status` shows the current branch, current commit, staged files, changed files, and untracked files
- `git log` shows a history of commits


### 7.3 Pushing and Pulling

- `git push`
- `git push <remote_name> <branch_name>`
- `git pull`
- `git pull <remote_name> <branch_name>`

### 7.X Branching and Merging

- `git checkout -b <branch_name>` create a branch
- `git branch -d <branch_name>` delete a branch
- `git branch` view branches, and which branch you're currently on
- `git checkout <branch_name>` switch to an existing branch




### 7.X Resources

- [git book](https://git-scm.com/book/en/v2)
- [git reference docs](https://git-scm.com/docs)
- [git tutorial](https://git-scm.com/docs/gittutorial/)
- [git cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [super simple git guide](https://rogerdudler.github.io/git-guide/)
