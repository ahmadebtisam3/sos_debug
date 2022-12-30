from .base import Plugin
from .debug_types import Command
from .utils import run


class System(Plugin):

    def __init__(self):
        super().__init__('system/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('uptime', run, 'uptime'))
        self.debugs.append(Command('date', run, 'date'))
        self.debugs.append(Command('ntpq -c rv', run, 'ntpq -c rv'))
        self.debugs.append(Command('ntpq -pwn', run, 'ntpq -pwn'))
        self.debugs.append(Command('ps -auxwwf', run, 'ps -auxwwf'))
        self.debugs.append(Command('mount', run, 'mount'))
        self.debugs.append(Command('df -T -h', run, 'df -T -h'))
        self.debugs.append(Command('swapon -s', run, 'swapon -s'))
        self.debugs.append(Command('lsmod', run, 'lsmod'))
        self.debugs.append(Command('dmesg', run, 'dmesg'))
        self.debugs.append(Command('vmstat', run, 'vmstat'))
        self.debugs.append(Command('hactl', run, 'hactl'))

