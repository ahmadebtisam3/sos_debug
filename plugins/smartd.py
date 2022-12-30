from .base import Plugin
from .debug_types import Command
from .utils import run


class smartd(Plugin):

    def __init__(self):
        super().__init__('smartd/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('smartd service status ', run, 'systemctl status smartd'))
