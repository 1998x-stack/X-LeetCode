from typing import List

def max_sub_array(nums: List[int]) -> int:
    """
    计算给定数组的最大子数组和。
    
    参数:
    nums: List[int] - 一个整数数组。
    
    返回:
    int - 最大子数组的和。
    
    示例:
    >>> max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_sub_array([1])
    1
    >>> max_sub_array([5,4,-1,7,8])
    23
    """
    # 初始化当前子数组的和为0，最大子数组和为负无穷大
    current_sum = max_sum = nums[0]
    # 遍历数组中的每个元素，除了第一个，因为我们已经用它来初始化了
    for num in nums[1:]:
        # 更新当前子数组的和，如果当前和为负，则从当前元素重新开始计算
        current_sum = max(num, current_sum + num)
        # 更新找到的最大子数组和
        max_sum = max(max_sum, current_sum)
    return max_sum

# 运行代码并打印结果进行测试
test_cases = [
    [-2,1,-3,4,-1,2,1,-5,4], # 示例 1
    [1], # 示例 2
    [5,4,-1,7,8] # 示例 3
]

# 执行测试案例
results = [max_sub_array(case) for case in test_cases]
print(results)