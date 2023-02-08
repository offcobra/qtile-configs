''' Module to define the widgets for the bar.. '''

from libqtile import qtile
from libqtile import widget

from settings.colors import colors, color_bar
from settings.helper import check_vpn, vpn_toggle, check_cpu


myTerm = "alacritty"      # My terminal of choice
myFont = "Source Code Pro"


# WIDGETS FOR THE BAR
#---------------------
#arch_symbols = '⮝⮝  ⋏ ◬ ⟑  ⩓'

# Separator with no with
def get_sep(width, pad=5, background=colors[0]):
    ''' get separator '''
    return widget.Sep(linewidth = width, padding = pad, foreground = colors[2], background = background)

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
        fontsize = 20,
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
    )
    return groupbox

# Current Layout
def get_current_layout():
    return widget.CurrentLayout(
        font = myFont + " Bold",
        foreground = colors[6],
        background = colors[0]
    )

# Current Window
def get_window_name():
    ''' get current window name..'''
    return widget.WindowName(
        font = myFont + " Bold",
        fontsize = 12,
        foreground = colors[6],
        background = colors[0],
    )

# Text Box
def get_text_box(backc, forec, txt='', size=37, cmd=''):
    ''' Get textBox for wiget'''
    return widget.TextBox(
        text = txt,
        font = "Ubuntu Mono",
        background = backc,
        foreground = forec,
        padding = 0,
        fontsize = size,
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(cmd)}
    )

# Genn Pool Text
vpn_widget = widget.GenPollText(
    font = myFont + " Bold",
    fontsize = 12,
    update_interval=2,
    func=lambda: check_vpn(),
    foreground=colors[6],
    background = color_bar[0],
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(myTerm + vpn_toggle()),
        'Button3': lambda: qtile.cmd_spawn(myTerm + ' --hold -e watch nordvpn status'),
    }
)

cpu_widget = widget.GenPollText(
    font = myFont + " Bold",
    fontsize = 12,
    update_interval=2,
    func=lambda: check_cpu(),
    foreground=["#191919", "#191919"],
    #foreground=colors[2],
    background = color_bar[1],
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn("bash /home/wally/.local/bin/toggle_cpu")
    }
)

# CPU Widget
cpu = widget.CPUGraph(
    border_color = colors[2],
    fill_color = colors[8],
    graph_color = colors[8],
    background = color_bar[1],
    border_width = 1,
    line_width = 1,
    core = "all",
    type = "box",
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bashtop')}
)

# Termal Sensor
thermal = widget.ThermalSensor(
    font = "Noto Sans Bold",
    foreground = colors[2],
    foreground_alert = colors[6],
    fontsize=10,
    bandwidth="down",
    background = color_bar[0],
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
    fill_color = colors[8],
    foreground=colors[2],
    background=color_bar[1],
    graph_color = colors[8],
    border_color = colors[2],
    padding = 0,
    border_width = 1,
    line_width = 1,
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -t TestInternetConn -e bash /home/wally/.local/bin/test-conn')}
)

# Memory
memory = widget.MemoryGraph(
    border_width = 1,
    border_color = colors[2],
    frequency = 1,
    background = color_bar[0],
)

# Clock
def clock(backc):
    ''' retruns clock '''
    return widget.Clock(
        font = myFont + " Bold",
        foreground = colors[2],
        background = backc,
        fontsize = 14,
        format="%H:%M %d-%m-%Y ",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -t Calender -e cal -3')}
    )

# SysTray
systray = widget.Systray(
    background = color_bar[0],
    icon_size=20,
    padding = 4
)

# Clock "🕗 "

def init_widgets_list():
    ''' Widgets for the main screen '''
    widgets_list = [
        get_sep(0, 10),
        py_image,
        get_sep(0, 5),
        get_group_box(),
        get_sep(2, 10),
        get_current_layout(),
        get_sep(2, 10),
        get_window_name(),
        get_text_box(colors[0], color_bar[0]),
        vpn_widget,
        get_text_box(color_bar[0], color_bar[1]),
        #get_text_box(color_bar[1], colors[6], " [{}]".format(check_cpu()), 12, cmd=myTerm + ' -e bashtop'),
        get_text_box(color_bar[1], ["#191919", "#191919"], "  =>", 13),
        #get_text_box(color_bar[1], colors[2], "  => ", 13),
        cpu_widget,
        cpu,
        get_text_box(color_bar[1], color_bar[0]),
        get_text_box(color_bar[0], colors[6], "🌡", 12, cmd=myTerm + ' --hold -t Sensors -e watch sensors'),
        thermal,
        get_text_box(color_bar[0], color_bar[1]),
        get_text_box(color_bar[1], colors[6], "", 14, cmd="websearch"),
        net,
        get_text_box(color_bar[1], color_bar[0]),
        get_text_box(color_bar[0], colors[6], "", 12),
        memory,
        get_text_box(color_bar[0], color_bar[1]),
        get_text_box(color_bar[1], colors[6], " ", 12, cmd=myTerm + ' --hold -t Calender -e /usr/bin/cal -y'),
        clock(color_bar[1]),
        get_text_box(color_bar[1], color_bar[0]),
        systray,
        get_sep(0, 5, background=color_bar[0]),
    ]
    return widgets_list


def init_widgets_secondary():
    ''' widgets for the secundary Screen '''
    widgets = init_widgets_list()[0:8].copy()
    widgets.extend([
        get_text_box(colors[0], color_bar[0]),
        get_text_box(color_bar[0], colors[6], " ", 12, cmd=myTerm + ' --hold -t Calender -e /usr/bin/cal -y'),
        clock(color_bar[0])
    ])
    return widgets
