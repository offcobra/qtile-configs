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

def go_to_group(group):
    ''' Function to focus group on default screen '''
    def f(qtile):
        if group in '13579':
            qtile.cmd_to_screen(0)
            qtile.groupMap[group].cmd_toscreen()
        else:
            qtile.cmd_to_screen(1)
            qtile.groupMap[group].cmd_toscreen()

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


def get_screens():
    ''' Create the Screens... '''
    return [Screen(top=bar.Bar(widgets=init_widgets_list('chill', 0), size=15, opacity=1, margin=[4,6,0,6])),
            Screen(top=bar.Bar(widgets=init_widgets_secondary('chill', 1), size=15, opacity=1, margin=[4,6,0,6]))]
