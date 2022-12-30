from .base import Plugin
from .debug_types import Command
from .utils import run


class ISCSI(Plugin):

    def __init__(self):
        super().__init__('iscsi/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('iscsi service status', run, 'systemctl status scst'))
        self.debugs.append(Command('Lists SCST device handlers', run, 'scstadmin -list_handler'))
        self.debugs.append(Command('Lists SCST devices.', run, 'scstadmin -list_device'))
        self.debugs.append(Command('Lists SCST drivers.', run, 'scstadmin -list_driver'))
        self.debugs.append(Command('Lists SCST targets.', run, 'scstadmin -list_target -driver iscsi'))
        self.debugs.append(Command('Lists SCST active sessions.', run, 'scstadmin -list-sessions'))
        self.debugs.append(Command('Lists SCST core attributes', run, 'scst -list_scst_attr'))
        self.debugs.append(Command('/etc/ctl.conf.shadow.', run, 'cat /etc/ctl.conf.shadow'))
