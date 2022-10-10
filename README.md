----
# git-cheat-sheat

To push your content to gihub....your local ssh key need to be stored at github ( can be located in ssh_keys menu of github). This will avoid typing you the github password again and again.
(Hot to create a ssh-key, see [here](https://gist.github.com/surhudm/4b04da1682a15ded4c7a1a3da0514955))

----

**To create a new repository** 
```shell
git init   
```

**To delete a repository**
```shell
rm -rf .git        #or rm -rf full_path_of_repo
```

**To add files for tracking**
```shell
git add -A           #  for all files
git add sample.txt   #   to add specific files
```

***Git reset***
```shell
git reset    #for undo git add -A
```

*You need to make a commint in order to push something on the web*
```shell
git commit -m "first commit"
```

**Add github url of the repository wiht some name of your choice i.e. 'origin'**

```shell
git remote add origin git@github.com:ratewalamit/POWMES.git
```

**Pushing local changes on remote server**

Note:*Before pushing local changes to server you need to do git add and git commint* 

```shell
git push -u origin master     # will push master branch to the server
```

**Starting default branch as main**

```shell
git branch --move master main   #  will rename master to main
#or 
#git branch -M main 
```
# Version History

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


**Push an existing repository from the command line**
```shell
git remote add origin git@github.com:ratewalamit/POWMES.git
git branch -M main
git push -u origin main
```

A local .gitignore file is usually placed in the repository’s root directory. However, you can create multiple .gitignore files in different subdirectories in your repository. The patterns in the .gitignore files are matched relative to the directory where the file resides.

**To sync on gihub main branch**
```shell
git branch -m master main 
```

**Gitignore: Putting upper limit on files size **
```shell
find . -size +45M >.gitignore
```
If the pattern starts with a slash, it matches files and directories only in the repository root.
If the pattern doesn’t start with a slash, it matches files and directories in any directory or subdirectory.
If the pattern ends with a slash, it matches only directories. When a directory is ignored, all of its files and subdirectories are also ignored. for more: [click-here](https://linuxize.com/post/gitignore-ignoring-files-in-git/#:~:text=gitignore%20Patterns-,.,%5C%20\)%20to%20escape%20the%20character)


**Remove added files to git only not from local machine**
```shell
git rm -rf --cahced .
```

**Syncing changes**

Imagine you(A) and your friend (B) cloned master branch of some project.

1. Now you both made a branch from master of the main project. 
2. Your friend has done some changes in his branch and created a pull request and now his repo is merged with master branch of the main project.
3. Now you want to pull changes made by him also along wiht your changes

Steps:
```shell
    git checkout -b master 
    git fetch origin master   #on completion of this step, your local  master is upto date wiht the changes pushed by your friend B
    git checkout -b <your branch>  #now you are on your local repo which you had created from clonned version of old master and you     have made changes in you repo.
    git rebase master   #now your repo is upto date wiht the updted local repo(changes from master of B).
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
