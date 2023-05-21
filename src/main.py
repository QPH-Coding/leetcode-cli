import json
import os
from typing import Dict, List

from src.common import utils
from src.leetcode import problem
from src.leetcode.user import get_user_status
from src.common.vars import G


def _config_main(args: Dict):
    pass


def _user_main(args: Dict):
    get_user_status()


def _problem_main(args: Dict):
    def _pull():
        info, ok = utils.find_problem_info(G.dataset_path, args["frontend_id"])
        if not ok:
            exit(127)
        problem.pull_problem_by_slug(G.prefer_lang, info)

    def _update():
        problem.update_problems(G.dataset_path)

    def _submit():
        problem.submit(args["file"])

    def _today():
        problem.today_question_for_search()

    router = {
        "pull": _pull,
        "update": _update,
        "submit": _submit,
        "today": _today
    }
    router[args["action"]]()


def _submission_main(args: Dict):
    pass


def main(args: Dict):
    print(G.dataset_path)
    # read config
    if not os.path.exists(G.base_path):
        os.makedirs(G.base_path)
    if os.path.exists(G.config_path):
        with open(G.config_path) as f:
            config = json.loads(f.read())
        if "lang" in config:
            G.prefer_lang = config["lang"]
    type_router = {
        "config": _config_main,
        "user": _user_main,
        "problem": _problem_main,
        "submission": _submission_main
    }
    type_router[args["type"]](args)
