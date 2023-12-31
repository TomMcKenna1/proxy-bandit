from heapq import heapify, heappush, heappop

from .gatherer import Gatherer
from .proxy import Proxy


class InvalidProxyPriority(Exception):
    pass


class ProxyBandit:
    def __init__(self, prioritise="speed"):
        if prioritise not in Proxy.ATTRIBUTES:
            base_error_message = f"Proxy does not have any attribute named `{prioritise}`. Please choose one of: "
            raise InvalidProxyPriority(base_error_message + ", ".join(Proxy.ATTRIBUTES))
        self.gatherer = Gatherer()
        self._unused_proxies = [
            (getattr(proxy, prioritise), proxy) for proxy in self.gatherer.gather()
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
