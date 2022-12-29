import shutil
import tempfile
import os.path


def generate_debug_report(plugins_objs: list):
    debug_folder = tempfile.mkdtemp(prefix="some-debugs-")
    for obj in plugins_objs:
        obj.generate_debug(debug_folder)
    shutil.make_archive(os.path.basename(debug_folder), 'zip', debug_folder)
    return debug_folder
