########## ===-->> Qtile Config <<--=== ###########
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

import os
import subprocess

from libqtile import qtile
from libqtile import layout, bar, hook
from libqtile.config import Match, Screen

from settings.keybindings import keybindings, mouse_keys
from settings.groups import def_groups
from settings.layouts import def_layouts
from settings.widgets import init_widgets_list, init_widgets_secondary


home = os.path.expanduser('~')


# KeyBindings
keys = keybindings

# MOUSE CONFIGURATION
mouse = mouse_keys

# Groups
groups = def_groups

# layouts
layouts = def_layouts

# Screens Definition
def init_screens():
    ''' Create the Screens... '''
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), size=16, opacity=0.9, margin=[4,6,0,6])),
            Screen(top=bar.Bar(widgets=init_widgets_secondary(), size=15, opacity=0.8, margin=[4,6,0,6])),
            Screen(top=bar.Bar(widgets=init_widgets_secondary(), size=16, opacity=0.8, margin=[4,6,0,6]))]
screens = init_screens()


dgroups_key_binder = None
dgroups_app_rules = []


main = None

@hook.subscribe.startup_once
def start_once():
    ''' Start once '''
    subprocess.call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup
def start_always():
    ''' Start always '''
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    ''' set floating '''
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
