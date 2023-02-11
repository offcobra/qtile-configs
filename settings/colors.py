''' Colors Module.. '''

# Possible Themes
# Doom ??
# Dracula
# Nord
# One - Ocean
# Snazzy
# Gruvbox
# Solarized dark

# Default Colors
colors = {
    "background": ["#282c34", "#282c34"],
    "foreground": ["#51afef", "#51afef"],
    "active": ["#a9a1e1", "#a9a1e1"],
    "inactive": ["#da8548", "#da8548"],
    "color1": ["#dfdfdf", "#dfdfdf"],
    "color2": ["#ff6c6b", "#ff6c6b"],
    "color3": ["#c678dd", "#c678dd"],
    "color4": ["#98be65", "#98be65"],
    "color5": ["#46d9ff", "#46d9ff"],
    "barg": ['#194d33', '#194d33'],
    "barr": ['#993333', '#993333']
}

# Testing new color Theme system
THEME = "/home/wally/.config/qtile/themes/doom.json"
def get_theme():
    ''' Function to get Theme '''
    with open(THEME, 'r') as f:
        try:
            print('Getting new color style')
            theme = json.loads(f.read())
        except:
            print('Getting old color style')
            theme = colors
    return theme


color_crimson = [["#4a4a46", "#4a4a46"], # color 0
                 ["#4a4a46", "#4a4a46"], # color 1
                 ["#c0c5ce", "#c0c5ce"], # color 2
                 ["#d33682", "#d33682"], # color 3
                 ["#cf3e3e", "#cf3e3e"], # color 4
                 ["#fdf6e3", "#fdf6e3"], # color 5
                 ["#d42121", "#d42121"], # color 6
                 ["#62FF00", "#62FF00"], # color 7
                 ["#cf3e3e", "#cf3e3e"], # color 8
                 ["#eb9b9b", "#eb9b9b"]] # color 9


color_default = [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9


color_dracula = [["#000000", "#000000"], # color 0
            ["#282A36", "#282A36"], # color 1
            ["#F8F8F2", "#F8F8F2"], # color 2
            ["#F1FA8C", "#F1FA8C"], # color 3
            ["#BD93F9", "#BD93F9"], # color 4
            ["#FF79C6", "#FF79C6"], # color 5
            ["#8BE9FD", "#8BE9FD"], # color 6
            ["#BFBFBF", "#BFBFBF"], # color 7
            ["#4D4D4D", "#4D4D4D"], # color 8
            ["#FF5555", "#FF5555"]] # color 9


color_nord = [["#3B4252", "#3B4252"], # color 0
            ["#2e3440", "#2e3440"], # color 1
            ["#A3BE8C", "#A3BE8C"], # color 2
            ["#EBCB8B", "#EBCB8B"], # color 3
            ["#81A1C1", "#81A1C1"], # color 4
            ["#D8DEE9", "#D8DEE9"], # color 5
            ["#88C0D0", "#88C0D0"], # color 6
            ["#E5E9F0", "#E5E9F0"], # color 7
            ["#4C566A", "#4C566A"], # color 8
            ["#BF616A", "#BF616A"]] # color 9


color_zion = [["#4a4a46", "#4a4a46"], # color 0
            ["#4a4a46", "#4a4a46"], # color 1
            ["#e3bbf1", "#e3bbf1"], # color 2
            ["#d33682", "#d33682"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#fdf6e3", "#fdf6e3"], # color 5
            ["#d42121", "#d42121"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#9742b5", "#9742b5"], # color 8
            ["#002b36", "#002b36"]] # color 9
