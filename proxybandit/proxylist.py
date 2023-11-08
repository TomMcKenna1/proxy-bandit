from .proxy import Proxy

class ProxyList():

    def __init__(self, proxy_list):
        self._index = 0
        self._list = proxy_list
    
    def __iter__(self):
        return iter(self._list)

    def to_csv(self, path):
        pass

    def add(self, proxy: Proxy) -> None:
        self.list.append(proxy)

    def remove(self, id: int) -> Proxy:
        pass
    
    def clean(self) -> None:
        # Will be used to remove proxies that no longer work
        pass