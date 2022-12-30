from .base import Plugin
from .debug_types import Command
from .utils import run


class Ldap(Plugin):

    def __init__(self):
        super().__init__('ldap/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('/etc/nsswitch.conf', run, 'cat /etc/nsswitch.conf'))
        self.debugs.append(Command('/etc/krb5.conf', run, '/etc/krb5.conf'))
        self.debugs.append(Command('keytab system', run, 'klist -ket'))
        self.debugs.append(Command('/etc/openldap/ldap.conf', run, 'cat /etc/openldap/ldap.conf'))
        self.debugs.append(Command('/etc/nslcd.conf', run, 'cat /etc/nslcd.conf'))
