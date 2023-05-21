import json
import re
import sys
from http.cookiejar import Cookie
from typing import List

import browser_cookie3


def header():
    org_header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://leetcode.cn",
        "Host": "leetcode.cn",
        "X-Requested-With": "XMLHttpRequest"
        # "Referer": referer
    }
    cj = browser_cookie3.chrome(domain_name=".leetcode.cn")

    class Redirect:
        content = ""

        def write(self, content: str):
            self.content += content

        def flush(self):
            self.content = ""

    r = Redirect()
    sys.stdout = r
    print(cj)
    sys.stdout = sys.__stdout__

    rgx = re.compile(r'Cookie (.*?) for')
    find: List[str] = rgx.findall(r.content)
    for f in find:
        if "csrftoken" in f:
            org_header["x-csrftoken"] = f.replace("csrftoken=", "")
    org_header["Cookie"] = "; ".join(find)
    return org_header


def set_cookie():
    cj = browser_cookie3.chrome(domain_name=".leetcode.cn")
