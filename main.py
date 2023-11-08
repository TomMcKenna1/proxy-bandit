import argparse
from proxybandit import ProxyBandit

if __name__ == "__main__":
    proxyClient = ProxyBandit()
    proxyClient.getProxy()
