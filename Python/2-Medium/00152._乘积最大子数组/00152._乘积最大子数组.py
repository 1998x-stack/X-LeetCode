from typing import List

def maxProduct(nums: List[int]) -> int:
    """
    寻找乘积最大子数组的乘积。

    Args:
    nums: List[int] - 整数数组。

    Returns:
    int - 乘积最大子数组的乘积。

    示例:
    >>> maxProduct([2,3,-2,4])
    6
    >>> maxProduct([-2,0,-1])
    0
    """
    
    if not nums:
        return 0
    
    # 初始化当前最大乘积、当前最小乘积和全局最大乘积
    max_prod = min_prod = global_max = nums[0]
    
    # 遍历数组
    for i in range(1, len(nums)):
        num = nums[i]
        
        # 计算包含当前元素的最大和最小乘积
        # 必须同时考虑当前最小乘积*当前数（处理负负得正）
        temp_max = max(num, max_prod * num, min_prod * num)
        min_prod = min(num, max_prod * num, min_prod * num)
        
        # 更新当前最大乘积
        max_prod = temp_max
        
        # 更新全局最大乘积
        global_max = max(global_max, max_prod)
    
    return global_max

# 运行测试示例
test_cases = [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
]

# 执行测试
results = {}
for nums, expected in test_cases:
    result = maxProduct(nums)
    results[str(nums)] = f"结果：{result}, 预期：{expected}, {'正确' if result == expected else '错误'}"

print(results)