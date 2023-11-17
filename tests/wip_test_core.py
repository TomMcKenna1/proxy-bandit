from proxybandit import ProxyBandit

def test_proxybandit():
    proxy_supplier = ProxyBandit()
    print(proxy_supplier.getProxy())