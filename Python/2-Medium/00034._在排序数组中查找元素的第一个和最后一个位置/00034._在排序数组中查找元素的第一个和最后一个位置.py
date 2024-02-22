from typing import List
def find_first_and_last_position(nums: List[int], target: int) -> List[int]:
    """
    在排序数组中查找元素的第一个和最后一个位置。

    Args:
    nums: 排序的整数数组。
    target: 目标值。

    Returns:
    一个列表，包含目标值在数组中的开始位置和结束位置。如果目标值不存在于数组中，则返回[-1, -1]。

    示例:
    >>> find_first_and_last_position([5,7,7,8,8,10], 8)
    [3, 4]
    """
    def binary_search_left(nums, target):
        """二分查找目标值的最左侧索引。"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(nums, target):
        """二分查找目标值的最右侧索引。"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = binary_search_left(nums, target)
    right_index = binary_search_right(nums, target)
    
    # 检查是否找到目标值
    if left_index <= right_index:
        return [left_index, right_index]
    else:
        return [-1, -1]

# 运行代码并测试示例
test_nums = [5, 7, 7, 8, 8, 10]
test_target = 8
print(find_first_and_last_position(test_nums, test_target))