from typing import Dict

from src.common import query
from src.common.http_core import Url, leetcode_request, Method


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
    memory_percent: str = "%.2f" % detail["memory_percentile"]
    runtime: str = detail["status_runtime"]
    runtime_percent: str = "%.2f" % detail["runtime_percentile"]
    print("Result: " + msg)
    print("PASS: %d / %d" % (pass_num, total))
    if msg == "Accepted":
        print("MEMORY: %s %s %%\nRUNTIME: %s %s %%" % (memory, memory_percent, runtime, runtime_percent))
    else:
        print("MEMORY: N/A\nRUNTIME: N/A")
        print("Last case:")
        print(last_testcase)
        print("Expect:")
        print(expect)


def list_submission_by_slug(slug: str):
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
    leetcode_request(method=Method.POST, url=Url.graphql, data=data)


def list_recent_ac_submission(header: Dict, user_slug: str):
    # data = {
    #     "operationName": "recentAcSubmissions",
    #     "variables": {
    #         "userSlug": user_slug
    #     },
    #     "query": query.recentAcSubmissions
    # }
    # resp = requests.post(url.graphql_noj_go, headers=header, data=json.dumps(data))
    # print(json.loads(resp.text))
    pass
