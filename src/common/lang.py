lang_list = ["cpp", "c", "python", "python3", "golang", "rust", "java", "javascript", "csharp", "swift", "scala"]
_lang_comment_template = {
    "python": "# @comment",
    "python3": "# @comment",
    "java": "// @comment",
    "javascript": "// @comment",
    "c": "// @comment",
    "cpp": "// @comment",
    "csharp": "// @comment",
    "php": "// @comment",
    "ruby": "# @comment",
    "swift": "// @comment",
    "objective-C": "// @comment",
    "kotlin": "// @comment",
    "golang": "// @comment",
    "r": "# @comment",
    "MATLAB": "% @comment",
    "perl": "# @comment",
    "scala": "// @comment",
    "typescript": "// @comment",
    "sql": "-- @comment",
}
_lang_suffix = {
    "python": ".py",
    "python3": ".py",
    "java": ".java",
    "javascript": ".js",
    "c": ".c",
    "cpp": ".cpp",
    "csharp": ".cs",
    "php": ".php",
    "ruby": ".rb",
    "swift": ".swift",
    "objective-C": ".m",
    "kotlin": ".kt",
    "golang": ".go",
    "r": ".r",
    "MATLAB": ".m",
    "perl": ".pl",
    "scala": ".scala",
    "typescript": ".ts",
    "sql": ".sql",
}


def lang_comment(lang: str, content: str) -> str:
    return _lang_comment_template[lang].replace("@comment", content) + "\n"


def lang_suffix(lang: str) -> str:
    return _lang_suffix[lang]
