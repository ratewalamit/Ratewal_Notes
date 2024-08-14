#install vim
#set trackpad settings, Please restart in order to see these settings into effect
#instll netextender from website #do update java while istallin, see instructions  on website to see how to isntall
#install chrome
#install ssh configs
#change bashrc #from github files
#install remmina from app center
#install trashcli
#install git
#install fingerprint 
#install libtools using: sudo apt install libinput-tools
#fix trackpad using forlloiwng commands
Putting these lines in sudo vim /etc/X11/xorg.conf.d/99-synaptics-overrides.conf
```shell
Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"
        Option "Tapping" "off"
        Option "ScrollSpeed" "0.5"
        Option "PalmDetection" "on"
        Option "PalmMinWidth" "5"
        Option "PalmMinZ" "50"
        Option "ClickMethod" "clickfinger"
        Option "MiddleClickEnabled" "true"
        Option "MiddleClickThreshold" "5"
        Option "PointerAcceleration" "0.5"
        Option "EdgeScrolling" "on"
        Option "EdgeScrollLeft" "0"
        Option "EdgeScrollRight" "0"
        Option "EdgeScrollUp" "0"
        Option "EdgeScrollDown" "0"
EndSection
```
