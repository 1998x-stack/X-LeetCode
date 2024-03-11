from typing import List

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # s3的长度不等于s1和s2的长度之和，直接返回False
    if len(s1) + len(s2) != len(s3):
        return False

    # 初始化dp数组，多加一行一列方便处理边界情况
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    # 初始化第一列，只用s1去匹配s3
    for i in range(1, len(s1) + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    # 初始化第一行，只用s2去匹配s3
    for j in range(1, len(s2) + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    # 动态规划填表
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                       (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    # 返回最终结果
    return dp[-1][-1]

# 测试示例
s1 = "abc"
s2 = "def"
s3 = "adbcef"
result = isInterleave(s1, s2, s3)
print(f"Can s1 and s2 interleave to form s3? {result}")