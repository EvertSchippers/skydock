
import datetime
import os


def wake_up():
    with open("wake_up.txt", "a") as f:
        f.write(f"Woke up at {datetime.datetime.now()}!\n")

    print("Hello, world!")
    print("And the repo is... ", os.environ.get("REPO", "No repo found."))
