class Proxy:
    PRIVACY_TRANSPARENT = 0
    PRIVACY_ANONYMOUS = 1
    PRIVACY_ELITE = 2
    TYPE_HTTP = 0
    TYPE_HTTPS = 1
    TYPE_SOCKS5 = 2

    def __init__(
        self,
        host: str,
        port: int,
        type: int = TYPE_HTTP,
        privacy: int = PRIVACY_TRANSPARENT,
        speed: float = 1.0,
        origin=None,
    ):
        self.type = type
        self.host = host
        self.port = port
        self.privacy = privacy
        self.origin = origin
        self.speed = speed

    def __lt__(self, other):
        return str(self) < other

    def __gt__(self, other):
        return str(self) > other

    def __str__(self):
        prefix = "http://"
        if self.type == Proxy.TYPE_HTTPS:
            prefix = "https://"
        elif self.type == Proxy.TYPE_SOCKS5:
            prefix = "socks5://"
        return f"{prefix}{self.host}:{self.port}"

    def to_dict(self) -> dict[str, str]:
        proxy_dict = {"http": f"http://{self.host}:{self.port}"}
        if self.type == Proxy.TYPE_SOCKS5:
            proxy_dict["http"] = str(self)
            proxy_dict["https"] = str(self)
        if self.type == Proxy.TYPE_HTTPS:
            proxy_dict["https"] = f"http://{self.host}:{self.port}"
        return proxy_dict

    def to_url(self) -> str:
        return f"http://{self}"
