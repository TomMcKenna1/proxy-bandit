import os
import re
import json
import asyncio

import aiohttp
from bs4 import BeautifulSoup, SoupStrainer
# This is used as the parser for bs4
import lxml

from .core import Proxy

class Gatherer:

    def __init__(self):
        base_filepath = os.path.join(os.path.dirname(__file__), 'data')
        with open(os.path.join(base_filepath, 'sources.json')) as f:
            self.source_list = json.load(f)
        self.anti_bot_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }

    async def _get(self, session, url):
        async with session.get(url) as http_response:
            return await http_response.read()

    async def _gather_proxy_sources(self, **kwargs):
        async with aiohttp.ClientSession(**kwargs) as session:
            http_response_futures = []
            for source in self.source_list:
                http_response_futures.append(asyncio.ensure_future(self._get(session, source.get("url"))))
            html_responses = await asyncio.gather(*http_response_futures)
            return html_responses

    def find_table_rows(self, raw_sources):
        table_rows = []
        soup_strainer = SoupStrainer('tbody')
        for source in raw_sources:
            source_soup = BeautifulSoup(source, "lxml", parse_only=soup_strainer)
            table_rows += source_soup.findAll('tr')
        return table_rows

    def get_host(self, raw):
        matches = re.search(
            r">[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}<",
            raw,
            flags=0
        )
        if matches:
            return matches.group(0)
        return None
    
    def get_port(self, raw):
        matches = re.search(
            r">\d{1,5}<",
            raw,
            flags=0
        )
        if matches:
            return matches.group(0)
        return None

    def gather(self):
        raw_sources = asyncio.run(self._gather_proxy_sources(headers=self.anti_bot_headers))
        raw_proxies = self.find_table_rows(raw_sources)
        proxy_list = {
            host[1:-1]+":"+port[1:-1] 
            for raw in raw_proxies
            if (str_raw := ''.join(str(raw).split())) and
            (host := self.get_host(str_raw)) and 
            (port := self.get_port(str_raw))
        }
        print(proxy_list)
        print(len(proxy_list))
        return proxy_list