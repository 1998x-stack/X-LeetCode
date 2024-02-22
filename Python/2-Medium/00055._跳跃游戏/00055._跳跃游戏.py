from typing import List

def can_jump(nums: List[int]) -> bool:
    """
    判断是否能跳到数组的最后一个位置。
    
    使用贪心算法，每次跳跃尽可能远，更新能到达的最远距离。
    
    Args:
    - nums: List[int]，一个整数数组，表示在每个位置可以跳跃的最大长度。
    
    Returns:
    - bool，如果能到达最后一个位置则返回 True，否则返回 False。
    
    示例:
    >>> can_jump([2,3,1,1,4])
    True
    >>> can_jump([3,2,1,0,4])
    False
    
    """
    max_reach = 0  # 初始化最远能到达的位置
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False  # 如果当前位置超过了最远能到达的位置，说明到不了当前位置
        max_reach = max(max_reach, i + jump)  # 更新最远能到达的位置
    return max_reach >= len(nums) - 1  # 如果最远能到达的位置大于等于最后一个位置，则返回 True

# 测试代码
test_cases = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
]

# 执行测试
for nums, expected in test_cases:
    result = can_jump(nums)
    print(f"can_jump({nums}) = {result} (Expected: {expected})")