import json
import re
import time
from typing import Dict, List

import html2text as html2text
import requests

from src.common import query, url, comment, auth, lang, utils
from src.leetcode import submission


def today_question_for_search():
    data = {
        "operationName": "todayQuestionForSearch",
        "query": query.todayQuestionForSearch,
        "variables": {}
    }
    resp = requests.post(url=url.graphql, headers=auth.header(), data=json.dumps(data))
    content = json.loads(resp.text)
    return content


def pull_problem_by_slug(lang_slug: str, info: utils.ProblemInfo):
    data = {
        'operationName': "questionData",
        'variables': {'titleSlug': info.slug},
        'query': query.questionData
    }
    referer: str = "https://leetcode.cn/problems/%s" % info.slug
    resp = requests.post(url=url.graphql, headers=auth.header(), data=json.dumps(data))
    content = json.loads(resp.text)
    question = content["data"]["question"]
    filename: str = "LC%s-%s" % (question['questionFrontendId'].zfill(4), question['titleSlug'])
    with open("%s.md" % filename, "w") as w:
        w.write("# %s (%s)" % (filename, question['translatedTitle']))
        w.write("\n\nDifficulty: %6s\n\n" % question['difficulty'])
        w.write("Tags: %s\n\n" % (", ".join([item["translatedName"] for item in question["topicTags"]])))
        w.write(html2text.html2text(question["translatedContent"]))
    with open("%s.cpp" % filename, "w") as w:
        comment_prefix = lang.lang_comment[lang_slug]
        w.write("%s %s\n" % (comment_prefix, comment.meta_start))
        w.write("%s \t@title: %s\n" % (comment_prefix, info.filename))
        w.write("%s \t@slug: %s\n" % (comment_prefix, info.slug))
        w.write("%s \t@difficult: %s\n" % (comment_prefix, info.difficulty))
        w.write("%s \t@ac_rate: %s\n" % (comment_prefix, info.ac_rate))
        w.write("%s \t@lang: %s\n" % (comment_prefix, lang_slug))
        w.write("%s \t@question_id: %s\n" % (comment_prefix, question["questionId"]))
        w.write("%s %s\n\n" % (comment_prefix, comment.meta_end))
        for snippet in question["codeSnippets"]:
            if snippet["langSlug"] == lang_slug:
                w.write("%s %s\n" % (comment_prefix, comment.code_start))
                w.write(snippet["code"] + "\n")
                w.write("%s %s\n" % (comment_prefix, comment.code_end))


def update_problems(path: str):
    has_more: bool = True
    limit: int = 100
    skip: int = 0
    total: List[Dict] = []
    while has_more:
        params = {
            'operationName': "problemsetQuestionList",
            'query': query.problemQuestionList,
            'variables': {
                '$categorySlug': "",
                'filter': {},
                'limit': limit,
                'skip': skip
            },
        }
        resp = requests.post(url=url.graphql, headers=auth.header(), data=json.dumps(params))
        content = json.loads(resp.text)
        question_list = content["data"]["problemsetQuestionList"]
        has_more = question_list["hasMore"]
        total = total + question_list["questions"]
        skip += len(question_list["questions"])
        utils.printProgress(skip, question_list["total"], prefix="Updating")
        time.sleep(1)
    with open(path, "w") as w:
        w.write(json.dumps(total, indent=2).encode('utf-8').decode("unicode_escape"))


def submit(filename: str):
    def _get_meta(filename_: str):
        with open(filename_) as f:
            lines = f.readlines()
        is_meta: bool = False
        meta_rgx = re.compile(r'@(.*?): (.*?)$')
        meta = {}
        for line in lines:
            if comment.meta_start in line:
                is_meta = True
                continue
            elif comment.meta_end in line:
                is_meta = False
                continue
            if is_meta:
                find = meta_rgx.findall(line)[0]
                meta[find[0]] = find[1]
        return meta

    def _get_code(filename_: str):
        content: List[str] = []
        with open(filename_) as f:
            lines = f.readlines()
        is_submit_code: bool = False
        for line in lines:
            if comment.code_start in line:
                is_submit_code = True
                continue
            elif comment.code_end in line:
                is_submit_code = False
                continue
            if is_submit_code:
                content.append(line)
        return "\n".join(content)

    meta = _get_meta(filename)
    code = _get_code(filename)
    # referer = "https://leetcode.cn/problems/%s/description/" % meta["slug"]
    data = {
        "lang": meta["lang"],
        "question_id": meta["question_id"],
        "typed_code": code
    }
    submit_resp = requests.post(url.submit(meta["slug"]), headers=auth.header(), data=json.dumps(data))
    print("Your code has submitted, waiting the result")
    submission_id = json.loads(submit_resp.text)["submission_id"]
    done: bool = False
    detail: Dict = {}
    while not done:
        time.sleep(1)
        check_resp = requests.get(url.submission_detail(str(submission_id)), headers=auth.header())
        detail = json.loads(check_resp.text)
        if detail["state"] == "SUCCESS":
            done = True
    submission.print_submission(detail)
