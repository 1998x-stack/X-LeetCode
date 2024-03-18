from typing import List

def three_sum_smaller(nums: List[int], target: int) -> int:
    """
    计算数组中三个数之和小于目标值的组合数量。

    Args:
    nums: List[int] - 整数数组。
    target: int - 目标值。

    Returns:
    int - 组合数量。

    示例:
    >>> three_sum_smaller([-2, 0, 1, 3], 2)
    2
    """
    nums.sort()  # 对数组进行排序
    count = 0  # 用于计数满足条件的组合数
    n = len(nums)
    
    for i in range(n-2):  # 固定第一个数，遍历到倒数第三个即可
        left, right = i+1, n-1  # 双指针初始化
        while left < right:
            if nums[i] + nums[left] + nums[right] < target:
                # 当前固定数和左右指针指向的数之和小于目标值
                count += right - left  # 加上所有可能的组合数
                left += 1  # 移动左指针以探索新的可能性
            else:
                right -= 1  # 和过大，需要移动右指针减小和

    return count

# 测试函数
test_nums = [-2, 0, 1, 3]
test_target = 2
result = three_sum_smaller(test_nums, test_target)
print(result)