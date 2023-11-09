import os

from proxybandit import Proxy, ProxyList

def test_to_csv():
    test_data = [
        Proxy("1.1.1.1","1"),
        Proxy("1.1.1.1","2"),
        Proxy("1.1.1.1","3"),
    ]
    test_proxy_list = ProxyList(test_data)
    test_proxy_list.to_csv('proxylist_test_to_csv.csv')
    os.remove('proxylist_test_to_csv.csv')