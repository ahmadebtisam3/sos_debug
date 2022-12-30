from .base import Plugin
from .debug_types import Command
from .utils import run


class Kubernetes(Plugin):

    def __init__(self):
        super().__init__('kubernetes/', 'dump')

    def setup_debug(self):
        self.debugs.append(Command('k3s logs', run, 'journalctl -u k3s | tail -n 1000'))
        self.debugs.append(Command('k3s nodes', run, 'k3s kubectl describe nodes'))
        self.debugs.append(Command('k3s resources', run,
                                   'k3s kubectl get pods,svc,daemonsets,deployments,statefulset,sc,pvc,ns,'
                                   'job --all-namespaces -o wide'))
        self.debugs.append(Command('k3s deployments.', run,
                                   'k3s kubectl describe deployments --all-namespaces'))
        self.debugs.append(Command('k3s pods', run, 'k3s kubectl describe pods --all-namespaces'))
        self.debugs.append(Command('k3s services.', run, 'k3s kubectl describe services --all-namespaces'))
        self.debugs.append(Command('k3s cronjob', run, 'k3s kubectl describe cronjob --all-namespaces'))
        self.debugs.append(Command('k3s daemonset.', run,
                                   'k3s kubectl describe daemonsets --all-namespaces'))
