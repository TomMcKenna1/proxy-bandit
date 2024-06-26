<div align="center">
  <a href="https://github.com/TomMcKenna1/proxy-bandit">
    <picture>
     <source media="(prefers-color-scheme: dark)" srcset="resources/logo-dark.png">
     <img src="resources/logo-light.png">
    </picture>
  </a>
  <h3 align="center">proxy-bandit</h3>

  <p align="center">
    Fast and easy to use rotating proxy provider, gathering proxies from a variety of sources.
    <br />
    <a href="https://github.com/TomMcKenna1/proxy-bandit/issues">Report Bug</a>
    ·
    <a href="https://github.com/TomMcKenna1/proxy-bandit/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#examples">Examples</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Proxy Bandit is a performant python module designed to simplify the gathering and utlisation of free proxies online. The module easily interfaces with both python's popular `requests` and `aiohttp` modules, allowing you to send proxied requests at no cost, with little setup.

**Features:**
- Gather thousands of proxies from multiple sources within seconds.
- Add your own proxy sources via json.
- Simple to use proxies that interface with both python requests and aiohttp.
- Export scraped proxies to a csv file.

**Requires:**
- aiohttp

<!-- GETTING STARTED -->
## Getting Started

To use Proxy Bandit in your own project, follow the steps below:

1. Install the package through pip
   ```sh
   pip install proxybandit
   ```
2. Import the ProxyBandit class into your python file
   ```python
   from proxybandit import ProxyBandit

   proxy_bandit = ProxyBandit()
   ```


<!-- USAGE EXAMPLES -->
## Usage

### Examples

<br />

Print 10 proxies:
```python
from proxybandit import ProxyBandit

proxy_bandit = ProxyBandit()

for i in range(10):
  print(proxy_bandit.get_proxy())
```
```sh
http://50.207.199.81:80
http://50.228.141.97:80
http://68.185.57.66:80
http://213.143.113.82:80
http://50.228.141.96:80
http://172.108.208.74:80
http://50.227.121.36:80
http://50.227.121.34:80
http://50.168.72.115:80
http://50.170.90.26:80
```

<br />

Send a request using a proxy:
```python
import requests
from proxybandit import ProxyBandit

proxy_bandit = ProxyBandit()
proxy = proxy_bandit.get_proxy()
res = requests.get("http://azenv.net/", proxies=proxy.to_dict())
```

<br />

Send 10 asynchronous requests, each with their own individual proxy:
```python
import aiohttp
import asyncio
from proxybandit import ProxyBandit

proxy_bandit = ProxyBandit()

async def async_get(session, url, proxy):
    async with session.get(url, proxy=proxy) as http_response:
        return await http_response.read()

async def async_get_many(url, number_of_requests):
    async with aiohttp.ClientSession() as session:
        http_response_futures = []
        for i in range(number_of_requests):
            # Here we get a new proxy using proxy bandit
            proxy = str(proxy_bandit.get_proxy())
            http_response_futures.append(
                asyncio.ensure_future(async_get(session, url, proxy))
            )
        html_responses = await asyncio.gather(*http_response_futures)
        return html_responses

number_of_requests = 10
res = asyncio.run(
  async_get_many("http://azenv.net/", number_of_requests)
)
```

<!-- ROADMAP -->
## Roadmap

- [ ] Asynchronously test proxies work on initialisation
- [ ] Add proxy metadata (country of origin, type, speed)
- [ ] Filter proxies by metadata

See the [open issues](https://github.com/TomMcKenna1/proxy-bandit/issues) for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**; I try to promptly check all of them!

If you have a suggestion that would improve this project, please fork the repo and create a pull request. You can also simply open an issue with the label "enhancement".
Don't forget to give the project a star! Thanks again.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Tom McKenna - [Follow me on LinkedIn!](https://www.linkedin.com/in/tom-m-8a70891a8/) - tom2mckenna@gmail.com

Project Link: [https://github.com/TomMcKenna1/proxy-bandit](https://github.com/TomMcKenna1/proxy-bandit)
