
import os


def wake_up():
    print("Hello, world!")
    print("And the repo is... ", os.environ.get("REPO", "No repo found."))
