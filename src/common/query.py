questionTitle = '''
query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    isPaidOnly
    difficulty
    likes
    dislikes
  }
}
'''
questionContent = '''
query questionContent($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    content
    mysqlSchemas
  }
}
'''
questionEditorData = '''
query questionEditorData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    codeSnippets {
      lang
      langSlug
      code
    }
    envInfo
    enableRunCode
  }
}
'''
questionHints = '''
query questionHints($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    hints
  }
}
'''
questionOfToday = '''
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    userStatus
    link
    question {
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      hasVideoSolution
      hasSolution
      topicTags {
        name
        id
        slug
      }
    }
  }
}
'''

submissionList = '''
query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!, $lang: Int, $status: Int) {
  questionSubmissionList(
    offset: $offset
    limit: $limit
    lastKey: $lastKey
    questionSlug: $questionSlug
    lang: $lang
    status: $status
  ) {
    lastKey
    hasNext
    submissions {
      id
      title
      titleSlug
      status
      statusDisplay
      lang
      langName
      runtime
      timestamp
      url
      isPending
      memory
      hasNotes
      notes
    }
  }
}
'''
submissionDetails = '''
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    runtime
    runtimeDisplay
    runtimePercentile
    runtimeDistribution
    memory
    memoryDisplay
    memoryPercentile
    memoryDistribution
    code
    timestamp
    statusCode
    user {
      username
      profile {
        realName
        userAvatar
      }
    }
    lang {
      name
      verboseName
    }
    question {
      questionId
    }
    notes
    topicTags {
      tagId
      slug
      name
    }
    runtimeError
    compileError
    lastTestcase
  }
}
'''

globalData = '''
query globalData {
  userStatus {
    isSignedIn
    isPremium
    username
    realName
    avatar
    userSlug
    isAdmin
    checkedInToday
    useTranslation
    premiumExpiredAt
    isTranslator
    isSuperuser
    isPhoneVerified
    isVerified
  }
  jobsMyCompany {
    nameSlug
  }
}
'''
progressList = '''
query progressList($pageNo: Int, $numPerPage: Int, $filters: ProgressListFilterInput) {
  isProgressCalculated
  solvedQuestionsInfo(pageNo: $pageNo, numPerPage: $numPerPage, filters: $filters) {
    currentPage
    pageNum
    totalNum
    data {
      totalSolves
      question {
        questionFrontendId
        questionTitle
        questionDetailUrl
        difficulty
        topicTags {
          name
          slug
        }
      }
      lastAcSession {
        time
        wrongAttempts
      }
    }
  }
}
'''

userQuestionProgress = '''
query userQuestionProgress($userSlug: String!) {
  userProfileUserQuestionProgress(userSlug: $userSlug) {
    numAcceptedQuestions {
      difficulty
      count
    }
    numFailedQuestions {
      difficulty
      count
    }
    numUntouchedQuestions {
      difficulty
      count
    }
  }
}
'''

userStatusGlobal = '''
query userStatusGlobal {
  userStatus {
    realName
    userSlug
  }
}
'''

todayQuestionForSearch = '''
query todayQuestionForSearch {
  todayRecord {
    question {
      title
      translatedTitle
      questionFrontendId
    }
  }
}
'''

problemQuestionList = '''
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    hasMore
    total
    questions {
      acRate
      difficulty
      freqBar
      frontendQuestionId
      paidOnly
      status
      title
      titleCn
      titleSlug
      topicTags {
        name
        nameTranslated
        id
        slug
      }
    }
  }
}
'''

questionData = '''
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    categoryTitle
    boundTopicId
    title
    titleSlug
    content
    translatedTitle
    translatedContent
    isPaidOnly
    difficulty
    isLiked
    similarQuestions
    contributors {
      username
      profileUrl
      avatarUrl
      __typename
    }
    langToValidPlayground
    topicTags {
      name
      slug
      translatedName
      __typename
    }
    companyTagStats
    codeSnippets {
      lang
      langSlug
      code
      __typename
    }
    stats
    hints
    solution {
      id
      canSeeDetail
      __typename
    }
    status
    sampleTestCase
    metaData
    judgerAvailable
    judgeType
    mysqlSchemas
    enableRunCode
    envInfo
    book {
      id
      bookName
      pressName
      source
      shortDescription
      fullDescription
      bookImgUrl
      pressImgUrl
      productUrl
      __typename
    }
    isSubscribed
    isDailyQuestion
    dailyRecordStatus
    editorType
    ugcQuestionId
    style
    exampleTestcases
    jsonExampleTestcases
    __typename
  }
}
'''

