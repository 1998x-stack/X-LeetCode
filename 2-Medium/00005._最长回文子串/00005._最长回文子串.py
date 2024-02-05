def longest_palindrome_2d(s: str) -> str:
    """
    寻找最长回文子串的函数。

    参数:
        s (str): 输入的字符串。

    返回:
        str: 最长的回文子串。

    示例:
        >>> longest_palindrome("babad")
        'bab'
    """
    n = len(s)
    if n < 2:
        # 如果字符串长度小于2，直接返回原字符串
        return s

    # 初始化动态规划表
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    # 基本情况
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_length = i, 2

    # 状态转移
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_length = i, length

    return s[start:start + max_length]

def longest_palindrome_1d(s: str) -> str:
    """
    使用一维数组策略寻找最长回文子串。

    参数:
        s (str): 输入的字符串。

    返回:
        str: 最长的回文子串。

    示例:
        >>> longest_palindrome("babad")
        'bab'
    """
    n = len(s)
    if n < 2:
        return s

    start, max_length = 0, 1

    def expand_around_center(left: int, right: int) -> None:
        nonlocal start, max_length
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start, max_length = left, right - left + 1
            left -= 1
            right += 1

    for i in range(n):
        # 奇数长度的回文
        expand_around_center(i, i)
        # 偶数长度的回文
        expand_around_center(i, i + 1)

    return s[start:start + max_length]

# 测试代码
if __name__ == "__main__":
    test_str = "babad"
    print(f"最长回文子串: {longest_palindrome_2d(test_str)}")
    print(f"最长回文子串: {longest_palindrome_1d(test_str)}")