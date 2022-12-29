from .base import Plugin, Command
from .utils import run


class smartd(Plugin):

    def __init__(self):
        super().__init__('smartd/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('smartd service status ', run, 'systemctl status smartd'))
