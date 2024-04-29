def minimum_delete_sum(s1: str, s2: str) -> int:
    """
    计算两个字符串的最小ASCII删除和。
    
    参数:
    s1 (str): 第一个字符串
    s2 (str): 第二个字符串
    
    返回:
    int: 最小ASCII删除和
    
    示例:
    >>> minimum_delete_sum("delete", "leet")
    425
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化dp数组，处理任一字符串为空的情况
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    
    # 填充dp数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
    
    return dp[m][n]

# 测试代码
result = minimum_delete_sum("delete", "leet")
print(result)