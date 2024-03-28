from typing import List

def numberOfArithmeticSlices(nums: List[int]) -> int:
    """
    计算给定数组中所有等差子数组的数量。
    
    Args:
    nums: List[int] 输入的整数数组。
    
    Returns:
    int 返回等差子数组的总数。
    
    示例:
    >>> numberOfArithmeticSlices([1, 2, 3, 4])
    3
    """
    # 数组长度小于3，直接返回0，因为无法形成等差数列
    if len(nums) < 3:
        return 0
    
    # 初始化等差数列计数为0
    total = 0
    # dp数组用于存储以每个位置结尾的等差数列个数，初始化为0
    dp = [0] * len(nums)
    
    # 从第三个元素开始遍历
    for i in range(2, len(nums)):
        # 如果满足等差数列的条件
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            # 更新dp值，dp[i]比dp[i-1]多1，表示新增的等差数列
            dp[i] = dp[i-1] + 1
            # 累加到总数
            total += dp[i]
    
    return total

# 测试代码
print(numberOfArithmeticSlices([1, 2, 3, 4])) # 3