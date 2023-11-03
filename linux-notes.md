
**Shell script are executed directly interpreted not compiled**

shell : A prtogram which takes command form keyboard and give it to os

Cli command line interface

terminal  : tool to send command to shell


### To see which shell scripts supported by our os

```bash
cat  etc/shell 
which bash       #tells where bash is located
#!/ bin/bash      #tells imterparator which bash to be used 
```


### what/which/version

```
what is ls      #give short info of command
which ls    gives path of ls

### version
packagename -version
```

### chmod : To give make executable permission

```chmod +x hello.sh
chmod ugo+rwx filename     #give  permission  to user group othres for  read write execute
#other equivalents (chmod a+rwx filename ) chmod a=rwx filename, chmod u=rwx,g=rwx,o=rwx filename
chmod u-x   filename     take permission execution from user

# Access rights of user, groups
drwxr-xr-x      rights of the users are separated by -   d direcotry  r read w write x:execute r read
```


      
 
### ls command (same for cd command)
```
ls /   list files in root directory
ls or ls ~   lists files in home directory
ls ../..  lists two foders back
ls .      Lists in pwd
ls -l     	lists in long format
ls -ltuh | head -15     list  latest 15 files
ls -a    list all files hidden also
ls -al in long format
ls -S   sort on basis of size  remember S
ls -t     sort on basis of time
ls -lS > out.txt   lists output of -lS command to out.txt
ls -d */    lists all directories only
man ls    referance of ls
```

### wc

```
wc filename     will give in file
wc -l/w/c filename
```


### cat
```
cat file1.txt file2.txt    
cat -b file1.txt       : add numbers in front of non blank lines
cat -n file1.txt      : add numbers to all lines
cat -s file1.tst   :display content squeezed means many blank lines in one line
cat -E file.txt         add $ in last of each line
cat > amit.txt   : write whatever you write after this command uptil you pust ctrl+D
      >>  for append mode in cat
cat file1.txt file2.txt > amit.txt
```


### searching a file:

```locate -i amit.txt    -i   #case insensitive```

### Create/Delete directories

```mkdir amit
mkdir -p amit/as   make amit and as, if amit even does not exist( equevalent to mkdir --parents amit/as)
mkdir -p amit/{subu,am,sub,d}    will create multiple daughter directories  Warning : no space bw subu,am,sub,d   
rmdir -p a/b/c/d   will remove a b c d if all are empty
rmdir -pv  a/b/c/d   will remove a b c d if all are empty, show extedned ifno ie what is happending in background
rm -r a/b/c    will removea, b,c with files or rm -r a will also do the same jobs
```

### Copy
```
#cp source dest
cp amti.txt am.txt
cp amit.txt ~/Desktop/am.txt     copy amit.txt to destination with name am.txt
cp amit.txt ~/Desktop/              copy amit.txt to destination with same name
cp -i   amit.txt am.txt                  will ask user before copyting if am.txt exist already
cp amit.txt am.txt                       will overwirte 
cp sourece   .                         will copy source file to pwd
cp  -R dir1 di3      copy directory1 content to   directory3   if directory3 doesnt exits
cp -R dir1 dir3       copy directory1 inside directory3 if directory 3 alredy exist
cp  -R ~/Desktop/111/.  222  copy content of 111 in 222(    . at end of 111 includes hidden files also)
```
### Server copy
To avoid password authentication in it, add id_pub of local to the ./ssh/authorized_keys on remote system
```
#scp source dest
scp amti.txt username@ipaddress:/home/username/
#in python
!scp source_file {os.environ["os_variable_name"]}/
```




### Rsync
```shell
#rysnc  -r  source/ dest      sync source and dest(if destination doesnot exist it will create it first)

#rsync -rv  --include  "*.py" --exclude "*"  --delete  /home/amit/Desktop/Covid_backup/github/weaklens_pipelin/   cami@pegasus.ac.iucaa.in:/mnt/home/student/camit/github/weaklens_peline/
#Note: above command will also delete files which you delted from source

rsync -r                              #will copy directiores and their content   
rysnc -a                             #will do same as -r but will also copy symlinks and preserve group user perimssions
rsync -a  --dry-run             # to see what will be copide
rysnc -a  --delete –dry-run    #to dry run to find it will  mirror source and dest but
rsync -t                       #keep time stapmp
rsync  -zaP                   #z for archive P for progress
rsync       soucrce      server_destination
rsync -u   #update
#server_destination:      username@ipadress:location (please mind ipadress is separated to location with : eg camit@pegasus.ac.in:/mnt/home/student/camit/
rysnc -azvP --dru-run   camit@pegasus.ac.in:/mnt/home/student/camit/
rsync -azvP  --include={"*.py","*.dat"}  --exclude "*" /home/amit/Desktop/test_local/ Desktop/tt  #will include only pythonand dat files excluding all
rsync -azvP   --include={"*/","*.py","*.dat","*.txt"} --exclude="*"   /home/amit/Desktop/test_local/ Desktop/tt/ #noticd diff with above command    it will copy py dat and txt file 	from all source subdirectoreis notice that how exclude is used 
rsync -azvP  --exclude={"*.py","*.dat"}  /home/amit/Desktop/test_local/ Desktop/tt #will include only pythonand dat files excluding all
#or
rsync -azvP  --include={"*"} --exclude={"*.py","*.dat"}    /home/amit/Desktop/test_local/ Desktop/tt/             #will exclude only py ad dat files from all directories and subdirectories 

#both commands above are equavalent
```

### less 

```
#less  used to see contern of a file same as cat but cat is not that handy(press q to quit)
less -N amt.txt    show amit wiht numbers
sudo : super user do
sudo -s : go to root user
ie sudo mkdir amit
```

### top
```shell
top : show memory usage of compputer
i    show/hide idle process
s   change refresh interval in seconds
k to kill any process
pidof processname   ie pidof unity-control-center    return a number
```
### kill

```kill number or kill -KILL number   forces the process to closed. Not recommended
kill -9 number      less stronger than KILL
ps -ux   long list of all running processes
ps -aux   process of all users
ps -u username  user specific processes
ps -C processname   process specifications
```
### echo

```
#echo    used in bash scripting mainly, dfine variables in terminal
#eg
var=”amit”       mind there is no space
echo  “valure of variablie is  =  $var”       will print amit
echo $var1
echo -e “ anit\tsib ” will print amiit	sib        -e enable escape sequence of \ ...it interperates \n as new line 
echo “`expr 32 \* $i`”
echo -e “connect 00:16:94:3A:21:F4” | bluetoothctl       will give connect  00:16:94:3A:21:F4 input to bluetoothctl command
```

### sh

```
#script is a text file which contain sequence of commands to be executed  by terminal
#you can declare variables in script and use them with $ symbol
#Note:  a scipt file need to have a execute permission for exucution. by default the script you create don’t have this execute permission
qsub  qsub.sh -v start=`expr 32 \* $i`
#see running_multiple_jobs_at_time.sh for passing variables to qsub and executing expressions
```

### useradd/passwd/userdel  
sudo useradd name_of_user -m -s /bin/usr/bash/ -g users -c “my comments”
passwd name_of_user password         #changes password for user
sudo userdel name_of_user         #deltes user but not files associated with that user
#(to remove files from deleted user user simple sudo rm -r path command)\


### groups
```
groups  #print all groups associated with curent user
cat /etc/groups    # all groups on system
sudo goupadd group_name
sudo groudel group_name
sudo gppasswd -a/-d  username groupname    #: to add or remove password to group
```


### bashrc

```
#bashrc is a script that gets executed whenever a new terminal session is added in interactiove mode ie  
alias aaaa=’clear’   will make aaaa to clear command
alis ls=”ls -l” change ls to ls -l
```

### du/df

```
df -h   #free space on disk 
du        #disk space used by files or folder  pwd
du -sh    #summary of pwd                            or    du -s -h 
du -sg    #g means giga    m mega  k kilobyte
du -sh   file/foldername
```


 
### watch

```
watch command   ies watch ls    (executes command at regular interval)
watch -n 5 ls                     refresh at the rate of 5 sec   (press ctrl+c to quit)
```

### head/tail

```
head <filename>     print first10 lines of file
tail  <filename>     print last 10linse
head -n 4 filename   or head -4 filename  will pirnt 4 lines of file
tail -f filename             will hangor follow ie it will keep in checking for the file changes
head file1name file2name     10 lines for both files
```




### find/locate

```
#find is used for finding file in diretory hiererhy, it can even find files newer than a mentioned file
find seachdirectory -name  'filename/directoryname'
find searchdirectory -name '*.txt'
find searchdirectory -mtime -5    seach files which were created within last 5 days

locate -b  *creat*fits*.py      # -b for case insensitive
```


### grep: to find text

```
grep -Ril "text-to-find-here" /
grep   #global representative enviorenmetn print    case sensitive
grep   -i  “paterntosearchfor”   filename #make case insensitive      
grep “hello” hello.txt    #will print lines containing hello 
grep -in “patterntosearch” filename       # will print line number aslo
grep -in “patterntosearch” filename1 filename2   # searching multiple files
grep -v “pattern” filename    #   will print all lines not containg pattern 
```


### date/cal

```
cal
cal 2019
cal 3 2014   3rd month of 2014
cal -2 2014   first 2 months of 2014
#

date    print det
date -s  “11/20/2020    17:00:00”          to set system date   in quotes as string
date “+%d%h-%y”    print  20Jan-20
```



###  run multiple commands

```
ls ; pwd                    #all commands separated by comman will be executed
ls  && pwd               #first or second commnd will be executed depending on result of firrst command 
 Ls && pwd       #no command will be executed 
ls && Pwd        #only ls will be executed
ls || pwd        # only ls will be executed
Ls||pwd          #pdw will be executed

#
command1 | command2     output of command1 will be used by command2
ls | grep “hleello”    # will print files having name hello  in their name from all files listed 
```


### apt-get

```
sudo apt-get install packagename     
sudo apt-get remove packagenem      will remove package not the libaraires installed dureing 					package installation
sudo apt -get –parse packagename     will remove package and associated libraries
```


### ifconfig/netstat

```
ifconfig #interface connection configration
ifconfig     #: give info of connections
inconfig eth0 up/down     enable/disable eth0

netstat -a 
netstat -a | less
```



### tar

```
tap archive  # just like zip
tar -cvf  #    c  creating archive     v verbose   f filename
#ie to make zip of  test folder    
tar -cvf  test.tar   test            # f need to be used to givefilename
tar -x                       #x   extarcting    
tar -xf test.tar
#tar.gz  #gz   means gzip      wil craeate zip in   tar.gz file

#tar -czf           
tar -czf test.tar.gz   test      #       ;remember z need ot come after c

#simailaly  tar -xzf test.tar.gz     
```   





### ssh

```
#ssh      secure shell
ssh user@ipadress -p portnumber
ssh localhost        #check open ssh sever is installed(this need to be installed  for accessing for other os to acces this system via terminal

sudo apt-get openssh -sever      # to install open sshserver
#now if open server is installled

ssh localhost 
#it will login you to  your own system via terminal
ssh filename ipadress  # ie ssh test.txt 192.168.0.15:/home/amit/Desktop/test.txt
#ssh ipadress        to login ipadress
ssh -x ipadress     #allow to use graphix applications
#connecting server iucaa usage
#https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
#you need to add someone's public key to your authorised keys ot allow him to use your adresss.
```



### ln

```
#Craeting Links in Linux
ln -sf  filename linkname         ## -s soft link, f-force in absence of  -s, it will crate a hard copy of teh file but bot files #will be linked. Its like twoo mirror copies of teh file. You cant create hard copy of a file on different disk.
#In absence of linkname it will use the filename as the link name.
```


### pip

```
#Install package to specific version of python
sudo python2.7 -m pip install pandas

#install package with pip to a particular location
pip install package_name -t   /home/amit/Desktop/

#To install pipeline to a particular location
sudo python setup.py install --install-scripts /home/amit/python_packages_for_weaklens_pipeline/    

pip install boost  -t /mnt/home/student/camit/.local/lib/python3.7/site-packages/
```



## installl softwaere with CPP and LDFlags


### gsl

```
#Install gsl:
see how_how_to_installl  file on my (surhud’s modified wp by amit) repository weaklens
How to install boost:

#
load anaconda3 gcc-8.2.0 mpich-3.3.1 latex fftw-2.1.5 gsl-2.6
LDFLAGS="`gsl-config --libs` -L/mnt/home/faculty/csurhud/libraries/lib/" CPPFLAGS="`gsl-config --cflags` -I/mnt/home/faculty/csurhud/libraries/include" python setup.py install --prefix=install
```

**pegasus hang**

```
export DISPLAY=:1
gnome-shell --replace
```

**Remote Jupyter Notebook**
```
ssh -L 8080:localhost:8080 camit@192.168.11.251
```
Run this command to forward local host to ip address.

Run a jupter noteobook on this server.
```
jupyter-notebook --no-browser --port=8080
```
In your local browser:
```
localhost:8080/
```

**Tmux**
```shell
tmux new #to create new window
tmux list-sessions #list all background tmux sessions
tmux atach -t [0-9]   #attach particular session running in background
tmux detach #or ctrl+b d
```

**Hotspot**
```shell
#create wifi hotspot for better sequrity #dont use gui
nmcli connection down Hotspot
nmcli connection modify Hotspot 802-11-wireless-security.key-mgmt sae
nmcli connection up Hotspot
```
