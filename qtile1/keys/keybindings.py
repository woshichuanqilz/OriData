
from libqtile.config import Click, Drag, Key, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger

# Import the function that move the window to the next and prev group
from functions import Functions, PWA
from typing import Callable

from config_keybindings import *



class Keybindings:

    keys = []
    
    spawn_keys = SPAWN_KEYS
    
    cmd_keys = SPAWN_CMD_KEYS

    def create_layout_keys(self):
        ############   BINDINGS FOR MONADTALL   ##############
        modifier = [MOVEMENT_KEY]
        
        layout_left  = Key(modifier, LEFT, lazy.layout.left())
        
        layout_right = Key(modifier, RIGHT, lazy.layout.right())
        
        layout_down  = Key(modifier, DOWN, lazy.layout.down())
        
        layout_up    = Key(modifier, UP, lazy.layout.up())

        toogle_layout = Key(modifier, 'z', lazy.next_layout())
        group_switch = Key([MOVEMENT_KEY, 'shift'], 'Tab', lazy.screen.toggle_group())
        self.keys += [layout_left, layout_right, layout_down, layout_up, toogle_layout, group_switch] 

    def create_swap_keys(self):
        modifier = [MOVEMENT_KEY, SWAP_KEY]

        left  = Key(modifier, SWAP_LEFT, lazy.layout.swap_left())
        right = Key(modifier, SWAP_RIGHT, lazy.layout.swap_right())
        down  = Key(modifier, SWAP_DOWN, lazy.layout.shuffle_down())
        up    = Key(modifier, SWAP_UP, lazy.layout.shuffle_up())
        
        flip  = Key(modifier, SWAP_FLIP, lazy.layout.flip()) 

        self.keys += [left, right, down, up, flip] 

    
    def create_windows_keys(self):
        
        modifier = [MOVEMENT_KEY] 

        grow      = Key(modifier, GROW, lazy.layout.grow())
        shrink    = Key(modifier, SHRINK, lazy.layout.shrink())
        normalize = Key(modifier, NORMALIZE, lazy.layout.normalize())
        maximize  = Key(modifier, MAXIMIZE, lazy.layout.maximize())
        
        self.keys += [grow, shrink, normalize, maximize] 
    
    def create_shutdown_keys(self):
        
        shutdown = Key(SHUTDOWN_MODIFIER, SHUTDOWN, lazy.shutdown())
        restart  = Key(SHUTDOWN_MODIFIER, RESTART, lazy.restart())
        
        self.keys += [shutdown, restart]
    
    def create_kill_keys(self):
        modifier = [MOVEMENT_KEY, ALTGR] 

        all_minus_current = Key(modifier, KILL_ALL_MINUS_CURRENT, 
                            Functions.kill_all_windows_minus_current())
        all_              = Key(modifier, KILL_ALL,
                            Functions.kill_all_windows())
        current           = Key([KILL_KEY], KILL_CURRENT,
                                lazy.window.kill())
       
        self.keys += [all_minus_current, all_, current] 

    def create_floating_keys(self):
        
        modifier = [MOVEMENT_KEY]

        floating = Key(modifier, TOOGLE_FLOATING, lazy.window.toggle_floating())
        full = Key(modifier, TOOGLE_FULL, lazy.window.toggle_fullscreen())
        
        self.keys += [floating, full]        
    
    def create_groups_keys(self):
        modifier      = [GROUPS_KEY]
        swap_modifier = [GROUPS_KEY, SWAP_GROUP_KEY]
        screen_modifier = [MOVEMENT_KEY]

        move_next = Key(modifier, NEXT_GROUP, lazy.screen.next_group()) 
        move_prev = Key(modifier, PREV_GROUP, lazy.screen.prev_group()) 
        
        swap_next = Key(swap_modifier, NEXT_GROUP, Functions.window_to_next_group()) 
        swap_prev = Key(swap_modifier, PREV_GROUP, Functions.window_to_prev_group()) 

        move_next_screen = Key(screen_modifier, NEXT_GROUP, lazy.next_screen()) 
        move_prev_screen = Key(screen_modifier, PREV_GROUP, lazy.next_screen()) 

        self.keys += [move_next, move_prev, swap_next, swap_prev, move_next_screen, move_prev_screen]

    def create_spawn_keys(self):
           
        for spawn_key in self.spawn_keys:
            
            modifier, key, command = spawn_key

            keybinding = Key(modifier, key, lazy.spawn(command)) 

            self.keys.append(keybinding)
            
    def create_cmd_keys(self):
                    
        for cmd_key in self.cmd_keys:
            
            modifier, key, command = cmd_key

            keybinding = Key(modifier, key, lazy.spawncmd(command)) 

            self.keys.append(keybinding)

    def go_to_group(self, name: str) -> Callable:
        def _inner(lazy) -> None:
            logger.warning('has something')
            logger.warning(type(lazy.groups[0]))
            if len(lazy.screens) == 1:
                lazy.groups[name].cmd_toscreen()
                return
            if name == 0:
                lazy.focus_screen(1)
                lazy.groups[name].cmd_toscreen()
            else:
                lazy.focus_screen(0)
                lazy.groups[name].cmd_toscreen()
        return _inner

    
    def init_keys_groups(self, groups):
        """
        Create bindings to move between groups
        """
        group_keys = []
        groups = [x for x in groups if x.__class__.__name__ == 'Group']
        for group in groups:
            index = (group.name[0]).lower()
            group_keys += [Key([MOVEMENT_KEY, SWAP_GROUP_KEY], index, lazy.window.togroup(group.name, switch_group=True))]
            # group_keys += [Key([MOVEMENT_KEY], index, lazy.group[icon].toscreen()), 
        index = 0
        for i in groups:
            group_keys.append(Key([MOVEMENT_KEY], i.name[0], lazy.function(self.go_to_group(index))))
            index += 1

        return group_keys        
    
    def self_define(self):
        scratchPad = Key([MOVEMENT_KEY], 'space', lazy.group['scratchpad'].dropdown_toggle('term'))
        self.keys += [scratchPad]


        
    def init_keys(self):
        
        self.create_layout_keys()
        self.create_swap_keys()
        self.create_windows_keys()
        self.create_shutdown_keys()
        self.create_kill_keys()
        self.create_floating_keys()
        self.create_groups_keys()

        self.create_cmd_keys() 
        self.create_spawn_keys()
        self.self_define()

        return self.keys
        

class Mouse:
    def __init__(self, mod_key=MOD):
        self.mod = mod_key

    def init_mouse(self):
        mouse = [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front())
        ]
        return mouse
