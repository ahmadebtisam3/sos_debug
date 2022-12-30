from .base import Plugin, Command
from .utils import run


class sysctl(Plugin):

    def __init__(self):
        super().__init__('sysctl/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('/etc/sysctl.conf', run, 'cat /etc/sysctl.conf'))
        self.debugs.append(Command('systcl values', run, 'sysctl -a'))

