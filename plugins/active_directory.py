from .base import Plugin, Command
from .utils import run


class ActiveDirectory(Plugin):

    def __init__(self):
        super().__init__('activate_directory/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('service winbind status', run, 'service winbind status'))
        self.debugs.append(Command('cat /etc/smb4.conf', run, 'cat /etc/smb4.conf'))
        self.debugs.append(Command('cat /etc/nsswitch.conf', run, 'cat /etc/nsswitch.conf'))
        self.debugs.append(Command('klist', run, 'klist'))
