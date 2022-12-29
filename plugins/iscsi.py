from .base import Plugin, Command
from .utils import run


class ISCSI(Plugin):

    def __init__(self):
        super().__init__('iscsi/dump')

    def setup_debug(self):
        self.debug_commands.append(Command('iscsi service status', run, 'systemctl status scst'))
        self.debug_commands.append(Command('Lists SCST device handlers', run, 'scstadmin -list_handler'))
        self.debug_commands.append(Command('Lists SCST devices.', run, 'scstadmin -list_device'))
        self.debug_commands.append(Command('Lists SCST drivers.', run, 'scstadmin -list_driver'))
        self.debug_commands.append(Command('Lists SCST targets.', run, 'scstadmin -list_target -driver iscsi'))
        self.debug_commands.append(Command('Lists SCST active sessions.', run, 'scstadmin -list-sessions'))
        self.debug_commands.append(Command('Lists SCST core attributes', run, 'scst -list_scst_attr'))
        self.debug_commands.append(Command('/etc/ctl.conf.shadow.', run, 'cat /etc/ctl.conf.shadow'))
