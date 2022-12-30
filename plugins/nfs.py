from .base import Plugin
from .debug_types import Command
from .utils import run


class Nfs(Plugin):

    def __init__(self):
        super().__init__('nfs/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('nfs service status ', run, 'systemctl status nfs-server'))
        self.debugs.append(Command('rpc-statd service status', run, 'systemctl status rpc-statd'))
        self.debugs.append(Command('rpc-gssd service status', run, 'systemctl status rpc-gssd'))
        self.debugs.append(Command('rpcinfo', run, 'rpcinfo -p'))
        self.debugs.append(Command('/etc/default/nfs-common', run, 'cat /etc/default/nfs-common'))
        self.debugs.append(Command('/etc/default/nfs-kernel-serve', run, 'cat /etc/default/nfs-kernel-serve'))
        self.debugs.append(Command('/etc/exports', run, 'cat /etc/exports'))
