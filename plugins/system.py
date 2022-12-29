from .base import Plugin, Command
from .utils import run


class System(Plugin):

    def __init__(self):
        super().__init__('system/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('uptime', run, 'uptime'))
        self.debug_commands.append(Command('date', run, 'date'))
        self.debug_commands.append(Command('ntpq -c rv', run, 'ntpq -c rv'))
        self.debug_commands.append(Command('ntpq -pwn', run, 'ntpq -pwn'))
        self.debug_commands.append(Command('ps -auxwwf', run, 'ps -auxwwf'))
        self.debug_commands.append(Command('mount', run, 'mount'))
        self.debug_commands.append(Command('df -T -h', run, 'df -T -h'))
        self.debug_commands.append(Command('swapon -s', run, 'swapon -s'))
        self.debug_commands.append(Command('lsmod', run, 'lsmod'))
        self.debug_commands.append(Command('dmesg', run, 'dmesg'))
        self.debug_commands.append(Command('vmstat', run, 'vmstat'))
        self.debug_commands.append(Command('hactl', run, 'hactl'))

