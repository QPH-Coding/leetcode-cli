import json
import os
import re
from typing import Dict

import browser_cookie3
import requests

from src.common.http_core import Url
from src.common.vars import G


def teaa(d: Dict):
    d = d["test"]
    print(d)


if __name__ == '__main__':
    cj = browser_cookie3.chrome(domain_name="leetcode.com")
    for c in cj:
        print(c.name + ": " + c.value)
    teaa({"test": "aaa"})
