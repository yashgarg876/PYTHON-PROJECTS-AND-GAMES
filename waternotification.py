import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "P`lease Drink Water Now",
        message = "Get up and, Drink it",
        app_icon = "",
        timeout = 2
    )