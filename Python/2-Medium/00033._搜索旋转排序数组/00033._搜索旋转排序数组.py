from typing import List
def search(nums: List[int], target: int) -> int:
    """
    在旋转排序数组中搜索一个给定的目标值。
    
    Args:
    nums: 旋转排序的数组。
    target: 需要搜索的目标值。
    
    Returns:
    int: 目标值在数组中的索引，如果不存在则返回-1。
    
    示例:
    >>> search([4,5,6,7,0,1,2], 0)
    4
    >>> search([4,5,6,7,0,1,2], 3)
    -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        # 判断旋转点在左边还是右边
        if nums[mid] >= nums[left]:  # 旋转点在mid右侧
            if nums[left] <= target < nums[mid]:  # 目标值在左半边
                right = mid - 1
            else:  # 目标值在右半边
                left = mid + 1
        else:  # 旋转点在mid左侧
            if nums[mid] < target <= nums[right]:  # 目标值在右半边
                left = mid + 1
            else:  # 目标值在左半边
                right = mid - 1
                
    return -1

# 测试代码
test_cases = [
    ([4,5,6,7,0,1,2], 0),  # 示例 1
    ([4,5,6,7,0,1,2], 3)   # 示例 2
]

# 运行测试
results = [search(nums, target) for nums, target in test_cases]
print(results)