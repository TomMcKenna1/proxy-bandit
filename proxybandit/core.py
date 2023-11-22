from .gatherer import Gatherer
from .tester import Tester


class ProxyBandit:
    def __init__(self):
        self.gatherer = Gatherer()
        self.tester = Tester()
        self.untested_proxy_list = self.gatherer.gather()
        self._proxy_index = 0

    def get_proxy(self):
        current_index = self._proxy_index
        if current_index + 1 < len(self.untested_proxy_list):
            self._proxy_index += 1
        else:
            self._proxy_index = 0
        return self.untested_proxy_list[current_index]
