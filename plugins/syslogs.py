from .base import Plugin
from .debug_types import Folder


class SysLogs(Plugin):

    def __init__(self):
        super().__init__('logs/')

    def setup_debug(self):
        self.debugs.append(Folder('/var/log'))
