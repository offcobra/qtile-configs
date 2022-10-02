# My Qtile config #
###################

import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer
#import arcobattery

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
myTerm = "alacritty"      # My terminal of choice
home = os.path.expanduser('~')


# Functions #
#############

def to_next(qtile, right=True):
    i = qtile.screens.index(qtile.current_screen)
    if i <= 1:
        qtile.cmd_to_screen(i + 1)
    else:
        qtile.cmd_to_screen(0)

def to_prev(qtile, right=True):
    i = qtile.screens.index(qtile.current_screen)
    if i > 0:
        qtile.cmd_to_screen(i - 1)
    else:
        qtile.cmd_to_screen(2)

def check_vpn():
    ''' Check if VPN is Actrive '''
    cmd = 'ip addr'
    process = subprocess.run(cmd.split(), stdout=suprocess.PIPE).stdout.decode('utf-8')
    if 'nordlynx' in process:
        result = ' vpn: YES '
    else:
        result = ' vpn: NO '
    return result


# User Defined KEYS
keys = [

# Most of our keybindings are in sxhkd file - except these
# sxhkd out of use
# Def my own Keybinding

    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "p", lazy.spawn("rofi -show run")),
    Key([mod, "shift"], "p", lazy.spawn("websearch")),
    #Key([mod], "e", lazy.spawn("emacsclient -c -a 'emacs'")),
    Key([mod], "w", lazy.spawn("brave")),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    Key([mod], "g", lazy.spawn("steam")),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "o", lazy.spawn("nitrogen")),
    Key([mod], "s", lazy.spawn("alacritty -e bashtop")),
    Key([mod, "shift"], "Return", lazy.spawn("kitty")),
    Key([mod, "shift"], "w", lazy.spawn("brave --incognito")),

# KEYCHORD BINDINGS
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
        Key([], "d",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
            desc='Emacsclient Dired'
            ),
        Key([], "t",
            lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
            desc='Emacsclient Vterm'
            )
    ]),

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
        #Key([], "L",
        #    lazy.spawn("librewolf --private-window"),
        #    desc='Librewolf Incognito'
        #    )
    ]),

# Monitor Resolution
    KeyChord([mod],"r", [
        Key([], "w",
            lazy.spawn("work.sh"),
            desc='Monitors in work mode'
            ),
        Key([], "c",
            lazy.spawn("chill.sh"),
            desc='Monitors in chill mode'
            )
    ]),

# SUPER + FUNCTION KEYS

    #Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "q", lazy.window.kill()),


# SUPER + SHIFT KEYS

    #Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),


# QTILE LAYOUT KEYS
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "m", lazy.function(to_next)),
    Key([mod], "n", lazy.function(to_prev)),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    #Key([mod, "shift"], "f", lazy.layout.flip()),

    ]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
    Key([mod,"shift"], "l", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "h", lazy.function(window_to_previous_screen, switch_screen=True)),
])

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=False)),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            #"border_focus": "#5e81ac",
            "border_focus": "#E33D1A",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

# Define Colors
colors_bak = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

color_bar = [
    ["#194d33", "#194d33"],
    #["#1c1f24", "#1c1f24"], #pretty good...
    ["#330000", "#330000"], #pretty good...
#    ["#800000", "#800000"]
]

# WIDGETS FOR THE BAR
def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
              widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       scale = "true",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
                       ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(
                        font = "Noto Sans Bold",
                        fontsize = 12,
                        margin_y = 4,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 2,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "line",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Sep(
                        linewidth = 2,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[6],
                        background = colors[0]
                        ),
               widget.Sep(
                        linewidth = 2,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(
                        font = "Noto Sans Bold",
                        fontsize = 12,
                        foreground = colors[6],
                        background = colors[0],
                        ),
              widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = color_bar[1],
                       padding = 0,
                       fontsize = 37
                       ),
                widget.TextBox(
                         font = "Noto Sans Bold",
                         #font="FontAwesome",
                         fontsize=28,
                         text="",
                         foreground=colors[6],
                         background = color_bar[1],
                         padding = 4,
                         #fontsize=16
                         ),
                widget.CPUGraph(
                         border_color = colors[2],
                         fill_color = colors[8],
                         graph_color = colors[8],
                         background = color_bar[1],
                         border_width = 1,
                         line_width = 1,
                         core = "all",
                         type = "box"
                         ),
              widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = color_bar[1],
                       foreground = color_bar[0],
                       padding = 0,
                       fontsize = 37
                       ),
                widget.TextBox(
                         font = "Noto Sans Bold",
                         #font="FontAwesome",
                         fontsize=10,
                         text="🌡",
                         foreground=colors[6],
                         background = color_bar[0],
                         padding = 4,
                         #fontsize=16
                         ),
                widget.ThermalSensor(
                        font = "Noto Sans Bold",
                         foreground = colors[2],
                         foreground_alert = colors[6],
                         fontsize=10,
                         bandwidth="down",
                         background = color_bar[0],
                         metric = True,
                         padding = 3,
                         threshold = 80
                         ),
              widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = color_bar[0],
                       foreground = color_bar[1],
                       padding = 0,
                       fontsize = 37
                       ),
                widget.TextBox(
                         font = "Noto Sans Bold",
                         #font="FontAwesome",
                         fontsize=24,
                         text="",
                         foreground=colors[6],
                         background=color_bar[1],
                         padding = 4,
                         #fontsize=16
                         ),
                widget.NetGraph(
                         font="Noto Sans",
                         fontsize=12,
                         bandwidth="down",
                         interface="auto",
                         fill_color = colors[8],
                         foreground=colors[2],
                         background=color_bar[1],
                         graph_color = colors[8],
                         border_color = colors[2],
                         padding = 0,
                         border_width = 1,
                         line_width = 1,
                         ),
              widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = color_bar[1],
                       foreground = color_bar[0],
                       padding = 0,
                       fontsize = 37
                       ),
                widget.TextBox(
                         font = "Noto Sans Bold",
                         #font="FontAwesome",
                         fontsize=25,
                         text="",
                         foreground=colors[6],
                         background=color_bar[0],
                         padding = 4,
                         #fontsize=16
                         ),
                widget.MemoryGraph(
                         border_width = 1,
                         border_color = colors[2],
                         frequency = 1,
                         background = color_bar[0],
                        ),
              widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = color_bar[0],
                       foreground = color_bar[1],
                       padding = 0,
                       fontsize = 37
                       ),
               widget.TextBox(
                        font = "Noto Sans Bold",
                        #font="FontAwesome",
                        text="🕗",
                        foreground=colors[6],
                        background=color_bar[1],
                        padding = 4,
                        fontsize=14
                        ),
               widget.Clock(
                        font = "Noto Sans Bold",
                        foreground = colors[2],
                        background = color_bar[1],
                        fontsize = 14,
                        format="%H:%M  %d-%m-%Y  "
                        ),
              widget.TextBox(
                       text = '',
                       font = "Ubuntu Mono",
                       background = color_bar[1],
                       foreground = color_bar[0],
                       padding = 0,
                       fontsize = 37
                       ),
#                widget.Sep(
#                         linewidth = 2,
#                         padding = 10,
#                         foreground = colors[2],
#                         background = colors[0]
#                         ),
               widget.Systray(
                        background = color_bar[0],
                        icon_size=20,
                        padding = 4
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()[2:7]
    widgets_screen2.pop(1)
    widgets_screen2.pop(1)
    widgets_screen2.extend([
        widget.TextBox(
                text = '',
                font = "Ubuntu Mono",
                background = colors[0],
                foreground = color_bar[0],
                padding = 0,
                fontsize = 37
                ),
        widget.TextBox(
                    font = "Noto Sans Bold",
                    #font="FontAwesome",
                    text="",
                    foreground=colors[6],
                    background = color_bar[0],
                    padding = 4,
                    fontsize=24
                    ),
        widget.Clock(
                font = "Noto Sans Bold",
                foreground = colors[2],
                background = color_bar[0],
                fontsize = 14,
                format="%H:%M  %d-%m-%Y"
                ),
    ])
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.8)),
            Screen(bottom=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.8)),
            Screen(bottom=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.8))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []


main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='csgo_linux64'),
    #Match(wm_class='ConanSandbox (64-bit, PCD3D_SM5)'),
    Match(wm_class='conky'),

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
