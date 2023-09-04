''' Module to host keybindings '''
from libqtile.command import lazy
from libqtile.config import Drag, Key, KeyChord

# Custom plugin
from settings import traverse

from settings.screens import (
    group_keys,
    window_to_next_group,
    window_to_previous_group
)


#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"


mod2 = "control"
#myTerm = "alacritty"      # My terminal of choice
myTerm = "foot"      # My terminal of choice


# Mouse keybindings
# -----------------
mouse_keys = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

# Keybindings
#------------
keybindings = [

# BASIC KEYBINDINGS
# Def my own Keybinding

    Key([mod], "Return", lazy.spawn("alacritty -e fish"), desc="Alacritty with fish shell"),
    Key([mod, "shift"], "Return", lazy.spawn("alacritty"), desc="Alacritty Term with bash"),
    Key([mod], "p", lazy.spawn("rofi -show run -theme ~/.config/rofi/theme.rasi"), desc="Programm Launcher"),
    Key([mod, "shift"], "p", lazy.spawn("bash /home/wally/.local/bin/websearch"), desc="Websearch Script"),
    Key([mod, "shift"], "b", lazy.hide_show_bar("top"), desc="Toggle Qtile Bar"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="File Manager"),
    Key([mod], "s", lazy.spawn("alacritty -e bashtop"), desc="Fancy System Monitor"),
    Key([mod], "u", lazy.spawn("alacritty -e bash /home/wally/.local/bin/update_system"), desc="Update System"),
    Key([mod], "z", lazy.spawn("archlinux-logout"), desc="Logout / Restart / Shutdown"),
    Key([mod], "w", lazy.widget["widgetbox"].toggle(), desc="Toggle the WidgetBox"),
    Key([mod], "x", lazy.spawn('flameshot gui'), desc="Start screen snipped"),

# KEYCHORD BINDINGS
# Basic Commands
    KeyChord([mod],"g", [
        Key([], "g",
            lazy.spawn("bash /home/wally/.local/bin/steam_start"),
            desc='steam'
            ),
        Key([], "u",
            lazy.spawn("/home/wally/.local/web_app/youtube-linux-x64/youtube"),
            desc='Youtube'
            ),
        Key([], "v",
            lazy.spawn("pavucontrol"),
            desc='Pavucontrol'
            ),
        Key([], "s",
            lazy.spawn("spotify"),
            desc='Spotify Music'
            ),
        Key([], "e",
            lazy.spawn("thunderbird"),
            desc='Mail Client'
            ),
        Key([], "p",
            lazy.spawn("start-esudo-apps gparted"),
            desc='Gparted'
            ),
        Key([], "t",
            lazy.spawn("bash /home/wally/.local/bin/tweak_theme"),
            desc='Launch GTK & QT tweaks Tools'
            ),
        Key([], "w",
            lazy.spawn("bash /home/wally/.local/bin/movie_time"),
            desc='Launch PopCornTime'
            ),
        Key([], "m",
            lazy.spawn("piper"),
            desc='Launch Piper mouse control'
            ),
        Key([], "a",
            lazy.spawn("archlinux-tweak-tool"),
            desc='ArcoTweakTool'
            ),
        Key([], "o",
            lazy.spawn("nitrogen"),
            desc='Nitrogen'
            )
    ], name="Common Programms"),

# Emacs
    KeyChord([mod],"e", [
        Key([], "e",
            lazy.spawn("emacsclient -c -a 'emacs'"),
            desc='Emacsclient Dashboard'
            ),
        Key([], "b",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
            desc='Emacsclient Ibuffer'
            ),
        Key([], "r",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(doom/reload)'"),
            desc='Emacsclient Ibuffer'
            ),
        Key([], "d",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
            desc='Emacsclient Dired'
            ),
        Key([], "t",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
            desc='Emacsclient Vterm'
            )
    ], name="Emacs"),

# Crypto Stuff
    KeyChord([mod],"c", [
        Key([], "b",
            lazy.spawn("binance"),
            desc='Binance Trading'
            ),
        Key([], "c",
            lazy.spawn("qutebrowser https://coinmarketcap.com/"),
            desc='CoinMarketCap'
            ),
        Key([], "p",
            lazy.spawn("qutebrowser https://mail.proton.me"),
            desc='ProtonMail'
            ),
        Key([], "e",
            lazy.spawn("exodus"),
            desc='Crypto Wallet'
            )
    ], name="Crypto Stuff"),

# Browser
    KeyChord([mod],"b", [
        Key([], "b",
            lazy.spawn("brave"),
            desc='Brave'
            ),
        Key([], "i",
            lazy.spawn("brave --incognito"),
            desc='Brave Incognito'
            ),
        Key([], "f",
            lazy.spawn("firefox"),
            desc='Firefox'
            ),
        Key([], "h",
            lazy.spawn("firefox --private-window"),
            desc='Firefox Incognito'
            ),
        Key([], "l",
            lazy.spawn("librewolf"),
            desc='Librewolf'
            ),
        Key([], "o",
            lazy.spawn("qutebrowser"),
            desc='QuteBrowser'
            ),
        Key([], "p",
            lazy.spawn("librewolf --private-window"),
            desc='Librewolf Incognito'
            )
    ], name="Browsers"),

# Monitor Resolution / Picom toggle
    KeyChord([mod],"t", [
        Key([], "t",
            lazy.spawn("bash /home/wally/.local/bin/theme_choose"),
            desc='Toggle / Choose Global Theme...'
            ),
        Key([], "f",
            lazy.spawn("bash /home/wally/.local/bin/screen_full"),
            desc='Monitors in full mode'
            ),
        Key([], "c",
            lazy.spawn("bash /home/wally/.local/bin/screen_chill"),
            desc='Monitors in chill mode'
            ),
        Key([], "w",
            lazy.spawn("bash /home/wally/.local/bin/screen_work"),
            desc='Monitors in work mode'
            ),
        Key([], "p",
            lazy.spawn("bash /home/wally/.local/bin/toggle_picom"),
            desc='Toggle Picom'
            ),
        Key([], "o",
            lazy.spawn("bash /home/wally/.local/bin/toggle_conky"),
            desc='Toggle Conky'
            ),
        Key([], "b",
            lazy.spawn("bash /home/wally/.local/bin/toggle_cpu"),
            desc='Toggle CPU Guvernor'
            ),
        Key([], "v",
            lazy.spawn("bash /home/wally/.local/bin/toggle_vpn"),
            desc='Toggle NordVPN'
            ),
        Key([], "s",
            lazy.spawn("bash /home/wally/.local/bin/toggle_service"),
            desc='Toggle System Service'
            ),
        Key([], "q",
            lazy.spawn("bash /home/wally/.local/bin/toggle_service stop"),
            desc='Stop all System Services'
            )
    ], name="Toggle Scripts"),

# Virtualization
    KeyChord([mod],"v", [
        Key([], "v",
            lazy.spawn("virtualbox"),
            desc='Spawns VirtualBox'
            ),
        Key([], "u",
            lazy.spawn("bash /home/wally/.local/bin/container_run ubuntu"),
            desc='Spawns Ubuntu Container'
            ),
        Key([], "p",
            lazy.spawn("bash /home/wally/.local/bin/container_run parrot"),
            desc='Spawns ParrotOs Container'
            ),
        Key([], "f",
            lazy.spawn("bash /home/wally/.local/bin/container_run fedora"),
            desc='Spawns Fedora Container'
            ),
        Key([], "k",
            lazy.spawn("bash /home/wally/.local/bin/container_run"),
            desc='Spawn and attach to Docker Container'
            ),
        Key([], "d",
            lazy.spawn("bash /home/wally/.local/bin/vms_run"),
            desc='Spawn and attach to Vm Distro'
            ),
        Key([], "s",
            lazy.spawn("bash /home/wally/.local/bin/stop_docker"),
            desc='Remove all docker Container'
            ),
        Key([], "m",
            lazy.spawn("bash /home/wally/.local/bin/virt-start"),
            desc='Spawns Virt-Manager'
            ),
        Key([], "w",
            lazy.spawn("bash /home/wally/.local/bin/vms_run win10"),
            desc='Start Windows'
            ),
        Key([], "b",
            lazy.spawn("flatpak run com.usebottles.bottles"),
            desc='Spawns Bottles'
            )
    ], name="Virtualization"),

# Chat Programms
    KeyChord([mod],"i", [
        Key([], "d",
            lazy.spawn("discord"),
            desc='Discord'
            ),
        Key([], "s",
            lazy.spawn("signal-desktop"),
            desc='Signal'
            ),
        Key([], "w",
            lazy.spawn("whatsapp-nativefier"),
            desc='Whatsapp'
            ),
        Key([], "t",
            lazy.spawn("teamspeak"),
            desc='TeamSpeak'
            ),
    ], name="Chating"),

# SUPER + FUNCTION KEYS

    #Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Normalize Layout"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
    Key([mod], "q", lazy.window.kill(), desc="Window Kill"),


# SUPER + SHIFT KEYS

    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),


# QTILE LAYOUT KEYS
    Key([mod], "space", lazy.next_layout(), desc="Next Layout"),

# CHANGE FOCUS
    Key([mod], "k", lazy.layout.up(), desc="Move Up"),
    Key([mod], "j", lazy.layout.down(), desc="Move Down"),
    #Key([mod], "h", lazy.layout.left()),
    #Key([mod], "l", lazy.layout.right()),
    #Key([mod], "m", lazy.function(to_next)),
    #Key([mod], "n", lazy.function(to_prev)),
    #
# Traverse Plugin
    #Key([mod], 'k', lazy.function(traverse.up)),
    #Key([mod], 'j', lazy.function(traverse.down)),
    Key([mod], 'h', lazy.function(traverse.left), desc="Move Left"),
    Key([mod], 'l', lazy.function(traverse.right), desc="Move Right"),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "mod1"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "mod1"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "mod1"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "mod1"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # MOVE WINDOWS left / right & up / down
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "l", lazy.function(window_to_next_group)),
    Key([mod,"shift"], "h", lazy.function(window_to_previous_group)),

]
keybindings.extend(group_keys)
