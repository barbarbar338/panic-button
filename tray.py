import keyboard
from infi.systray import SysTrayIcon


def on_quit(tray):
    keyboard.unhook_all_hotkeys()


systray = SysTrayIcon(
    "assets/favicon.ico", "Panic Button by @barbarbar338", on_quit=on_quit
)
