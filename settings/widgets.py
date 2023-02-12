''' Module to define the widgets for the bar.. '''

from libqtile import qtile
from libqtile import widget

#from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

from settings.colors import get_theme
from settings.helper import check_vpn, vpn_toggle, check_cpu


myTerm = "alacritty"      # My terminal of choice
myFont = "Source Code Pro"


colors = get_theme()

# WIDGETS FOR THE BAR
#---------------------
#arch_symbols = '⮝⮝  ⋏ ◬ ⟑  ⩓'

# Separator with no with
def get_sep(width, pad=5, background=colors['background']):
    ''' get separator '''
    return widget.Sep(linewidth = width, padding = pad, foreground = colors['color1'], background = background)

# Display Python Image
py_image = widget.Image(
    filename = "~/.config/qtile/icons/python-white.png",
    scale = True,
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(
            myTerm + ' -t "Qtile Docs" --hold -e bat /home/wally/.config/docs/shortcuts.org'
    )})

# Groupbox for Display Groups
def get_group_box():
    ''' get group box '''
    groupbox = widget.GroupBox(
        font = myFont + ' Bold',
        fontsize = 8,
        margin_y = 4,
        margin_x = 0,
        padding_y = 5,
        padding_x = 5,
        borderwidth = 2,
        disable_drag = True,
        active = colors['active'],
        inactive = colors['inactive'],
        rounded = False,
        highlight_method = "line",
        this_current_screen_border = colors['color1'],
        foreground = colors['foreground'],
        background = colors['background']
    )
    return groupbox

# Current Layout
def get_current_layout():
    return widget.CurrentLayout(
        font = myFont + " Bold",
        fontsize = 10,
        foreground = colors['color1'],
        background = colors['background'],
        decorations=[
            BorderDecoration(
                colour = colors['color1'],
                border_width = [0, 0, 1, 0],
                padding_x = 5,
                padding_y = None,
            )
        ],
    )

# Current Window
def get_window_name():
    ''' get current window name..'''
    return widget.WindowName(
        font = myFont + " Bold",
        fontsize = 10,
        foreground = colors['active'],
        background = colors['background']
    )

# Text Box
def get_text_box(backc, forec, txt='', size=37, cmd=''):
    ''' Get textBox for wiget'''
    return widget.TextBox(
        text = txt,
        font = myFont + " Bold",
        background = backc,
        foreground = forec,
        padding = 0,
        fontsize = size,
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(cmd)}
    )

# Genn Pool Text
vpn_widget = widget.GenPollText(
    font = myFont + " Bold",
    fontsize = 10,
    update_interval=2,
    func=lambda: check_vpn(),
    foreground = colors['foreground'],
    background = colors['background'],
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(myTerm + vpn_toggle()),
        'Button3': lambda: qtile.cmd_spawn(myTerm + ' --hold -e watch nordvpn status'),
    }
)

cpu_widget = widget.GenPollText(
    font = myFont + " Bold",
    fontsize = 10,
    update_interval=2,
    func=lambda: check_cpu(),
    foreground = colors['color1'],
    background = colors['background'],
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn("bash /home/wally/.local/bin/toggle_cpu")
    }
)

# CPU Widget
cpu = widget.CPUGraph(
    fill_color = colors['color1'],
    graph_color = colors['color1'],
    background = colors['background'],
    border_width = 1,
    line_width = 1,
    core = "all",
    type = "box",
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bashtop')}
)

# Termal Sensor
thermal = widget.ThermalSensor(
    font = "Noto Sans Bold",
    foreground = colors['color4'],
    background = colors['background'],
    foreground_alert = colors['color2'],
    fontsize=8,
    bandwidth="down",
    metric = True,
    padding = 3,
    threshold = 80,
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + " --hold -t Sensors -e watch sensors")}
)

# NetGraph
net = widget.NetGraph(
    font="Noto Sans",
    fontsize=12,
    bandwidth="down",
    interface="auto",
    foreground = colors['foreground'],
    background = colors['background'],
    graph_color = colors['color2'],
    fill_color = colors['color2'],
    padding = 0,
    border_width = 1,
    line_width = 1,
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -t TestInternetConn -e bash /home/wally/.local/bin/test-conn')}
)

# Memory
memory = widget.MemoryGraph(
    foreground = colors['foreground'],
    background = colors['background'],
    graph_color = colors['color3'],
    fill_color = colors['color3'],
    border_width = 1,
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bashtop')},
    frequency = 1
)

# Clock
def clock(backc):
    ''' retruns clock '''
    return widget.Clock(
        font = myFont + " Bold",
        foreground = colors['color1'],
        background = backc,
        fontsize = 11,
        format="%H:%M %d-%m-%Y ",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -t Calender -e cal -y')}
    )

# SysTray
systray = widget.Systray(
    background = colors['background'],
    icon_size=14,
    padding = 7,
)


def init_widgets_list():
    ''' Widgets for the main screen '''
    widgets_list = [
        get_sep(0, 10),
        py_image,
        get_sep(0, 5),
        get_group_box(),
        get_current_layout(),
        get_window_name(),
        vpn_widget,
        get_text_box(colors['background'], colors['foreground'], " ", 14),
        get_text_box(colors['background'], colors['color1'], "", 16),
        cpu_widget,
        cpu,
        get_text_box(colors['background'], colors['foreground'], " ", 14),
        get_text_box(colors['background'], colors['color4'], "🌡", 10, cmd=myTerm + ' --hold -t Sensors -e watch sensors'),
        thermal,
        get_text_box(colors['background'], colors['foreground'], " ", 14),
        get_text_box(colors['background'], colors['color2'], "", 14, cmd="websearch"),
        net,
        get_text_box(colors['background'], colors['foreground'], " ", 14),
        get_text_box(colors['background'], colors['color3'], "", 20),
        memory,
        get_text_box(colors['background'], colors['foreground'], " ", 14),
        #clock(colors['background']),
        systray,
        get_sep(0, 10, background=colors['background']),
    ]
    return widgets_list


def init_widgets_secondary():
    ''' widgets for the secundary Screen '''
    widgets = init_widgets_list()[0:6].copy()
    widgets.extend([
        clock(colors['background'])
    ])
    return widgets
