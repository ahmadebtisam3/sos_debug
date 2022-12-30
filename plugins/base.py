import os

from .exception import DebugException
from .debug_types import Debugs


class Plugin:

    def __init__(self, basedir='', file=''):
        self.debugs = []
        self.basedir = basedir
        self.file_path = file

    def setup_debug(self):
        NotImplemented

    def process_debug(self):
        for debug in self.debugs:
            if (not isinstance(debug, Debugs)) or (isinstance(debug, Debugs) and not debug.validate()):
                raise DebugException('Invalid debug Type')

    def generate_debug(self, parent_path):
        self.setup_debug()
        self.process_debug()
        dir_path = os.path.join(parent_path, self.basedir)
        for debug in self.debugs:
            debug.write_debug(dir_path, self.file_path)
