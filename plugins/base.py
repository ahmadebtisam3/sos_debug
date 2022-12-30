import shutil
import os

from .exception import DebugException


class Debugs:

    def write_debug(self, folder_path, file_path) -> None:
        os.makedirs(folder_path, exist_ok=True)

    def validate(self):
        return True


class Command(Debugs):

    def __init__(self, title, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.title = title

    def write_debug(self, folder_path, file_path) -> None:
        super().write_debug(folder_path, file_path)
        output = self.callback(*self.args, **self.kwargs)
        with open(os.path.join(folder_path, file_path), 'a') as wr:
            wr.write(self.title + '************************************ \n')
            wr.write(output + '\n')

    def get_command_title(self):
        return self.title


class File(Debugs):

    def __init__(self, source_path):
        self.src_path = source_path

    def validate(self):
        return os.path.isfile(self.src_path)

    def write_debug(self, folder_path, file_path):
        super().write_debug(folder_path, file_path)
        shutil.copy(self.src_path, folder_path)


class Folder(Debugs):

    def __init__(self, source_path):
        self.src_path = source_path

    def validate(self):
        return os.path.isdir(self.src_path)

    def write_debug(self, folder_path, file_path):
        shutil.copytree(self.src_path, folder_path)


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
