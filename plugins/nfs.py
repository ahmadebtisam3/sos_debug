from .base import Plugin, Command
from .utils import run


class Nfs(Plugin):

    def __init__(self):
        super().__init__('nfs/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('nfs service status ', run, 'systemctl status nfs-server'))
        self.debug_commands.append(Command('rpc-statd service status', run, 'systemctl status rpc-statd'))
        self.debug_commands.append(Command('rpc-gssd service status', run, 'systemctl status rpc-gssd'))
        self.debug_commands.append(Command('rpcinfo', run, 'rpcinfo -p'))
        self.debug_commands.append(Command('/etc/default/nfs-common', run, 'cat /etc/default/nfs-common'))
        self.debug_commands.append(Command('/etc/default/nfs-kernel-serve', run, 'cat /etc/default/nfs-kernel-serve'))
        self.debug_commands.append(Command('/etc/exports', run, 'cat /etc/exports'))
