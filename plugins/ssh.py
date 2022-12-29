from .base import Plugin, Command
from .utils import run


class ssh(Plugin):

    def __init__(self):
        super().__init__('ssh/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('/etc/ssl file and outputs', run, 'find /etc/ssl -print0 | xargs -0 ls -l'))
        self.debug_commands.append(Command('/etc/certificates', run, 'find /etc/certificates -print0 | xargs -0 ls -l'))
        self.debug_commands.append(Command('/etc/ssl/openssl.cnf', run, 'cat /etc/ssl/openssl.cnf'))

