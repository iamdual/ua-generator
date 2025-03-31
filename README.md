# ua-generator

A random user-agent generator for Python >= 3.9

# Features

- No external user-agent list. No downloads.
- Templates are hardcoded into the code.
- Platform and browser versions are based on real releases.
- Client Hints (Sec-CH-UA fields).
- Easy to integrate into HTTP libraries.

# Installing

```bash
pip3 install -U ua-generator
```

# Basic usage

```python
import ua_generator

ua = ua_generator.generate()
print(ua) # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/15.2 Safari/604.1.38
```

# Customization

**It takes three different parameters to customize the user-agent.**

```python
device = ('desktop', 'mobile')
platform = ('windows', 'macos', 'ios', 'linux', 'android')
browser = ('chrome', 'edge', 'firefox', 'safari')
```
_All parameters are optional and multiple types can be specified using a list (or tuple)._
## Customized user-agent generation:

```python
import ua_generator

# Example 1:
ua = ua_generator.generate(device='desktop', browser=('chrome', 'edge'))
print(ua.text) # Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.145 Safari/537.36
print(ua.platform) # windows
print(ua.browser) # chrome
print(ua.ch.brands) # "Not A(Brand";v="99", "Chromium";v="108", "Google Chrome";v="108"
print(ua.ch.mobile) # ?0
print(ua.ch.platform) # "Windows"
print(ua.ch.platform_version) # "13.0.0"
print(ua.ch.bitness) # "64"
print(ua.ch.architecture) # "x86"

# Example 2:
ua = ua_generator.generate(platform=('ios', 'macos'), browser='chrome')
print(ua.text) # Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/119.0.6045.176 Mobile/15E148 Safari/537.36
print(ua.platform) # ios
print(ua.browser) # chrome
print(ua.ch.brands) # "Not A(Brand";v="99", "Chromium";v="119", "Google Chrome";v="119"
print(ua.ch.mobile) # ?1
print(ua.ch.platform) # "iOS"
print(ua.ch.platform_version) # "17.0.2"
print(ua.ch.bitness) # "64"
print(ua.ch.architecture) # "arm"
```

# Headers

```python
ua = ua_generator.generate(browser=('chrome', 'edge'))

# This will return a dictionary containing the generated user-agent:
print(ua.headers.get())
{
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.43 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Chromium";v="103", "Google Chrome";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
}

# Extending the "Client Hints" by a value of the "Accept-CH" header:
print(ua.headers.accept_ch('Sec-CH-UA-Platform-Version, Sec-CH-UA-Full-Version-List'))
print(ua.headers.get())
{
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Chromium";v="122", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.1.0"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Chromium";v="122.0.6261.94", "Google Chrome";v="122.0.6261.94"'
}
```

## Integrating into the [requests](https://pypi.org/project/requests/):

```python
import requests
import ua_generator

ua = ua_generator.generate(browser=('chrome', 'edge'))
r = requests.get('https://httpbin.org/get', headers=ua.headers.get())

# or, usage with requests.Session():
ua = ua_generator.generate(browser=('chrome', 'edge'))
s = requests.Session()
s.headers.update(ua.headers.get())
r = s.get('https://httpbin.org/get')
```

## Integrating into the [httpx](https://pypi.org/project/httpx/):

```python
import httpx
import ua_generator

ua = ua_generator.generate(browser=('chrome', 'edge'))
r = httpx.get('https://httpbin.org/get', headers=ua.headers.get())

# or, usage with httpx.Client():
ua = ua_generator.generate(browser=('chrome', 'edge'))
c = httpx.Client(headers=ua.headers.get())
r = c.get('https://httpbin.org/get')
```

## Integrating into the [urllib](https://docs.python.org/3/library/urllib.request.html):

```python
import urllib.request
import ua_generator

ua = ua_generator.generate(browser=('chrome', 'edge'))
request = urllib.request.Request('https://httpbin.org/get', headers=ua.headers.get())
handler = urllib.request.urlopen(request)
response = handler.read().decode('utf-8')
```

# Options

You can define options using the "options" parameter for further customization.

## weighted_versions
To increase the probability of the latest versions being chosen. Default is `False`.

```python
import ua_generator
from ua_generator.options import Options

# Enabling weighted versions
options = Options()
options.weighted_versions = True
ua = ua_generator.generate(browser=('chrome', 'edge'), options=options)
```

## version_ranges
To choose only versions within specified ranges. Default is `None`.

```python
import ua_generator
from ua_generator.options import Options
from ua_generator.data.version import VersionRange

# Choosing only versions within specified ranges
options = Options()
options.version_ranges = {
    'chrome': VersionRange(125, 129),  # Choose version between 125 and 129
    'edge': VersionRange(min_version=120),  # Choose version 120 minimum
}
ua = ua_generator.generate(browser='chrome', options=options)
```

# Issues

You can create an issue [from here](https://github.com/iamdual/ua-generator/issues) if you are experiencing a problem.

# Contributing

Pull requests are welcome. Don't forget to run tests.

# Contributors

Ekin Karadeniz ([@iamdual](https://github.com/iamdual)) and [the GitHub community](https://github.com/iamdual/ua-generator/graphs/contributors).
