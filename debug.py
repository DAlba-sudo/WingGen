from settings import DEBUG
from os import path, system

class Debug():
    def __init__(self) -> None:
        self.DATA_PATH = path.join(path.dirname(__file__), "/Data/")

    def print(msg: str, cat="warning"):
        if DEBUG:
            print(f"{cat}: ".rjust(6) + f"{msg}")

