----
# Learning Github: git-cheat-sheat  
To push your content to gihub....your local ssh key need to be stored at github ( can be located in ssh_keys menu of github). This will avoid typing you the github password again and again.
(Hot to create a ssh-key, see [here](https://gist.github.com/surhudm/4b04da1682a15ded4c7a1a3da0514955))

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
```
#make a branch with name my_branch(if it does not exist, if it exist it switches from curretn branch to my_branch branch )
----

**To delete a repository**
```shell
rm -rf .git        #or rm -rf full_path_of_repo
```

To delete a repo from local which is deleted from server

```shell
git remote prune origin
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
git reset <file>
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

**Add github url of the repository**

wiht some name of your choice i.e. 'origin'

```shell
git remote add origin git@github.com:ratewalamit/POWMES.git
```
----

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


git pull --force origin new_branch2:master

	 	 	 	
git pull --force origin new_branch2:master


**Remove/delete files created after last commit**
```
git clean -fd
#It will remove the files affected after last commit
```

**Remove/delete branch created along with its files(even if you have made any commit on new branch) **
```
git branch -d branchmname      #deletes branch without deleting files...files will move to parent branch if new branch deleted
git branch -D branchmname      #mind the capital D...it deletes the files
#It will remove the files affected after last commit
```


**Using tokens for github authentications**
First generate a token with some rights(atlest repo rights)
```
git remote remove origin
git remote add origin https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]
git push
```


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



Git merge
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








// delete branch locally
git branch -d localBranchName

// delete branch remotely
git push origin --delete remoteBranchName








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
