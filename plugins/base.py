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


class Plugin:

    def __init__(self):
        self.debug = {}

    def setup_debug(self):
        NotImplemented

    def process_debug(self):
        for path, debug in self.debug.items():
            if path[0] == '/' or path[-1] == '/':
                raise DebugException('Invalid Path: relative path is required and it should be a file')
            if not isinstance(debug, Command) and not isinstance(debug, str):
                raise DebugException('Debug must command or a file')
            if isinstance(debug, str) and not os.path.isfile(debug):
                raise DebugException('Debug must be a valid file')

    def generate_debug(self, parent_path):
        self.setup_debug()
        self.process_debug()
        for path, debug in self.debug.items():
            complete_path = os.path.join(parent_path, path)
            os.makedirs(os.path.dirname(complete_path), exist_ok=True)
            if isinstance(debug, Command):
                with open(complete_path, 'w') as wr:
                    wr.write(debug.get_command_title() + '\n')
                    if debug_output := debug.execute():
                        wr.write(debug_output + '\n')
            else:
                shutil.copy(debug, complete_path)
