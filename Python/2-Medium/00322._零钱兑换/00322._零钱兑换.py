from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    """
    动态规划解决零钱兑换问题

    Args:
    coins (List[int]): 硬币数组
    amount (int): 总金额

    Returns:
    int: 凑成总金额所需的最少的硬币个数，如果无法凑成则返回-1

    示例:
    >>> coin_change([1, 2, 5], 11)
    3
    >>> coin_change([2], 3)
    -1
    """
    # 初始化dp数组，金额i的最小硬币数初始化为一个大数，这里用amount+1表示无法达成的状态
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # 基础情况，总金额为0时不需要硬币

    # 动态规划填表
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # 如果dp[amount]仍然是初始化的amount+1，则表示无法凑成总金额
    return dp[amount] if dp[amount] != amount + 1 else -1

# 测试代码
test_cases = [([1, 2, 5], 11), ([2], 3)]
results = [coin_change(coins, amount) for coins, amount in test_cases]
print(results)