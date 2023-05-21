import os


class G:
    base_path: str = os.path.join(os.getenv("HOME"), ".config", "leetcode-cli/")
    config_path: str = os.path.join(base_path, "config.json")
    dataset_path: str = os.path.join(base_path + "dataset.json")
    cookie_path: str = os.path.join(base_path + "cookie.json")
    prefer_lang: str = "cpp"
