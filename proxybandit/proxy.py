class Proxy:

    __count = 0
    PRIVACY_TRANSPARENT = 0
    PRIVACY_ANONYMOUS = 1
    PRIVACY_ELITE = 2
    TYPE_HTTP = 0
    TYPE_SOCKS4 = 1
    TYPE_SOCKS5 = 2

    def __init__(
        self,
        type: int,
        host: str,
        port: int,
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