from .base import Plugin, Command
from .utils import run


class smb(Plugin):

    def __init__(self):
        super().__init__('smb/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('smb version', run, 'smbd -V'))
        self.debug_commands.append(Command('/etc/smb4.conf', run, 'cat /etc/smb4.conf'))
        self.debug_commands.append(Command('global configuration for SMB', run, 'net conf showshare global'))
        self.debug_commands.append(Command('SAMBA build information', run, 'smbd -b'))
        self.debug_commands.append(Command('SAMBA configuration files', run, 'testparm -s'))
        self.debug_commands.append(Command('SID of the local server', run, 'net getlocalised'))
        self.debug_commands.append(Command(' SID of the current domain', run, 'net getdomainsid'))
        self.debug_commands.append(Command('net status sessions', run, 'net status sessions | head -50'))
        self.debug_commands.append(Command('net status shares', run, 'net status shares'))
        self.debug_commands.append(Command('locks information', run, 'smbstatus -L | head -50'))
