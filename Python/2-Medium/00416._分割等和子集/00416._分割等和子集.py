from typing import List

def can_partition(nums: List[int]) -> bool:
    """
    判断给定的非负整数数组是否可以分割成两个子集，使得这两个子集的总和相等。
    
    参数:
    nums: 给定的非负整数数组
    
    返回:
    布尔值，表示是否可以分割成两个和相等的子集。
    
    示例:
    >>> can_partition([1, 5, 11, 5])
    True
    >>> can_partition([1, 2, 3, 5])
    False
    """
    total_sum = sum(nums)
    # 如果总和是奇数，直接返回False
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # 不选择任何元素时，总和为0
    
    for num in nums:
        # 从target倒序遍历到num
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

# 测试代码
test_cases = [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
]

for nums, expected in test_cases:
    result = can_partition(nums)
    print(f"nums: {nums}, expected: {expected}, got: {result}")