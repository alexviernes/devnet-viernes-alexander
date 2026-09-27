# Module 1 — Git & GitHub

**Student:** Viernes, Alexander, Jr. M.
**Date:** September 27, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a version control system  installed directly in the computer. It was created to track all changes made to your files or source code.
GitHub is a cloud-based website or platform where you upload and store projects that use Git.
---

## Key vocabulary (in your own words)

- repository: repository is a container where my project files stored
- commit:commit is the act of saving or recording the changes you have made to your code
- branch: A branch is like a separate version or line of your project where you can create and test new code without disrupting the code you are working on in the main branch.
- push / pull: Push sends my local changes to GitHub, while pull gets the latest changes from GitHub
- pull request: Request to add my changes from one branch to another branch or to my main branch
- merge conflict: Problem that happens when Git finds different changes in the same part of a file.

---

## Walking through what I did

I created a branch for my work. Then I made changes to my files and used
git add to prepare them. After that, I used git commit to save my changes.
Finally, I used git push to upload my branch and changes to GitHub.

```
git switch -c module-1-notes  
git add .  
git commit -m "Completed Module 1 notes"  
git push -u origin module-1-notes

```

---

## A mistake I made (or one I want to avoid)

The mistake I want to avoid is committing my changes to the wrong branch. I
also need to check my current branch before making a commit so my work goes to
the correct place.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
