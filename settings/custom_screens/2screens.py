''' Module to define de Qtile Groups... '''

from libqtile import bar
from libqtile.command import lazy
from libqtile.config import Group, Key, Screen

from settings.widgets import init_widgets_list, init_widgets_secondary


mod = "mod4"

# GROUPS
#--------
def_groups = []
group_keys = []

# FOR KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_labels = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

group_layouts = [
    "monadtall","monadtall","monadtall","monadtall","monadtall",
    "monadtall","monadtall","monadtall","monadtall","monadtall"
]

from libqtile.log_utils import logger

DEFAULT_GROUPS = [[1,2], [3,4], [5,6], [7,8]]
SDEFAULT_GROUPS = [[3,4], [5,6], [7,8], [9,0]]

def next_room(qtile):
    ''' Function to chnage all group on screen... '''
    screens = qtile.screens
    group_first_screen = screens[0].group.name
    group_second_screen = screens[1].group.name
    if [int(group_first_screen), int(group_second_screen)] not in DEFAULT_GROUPS:
        qtile.cmd_to_screen(0)
        qtile.groups_map['1'].cmd_toscreen()
        qtile.cmd_to_screen(1)
        qtile.groups_map['2'].cmd_toscreen()

    else:
        fgroup = str(int(group_first_screen) + 2)
        sgroup = '0' if str(int(group_second_screen) + 2) == '10' else str(int(group_second_screen) + 2)
        qtile.cmd_to_screen(0)
        qtile.groups_map[fgroup].cmd_toscreen()
        qtile.cmd_to_screen(1)
        qtile.groups_map[sgroup].cmd_toscreen()

def prev_room(qtile):
    ''' Function to chnage all group on screen... '''
    screens = qtile.screens
    group_first_screen = screens[0].group.name
    group_second_screen = screens[1].group.name
    if [int(group_first_screen), int(group_second_screen)] not in SDEFAULT_GROUPS:
        qtile.cmd_to_screen(0)
        qtile.groups_map['9'].cmd_toscreen()
        qtile.cmd_to_screen(1)
        qtile.groups_map['0'].cmd_toscreen()

    else:
        fgroup = '9' if str(int(group_first_screen) - 2) == '-1' else str(int(group_first_screen) - 2)
        sgroup = str(10 - 2) if group_second_screen == '0' else str(int(group_second_screen) - 2)
        qtile.cmd_to_screen(0)
        qtile.groups_map[fgroup].cmd_toscreen()
        qtile.cmd_to_screen(1)
        qtile.groups_map[sgroup].cmd_toscreen()



def go_to_group(group):
    ''' Function to focus group on default screen '''
    def f(qtile):
        if group in '13579':
            qtile.cmd_to_screen(0)
            qtile.groups_map[group].cmd_toscreen()
        else:
            qtile.cmd_to_screen(1)
            qtile.groups_map[group].cmd_toscreen()

    return f

for i, value in enumerate(group_names):
    def_groups.append(
        Group(
            name=value,
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in def_groups:
    group_keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.function(go_to_group(i.name))),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

group_keys.extend([
    Key([mod], "n", lazy.function(prev_room)),
    Key([mod], "m", lazy.function(next_room))
])


def get_screens():
    ''' Create the Screens... '''
    return [Screen(top=bar.Bar(widgets=init_widgets_list('chill', 0), size=15, opacity=1, margin=[4,6,0,6])),
            Screen(top=bar.Bar(widgets=init_widgets_secondary('chill', 1), size=15, opacity=1, margin=[4,6,0,6]))]
