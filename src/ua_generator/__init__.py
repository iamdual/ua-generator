"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
#ua-generator/src/__init__.py
import typing
from . import user_agent, options as _options
from src.ua_generator.data import VERSION_SUPPORTED_MODULES
from src.ua_generator.data.browsers import chrome,firefox,edge,safari
from src.ua_generator.data.platforms import ios, macos, windows,linux
from src.ua_generator.data.platforms.android import android_nexus,android_samsung,android_pixel
from src.ua_generator.exceptions import InvalidArgumentError
versions_idx_map = {"chrome":{}, 'edge':{},'safari':{},'firefox':{},'ios':{},'windows':{},'macos':{},'linux':{},'android_samsung':{},'android_nexus':{},'android_pixel':{}}
"""
Initialize an index map containing a mapping of version to index in the original 
respective versions array. Only occurs once upon the first generate using
options as a parameter. Verified with print statements.
"""
def initialize_idx_map(option):
    global versions_idx_map
    module = globals()[option]
    for idx,val in enumerate(module.versions):
        if(val.major not in versions_idx_map[option]):
            versions_idx_map[option][val.major] = idx
    module.versions_idx_map = versions_idx_map[option]

def get_versions(option:str):
    if option in VERSION_SUPPORTED_MODULES:
       module = globals()[option]
       return module.versions
    else:
        raise InvalidArgumentError("{} is not a valid browser/platform with versions.\tValid options include : {}\n".format(option,VERSION_SUPPORTED_MODULES))

def generate(device: typing.Union[tuple, str, None] = None,
             platform: typing.Union[tuple, str, None] = None,
             browser: typing.Union[tuple, str, None] = None,
             options: typing.Union[_options.Options, None] = None) -> user_agent.UserAgent:
    global versions_idx_map
    if options is not None and options.version_ranges is not None:
        for option in options.version_ranges.keys():
            """initialize each index map for each browser/platform dynamically 
            and do this AT MOST across generates
            for the same browser/platform where a version range is specified"""
            if option in versions_idx_map and len(versions_idx_map[option]) == 0:
                initialize_idx_map(option)
    return user_agent.UserAgent(device, platform, browser, options)
