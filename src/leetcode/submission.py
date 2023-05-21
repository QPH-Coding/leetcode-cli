import json
from typing import Dict

import requests

from src.common import url, query


def print_submission(detail: Dict):
    if not detail["run_success"]:
        print("Your code can not run successfully!!!")
        print(detail["full_compile_error"])
        return
    pass_num: int = detail["total_correct"]
    total: int = detail["total_testcases"]
    msg: str = detail["status_msg"]
    last_testcase: str = detail["last_testcase"]
    expect: str = detail["expected_output"]
    memory: str = detail["status_memory"]
    memory_percent: str = "%.2f" % (detail["memory_percentile"] * 100)
    runtime: str = detail["status_runtime"]
    runtime_percent: str = "%.2f" % (detail["runtime_percentile"] * 100)
    print(msg)
    print("PASS: %d / %d" % (pass_num, total))
    if msg == "Accepted":
        print("MEMORY: %s %s %%; RUNTIME: %s %s %%" % (memory, memory_percent, runtime, runtime_percent))
    else:
        print("MEMORY: N/A; RUNTIME: N/A")
        print("Last case:")
        print(last_testcase)
        print("Expect:")
        print(expect)


def list_submission_by_slug(header: Dict, slug: str):
    data = {
        "operationName": "submissionList",
        "variables": {
            "questionSlug": slug,
            "offset": 0,
            "limit": 20,
            "lastKey": None,
            "status": None
        },
        "query": query.submissionList
    }
    requests.post(url=url.graphql, headers=header, data=json.dumps(data))


def list_recent_ac_submission(header: Dict, user_slug: str):
    data = {
        "operationName": "recentAcSubmissions",
        "variables": {
            "userSlug": user_slug
        },
        "query": query.recentAcSubmissions
    }
    resp = requests.post(url.graphql_noj_go, headers=header, data=json.dumps(data))
    print(json.loads(resp.text))
