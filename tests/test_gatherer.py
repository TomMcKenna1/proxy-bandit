from proxybandit import Gatherer

def test_gather():
    gatherer = Gatherer()
    proxy_list = gatherer.gather()
    assert len(proxy_list) > 0