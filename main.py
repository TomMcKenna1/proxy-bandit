import argparse
from proxybandit import ProxyBandit

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(
        prog='ProxyBandit',
        description='A fast and feature rich proxy manager.'
    )
    proxyClient = ProxyBandit()
    proxyClient.getProxy()
