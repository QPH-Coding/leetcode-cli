# Author: @jj1118 https://zhuanlan.zhihu.com/p/33579027
import json
from typing import List, Dict, Tuple

from fuzzywuzzy import fuzz


def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    """
    Call in a loop to create a terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    import sys
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


class ProblemInfo:
    def __init__(self):
        self.frontend_id = ""
        self.title = ""
        self.slug = ""
        self.filename = ""
        self.difficulty = ""
        self.ac_rate = ""


def find_problem_info(path: str, frontend_id: str) -> Tuple[ProblemInfo, bool]:
    with open(path) as f:
        problems: List[Dict] = json.loads(f.read())
    similar: List[str] = []
    info = ProblemInfo()
    for problem in problems:
        info.frontend_id = problem["frontendQuestionId"]
        info.title = problem["title"]
        if info.frontend_id == frontend_id:
            info.slug = problem["titleSlug"]
            info.ac_rate = str(problem["acRate"] * 100) + "%"
            info.difficulty = problem["difficulty"]
            info.filename = "%s-%s(%s)" % (frontend_id, info.title, problem["titleCn"])
            print("Found: %s %s %6s %s" % (info.frontend_id, info.title, info.difficulty, info.ac_rate))
            break
        if fuzz.partial_ratio(frontend_id, info.frontend_id) > 65:
            similar.append("Frontend id: %8s, Name: %s" % (info.frontend_id, info.title))
    if not info.slug:
        print("Problem not found in dataset")
        if similar:
            print("The similar frontend question id:")
            print("\n".join(similar))
        print("Or try to update dataset:\n"
              "\tleetcode-cli problem update")
        return info, False
    return info, True
