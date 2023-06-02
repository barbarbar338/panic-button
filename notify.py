from notifypy import Notify


def notify(title, message):
    notification = Notify()
    notification.application_name = "Panic Button"
    notification.title = title
    notification.message = message
    notification.icon = "assets/favicon.ico"
    notification.send()
