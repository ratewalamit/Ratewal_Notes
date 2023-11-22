----
# Learning Github: git-cheat-sheat  
To push your content to gihub....your local ssh key need to be stored at github ( can be located in ssh_keys menu of github). This will avoid typing you the github password again and again.
(Hot to create a ssh-key, see [here](https://gist.github.com/surhudm/4b04da1682a15ded4c7a1a3da0514955))

----

----
## A sample global gitconfig file ~/.gitconfig
```shell
[user]
    email = ratewalamit@gmail.com
    name = ratewalamit
[core]
    excludesFile = /mnt/home/student/camit/.gitignore
    askPass =
[push]
    default = matching
[init]
    defaultBranch = main
[credential "https://lsst-sqre-prod-git-lfs.s3-us-west-2.amazonaws.com"]
    helper = store
[credential "https://s3.lsst.codes"]
    helper = store
[filter "lfs"]
    clean = git-lfs clean -- %f
    smudge = git-lfs smudge -- %f
    process = git-lfs filter-process
    required = true
[diff]
    tool = vimdiff
[difftool]
    prompt = false
```
----
----


**To create a new repository** 
```shell
git init  
#git init amit       #will start repository wiht name amit

----
```
**git branches**
```
git branch branch_name #creating a branch
git checkout my_branch 
#make a branch with name my_branch(if it does not exist, if it exist it switches from curretn branch to my_branch branch )
```
----

**To delete a repository**
```shell
rm -rf .git        #or rm -rf full_path_of_repo
```


**Remove/delete a local/remote  branch**

```shell
#Remove/delete branch created along with its files(even if you have made any commit on new branch)
git branch -d branchmname      #deletes branch without deleting files...files will move to parent branch if new branch deleted
git branch -D branchmname      #mind the capital D...it deletes the files

#deleting a remote branch
git push -d <remote_name> <branchname>   #**Note:** In most cases, `<remote_name>` will be `origin`.


#To delete a repo from local which is deleted from server
git push origin -d deploy  #after deleing deploy from local, deleting from server also 

#To clean all the local tracking for deleted branches 
git remote prune origin

#To delete the ***local*** branch, use one of the following:
git branch -d <branch_name>    #- The `-d` option is an alias for `--delete`, which only deletes the branch if it has already been fully merged in its upstream branch.

git branch -D <branch_name>  #- The `-D` option is an alias for `--delete --force`, which deletes the branch "irrespective of its merged status." [Source: `man git-branch`]

#Note: You will receive an error if you try to delete the currently selected branch.
```

----
**To add files for tracking**
```shell
git add -A           #  for all files
git add sample.txt   #   to add specific files
```

*Use git **LFS** for tracking*
install first git LFS  #(download the package from website and install it)
```shell
git lfs track "*.pdf"    #will track all pdf files even within subdirectories
#git lfs track "myfolder/**"     to track specific folder and its content
#git lfs track "**/myfolder/**"     to track specific folder anywhere in the directory and its content
git lfs status # to see tracked file after setting up folder thracknig and git add after that.
git lfs ls-files
```

A local .gitignore file is usually placed in the repository’s root directory. However, you can create multiple .gitignore files in different subdirectories in your repository. The patterns in the .gitignore files are matched relative to the directory where the file resides.

----
**Remove file from tracking/untrack a file**

```
git restore --staged file.txt  (undo git add for this file)
git reset <file>
```
**Untrack**  *if the file is already tracked and more commits were made after that commit too*
```shell
git filter-repo --invert-paths --force --path test_table.fits 
git push --force
#python3 -m pip install --user git-filter-repo   #to install git-filter-repo
```

**Remove/delete files created after last commit**
```
git clean -fd   #don't ever use it
#It will remove the files(possible untarckted also) affected after last commit
```


**Git restore vs reset**
```shell
#restore is a newer feature compared to reset

#Discarding local changes
git restore file.js # Copies file.js from index to working directory
#it will undo changes in file.js made after git add to this file.

git restore --staged file.js # remove it from tracked files or Unstaging files (undoing git add)
#Now you cant undo your local changes, since git dont know any index of file.js with respect to which it could restore the file.


git restore . # Discards all local changes made after last git add (except untracked files)
Restoring an earlier version of a file
git restore ——source=HEAD~2 file.js
#
git reset file.txt 
#will simply wont affect your working copy, but will remove it from tracked file
```

**Git clean**
```
#affect only untracked files/folders
git clean -xnd    #x  will effecte executable files, n for files, d for directiries
#The above command will result to a warning,that whis operation will remove which files or directories
if you wish to remove those files
 
git clean -f -xnd    #--force
Now it will remove above mentioned fiels and directories 
```

**Git reset: Remove added files to git only from local machine**
```shell
git reset    #for undo git add -A
#remove already tacked file/folder but now in .gitignore
#git rm --cached <filename>
#git rm -rf --cached .  
#git rm -r --cached <foldername>
```
*You need to make a commit in order to push something on the web*
```shell
git commit -m "first commit"
```
----
**History of a file**
```
git log -p -- <filename>
#there is sapce after --
```

**Add github url of the repository**

wiht some name of your choice i.e. 'origin'

```shell
git remote add origin git@github.com:ratewalamit/POWMES.git
```
----

**Git diff**
```
git diff    #changes in working copy with respect to index(last git add)
git diff HEAD #changes with respect to last commit
git diff --staged # changes bw added and last commit....Assume you have made changes after last git add,now do git diff --cached, you will see nothing, but now do git add -A,  and again do git diff --cached, now you will see what you saw with git diff  
```

**Undoing commits**
```shell
#its better to use revert than reset
#reset is only for reverting local changes only, if the changes have been pushed use revert.
#reset rewrite the commit history, hence avoid it.

Reverting commits
git revert 72856ea  ——no-commit # Reverts the given commit, ——no-commit make sure this reverting is to avoid commiting changes made by this revert.
git revert HEAD~3..Head #or git revert HEAD~3.. # Reverts the last three commits  
#you can use commit names also instead of head
git revert commitA commitC #will revert commit A&C leaving B as it is.
#

git reset ——soft HEADA # Removes the last commit, keeps changed staged
git reset ——mixed HEADA  # Unstages the changes as well
git reset -~hard HEADA # Discards local changes
git reset commitP --hard #delete everything after commitP happened to working copy
```

**Recovering lost commits/See full history of HEAD**
```shell
git reflog # Shows the history of HEAD
git reflog show bugfix # Shows the history of bugfix pointer
```

**Amending the last commit**
```shell
git commit --amend   # modify last commit without creating a new commit
```

**Pushing local changes on remote server**

Note:  *Before pushing local changes to server you need to do git add and git commint* 

```shell
git push -u origin master     # will push master branch to the server
```

----

```shell
#git branch --move master main   #  will rename master to main
#or 
#git branch -M main 
```
specifically useful if you made dirty commits in head branch. Commit and checkout to a new branch, then delete the old branch (git branch -D old_branch_name), then rename the new branch to old one. All the commints made to deleted branch will be lost.

----

Starting a new repository with name main

* In **old** versions of git:
     ```shell
    git init
    git checkout -b main```

* In **new** git versions:
     ```shell
    git config --global init.defaultBranch main        #after this it will start new repo with main branch
    # for without adding git config global:
    #git init --initial-branch=main
    git init -b main```

----


**Push an existing repository from the command line**
```shell
git remote add origin git@github.com:ratewalamit/POWMES.git
git branch -M main
git push -u origin main
```
----


**To sync on gihub main branch**
```shell
git branch -m master main
```
----

**Gitignore: Putting upper limit on files size**
```shell
find . -size +45M >.gitignore
```

If the pattern starts with a slash, it matches files and directories only in the repository root.
If the pattern doesn’t start with a slash, it matches files and directories in any directory or subdirectory.
If the pattern ends with a slash, it matches only directories. When a directory is ignored, all of its files and subdirectories are also ignored. for more: [click-here](https://linuxize.com/post/gitignore-ignoring-files-in-git/#:~:text=gitignore%20Patterns-,.,%5C%20\)%20to%20escape%20the%20character)

----

**Push changes from local to remote**
```
git checkout master
git pull               # to update the state to the latest remote master state
git merge testing      # to bring changes to local master from your develop branch
git push origin master # push current HEAD to remote master branch
```
*To push your local branch to particular remtote branch*
```#git push <remote> <local branch name>:<remote branch to push into>``` 


**Deploy from a particular folder**

```shell
# Deploy from html folder to deploy branch...on local deploy branch has lot more data than remote branch which will contain only content of html folder
git subtree push  --prefix build/html origin deploy  
```


**Syncing changes: git rebase**

Imagine you(A) and your friend (B) cloned master branch of some project.

1. Now you both made a branch from master of the main project. 
2. Your friend has done some changes in his branch and created a pull request and now his repo is merged with master branch of the main project.
3. Now you want to pull changes made by him also along wiht your changes

Steps:
```shell
    git checkout -b master 
    git pull origin master   #on completion of this step, your local  master is upto date wiht the changes pushed by your friend B
    git checkout -b <your branch>  #now you are on your local repo which you had created from clonned version of old master and you     have made changes in you repo.
    git rebase master   #now your repo is upto date wiht the updted local repo(changes from master of B).
    #git push origin <feature_branch>   # in case you want to push changes to the origin/feature_branch you need to use --force
```


git merge my_branch (merge my_branch to the branch I am working on. When I branched all files from parent got copied to my_branch . Now after this merge command extra files in my_branch will also get added to present working branch.(upto last commit of datughter branch)


git rebase my_branch(will change commits to parent branch making us look daughter was never a branch))

git remote add origin git @github.com:amitkiucaa:ggjklfalgd.git create a remote of name “origin ” of url(git@.....git)


(Before pushing anything please add your public ssh key to your github account in order to be able to use push/pull)
git push -u origin master(if fast forwarding wont lose history) (def of origin in above line , you can push to other branch also)
git push --force origin master(forcefully merge will lose history)

git push server_repo repository_name (server_repo: is deifned as git remote add server_repo <url_of_repo> i.e. analogus to origin
(will push whatever is there in current working branch to url embadded in server_repo, with branch repository_name, if repository_name does not exist it will create it)
git push server_repo repository_name:


Note : if you cloned some repository :
and now you want to commit changes to the repository
first set your user identity ie
git config --global user.email ratewalamit@gmail.com
git config --global user.name  ratewalamit
(remove –global to set identity to this repository only)

otehrewise you wont be able to commit changes.



git push --mirror https://github.com/exampleuser/new-repository.git #will push exact mirror image of the repository to the repository defined by the link


	 	 	 	
Git Push

git push server_repo local_branch_name:server_branch_name

	server_repo : contain url of the repository
	if local_branch_name dont exist > will give error
if server_branch_name dont exist > will create server_branch_name branch at server
if both exist will paste local_bramch_name into serer_branch_name



Git Merge



**Syncing changes: git pull**
Let us assume you have file1.py file2.py file3.py along with folder1/file1.py folder2/file1.py
now you simply strat wiht adding origin to remote directory and let us see how fun stuff goes there

```
git push origin master   #will copy your local to origin
```
Now make a change in folder1/file1.py at local and push it. It will simply be pushed to remote.
*Now make changes in folder1/file1.py at **remote**, try to push it. It will give an **error**. To **resolve** it, firt pull remote to local by* 
```
git pull origin master
# git --set-upstream-to origin/master  #set this once to avoid writing origin master in pull statement repeatedly
```

Now if you have stopped tracking something on local, and delete it
git pull origin source_branch:desitanton_branch
use --force to forcefull copy
```
git pull --force origin new_branch2:master	 	 	 
git pull --force origin new_branch2:master
```


**Using tokens for github authentications**(Better is using ssh keys, see below)
First generate a token with some rights(atlest repo rights)
```
git remote remove origin
git remote add origin https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]
git push
```

**Using ssh-keys for github authentications**

Edit your local ~/.ssh/config
```
Host your_github_username
    Hostname github.com
    IdentityFile ~/.ssh/id_rsa.github
    #IdentitiesOnly yes # remove this line you you want to use id_rsa.pub for authentication, it bypasses the  and use the id_rsa.github instead of id_rsa 
```
Modify the remote origin
```
git remote remove origin
git remote add origin git@github.com:your_github_username/repository_name.git
git push
```


**Git merge**
first ceckout to the branch where you want to merge( ie Master)
now use:
git merge bracnh_name     (it will merge branchname to Master)
if there is any commin file in branch_name and master: it will be kept( If you merge updated copy of the file then it will simply replace updated copy with the orignal in master. But if in branchname there are come changes made,then you commited in branchname, now you have come to master made some changes and commited in master, now you want to merge , since in master the copy is updated one, hence it will raise some conflicts and ask u to address them.)
if there are files in master not in branch_name : keep those as it is
if there are files in branch_name not in master: would be copied to master
(Note if there was a file present in both repo esrlier and it has been deleted in brach_name, on mergng exp to master this file in the master will also be deleted.)


Now: if two branches ie master and exp are mergeed 
and you make changes to master
it will also be copied to exp
now checkout to exp
you will see new files from master in exp
but now make chaneges in exp after checking out ie add 1 file
now checkout back to master
now make changes in master again 
these new changes wont be there in exp agian since it was checked out earlier.








********************************************
Creating Snapshot

Initializing a repository

git init

Staging files

git add filel.js # Stages a single file

git add filel.jsfile2.js # Stages multiple files

git add *.js # Stages with a pattern

git add . # Stages the current directory and all its content

Viewing the status

git status # Full status
git status -s # Short status
Committing the staged files

git commit -m “Message” # Commits with a one-line message

git commit # Opens the default editor to type a long message

Skipping the staging area
git commit —am “Message”

Removing files
git rm filel js # Removes from working directory and staging area
git rm --cached filel.js # Removes from staging area only

Renaming or moving files
git mv filel.js file]. txt
Viewing the staged/unstaged changes


Viewing the history

git log # Full history
git log --oneline # Summary
git log —-reverse # Lists the commits from the oldest to the newest

Viewing a commit

git show 921a2ff # Shows the given commit

git show HEAD # Shows the last commit

git show HEAD~2 # Two steps before the last commit

git show HEAD:file.js # Shows the version of file.js stored in the last commit

Unstaging files (undoing git add)
git restore --staged file.js # Copies the last version of file.js from repo to index

Discarding local changes

git restore file.js # Copies file.js from index to working directory

git restore filel.js file2.js # Restores multiple files in working directory

git restore . # Discards all local changes (except untracked files)
git clean -fd # Removes all untracked files

Restoring an earlier version of a file
git restore ——source=HEAD~2 file.js
Browsing History

Viewing the history
git log --stat # Shows the list of modified files

git log --patch # Shows the actual changes (patches)

Filtering the history

git log -3 # Shows the last 3 entries
git log ——author="Mosh"

git log —before="2020-08-17"

git log ——after="one week ago”

git log ——grep="GUI" # Commits with “GUI" in their message
git log -5"GUI" # Commits with "GUI" in their patches
git log hash1..hash2
git log file.txt

Hi

Range of commits

4

¢ Commits that touched file. txt

Formatting the log output
git log ——pretty=format:"%an committed %H"

Creating an alias
git config ——global alias.lg “log ——oneline”

Viewing a commit
git show HEAD~2
git show HEAD~2:filel.txt  # Shows the version of file stored in this commit

Comparing commits
git diff HEAD~2 HEAD # Shows the changes between two commits

git diff HEAD~2 HEAD file.txt # Changes to file.txt only
Checking out a commit
git checkout dad47ed
git checkout master

Finding a bad commit
git bisect start

git bisect bad
git bisect good ca49180
git bisect reset

Finding contributors
git shortlog

Viewing the history of a file

git log file.txt
git log —-stat file.txt

git log --patch file.txt

Finding the author of lines
git blame file.txt

Tagging

git tag v1.0

git tag v1.0 5e7a828
git tag

git tag -d v1.0

#
i

¥

#

+

Checks out the given commit

Checks out the master branch

Marks the current commit as a bad commit
Marks the given commit as a good commit

Terminates the bisect session

Shows the commits that touched file.txt
Shows statistics (the number of changes) for file.txt

Shows the patches (changes) applied to file.txt

Shows the author of each line in file.txt

Tags the last commit as v1.0
Tags an earlier commit
Lists all the tags

Deletes the given tag
Branching & Merging

Managing branches

git branch bugfix # Creates a new branch called bugfix
git checkout bugfix # Switches to the bugfix branch

git switch bugfix # Same as the above

git switch -C bugfix # Creates and switches

git branch -d bugfix # Deletes the bugfix branch

Comparing branches

git log master..bugfix # Lists the commits in the bugfix branch not in master
git diff master..bugfix # Shows the summary of changes

Stashing

git stash push -m “New tax rules" # Createsa new stash

git stash list # Lists all the stashes

git stash show stash@{1} # Shows the given stash
git stash show 1 # shortcut forstash@{1}
+

git stash apply 1 + Applies the given stash to the working dir

git stash drop 1 # Deletes the given stash

git stash clear # Deletes all the stashes

Merging

git merge bugfix # Merges the bugfix branch into the current branch

git merge —no-ffbugfix # Createsa merge commit even if FF is possible
git merge ——squash bugfix # Performs a squash merge

git merge —abort # Aborts the merge
Viewing the merged branches

git branch --merged # Shows the merge

git branch ——no-merged # Shows the unmerged |

Rebasing

git rebase master # Changes the base of the
Cherry picking
git cherry-pick dad47ed # Applies tl en com
Collaboration

Cloning a repository
git clone url

Syncing with remotes

git fetch origin master # Fetches master from origin

git fetch origin # Fetches all objects from origin

git fetch # Shortcut for "git fetch origin

git pull # Fetch + merge

git push origin master # Pushes master to origin

git push # Shortcut for “git push origin master”

Sharing tags
git push origin v1.0 # Pushes tag vl.0to origir

git push origin —delete v1.0

Sharing branches

git branch -r # Shows remote tracking branches

git branch -vv # Shows local & remote tracking branches
git push -u origin bugfix # Pushes bugfix to origi

git push —d origin bugfix # Removes bugfix from origin

Managing remotes

git remote # Shows remote repos
git remote add upstream url # Adds a new remote called upstream
git remote rm upstream # Remotes upstream
Rewriting History





*************************************************


































































































**Add comment to git .md file**
```
#all written below will be commented out in .md generated file
<!--- 

README.md writing sytle [help](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links)

**This is bold text**	This is bold text

*This text is italicized*	This text is italicized

~~This was mistaken text~~	This was mistaken text

**This text is _extremely_ important**	This text is extremely important

***All this text is important***	All this text is important
 --->

```







<!--- 
# How to write in Readme.md

README.md writing sytle [help](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links)

**This is bold text**	This is bold text

*This text is italicized*	This text is italicized

~~This was mistaken text~~	This was mistaken text

**This text is _extremely_ important**	This text is extremely important

***All this text is important***	All this text is important
 --->
----
