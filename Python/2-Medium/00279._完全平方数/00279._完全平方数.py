from typing import List

def numSquares(n: int) -> int:
    """
    计算组成 n 所需的最少平方数的数量。
    
    Args:
    n: int，给定的正整数。
    
    Returns:
    int，组成 n 所需的最少平方数的数量。
    
    示例：
    >>> numSquares(12)
    3
    >>> numSquares(13)
    2
    """
    dp = [float('inf')] * (n + 1)  # 初始化 dp 数组，所有值设为无限大
    dp[0] = 0  # base case，0 不需要平方数
    for i in range(1, n + 1):  # 从 1 到 n 填充 dp 数组
        j = 1
        while j * j <= i:  # 遍历所有小于等于 i 的平方数
            dp[i] = min(dp[i], dp[i - j * j] + 1)  # 更新 dp[i]
            j += 1
    return dp[n]  # 返回结果

# 测试代码
print(numSquares(12))  # 应该输出 3
print(numSquares(13))  # 应该输出 2