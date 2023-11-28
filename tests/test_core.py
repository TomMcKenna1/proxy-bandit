from proxybandit import ProxyBandit, Proxy


def test_get_proxy():
    proxy_supplier = ProxyBandit()
    proxy = proxy_supplier.get_proxy()
    assert isinstance(proxy, Proxy)
