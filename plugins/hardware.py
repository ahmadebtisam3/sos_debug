from .base import Plugin
from .debug_types import Command
from .utils import run


class Hardware(Plugin):

    def __init__(self):
        super().__init__('hardware/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('host machine name', run, 'uname -m'))
        self.debugs.append(Command('cpu Info', run,
                                   "lscpu | grep 'Model name' | cut -d ':' -f 2 | sed -e 's/^{{:space:}}*//'"))
        self.debugs.append(Command('number of active CPUs.', run, 'grep -c "model name" /proc/cpuinfo'))
        self.debugs.append(Command('number of CPUs online', run, 'lscpu -p=online | grep "^#" | grep -c "y"'))
        self.debugs.append(Command('PCI info', run, 'lspci -vvvD'))
        self.debugs.append(Command('USB devices info', run, 'cat /sys/kernel/debug/usb/devices'))
        self.debugs.append(Command('hardware related information', run, 'dmidecode'))
        self.debugs.append(Command('list all available block devices', run,  'lsblk -o NAME,ALIGNMENT,MIN-IO,OPT-IO'
                                   ',PHY-SEC,LOG-SEC,ROTA,SCHED,RQ-SIZE,RA,WSAME,HCTL,PATH'))
        self.debugs.append(Command('Outputs the sensors available', run, 'sensors -j'))
