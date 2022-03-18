# ua-generator

A random user-agent generator for Python >= 3.6

# Features
* No external user-agent list. No downloads.
* Templates are hardcoded into the code.
* Platform and browser versions are based on real releases.

# Installing

```bash
pip3 install ua-generator
```

# Basic usage

```python
import ua_generator

ua = ua_generator.generate()
print(ua)
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/15.2 Safari/604.1.38
```

# Customization

```python
import ua_generator

ua = ua_generator.generate(platform=('ios', 'macos'), browser='safari')
print(ua)
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38

ua = ua_generator.generate(device='mobile', browser=('safari', 'chrome'))
print(ua)
# Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1.38

ua = ua_generator.generate(device='desktop', browser='firefox')
print(ua)
# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
```

# Author

Ekin Karadeniz (iamdual@icloud.com)