from heapq import heapify, heappush, heappop

from .gatherer import Gatherer
from .tester import Tester
from .proxy import Proxy


class InvalidProxyPriority(Exception):
    pass


class ProxyBandit:
    def __init__(self, prioritise="speed"):
        if prioritise not in Proxy.ATTRIBUTES:
            base_error_message = f"Proxy does not have any attribute named `{prioritise}`. Please choose one of: "
            valid_attr = [
                f"{attribute}, " if i < len(Proxy.ATTRIBUTES) - 1 else f"{attribute}"
                for i, attribute in enumerate(Proxy.ATTRIBUTES)
            ]
            raise InvalidProxyPriority(base_error_message + "".join(valid_attr))
        self.gatherer = Gatherer()
        self.tester = Tester()
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
