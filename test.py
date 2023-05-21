import json
import os
import re
from typing import Dict

import browser_cookie3
import requests

from src.common.http_core import Url
from src.common.vars import G

if __name__ == '__main__':
    content = {'data': {'userProfileUserQuestionProgress': {
        'numAcceptedQuestions': [{'difficulty': 'EASY', 'count': 60}, {'difficulty': 'MEDIUM', 'count': 92},
                                 {'difficulty': 'HARD', 'count': 12}],
        'numFailedQuestions': [{'difficulty': 'EASY', 'count': 0}, {'difficulty': 'MEDIUM', 'count': 2},
                               {'difficulty': 'HARD', 'count': 0}],
        'numUntouchedQuestions': [{'difficulty': 'EASY', 'count': 730}, {'difficulty': 'MEDIUM', 'count': 1538},
                                  {'difficulty': 'HARD', 'count': 653}]}}}

