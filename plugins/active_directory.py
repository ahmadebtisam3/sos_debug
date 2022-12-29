from .base import Plugin, Command
from .utils import run


class ActiveDirectory(Plugin):

    def __init__(self):
        super().__init__('activate_directory/activedirectory')

    def setup_debug(self):
        self.debug_commands.append(Command('service winbind status', run, 'service winbind status'))
        self.debug_commands.append(Command('cat /etc/smb4.conf', run, 'cat /etc/smb4.conf'))
        self.debug_commands.append(Command('cat /etc/nsswitch.conf', run, 'cat /etc/nsswitch.conf'))
        self.debug_commands.append(Command('klist', run, 'klist'))
