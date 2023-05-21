import json
from typing import List, Dict

import requests

from src.common import query, model
from src.common.http_core import leetcode_request, Url, Method


def get_user_status():
    name, slug = get_user_name_slug()
    content = user_question_progress(slug)
    print("Name: %s" % name)
    print("Slug: %s" % slug)
    print("Progress:")

    class ProblemCount:
        def __init__(self):
            self.accepted = 0
            self.failed = 0
            self.untouched = 0

        def percent(self):
            total = self.accepted + self.failed + self.untouched
            accepted_rate = (self.accepted / total) * 100
            failed_rate = (self.failed / total) * 100
            untouched_rate = (self.untouched / total) * 100
            return accepted_rate, failed_rate, untouched_rate

        def print(self, difficulty: str):
            total = self.accepted + self.failed + self.untouched
            accepted_rate = (self.accepted / total) * 100
            failed_rate = (self.failed / total) * 100
            untouched_rate = (self.untouched / total) * 100
            accepted_progress = ["*" for i in range(int(accepted_rate))]
            failed_progress = ["x" for i in range(int(failed_rate))]
            untouched_progress = ["-" for i in range(int(untouched_rate))]
            print("  %-8s: |%s%s%s| ( %4d/%4d/%4d/%4d )" % (
                difficulty, "".join(accepted_progress), "".join(failed_progress), "".join(untouched_progress),
                self.accepted, self.failed, self.untouched, total))

    accepted: List[Dict] = content["data"]["userProfileUserQuestionProgress"]["numAcceptedQuestions"]
    failed: List[Dict] = content["data"]["userProfileUserQuestionProgress"]["numFailedQuestions"]
    untouched: List[Dict] = content["data"]["userProfileUserQuestionProgress"]["numUntouchedQuestions"]
    progress = {
        "EASY": ProblemCount(),
        "MEDIUM": ProblemCount(),
        "HARD": ProblemCount()
    }
    for item in accepted:
        progress[item["difficulty"]].accepted += item["count"]
    for item in failed:
        progress[item["difficulty"]].failed += item["count"]
    for item in untouched:
        progress[item["difficulty"]].untouched += item["count"]
    for item in progress:
        progress[item].print(item)


def user_question_progress(user_slug: str):
    data = {
        "operationName": "userQuestionProgress",
        "variables": {
            "userSlug": user_slug
        },
        "query": query.userQuestionProgress
    }
    resp = leetcode_request(url=Url.graphql, data=data)
    content = json.loads(resp.text)
    return content


def get_user_name_slug():
    data = {
        "operationName": "userStatusGlobal",
        "query": query.userStatusGlobal,
        "variables": {}
    }
    resp = leetcode_request(url=Url.noj_go, data=data)
    status = json.loads(resp.text)["data"]["userStatus"]
    return status["realName"], status["userSlug"]
