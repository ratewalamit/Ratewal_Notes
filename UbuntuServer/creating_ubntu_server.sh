sudo apt update
sudo apt upgrade
sudo apt install tasksel
sudo apt install slim -y
sudo tasksel
sudo apt install tigervnc-standalone-server
vncserver -list
sudo adduser tony
su - tony
vncserver -localhost no 
vncserver -lsit

#Now loging in remmina with ip address and the port on vncserver running eg: 192.168.xx:yy:5902
