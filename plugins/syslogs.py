from .base import Plugin, Folder


class SysLogs(Plugin):

    def __init__(self):
        super().__init__('logs/')

    def setup_debug(self):
        self.debugs.append(Folder('/var/log'))
