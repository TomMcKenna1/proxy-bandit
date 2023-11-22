import asyncio

import aiohttp

from .proxy import Proxy
from .proxylist import ProxyList


class Tester:
    async def _get(self, session, url, proxy):
        async with session.get(url, proxy=proxy) as http_response:
            return await http_response.read()

    async def _test_proxies(self, **kwargs) -> list[bytes]:
        async with aiohttp.ClientSession(**kwargs) as session:
            http_response_futures = []
            for source in self._source_list:
                http_response_futures.append(
                    asyncio.ensure_future(self._get(session, source.get("url")))
                )
            html_responses = await asyncio.gather(*http_response_futures)
            return html_responses

    def test(self, proxy: Proxy):
        pass

    def test_all(self, proxy_list: ProxyList):
        pass
