#!/usr/bin/env python3
import os, sys
from you_get import common
import re

if __name__ == '__main__':
    url = "https://bangumi.bilibili.com/anime/3756/play#86248"
    if re.match(r'https?://', url) is None:
        url = 'http://' + url
    # if cookies:
    #     common.load_cookies(cookies)
    m, url = common.url_to_module(url)
    kwargs = {'json_output': True, 'keep_obj': True}
    m.download(url, **kwargs)
    print(m.get_json())

