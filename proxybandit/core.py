from .gatherer import Gatherer
from .tester import Tester


class ProxyBandit:
    def __init__(self):
        self.gatherer = Gatherer()
        self.tester = Tester()
        self.untested_proxy_list = self.gatherer.gather()

    def getProxy(self):
        # Currently test logic
        return self.untested_proxy_list[0]
