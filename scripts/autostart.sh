#!/bin/bash

#autostart ArcoLinux Welcome App
#run dex $HOME/.config/autostart/arcolinux-welcome-app.desktop &

#Some ways to set your wallpaper besides variety or nitrogen
#feh --bg-fill /usr/share/backgrounds/arcolinux/arco-wallpaper.jpg &
#wallpaper for other Arch based systems
#feh --bg-fill /usr/share/archlinux-tweak-tool/data/wallpaper/wallpaper.png &
#start the conky to learn the shortcuts
(conky -c $HOME/.config/qtile/scripts/system-overview) &

#start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &


#starting utility applications at boot time
##run variety 

echo "Setting Screen resolution...."
bash ~/.screenlayout/work.sh &

echo "Starting Tray applets..."
nm-applet &
pamac-tray &
volumeicon &
xfce4-power-manager &
#numlockx on &
#blueberry-tray &

echo "Starting Picom"
picom --config $HOME/.config/qtile/scripts/picom.conf &

echo "Auth Agent & Notifyd"
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

echo "Setting Wallpapers"
nitrogen --restore &

echo "Start emacs daemon..."
emacs --daemon &
