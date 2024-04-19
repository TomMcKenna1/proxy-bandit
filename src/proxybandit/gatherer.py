import os
import re
import json
import asyncio

import aiohttp
from bs4 import BeautifulSoup, SoupStrainer, Tag

# This is used as the parser for bs4
import lxml

from .proxy import Proxy
from .proxylist import ProxyList


class Gatherer:
    def __init__(self) -> None:
        base_filepath = os.path.join(os.path.dirname(__file__), "data")
        with open(os.path.join(base_filepath, "sources.json")) as f:
            self._source_list = json.load(f)
        self._anti_bot_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }

    async def _get(self, session, url):
        async with session.get(url) as http_response:
            return await http_response.read()

    async def _gather_proxy_sources(self, **kwargs) -> list[bytes]:
        async with aiohttp.ClientSession(**kwargs) as session:
            http_response_futures = []
            for source in self._source_list:
                http_response_futures.append(
                    asyncio.ensure_future(self._get(session, source.get("url")))
                )
            html_responses = await asyncio.gather(*http_response_futures)
            return html_responses

    def _find_table_rows(self, raw_sources) -> list[Tag]:
        table_rows = []
        soup_strainer = SoupStrainer("tbody")
        for source in raw_sources:
            source_soup = BeautifulSoup(source, "lxml", parse_only=soup_strainer)
            table_rows += source_soup.findAll("tr")
        return table_rows

    def _get_first_regex_match(self, raw, regex) -> str | None:
        matches = re.search(regex, raw, flags=0)
        if matches:
            return matches.group(0)
        return None

    def _extract_proxies(self, raw_proxies) -> list[Proxy]:
        seen = set()
        proxy_list = []
        for raw_proxy in raw_proxies:
            zero_whitespace_raw_proxy = "".join(str(raw_proxy).split())
            host = self._get_first_regex_match(
                zero_whitespace_raw_proxy,
                r">[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}<",
            )
            port = self._get_first_regex_match(zero_whitespace_raw_proxy, r">\d{1,5}<")
            if not (host and port):
                continue
            f_host = host[1:-1]
            f_port = port[1:-1]
            f_proxy = f_host + ":" + f_port
            if f_proxy in seen:
                continue
            seen.add(f_proxy)
            proxy = Proxy(f_host, f_port)
            proxy_list.append(proxy)
        return proxy_list

    def gather(self) -> ProxyList:
        raw_sources = asyncio.run(
            self._gather_proxy_sources(headers=self._anti_bot_headers)
        )
        raw_proxies = self._find_table_rows(raw_sources)
        proxy_list = self._extract_proxies(raw_proxies)
        return ProxyList(proxy_list)
