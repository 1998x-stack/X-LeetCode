from typing import List

def quick_select(nums: List[int], left: int, right: int, k: int) -> int:
    """
    快速选择算法的辅助函数，用于找到数组中第k大的元素。
    
    参数:
    - nums: List[int], 输入的数组
    - left: int, 考虑的数组部分的左边界
    - right: int, 考虑的数组部分的右边界
    - k: int, 需要找的第k大的元素的索引
    
    返回:
    - int, 数组中第k大的元素
    """
    # 基准选择（这里简单选择最右侧元素作为基准）
    pivot = nums[right]
    pIndex = left
    for i in range(left, right):
        # 如果当前元素小于等于基准，交换到左侧
        if nums[i] <= pivot:
            nums[i], nums[pIndex] = nums[pIndex], nums[i]
            pIndex += 1
    # 把基准放到中间
    nums[pIndex], nums[right] = nums[right], nums[pIndex]
    
    # 如果基准正好是第k大的元素
    if len(nums) - pIndex == k:
        return nums[pIndex]
    elif len(nums) - pIndex > k:
        # 如果第k大的元素在基准右侧，递归右侧
        return quick_select(nums, pIndex + 1, right, k)
    else:
        # 如果第k大的元素在基准左侧，递归左侧
        return quick_select(nums, left, pIndex - 1, k)

def findKthLargest(nums: List[int], k: int) -> int:
    """
    找到数组中第k个最大的元素。
    
    参数:
    - nums: List[int], 输入的数组
    - k: int, 需要找的第k大的元素
    
    返回:
    - int, 数组中第k大的元素
    """
    return quick_select(nums, 0, len(nums) - 1, k)

# 测试示例
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))  # 5