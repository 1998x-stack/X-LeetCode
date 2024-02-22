from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    寻找数组中所有不重复的三元组，这些三元组的和为0。

    Args:
    nums (List[int]): 输入的整数数组。

    Returns:
    List[List[int]]: 所有和为0的不重复三元组列表。

    Examples:
    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> three_sum([])
    []
    >>> three_sum([0])
    []
    """
    nums.sort()  # 对数组进行排序
    n = len(nums)
    result = []

    # 遍历数组，用nums[i]作为三数之和中的第一个数
    for i in range(n):
        # 跳过重复的值
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 使用双指针寻找剩余两个数
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # 跳过重复的值
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1  # 和小于0，左指针右移
            else:
                right -= 1  # 和大于0，右指针左移
    return result


test_nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(test_nums)
print(result)
