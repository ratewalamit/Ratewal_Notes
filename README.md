# git-cheat-sheat

to push your content to gihub....your local ssh key need to be stored at github in ssh_keys menu. This will avoid typing you the github password again and again.



**#…or create a new repository on the command line**

git init
git add -A  (git reset for undo git add -A)
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:ratewalamit/POWMES.git
git push -u origin main



**#…or push an existing repository from the command line**
git remote add origin git@github.com:ratewalamit/POWMES.git
git branch -M main
git push -u origin main

A local .gitignore file is usually placed in the repository’s root directory. However, you can create multiple .gitignore files in different subdirectories in your repository. The patterns in the .gitignore files are matched relative to the directory where the file resides.

# to sync on gihub main branch
git branch -m master main 


# to delete a repository
rm -rf .git



or rm -rf full_path_of_repo

# putting upper limit on files size
find . -size +45M >.gitignore

If the pattern starts with a slash, it matches files and directories only in the repository root.
If the pattern doesn’t start with a slash, it matches files and directories in any directory or subdirectory.
If the pattern ends with a slash, it matches only directories. When a directory is ignored, all of its files and subdirectories are also ignored.
See link for more:
https://linuxize.com/post/gitignore-ignoring-files-in-git/#:~:text=gitignore%20Patterns-,.,%5C%20)%20to%20escape%20the%20character.

# remove added files to git only not from local machine
git rm -rf --cahced .

