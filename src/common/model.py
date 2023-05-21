from typing import Dict


class UserStatus:
    def __init__(self, d: Dict):
        d = d["data"]["userStatus"]
        self.userSlug = d["userSlug"]
        self.isSignedIn = d["isSignedIn"]
        self.isPremium = d["isPremium"]
        self.isVerified = d["isVerified"]
        self.username = d["username"]


class UserProgress:
    class Question:
        def __init__(self, d: Dict):
            self.questionFrontendId = d["questionFrontendId"]
            self.questionTitle = d["questionTitle"]
            self.difficulty = d["difficulty"]
            self.topicTags = d["topicTags"]["slug"]

    def __init__(self, d: Dict):
        d = d["data"]["solvedQuestionsInfo"]
        self.currentPage = d["currentPage"]
        self.pageNum = d["pageNum"]
        self.totalNum = d["totalNum"]
        self.totalSolves = d["data"]["totalSolves"]
        self.question = d["data"]["question"]
