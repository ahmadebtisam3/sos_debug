import shutil
import os

from .exception import DebugException


class Command:

    def __init__(self, title, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.title = title

    def execute(self) -> str:
        return self.callback(*self.args, **self.kwargs)

    def get_command_title(self):
        return self.title


class File:

    def __init__(self, source_path):
        self.source_path = source_path

    def valid_file(self):
        return os.path.isfile(self.source_path)

    @property
    def source_path(self):
        return self.source_path

class Plugin:

    def __init__(self, basedir=''):
        self.debug_commands = []
        self.debug_files = []
        self.basedir = basedir

    def setup_debug(self):
        NotImplemented

    def process_debug(self):
        for debug_command in self.debug_commands:
            if not isinstance(debug_command, Command):
                raise DebugException('Debug must be a list of command')
        for debug_file in self.debug_files:
            if (not isinstance(debug_file, File)) or (isinstance(debug_file, File) and not debug_file.valid_file()):
                raise DebugException('Invalid file path defined.')

    def generate_debug(self, parent_path):
        self.setup_debug()
        self.process_debug()
        complete_path = os.path.join(parent_path, self.basedir)
        for debug_command in self.debug_commands:
            os.makedirs(os.path.dirname(complete_path), exist_ok=True)
            with open(complete_path, 'a') as wr:
                wr.write(debug_command.get_command_title() + '************************************ \n')
                if debug_output := debug_command.execute():
                    wr.write(debug_output + '\n')
        for debug_file in self.debug_files:
            shutil.copy(debug_file.source_path, os.path.join(complete_path, os.path.basename(debug_file.source_path)))
