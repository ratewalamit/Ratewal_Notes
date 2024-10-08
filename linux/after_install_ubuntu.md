#exchange bios ctrl and fn keys for lenovo keyboards
#perform sudo apt upgrade 
#set trackpad settings, Please restart in order to see these settings into effect
#install the following packages
```shell
sudo apt upgrade
sudo apt-get -y install vim vlc gimp synaptic trash-cli git git-restore-mtime libinput-tools texlive-full gparted preload gnome-tweaks ubuntu-restricted-extras  
```
#install chrome
#install ssh configs
#install slack
#change bashrc #from github files
#install fingerprint 
## Follow this video https://www.youtube.com/watch?v=xS7ky-ihQU8

#change desktop icon setting and dock behaviour: these options will be available on right click like desktop setting in windows
#install libtools using: sudo apt install libinput-tools
#follow this video for customisations and recommended downlaods after installaition of Ubuntu24 https://www.youtube.com/watch?v=vLm2EHIaxOo
#remove touchpad drivers, ubuntu 24 right now dont have good touchpad driver using sudo apt-get remove xserver-xorg-input-synaptics
#fix trackpad using forlloiwng commands, you may need to execute fixtouchpad command multiple times to get desired results. put it in bashrc
**put to automatically load keypad after suspend**
Put these lines in file with execute persmission /lib/systemd/system-sleep/attach_detach_toucpad 
```shell
#!/bin/sh

case $1/$2 in
  pre/*)
    echo "Going to $2..."
    # Place your pre suspend commands here, or `exit 0` if no pre suspend action required
    modprobe -r psmouse
    ;;
  post/*)
    echo "Waking up from $2..."
    # Place your post suspend (resume) commands here, or `exit 0` if no post suspend action required
    sleep 2
    modprobe psmouse
    ;;
esac

#also perform these actions
fixtouchpad()
{
sudo modprobe -r psmouse
sudo modprobe psmouse
}
```

