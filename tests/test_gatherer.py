import pytest

from proxybandit import Gatherer

def test_gatherer():
    gatherer = Gatherer()
    proxy_list = gatherer.gather()
    for proxy in proxy_list:
        print(proxy)