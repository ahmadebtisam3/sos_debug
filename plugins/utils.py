import os
from middlewared.client import Client


def run(command: str) -> str:
    return os.popen(command).read()


def call(command: str, *args) -> dict:
    with Client() as c:
        return c.call(command, *args)
