#!/bin/bash

##### ===-->> Qtile autostart Config <<--=== ######
#------------------
# This is a config of:
#  ___   __  __ _____ _        __        __    _ _
# / _ \ / _|/ _|_   _| |__   __\ \      / /_ _| | |
#| | | | |_| |_  | | | '_ \ / _ \ \ /\ / / _` | | |
#| |_| |  _|  _| | | | | | |  __/\ V  V / (_| | | |
# \___/|_| |_|   |_| |_| |_|\___| \_/\_/ \__,_|_|_|
#
#
# Github Url: https://github.com/offcobra/dotfiles
# Github Ssh: git@github.com:offcobra/dotfiles.git
#--------------------------------------------------

#Some ways to set your wallpaper besides variety or nitrogen
#wallpaper for other Arch based systems
#run variety -> To cycle wallpapers
#feh --bg-fill /usr/share/archlinux-tweak-tool/data/wallpaper/wallpaper.png &
#start the conky to learn the shortcuts
#(conky -c $HOME/.config/qtile/scripts/system-overview) &

#start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &


#starting utility applications at boot time

echo "Setting Screen resolution...."
screen_work &

echo "Starting Tray applets..."
nm-applet &
#pamac-tray &
volumeicon &
#xfce4-power-manager &
#numlockx on &
#blueberry-tray &

echo "Starting Picom"
picom --config $HOME/.config/picom/picom.conf &

echo "Auth Agent & Notifyd"
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

echo "Setting Wallpapers"
nitrogen --restore &

echo "Start emacs daemon..."
emacs --daemon &
