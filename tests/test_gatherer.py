import pytest

from proxybandit import Gatherer

def test_gatherer():
    gatherer = Gatherer()
    print(gatherer.gather())