### GIT Interview questions?

### Question 1 You are in the middle of a merge and encounter a conflict. How would you resolve this conflict and complete the merge?

***Identify the Conflict** When you try to merge branches and encounter a conflict, Git will notify you which files have conflicts. The conflicted files will be marked, and you can see a list of them with:

`git status`

**Open and Inspect the Conflicted Files:**
Open the conflicted files in your text editor or IDE. Look for conflict markers. 

**Resolve the Conflict:**
Edit the file to resolve the conflict. Decide which changes to keep, or combine the changes as needed. After resolving the conflict, remove the conflict markers.

**Mark the Conflict as Resolved:**
After resolving conflicts in all files, you need to add them to the staging area to mark them as resolved:

`git add <conflicted-file>`

**Complete the Merge:**
Once all conflicts are resolved and added to the staging area, complete the merge by committing:

`git commit`

**Push the Changes:**
Push the resolved merge commit to the remote repository:

`git push origin <branch-name>`

### Question 2 A teammate accidentally pushed a commit that breaks the build. How would you revert the changes made by this commit ?

**Identify the Commit:**
First, identify the commit hash of the problematic commit. You can do this using the git log command:

`git log`

This will show you a list of commits with their hashes, messages, authors, and dates. Find the commit hash of the commit that needs to be reverted.

**Revert the Commit:**

Use the git revert command followed by the commit hash to create a new commit that undoes the changes from the specified commit. For example:

`git revert <commit-hash>`

Replace <commit-hash> with the actual hash of the commit you want to revert.

**Alternative: Reverting Multiple Commits**

If you need to revert multiple commits, you can specify a range of commits or use multiple git revert commands. For example:

**Revert a range of commits**
`git revert <oldest-commit-hash>..<newest-commit-hash>`

**Revert multiple individual commits**
`git revert abc1234 def5678 ghi9101`


**Question 3: Your team follows Git Flow. Describe how you would create a feature branch and then merge it back into the develop branch once completed.**

**Workflow to Create a Feature Branch:**

`git checkout develop`
`git fetch`
`git pull origin develop`
`git checkout -b feature/new-feature`

**Develop the Feature**
Work on your feature in the feature branch. Add, commit, and push your changes as necessary.

`git add .`
`git commit -m "Implement new feature"`
`git push origin feature/new-feature`

**Steps to Merge the Feature Branch Back into Develop**

Switch to the Develop Branch: Once the feature is complete, switch back to the develop branch:

`git checkout develop`

Pull the Latest Changes: Ensure your develop branch is up to date:

`git pull origin develop`

Merge the Feature Branch: Merge your feature branch into the develop branch:

`git merge --no-ff feature/<feature-name>`

The --no-ff flag ensures that a merge commit is created, preserving the history of the feature branch.

Resolve Any Conflicts: If there are any conflicts, resolve them, add the resolved files, and commit the merge:

`git add <resolved-file>`
`git commit`

Push the Changes: Push the updated develop branch to the remote repository:

`git push origin develop`

**Workflow to Merge a Feature Branch:**

`git checkout develop`
`git pull origin develop`
`git merge --no-ff feature/new-feature`
**If there are conflicts, resolve them, then:**
`git add <resolved-file>`
`git commit`
**Push the updated develop branch**
`git push origin develop`

**Cleanup**
After successfully merging the feature branch, you can delete the feature branch both locally and remotely:

**Delete the local feature branch**
`git branch -d feature/new-feature`
**Delete the remote feature branch**
`git push origin --delete feature/new-feature`


### Question 4 Explain when you would use git rebase instead of git merge and vice versa.

**When to Use git merge**
Scenario: Preserving Complete History

Merging Branches: When you want to combine the changes from one branch into another and keep the complete history of both branches. This includes all individual commits and the branch's timeline.
Feature Branch Integration: Merging a feature branch into the main branch (main or master) to keep track of all the work done on the feature.
Multiple Contributors: In a project with multiple contributors, merging ensures that the history of contributions is preserved.
Conflict Resolution in Context: If you want to see how conflicts are resolved in a merge commit, which can provide context for future debugging.

**When to Use git rebase**
Scenario: Linear and Clean History

Cleaning Up Commits: When you want to create a linear history without the noise of merge commits. This makes the project's history easier to follow.
Rewriting History: To replay commits from one branch onto another. This is useful for integrating changes from the main branch into a feature branch cleanly.
Single Developer: In a single-developer workflow or when working with a small team where everyone agrees on using rebase.
Feature Branch Synchronization: Regularly rebasing your feature branch onto the main branch to ensure it's up-to-date without merge commits cluttering the history.

You find yourself in a detached HEAD state. How would you get back to your branch and ensure no changes are lost

## Question 5: When you find yourself in a detached HEAD state in Git, it means that you are not currently on any branch but rather on a specific commit. To get back to your branch and ensure no changes are lost, you can follow these steps:

Step 1: Commit or Stash Your Changes
First, ensure that any changes you've made are not lost. You can either commit them directly or stash them if you don't want to commit yet.

Option 1: Commit Changes

If you want to keep the changes:

`git add .`
`git commit -m "WIP: Saving changes before switching branches"`

Option 2: Stash Changes

If you don't want to commit yet:

`git stash`

Step 2: Switch Back to Your Branch
Next, switch back to your original branch. You can check the list of branches and switch to the appropriate one.

`git checkout <branch-name>`

Replace <branch-name> with the name of your branch (e.g., main, develop, etc.).

Step 3: Apply Your Changes
Finally, if you stashed your changes, you'll need to apply the

`git stash pop`


## Question 6: You need to switch branches, but you have uncommitted changes that you want to save. How would you use `git stash` to handle this

You Have Uncommitted Changes:
You have made some changes in your working directory but haven't committed them yet.

Stash your changes:

`git stash push -m "WIP: Saving changes before switching branches"`

Switch to another branch:

`git checkout feature-branch`

Apply Your Stashed Changes:

`git stash pop`

Or, if you want to keep the stash for future use:

`git stash apply`

Additional git stash Commands

List stashes

`git stash list`

Apply a Specific Stash:

`git stash apply stash@{n}`

Replace n with the appropriate stash index from the list.

Drop a Stash:

`git stash drop stash@{n}`

Replace n with the appropriate stash index you want to drop.

Clear All Stashes:

`git stash clear`


## Question 7: How would you squash multiple commits into a single commit before merging to the main branch

Start an Interactive Rebase:
Begin an interactive rebase for the range of commits you want to squash. If you want to squash the last N commits, use:

`git rebase -i HEAD~N`

Replace N with the number of commits you want to squash.

Mark Commits for Squashing:
In the interactive rebase screen, you'll see a list of commits like this:

`pick <commit-hash> Commit message 1`
`pick <commit-hash> Commit message 2`
`pick <commit-hash> Commit message 3`

Change the word pick to squash (or s) for all commits you want to squash into the previous commit. Only the first commit should remain as pick.

`pick <commit-hash> Commit message 1`
`squash <commit-hash> Commit message 2`
`squash <commit-hash> Commit message 3`

Save and Exit the Editor:
After making your changes, save and close the editor. For example, in vim, you would press Esc, then type :wq and press Enter.

Edit Commit Message:
After saving, another editor screen will appear, allowing you to edit the commit message for the squashed commit. You can combine the commit messages or write a new one.

Complete the Rebase:
Save and close the editor to complete the rebase process.

