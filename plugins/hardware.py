from .base import Plugin, Command
from .utils import run


class Hardware(Plugin):

    def __init__(self):
        super().__init__('hardware/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('host machine name', run, 'uname -m'))
        self.debug_commands.append(Command('cpu Info', run,
                                           "lscpu | grep 'Model name' | cut -d ':' -f 2 | sed -e 's/^{{:space:}}*//'"))
        self.debug_commands.append(Command('number of active CPUs.', run, 'grep -c "model name" /proc/cpuinfo'))
        self.debug_commands.append(Command('number of CPUs online', run, 'lscpu -p=online | grep "^#" | grep -c "y"'))
        self.debug_commands.append(Command('PCI info', run, 'lspci -vvvD'))
        self.debug_commands.append(Command('USB devices info', run, 'cat /sys/kernel/debug/usb/devices'))
        self.debug_commands.append(Command('hardware related information', run, 'dmidecode'))
        self.debug_commands.append(Command('list all available block devices', run,
                                           'lsblk -o NAME,ALIGNMENT,MIN-IO,OPT-IO'
                                           ',PHY-SEC,LOG-SEC,ROTA,SCHED,RQ-SIZE,RA,WSAME,HCTL,PATH'))
        self.debug_commands.append(Command('Outputs the sensors available', run, 'sensors -j'))
