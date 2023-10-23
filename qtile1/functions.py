from libqtile.command import lazy
from libqtile.log_utils import logger
# from libqtile.command_client import InteractiveCommandClient
import subprocess


class Functions:

    ##### MOVE WINDOW IN GROUPS #####

    @staticmethod
    def window_to_prev_group():
        @lazy.function
        def __inner(qtile):
            i = qtile.groups.index(qtile.current_group)

            if qtile.current_window and i != 0:
                group = qtile.groups[i - 1].name
                qtile.current_window.togroup(group, switch_group=True)

        return __inner

    @staticmethod
    def smart_terminal(qtile):
        qtile.cmd_spawn('kate')
        logger.warning(qtile.current_window.name)

    @staticmethod
    def window_to_next_group():
        @lazy.function
        def __inner(qtile):
            i = qtile.groups.index(qtile.current_group)

            if qtile.current_window and i != len(qtile.groups):
                group = qtile.groups[i + 1].name
                qtile.current_window.togroup(group, switch_group=True)

        return __inner

    ##### KILL ALL WINDOWS #####

    @staticmethod
    def kill_all_windows():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                window.kill()

        return __inner

    @staticmethod
    def kill_all_windows_minus_current():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                if window != qtile.current_window:
                    window.kill()

        return __inner


class PWA:
    def __init__(self):
        pass

    @staticmethod
    def notion():
        return "google-chrome-stable --profile-directory=Default --app=https://notion.so"

    @staticmethod
    def music():
        return "google-chrome-stable --profile-directory=Default --app=https://music.youtube.com/"

    @staticmethod
    def spotify():
        return "google-chrome-stable --profile-directory=Default --app=https://open.spotify.com/"

    @staticmethod
    def youtube():
        return "google-chrome-stable --user-data-dir=Default --app=https://www.youtube.com"

    @staticmethod
    def calendar():
        return "google-chrome-stable --profile-directory=Default --app=https://calendar.google.com/calendar/"

    @staticmethod
    def habitica():
        return "google-chrome-stable --profile-directory=Default --app=https://habitica.com/"




if __name__ == "__main__":
    print("This is an utilities module")
