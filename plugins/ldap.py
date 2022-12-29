from .base import Plugin, Command
from .utils import run


class Ldap(Plugin):

    def __init__(self):
        super().__init__('ldap/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('/etc/nsswitch.conf', run, 'cat /etc/nsswitch.conf'))
        self.debug_commands.append(Command('/etc/krb5.conf', run, '/etc/krb5.conf'))
        self.debug_commands.append(Command('keytab system', run, 'klist -ket'))
        self.debug_commands.append(Command('/etc/openldap/ldap.conf', run, 'cat /etc/openldap/ldap.conf'))
        self.debug_commands.append(Command('/etc/nslcd.conf', run, 'cat /etc/nslcd.conf'))
