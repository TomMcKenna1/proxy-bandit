from heapq import heapify, heappush, heappop

from .gatherer import Gatherer
from .tester import Tester


class ProxyBandit:
    def __init__(self):
        self.gatherer = Gatherer()
        self.tester = Tester()
        self._unused_proxies = [
            (proxy.speed, proxy) for proxy in self.gatherer.gather()
        ]
        heapify(self._unused_proxies)
        self._used_proxies = []

    def get_proxy(self):
        if not self._unused_proxies:
            self._unused_proxies = self._used_proxies
            self._used_proxies = []
        speed, proxy = heappop(self._unused_proxies)
        heappush(self._used_proxies, (speed, proxy))
        return proxy
