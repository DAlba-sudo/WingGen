from settings import DEBUG

class Debug():
    def __init__(self) -> None:
        pass

    def print(msg: str, cat="warning"):
        if DEBUG:
            print(f"{cat}: ".rjust(6) + f"{msg}")