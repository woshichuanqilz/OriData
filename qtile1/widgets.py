import os
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen

from functions import PWA
# widget_defaults = dict(
#     font="Ubuntu Mono",
#     fontsize = 12,
#     padding = 2,
#     background=colors[2]
# )

# extension_defaults = widget_defaults.copy()
myFontSize = 50
iconSize = 60
SepMark = '󱎕'


class MyWidgets:
    def __init__(self):
        self.colors = [["#001f3f", "#001f3f"],  # panel background
                       # background for current screen tab
                       ["#434758", "#434758"],
                       ["#01FF70", "#01FF70"],  # font color for group names
                       # border line color for current tab
                       ["#bc13fe", "#bc13fe"],  # Group down color
                       # border line color for other tab and odd widgets
                       ["#8d62a9", "#8d62a9"],
                       ["#668bd7", "#668bd7"],  # color for the even widgets
                       ["#F39C12", "#F39C12"],  # window name

                       ["#000000", "#000000"],
                       ["#AD343E", "#AD343E"],
                       ["#f76e5c", "#f76e5c"],
                       ["#F39C12", "#F39C12"],
                       ["#F7DC6F", "#F7DC6F"],
                       ["#f1ffff", "#f1ffff"],
                       ["#4c566a", "#4c566a"], ]

        self.termite = "termite"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.Image(
                filename="~/.config/qtile/icons/ArchIcon.svg",
                mouse_callbacks={
                    'Button1': lambda qtile: qtile.cmd_spawn('dmenu_run -p "Run: "')}
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.GroupBox(
                font="Ori Iosevka",
                fontsize=myFontSize,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=self.colors[-2],
                inactive=self.colors[-1],
                # rounded=True,
                highlight_method='block',
                urgent_alert_method='block',
                this_current_screen_border=self.colors[9],
                this_screen_border=self.colors[4],
                other_current_screen_border=self.colors[0],
                other_screen_border=self.colors[0],
                foreground=self.colors[2],
                background=self.colors[0],
                disable_drag=True
            ),
            widget.Prompt(
                prompt=lazy.spawncmd(),
                padding=10,
                fontsize=myFontSize,
                foreground=self.colors[3],
                background=self.colors[1]
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.WindowName(
                font="Smiley Sans",
                fontsize=myFontSize,
                foreground=self.colors[6],
                background=self.colors[0],
                padding=50,
                max_chars=40,
            ),
            widget.Systray(
                background=self.colors[0],
                icon_size=60,
                padding=5
            ),
            widget.TextBox(
                text=SepMark,
                background=self.colors[0],
                foreground=self.colors[11],
                padding=0,
                fontsize=iconSize
            ),
            widget.TextBox(
                text=" 󰻠 ",
                foreground=self.colors[7],
                background=self.colors[11],
                padding=-20,
                fontsize=iconSize
            ),
            widget.Memory(
                font="Ori Iosevka",
                fontsize=myFontSize,
                foreground=self.colors[7],
                background=self.colors[11],
                mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
                    self.termite + ' -e htop')},
                padding=5
            ),
            widget.TextBox(
                text=SepMark,
                background=self.colors[11],
                foreground=self.colors[10],
                padding=0,
                fontsize=iconSize
            ),
            widget.TextBox(
                text="  ",
                fontsize=iconSize,
                foreground=self.colors[7],
                background=self.colors[10],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn("pavucontrol")}
            ),
            widget.Volume(
                font="Ori Iosevka",
                fontsize=myFontSize,
                foreground=self.colors[7],
                background=self.colors[10],
                padding=5
            ),
            widget.TextBox(
                text=SepMark,
                background=self.colors[10],
                foreground=self.colors[9],
                padding=0,
                fontsize=iconSize
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser(
                    "~/.config/qtile/icons")],
                foreground=self.colors[0],
                background=self.colors[9],
                padding=0,
                scale=0.7
            ),
            widget.CurrentLayout(
                foreground=self.colors[7],
                background=self.colors[9],
                font="Ori Iosevka",
                fontsize=myFontSize,
                padding=5
            ),
            widget.TextBox(
                text=SepMark,
                foreground=self.colors[8],
                background=self.colors[9],
                padding=0,
                fontsize=iconSize
            ),
            widget.TextBox(
                text='',
                foreground=self.colors[7],
                background=self.colors[8],
                padding=20,
                fontsize=iconSize
            ),
            widget.Clock(
                foreground=self.colors[7],
                background=self.colors[8],
                font="Ori Iosevka",
                fontsize=myFontSize,
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn(PWA.calendar())},
                format="%b-%d %H:%M  "
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[0],
                background=self.colors[8]
            ),
        ]
        return widgets_list

    def init_widgets_screen(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen = self.init_widgets_list()
        return widgets_screen

    def init_widgets_screen2(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''

        widgets_screen2 = [x for x in self.init_widgets_screen() if not isinstance(x, widget.Systray)] 
        return widgets_screen2

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        bar_size = 60
        return [Screen(bottom=bar.Bar(widgets=self.init_widgets_screen(), opacity=1.0, size=bar_size)),
                Screen(bottom=bar.Bar(
                    widgets=self.init_widgets_screen2(), opacity=1.0, size=bar_size))
                ]
