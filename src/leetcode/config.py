import json
import os.path
from typing import Dict

from src.common.vars import G


class Config:
    lang: str = "cpp"
    browser: str = "chrome"

    @classmethod
    def load(cls, d: Dict):
        if "lang" in d:
            cls.lang = d["lang"]
        if "browser" in d:
            cls.browser = d["browser"]

    @classmethod
    def dump(cls):
        return {"lang": cls.lang, "browser": cls.browser}


def read_config():
    if os.path.exists(G.config_path):
        with open(G.config_path) as f:
            Config.load(json.loads(f.read()))


def config_lang(lang: str):
    with open(G.config_path, "r+") as rw:
        Config.load(json.loads(rw.read()))
        rw.seek(0)
        Config.lang = lang
        rw.write(json.dumps(Config.dump()))


def config_browser(browser: str):
    with open(G.config_path, "r+") as rw:
        Config.load(json.loads(rw.read()))
        rw.seek(0)
        Config.browser = browser
        rw.write(json.dumps(Config.dump()))
