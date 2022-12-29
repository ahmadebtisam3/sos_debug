from .base import Plugin, Command
from .utils import run


class sysctl(Plugin):

    def __init__(self):
        super().__init__('sysctl/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('/etc/sysctl.conf', run, 'cat /etc/sysctl.conf'))
        self.debug_commands.append(Command('systcl values', run, 'sysctl -a'))

