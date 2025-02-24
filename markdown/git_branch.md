# Git
## Git Flow and GitHub Flow
* Git flow and GitHub flow are widely known branch rules: 
  + Gitflow: `main`, `develop`, `feature` and others branches
  + GitHub flow: `main` and `feature-x` (any name)
  + https://supersoftware.jp/tech/20221021/17928/
* Here we use GitHub flow as it is simpler.
* main: Branch for public release
* feature: Branch for feature development. Use descriptive branch names
* *feature* can be freely pushed, and when functionality is stable, create a pull request to *main*.
* It is sometimes useful to name *yourname/feature*, so that who is working on that branch --> we are going to use that rule.
* Pull requests from *feature* to *main* are done by administrators.

## Pull Request
* The process of merging code from one branch into another
* Usually requires review and approval from administrators before completion.

### Procedure
* Below is the process of creating a *feature* branch and making a pull request to *master*.
0. Clone the original repository
  * `git clone https://github... .`
1. Create a working branch (*feature*)
  * `git branch john/feature`
2. Edit files
  * `vi ...`
3. Add and commit edited files
  * `git add .`
  * `git commit -m "made some change"`
4. Push from *feature* to origin branch on Github
  * First time only: `git push --set-upstream origin feature`
  * Subsequent times: `git push`
5. Access the repository on Github (browser) and create a Pull request
  * Click the green "Compare & Pull request" button
  * Verify that "base" is the *merge destination* and "compare" is the *merge source*
  * If these tabs aren't visible, select "feature" from branch selection and click "Contribute", "Open pull request"
6. Click "Create pull request"
  * Add comments and other information
  * Review code differences
7. Merge the branch
  * Done by administrators
  * To approve pull request, click "Confirm merge"
  * To reject, click "Close pull request"
  * To undo an approved merge, click "revert"
  * If Github Actions checks are configured for pull requests, they run at this stage
    + If checks fail, the status becomes "failed"
    + Merging is still possible even if checks fail

* When *main* branch is updated, other branches like *feature* should also be updated
  + In browser, go to *feature* branch and click "This branch is X commits behind main" -> merge via pull request