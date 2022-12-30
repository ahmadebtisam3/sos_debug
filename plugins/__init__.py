import os
from importlib import import_module

from .base import Plugin

BUILTIN_FILES = [
    '__init__.py',
    'base.py',
    'utils.py',
    'exception.py',
    'debug_types.py',
]


def get_plugins() -> list:
    for module in os.listdir(os.path.dirname(__file__)):
        if module in BUILTIN_FILES or module[-3:] != '.py':
            continue
        import_module(f'plugins.{module[:-3]}')
    return Plugin.__subclasses__()

