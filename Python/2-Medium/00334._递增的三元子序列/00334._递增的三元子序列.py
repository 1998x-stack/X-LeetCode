from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    """
    检查一个数组中是否存在长度为3的递增子序列。
    
    Args:
    nums: List[int] 输入的整数数组
    
    Returns:
    bool 表示数组中是否存在长度为3的递增子序列
    
    示例:
    >>> increasingTriplet([1, 2, 3, 4, 5])
    True
    >>> increasingTriplet([5, 4, 3, 2, 1])
    False
    >>> increasingTriplet([2, 1, 5, 0, 4, 6])
    True
    """
    # 初始化两个变量，first 和 second，用于存储遍历过程中遇到的最小值和次小值
    first, second = float('inf'), float('inf')
    for num in nums:
        if num <= first:  # 更新最小值
            first = num
        elif num <= second:  # 更新次小值
            second = num
        else:  # 找到了一个比first和second都大的数，即存在递增的三元子序列
            return True
    return False

# 运行代码并测试
test_cases = [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([2, 1, 5, 0, 4, 6], True)
]

# 执行测试并打印结果
results = {}
for nums, expected in test_cases:
    result = increasingTriplet(nums)
    results[str(nums)] = "通过" if result == expected else "失败"

print