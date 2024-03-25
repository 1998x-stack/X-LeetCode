from typing import List

def integer_break(n: int) -> int:
    """
    动态规划解决整数拆分问题。
    
    Args:
    - n: int, 需要被拆分的正整数。
    
    Returns:
    - int, 最大乘积。
    
    示例:
    >>> integer_break(2)
    1
    >>> integer_break(10)
    36
    """
    # dp 数组初始化，dp[i] 表示数字 i 拆分后的最大乘积
    dp: List[int] = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            # 更新 dp[i]，尝试不同的拆分方法
            dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
    return dp[n]

# 运行代码测试
# 测试 n = 2 和 n = 10 的情况
test_cases = [2, 10]
results = [integer_break(n) for n in test_cases]
print(results)  # [1, 36]