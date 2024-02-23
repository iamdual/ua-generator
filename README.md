# ua-generator

A random user-agent generator for Python >= 3.6

# Features
* No external user-agent list. No downloads.
* Templates are hardcoded into the code.
* Platform and browser versions are based on real releases.
* Client hints (Sec-CH-UA fields).

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
There are three different parameters to the generate user-agent by the certain conditions.
```python
device = ('desktop', 'mobile')
platform = ('windows', 'macos', 'ios', 'linux', 'android')
browser = ('chrome', 'edge', 'firefox', 'safari')
```

All of the parameters are optional, and the types can be choose multiple.
```python
import ua_generator

ua = ua_generator.generate(device='desktop', browser='firefox')
print(ua.text) # Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0.1) Gecko/20100101 Firefox/121.0.1
print(ua.platform) # macos
print(ua.browser) # firefox
print(ua.ch.brands) # "Not A(Brand";v="99"
print(ua.ch.mobile) # ?0
print(ua.ch.platform) # "macOS"
print(ua.ch.platform_version) # "14.0.1"

ua = ua_generator.generate(platform=('ios', 'macos'), browser='chrome')
print(ua.text) # Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/119.0.6045.176 Mobile/15E148 Safari/537.36
print(ua.platform) # ios
print(ua.browser) # chrome
print(ua.ch.brands) # "Not A(Brand";v="99", "Chromium";v="119", "Google Chrome";v="119"
print(ua.ch.mobile) # ?1
print(ua.ch.platform) # "iOS"
print(ua.ch.platform_version) # "17.0.2"
```

# Author
Ekin Karadeniz (iamdual@icloud.com)