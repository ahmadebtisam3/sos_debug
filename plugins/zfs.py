from .base import Plugin
from .debug_types import Command
from .utils import run


class Zfs(Plugin):

    def __init__(self):
        super().__init__('zfs/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('list zpool', run, 'zpool list -v'))
        self.debugs.append(Command('zfs list', run, 'zfs list -ro space,refer,mountpoint'))
        self.debugs.append(Command('pool status', run, 'zpool status -v'))
        self.debugs.append(Command('pool history', run, 'zpool history'))
        self.debugs.append(Command('zpool get all', run, 'zpool get all'))
        self.debugs.append(Command('snapshot', run, 'zfs list -t snapshot -o name,used,available,'
                                                    'referenced,mountpoint,freenas:state'))
