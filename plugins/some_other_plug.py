from .base import Plugin


class SomeOtherDebug(Plugin):

    def setup_debug(self):
        print("in somesetup")
        self.debug['some_debug/dump.txt'] = '/home/ibtisam/test_summary.txt'
