from typing import List

def largest_divisible_subset(nums: List[int]) -> List[int]:
    """
    找到给定集合中的最大整除子集。
    
    Args:
    nums: 一个整数列表。
    
    Returns:
    一个整数列表，表示最大整除子集。
    
    示例:
    >>> largest_divisible_subset([1,2,3])
    [1, 2]
    >>> largest_divisible_subset([1,2,4,8])
    [1, 2, 4, 8]
    """
    # 边界条件处理
    if not nums:
        return []
    
    # 排序，保证后面的元素都大于前面的元素
    nums.sort()
    
    n = len(nums)
    dp = [1] * n  # dp[i]表示包括第i个元素的最大整除子集的大小
    parent = [-1] * n  # parent[i]记录dp[i]是由哪个前驱节点转移而来
    
    max_size = 1  # 记录最大子集的大小
    max_val_index = 0  # 记录达到最大子集大小时的索引
    
    # 动态规划计算dp和parent数组
    for i in range(1, n):
        for j in range(i):
            # 如果nums[i]能被nums[j]整除，并且包含nums[j]的子集大小加1大于dp[i]
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j  # 更新前驱节点为j
                # 更新最大子集的大小和索引
                if dp[i] > max_size:
                    max_size = dp[i]
                    max_val_index = i
    
    # 通过parent数组回溯构造最大整除子集
    result = []
    while max_val_index != -1:
        result.append(nums[max_val_index])
        max_val_index = parent[max_val_index]
    
    return result[::-1]  # 反转结果列表，因为我们是从后往前回溯的

# 测试代码
test_cases = [
    [1, 2, 3],
    [1, 2, 4, 8]
]

# 运行测试用例
results = [largest_divisible_subset(nums) for nums in test_cases]
print(results)