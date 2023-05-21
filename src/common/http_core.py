import json
import os.path
import re
from enum import Enum
from typing import Dict, Tuple

import browser_cookie3
import requests

from src.common import query, model
from src.common.vars import G


class Url:
    _base = "https://leetcode.cn"
    graphql = _base + "/graphql/"
    noj_go = _base + "/graphql/noj-go/"
    login = _base + "/accounts/login/"

    @staticmethod
    def submit(problem_slug: str):
        return "%s/problems/%s/submit/" % (Url._base, problem_slug)

    @staticmethod
    def submission_detail(id: str):
        return "%s/submissions/detail/%s/check/" % (Url._base, id)

    @staticmethod
    def submission(slug: str):
        return "%s/problems/%s/submissions/" % (Url._base, slug)


class Method(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"


def leetcode_request(url: str, data: Dict, method: Method = Method.POST) -> requests.Response:
    def unmarshal_set_cookie(r: requests.Response) -> Dict[str, str]:
        if "set-cookie" not in r.headers:
            return {}
        rgx = re.compile(r' (.*?)=(.*?);')
        finds = rgx.findall(" " + r.headers["set-cookie"])
        cookie = {}
        for find in finds:
            cookie[find[0]] = find[1]
        return cookie

    def marshal_cookie(cookie: Dict[str, str]) -> str:
        cookie_str = ""
        for key in cookie:
            cookie_str += key + "=" + cookie[key] + "; "
        return cookie_str

    if os.path.exists(G.cookie_path):
        with open(G.cookie_path) as f:
            cookies = json.loads(f.read())
    else:
        cj = browser_cookie3.chrome(domain_name=".leetcode.cn")
        cookies = {}
        for c in cj:
            cookies[c.name] = c.value
        with open(G.cookie_path, "w") as w:
            w.write(json.dumps(cookies))
    headers = {
        'x-csrftoken': cookies["csrftoken"],
        "Host": "leetcode.cn",
        "Connection": "keep-alive",
        'User-Agent': "Mozilla/5.0 (Macintosh; "
                      "Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        'Origin': 'https://leetcode.cn',
        'content-type': 'application/json',
        "Cookie": marshal_cookie(cookies)
    }
    # NOTE: check user sign in
    user_status_data = {
        "operationName": "globalData",
        "query": query.globalData,
        "variables": {}
    }
    user_status_resp = requests.post(url=Url.noj_go, headers=headers, data=json.dumps(user_status_data))
    # HINT: Here I think the global status will not set new cookie
    user_status = model.UserStatus(json.loads(user_status_resp.text))
    if not user_status.isSignedIn:
        # NOTE: Delete the cookie file, and the next time will be read from chrome
        if os.path.exists(G.cookie_path):
            os.remove(G.cookie_path)
        print("Warning: Has not logged in or the session has expired.\n"
              "Please Login the leetcode.com in browser.")
        exit(127)
    method_router = {
        Method.GET: requests.get,
        Method.POST: requests.post,
        Method.PUT: requests.put
    }
    resp = method_router[method](url=url, headers=headers, data=json.dumps(data))
    if resp.status_code == 200:
        set_cookie = unmarshal_set_cookie(resp)
        for key in set_cookie:
            cookies[key] = set_cookie[key]
        with open(G.cookie_path, "w") as w:
            w.write(json.dumps(cookies, indent=2))
    return resp
