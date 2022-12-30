import os
import shutil


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
