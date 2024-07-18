### GIT Interview questions?

**Question 1** You are in the middle of a merge and encounter a conflict. How would you resolve this conflict and complete the merge?

### Steps to Resolve a Merge Conflict:

* **Identify the Conflict** When you try to merge branches and encounter a conflict, Git will notify you which files have conflicts. The conflicted files will be marked, and you can see a list of them with:

`git status`

**Open and Inspect the Conflicted Files:**
Open the conflicted files in your text editor or IDE. Look for conflict markers. The conflict markers look like this:

`<<<<<<< HEAD
Your changes (from the current branch)
=======
Incoming changes (from the branch you are merging)
>>>>>>> branch-name`


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