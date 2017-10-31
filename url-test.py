#!/usr/bin/env python3
import os, sys
from you_get import common
import re
from you_get import json_output

if __name__ == '__main__':
    url = "http://www.iqiyi.com/v_19rrb9xito.html#vfrm=19-9-0-1"
    if re.match(r'https?://', url) is None:
        url = 'http://' + url
    # if cookies:
    #     common.load_cookies(cookies)
    m, url = common.url_to_module(url)
    kwargs = {'json_output': True, 'keep_obj': True}
    m.download(url, **kwargs)
    print(json_output.global_json)
