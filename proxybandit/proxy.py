class Proxy:

    __count = 0
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
        origin = None,
        speed = None
    ):
        self.id = Proxy.__count
        self.type = type
        self.host = host
        self.port = port
        self.privacy = privacy
        self.origin = origin
        self.speed = speed
        Proxy.__count += 1

    def __str__(self):
        return f"{self.host}:{self.port}"
    
    def to_dict(self) -> dict[str, str]:
        proxy_dict = {'http': f"http://{self}"}
        if self.type == Proxy.TYPE_SOCKS5:
            proxy_dict['http'] = f"socks5://{self}"
            proxy_dict['https'] = f"socks5://{self}"
        if self.type == Proxy.TYPE_HTTPS:
            proxy_dict['https'] = proxy_dict['http']
        return proxy_dict

    def to_url(self) -> str:
        return f"http://{self}"