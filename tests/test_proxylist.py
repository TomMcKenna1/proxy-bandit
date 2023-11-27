import os
import csv

from proxybandit import Proxy, ProxyList


def test_to_csv():
    test_data = [
        Proxy("1.1.1.1", "1"),
        Proxy("1.1.1.1", "2"),
        Proxy("1.1.1.1", "3"),
    ]
    expected_output = [
        ["0", "1.1.1.1", "1", "0", "", "1.0"],
        ["0", "1.1.1.1", "2", "0", "", "1.0"],
        ["0", "1.1.1.1", "3", "0", "", "1.0"],
    ]
    test_proxy_list = ProxyList(test_data)
    test_proxy_list.to_csv("__test_to_csv.csv")
    try:
        with open("__test_to_csv.csv", "r") as file:
            csv_reader = csv.reader(file)
            assert expected_output == list(csv_reader)
    finally:
        os.remove("__test_to_csv.csv")
