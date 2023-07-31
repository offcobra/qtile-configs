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

#starting utility applications at boot time


if [[ -z $WAYLAND_DISPLAY ]]
then
    echo -e "X11 Session detected!!!\n\n"

    echo "Setting Screen resolution...."
    bash /home/wally/.local/bin/screen_full &

    echo "Fix for GTK Apps starting slow..."
    /usr/lib/xdg-desktop-portal &
    /usr/lib/xdg-desktop-portal-gnome &

    dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &

    echo "Starting Picom"
    picom --config $HOME/.config/picom/picom.conf &

    echo "Setting Wallpapers"
    nitrogen --restore &

    echo "Starting Flameshot Screenshot tool"
    flameshot &

    echo "Starting Conky"
    conky -c $HOME/.config/conky/theme.conkyrc
fi

echo "Starting Tray applets..."
nm-applet &
#pamac-tray &
volumeicon &
#xfce4-power-manager &
#numlockx on &
#blueberry-tray &

echo "Auth Agent & Notifyd"
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
#dunst &

echo "Start emacs daemon..."
emacs --daemon &

echo "Start signal in tray"
signal-desktop --start-in-tray &

notify-send -t 3000 "Qtile AutoStart" "All Autostart Apps Loaded..."
