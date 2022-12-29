from .base import Plugin, Command
from .utils import run


class Zfs(Plugin):

    def __init__(self):
        super().__init__('zfs/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('list zpool', run, 'zpool list -v'))
        self.debug_commands.append(Command('zfs list', run, 'zfs list -ro space,refer,mountpoint'))
        self.debug_commands.append(Command('pool status', run, 'zpool status -v'))
        self.debug_commands.append(Command('pool history', run, 'zpool history'))
        self.debug_commands.append(Command('zpool get all', run, 'zpool get all'))
        self.debug_commands.append(Command('snapshot', run, 'zfs list -t snapshot -o name,used,available,'
                                                            'referenced,mountpoint,freenas:state'))
