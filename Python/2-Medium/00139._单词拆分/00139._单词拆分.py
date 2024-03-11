from typing import List

def word_break(s: str, wordDict: List[str]) -> bool:
    """
    判断字符串 s 是否可以被空格拆分为 wordDict 中的单词。

    Args:
    s: 待判断的字符串。
    wordDict: 单词字典列表。

    Returns:
    bool: 如果可以拆分，返回 True；否则返回 False。

    示例:
    >>> word_break("leetcode", ["leet", "code"])
    True
    >>> word_break("applepenapple", ["apple", "pen"])
    True
    >>> word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    False
    """
    # 将单词字典转化为集合，便于快速查找
    word_set = set(wordDict)
    # 初始化动态规划数组，dp[i] 表示 s[:i] 能否被拆分
    dp = [False] * (len(s) + 1)
    dp[0] = True  # 空字符串可以被拆分
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            # 如果 s[:j] 可以被拆分，并且 s[j:i] 在单词字典中，那么 s[:i] 也可以被拆分
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # 找到一种拆分方式即可
    
    return dp[len(s)]

# 运行示例测试
test_cases = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"])
]

results = [word_break(s, wordDict) for s, wordDict in test_cases]
results
