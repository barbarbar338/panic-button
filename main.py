import keyboard
from config import panic_key
from tray import systray
from notifypy import Notify


def on_panic():
    try:
        print("Panic button pressed!")
        keyboard.press_and_release("ctrl+w, ctrl+n")
        keyboard.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        keyboard.press_and_release("enter")
        print("New window opened!")
    except Exception as e:
        print("Error: {}".format(e))


def main():
    keyboard.add_hotkey(panic_key, on_panic)

    notification = Notify()
    notification.application_name = "Panic Button"
    notification.title = "Panic Button started"
    notification.message = "App is running on system tray. Press {} to close current browser tab and right click on the icon and click on 'Quit' button to quit app.".format(
        panic_key
    )
    notification.icon = "assets/favicon.ico"
    notification.send()

    systray.start()


if __name__ == "__main__":
    main()
