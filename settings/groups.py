''' Module to define de Qtile Groups... '''

from libqtile.command import lazy
from libqtile.config import Group, Key


mod = "mod4"

# GROUPS
#--------
def_groups = []
group_keys = []

# FOR KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
group_labels = ["", "", "", "", "", "", "", "", "", "",]

group_layouts = [
    "monadtall","monadtall","monadtall","monadtall","monadtall",
    "monadtall","monadtall","monadtall","monadtall","monadtall"
]

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
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=False)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])
