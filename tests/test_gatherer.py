from proxybandit import Gatherer, ProxyList

def test_gather():
    gatherer = Gatherer()
    proxy_list = gatherer.gather()
    assert isinstance(proxy_list, ProxyList)
    assert len(proxy_list) > 0