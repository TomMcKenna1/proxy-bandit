import os
import json
import asyncio

import aiohttp
import lxml
from bs4 import BeautifulSoup, SoupStrainer

from .core import Proxy

class Gatherer:

    def __init__(self):
        base_filepath = os.path.dirname(__file__)
        data_directory = os.path.join(base_filepath, 'data')
        with open(os.path.join(data_directory, 'sources.json')) as f:
            self.source_list = json.load(f)
        self.proxies = []
        self.anti_bot_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }

    async def _get_proxy_list(self, session, proxy_list_url):
        async with session.get(proxy_list_url) as proxy_list_response:
            return await proxy_list_response.read()

    async def _gather_proxy_lists(self, **kwargs):
        async with aiohttp.ClientSession(**kwargs) as session:
            html_response_futures = []
            for proxy_source in self.source_list:
                html_response_futures.append(asyncio.ensure_future(self._get_proxy_list(session, proxy_source.get("url"))))
            html_responses = await asyncio.gather(*html_response_futures)
            return html_responses

    def find_table_rows(self, raw_sources):
        table_rows = []
        soup_strainer = SoupStrainer('tbody')
        for source in raw_sources:
            source_soup = BeautifulSoup(source, "lxml", parse_only=soup_strainer)
            table_rows += source_soup.findAll('tr')
        return table_rows

    def gather(self):
        raw_sources = asyncio.run(self._gather_proxy_lists(headers=self.anti_bot_headers))
        raw_proxies = self.find_table_rows(raw_sources)
        print(raw_proxies)