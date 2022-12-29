import errno


class DebugException(Exception):
    def __init__(self, error_msg, error_no=errno.EFAULT):
        self.errmsg = error_msg
        self.errno = error_no

    def get_error_name(self):
        return errno.errorcode.get(self.errno) or 'EUNKNOWN'

    def __str__(self):
        return f'[{self.get_error_name()}] {self.errmsg}'
