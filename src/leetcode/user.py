import json

import requests

from src.common import query, url, auth, model
from src.common.http_core import leetcode_request, Url, Method


def get_user_status():
    name, slug = get_user_name_slug()
    content = user_question_progress(slug)
    print("Name: %s" % name)
    print("Slug: %s" % slug)
    print("Progress:")
    print(content)


def user_question_progress(user_slug: str):
    data = {
        "operationName": "userQuestionProgress",
        "variables": {
            "userSlug": user_slug
        },
        "query": query.userQuestionProgress
    }
    url_: str = url.graphql
    resp = requests.post(url=url_, headers=auth.header(), data=json.dumps(data))
    content = json.loads(resp.text)
    return content


def get_user_name_slug():
    data_ = {
        "operationName": "userStatusGlobal",
        "query": query.userStatusGlobal,
        "variables": {}
    }
    url_: str = url.graphql_noj_go
    resp = requests.post(url=url_, headers=auth.header(), data=json.dumps(data_))
    status = json.loads(resp.text)["data"]["userStatus"]
    return status["realName"], status["userSlug"]
