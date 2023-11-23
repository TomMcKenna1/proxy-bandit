import pytest

from proxybandit import Proxy

proxy_types = [Proxy.TYPE_HTTP, Proxy.TYPE_HTTPS, Proxy.TYPE_SOCKS5]


@pytest.mark.parametrize("proxy_type", proxy_types)
def test_to_string(proxy_type):
    proxy = Proxy("1.1.1.1", "80", proxy_type)
    expected_proxy_strings = {
        Proxy.TYPE_HTTP: "http://1.1.1.1:80",
        Proxy.TYPE_HTTPS: "https://1.1.1.1:80",
        Proxy.TYPE_SOCKS5: "socks5://1.1.1.1:80",
    }
    assert str(proxy) == expected_proxy_strings[proxy_type]


@pytest.mark.parametrize("proxy_type", proxy_types)
def test_to_dict(proxy_type):
    proxy = Proxy("1.1.1.1", "80", proxy_type)
    proxy_dict = proxy.to_dict()
    expected_proxy_dicts = {
        Proxy.TYPE_HTTP: {"http": f"http://1.1.1.1:80"},
        Proxy.TYPE_HTTPS: {"http": f"http://1.1.1.1:80", "https": f"http://1.1.1.1:80"},
        Proxy.TYPE_SOCKS5: {
            "http": f"socks5://1.1.1.1:80",
            "https": f"socks5://1.1.1.1:80",
        },
    }
    assert proxy_dict == expected_proxy_dicts[proxy_type]
