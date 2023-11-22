import csv

from .proxy import Proxy


class ProxyList:
    def __init__(self, proxy_list: list[Proxy]):
        self._index = 0
        self._list = proxy_list

    def __iter__(self):
        return iter(self._list)

    def __getitem__(self, item: int) -> Proxy:
        return self._list[item]
    
    def __len__(self) -> int:
        return len(self._list)

    def to_csv(self, path):
        with open(path, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",")
            for proxy in self._list:
                csv_writer.writerow(
                    [
                        proxy.type,
                        proxy.host,
                        proxy.port,
                        proxy.privacy,
                        proxy.origin,
                        proxy.speed,
                    ]
                )

    def add(self, proxy: Proxy) -> None:
        self.list.append(proxy)

    def remove(self, id: int) -> Proxy:
        pass

    def clean(self) -> None:
        # Will be used to remove proxies that no longer work
        pass
