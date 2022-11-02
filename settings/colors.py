''' Colors Module.. '''

# TODO Test PyWal allready installed
# setting colors



# COLORS
#-------
colors = [["#282c34", "#282c34"],# 0
          ["#1c1f24", "#1c1f24"],# 1
          ["#dfdfdf", "#dfdfdf"],# 2
          ["#ff6c6b", "#ff6c6b"],# 3
          ["#98be65", "#98be65"],# 4
          ["#da8548", "#da8548"],# 5
          ["#51afef", "#51afef"],# 6
          ["#c678dd", "#c678dd"],# 7
          ["#46d9ff", "#46d9ff"],# 8
          ["#a9a1e1", "#a9a1e1"]]# 9

test = '#993333'
#test = '#ffffff'
black = '#000000'

color_bar = [
    ["#194d33", "#194d33"],
    [test, test],
    #["#1c1f24", "#1c1f24"], #pretty good...
    #["#330000", "#330000"], # This is last one
    #["#662200", "#662200"] -> rot...
    #["#4d1a00", "#4d1a00"]
]

test = {
    "sep": {
        "background": ["#282c34", "#282c34"],
        "foreground": ["#dfdfdf", "#dfdfdf"]
    },
    "gbox" : {
        "active": ["#a9a1e1", "#a9a1e1"],
        "inactive": ["#da8548", "#da8548"],
        "background": ["#282c34", "#282c34"],
        "foreground": ["#dfdfdf", "#dfdfdf"]
    },
    "cur_layout" : {
        "background": ["#282c34", "#282c34"],
        "foreground": ["#51afef", "#51afef"], # Color 6
    },
    "window_name": {
        "background": ["#282c34", "#282c34"],
        "foreground": ["#51afef", "#51afef"],
    },
    "vpn": {
        "foreground": ["#51afef", "#51afef"], # Color 6
        "background": ["#194d33", "#194d33"]  # Color Bar 0
    }
}
