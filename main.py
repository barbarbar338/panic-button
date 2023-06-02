import keyboard
from config import panic_key
from tray import systray
from notify import notify


def on_panic():
    try:
        keyboard.press_and_release("ctrl+w, ctrl+n")
        keyboard.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        keyboard.press_and_release("enter")
    except Exception as e:
        notify("Error", "Error: {}".format(e))


def main():
    keyboard.add_hotkey(panic_key, on_panic)

    notify(
        "Panic Button started",
        "App is running on system tray. Press {} to close current browser tab and right click on the icon and click on 'Quit' button to quit app.".format(
            panic_key
        ),
    )

    systray.start()


if __name__ == "__main__":
    main()
