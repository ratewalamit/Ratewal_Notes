# git-cheat-sheat

to push your content to gihub....your local ssh key need to be stored at github in ssh_keys menu. This will avoid typing you the github password again and again.

**#…or create a new repository on the command line**

echo "# POWMES" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:ratewalamit/POWMES.git
git push -u origin main



**#…or push an existing repository from the command line**
git remote add origin git@github.com:ratewalamit/POWMES.git
git branch -M main
git push -u origin main


# to sync on gihub main branch
git branch -m master main 


# to delete a repository
rm -rf .git
