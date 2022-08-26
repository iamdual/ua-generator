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
print(ua.text)      # Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0
print(ua.platform)  # linux
print(ua.browser)   # firefox
print(ua.ch.brands) # " Not A;Brand";v="99"
print(ua.ch.mobile) # ?0

ua = ua_generator.generate(platform=('ios', 'macos'), browser='chrome')
print(ua.text)      # Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/80.0.3987.44 Mobile/15E148 Safari/537.36
print(ua.platform)  # ios
print(ua.browser)   # chrome
print(ua.ch.brands) # " Not A;Brand";v="99", "Chromium";v="80", "Google Chrome";v="80"
print(ua.ch.mobile) # ?1
```

# Author
Ekin Karadeniz (iamdual@icloud.com)