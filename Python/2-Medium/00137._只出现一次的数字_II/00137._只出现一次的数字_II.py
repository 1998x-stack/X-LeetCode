from typing import List

def singleNumber(nums: List[int]) -> int:
    """
    找出数组中唯一一个不是出现三次的数字。
    
    参数:
    nums: 包含整数的列表，其中除了一个元素出现一次外，其他元素都出现三次。
    
    返回:
    int: 只出现一次的那个数字。
    
    示例:
    >>> singleNumber([2,2,3,2])
    3
    >>> singleNumber([0,1,0,1,0,1,99])
    99
    """
    once, twice = 0, 0
    for num in nums:
        # 更新once和twice
        once = ~twice & (once ^ num)
        twice = ~once & (twice ^ num)
    return once

# 测试示例
test_cases = [
    ([2, 2, 3, 2], 3),
    ([0, 1, 0, 1, 0, 1, 99], 99),
]

# 运行测试用例
results = [(nums, singleNumber(nums)) for nums, expected in test_cases]

results