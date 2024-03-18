from typing import List

def rob(nums: List[int]) -> int:
    """
    在环形街区偷窃的最大金额。

    Args:
    nums: 一个代表每个房屋存放金额的非负整数数组。

    Returns:
    一个整数，表示不触动警报情况下能偷窃到的最大金额。

    示例:
    >>> rob([2,3,2])
    3
    >>> rob([1,2,3,1])
    4
    """
    def rob_linear(houses: List[int]) -> int:
        """
        解决非环形街区的偷窃问题。

        Args:
        houses: 非环形街区的房屋金额数组。

        Returns:
        int: 最大可偷窃金额。
        """
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        dp = [0] * len(houses)
        dp[0], dp[1] = houses[0], max(houses[0], houses[1])
        for i in range(2, len(houses)):
            dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
        return dp[-1]
    
    if len(nums) == 1:
        return nums[0]
    
    # 不包括第一个房屋
    max_without_first = rob_linear(nums[1:])
    # 不包括最后一个房屋
    max_without_last = rob_linear(nums[:-1])
    
    # 返回两种情况的最大值
    return max(max_without_first, max_without_last)

# 测试代码
test_cases = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([0], 0),
]

for nums, expected in test_cases:
    assert rob(nums) == expected, f"For {nums}, expected {expected} but got {rob(nums)}"