import pytest

from proxybandit import Proxy


def test_to_string():
    proxy = Proxy("1.1.1.1", "80")
    expected_proxy_string = "1.1.1.1:80"
    assert str(proxy) == expected_proxy_string


@pytest.mark.parametrize(
    "proxy_type", [Proxy.TYPE_HTTP, Proxy.TYPE_HTTPS, Proxy.TYPE_SOCKS5]
)
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
