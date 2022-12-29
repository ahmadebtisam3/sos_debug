from .base import Plugin, Command
from .utils import run


class Network(Plugin):

    def __init__(self):
        super().__init__('network/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('hostname ', run, 'hostname'))
        self.debug_commands.append(Command('/etc/hosts', run, 'cat /etc/hosts'))
        self.debug_commands.append(Command('/etc/resolve.conf', run, 'cat /etc/resolve.conf'))
        self.debug_commands.append(Command('output default route.', run,
                                           "ip route show default | awk '/default/ {print $3}'"))
        self.debug_commands.append(Command('routing table', run, 'netstat -nrW'))
        self.debug_commands.append(Command('Ip routes', run, 'ip route show table all'))
        self.debug_commands.append(Command('ip rules', run, 'ip rule list'))
        self.debug_commands.append(Command('iptables rules.', run, 'iptables-save -c'))
        self.debug_commands.append(Command('Nftables ruleset', run, 'nft -a list ruleset'))
        self.debug_commands.append(Command(' IPVS rules', run, 'ipvsadm -L'))
        self.debug_commands.append(Command('IPSET rules', run, 'ipset --list'))
        self.debug_commands.append(Command('ARP entries', run, 'arp -an'))

