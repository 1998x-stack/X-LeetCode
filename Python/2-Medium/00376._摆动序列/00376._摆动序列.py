from typing import List

def wiggleMaxLength(nums: List[int]) -> int:
    """
    计算给定序列作为摆动序列的最长子序列的长度。
    
    Args:
    nums: List[int], 一个整数序列。
    
    Returns:
    int, 最长摆动序列的长度。
    
    示例:
    >>> wiggleMaxLength([1,7,4,9,2,5])
    6
    >>> wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
    7
    >>> wiggleMaxLength([1,2,3,4,5,6,7,8,9])
    2
    """
    if len(nums) < 2:
        return len(nums)
    
    up = down = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    
    # 返回最大摆动序列的长度
    return max(up, down)

# 运行代码并打印输出以验证正确性
test_cases = [
    ([1,7,4,9,2,5], 6),
    ([1,17,5,10,13,15,10,5,16,8], 7),
    ([1,2,3,4,5,6,7,8,9], 2),
]

# 测试并验证
for inputs, expected in test_cases:
    result = wiggleMaxLength(inputs)
    print(f"输入: {inputs}, 预期结果: {expected}, 实际结果: {result}, {'正确' if result == expected else '错误'}")