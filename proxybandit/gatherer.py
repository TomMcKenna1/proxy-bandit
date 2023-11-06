from .core import Proxy
import aiohttp
import asyncio

class Gatherer:

    def __init__(self):
        self.proxy_list_urls = []
        self.proxies = []

    async def _get_proxy_list(self, session, proxy_list_url):
        async with session.get(proxy_list_url) as proxy_list_response:
            return await proxy_list_response.read()

    async def _gather_proxy_lists(self):
        async with aiohttp.ClientSession() as session:
            html_response_futures = []
            for proxy_list_url in self.proxy_list_urls:
                html_response_futures.append(asyncio.ensure_future(self._get_proxy_list(session, proxy_list_url)))
            html_responses = await asyncio.gather(*html_response_futures)
            return html_responses

    def gather(self):
        print(self.proxy_list_urls)
        return asyncio.run(self._gather_proxy_lists())