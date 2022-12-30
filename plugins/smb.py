from .base import Plugin, Command
from .utils import run


class smb(Plugin):

    def __init__(self):
        super().__init__('smb/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('smb version', run, 'smbd -V'))
        self.debugs.append(Command('/etc/smb4.conf', run, 'cat /etc/smb4.conf'))
        self.debugs.append(Command('global configuration for SMB', run, 'net conf showshare global'))
        self.debugs.append(Command('SAMBA build information', run, 'smbd -b'))
        self.debugs.append(Command('SAMBA configuration files', run, 'testparm -s'))
        self.debugs.append(Command('SID of the local server', run, 'net getlocalised'))
        self.debugs.append(Command(' SID of the current domain', run, 'net getdomainsid'))
        self.debugs.append(Command('net status sessions', run, 'net status sessions | head -50'))
        self.debugs.append(Command('net status shares', run, 'net status shares'))
        self.debugs.append(Command('locks information', run, 'smbstatus -L | head -50'))
