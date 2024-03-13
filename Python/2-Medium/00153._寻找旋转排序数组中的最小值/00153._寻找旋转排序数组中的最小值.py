from typing import List

def findMin(nums: List[int]) -> int:
    """
    寻找旋转排序数组中的最小值

    Args:
    nums (List[int]): 旋转排序的数组

    Returns:
    int: 数组中的最小值

    示例:
    >>> findMin([3,4,5,1,2])
    1
    >>> findMin([4,5,6,7,0,1,2])
    0
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # 如果中间元素小于最右边元素，最小值在左半部分
        if nums[mid] < nums[right]:
            right = mid
        else:
            # 最小值在右半部分
            left = mid + 1
    # 当左指针等于右指针时，找到最小值
    return nums[left]

# 测试用例
test_cases = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11)  # 未旋转的数组
]

# 运行测试用例，验证代码正确性
results = []
for nums, expected in test_cases:
    result = findMin(nums)
    results.append((nums, result == expected, result))

print(results)