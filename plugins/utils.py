import os


def run(command: str) -> str:
    return os.popen(command).read()
