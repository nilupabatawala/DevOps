### GIT Interview questions?

**Question 1** You are in the middle of a merge and encounter a conflict. How would you resolve this conflict and complete the merge?

**Steps to Resolve a Merge Conflict:**

* **Identify the Conflict** When you try to merge branches and encounter a conflict, Git will notify you which files have conflicts. The conflicted files will be marked, and you can see a list of them with:

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

**Question 2** A teammate accidentally pushed a commit that breaks the build. How would you revert the changes made by this commit ?

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

# Revert a range of commits
`git revert <oldest-commit-hash>..<newest-commit-hash>`

# Revert multiple individual commits
`git revert abc1234 def5678 ghi9101`


