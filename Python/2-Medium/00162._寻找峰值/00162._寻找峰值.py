from typing import List

def find_peak_element(nums: List[int]) -> int:
    """
    使用二分查找算法寻找峰值元素的索引。
    
    Args:
    nums: 一个整数数组。
    
    Returns:
    峰值元素的索引。
    
    示例:
    >>> find_peak_element([1, 2, 3, 1])
    2
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # 如果中间元素小于其右侧元素，则峰值在右侧
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            # 否则，峰值在左侧或就是中间元素本身
            right = mid
    return left

# 运行代码
# 示例数组
nums_example = [1, 2, 3, 1]
# 寻找峰值
peak_index = find_peak_element(nums_example)
print(peak_index)  # 输出: 2