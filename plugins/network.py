from .base import Plugin, Command
from .utils import run


class Network(Plugin):

    def __init__(self):
        super().__init__('network/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('hostname ', run, 'hostname'))
        self.debugs.append(Command('/etc/hosts', run, 'cat /etc/hosts'))
        self.debugs.append(Command('/etc/resolve.conf', run, 'cat /etc/resolve.conf'))
        self.debugs.append(Command('output default route.', run,
                                   "ip route show default | awk '/default/ {print $3}'"))
        self.debugs.append(Command('routing table', run, 'netstat -nrW'))
        self.debugs.append(Command('Ip routes', run, 'ip route show table all'))
        self.debugs.append(Command('ip rules', run, 'ip rule list'))
        self.debugs.append(Command('iptables rules.', run, 'iptables-save -c'))
        self.debugs.append(Command('Nftables ruleset', run, 'nft -a list ruleset'))
        self.debugs.append(Command(' IPVS rules', run, 'ipvsadm -L'))
        self.debugs.append(Command('IPSET rules', run, 'ipset --list'))
        self.debugs.append(Command('ARP entries', run, 'arp -an'))

