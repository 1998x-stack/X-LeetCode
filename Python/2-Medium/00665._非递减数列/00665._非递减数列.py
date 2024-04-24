from typing import List

def check_non_decreasing(nums: List[int]) -> bool:
    """
    检查通过修改最多一个元素后，数组是否能成为非递减数组。
    
    参数:
        nums (List[int]): 输入的整数数组。
    
    返回:
        bool: 如果可以修改最多一个元素使数组非递减返回 True，否则返回 False。
    
    示例:
        >>> check_non_decreasing([4, 2, 3])
        True
        >>> check_non_decreasing([3, 4, 2, 3])
        False
    """
    modify_count = 0
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            if modify_count == 1:
                return False
            modify_count += 1
            if i == 1 or nums[i - 2] <= nums[i]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
                
    return True


# 测试代码
if __name__ == "__main__":
    test_cases = [
        ([4, 2, 3], True),
        ([3, 4, 2, 3], False),
        ([1], True)
    ]
    
    for nums, expected in test_cases:
        result = check_non_decreasing(nums)
        print(f"check_non_decreasing({nums}) = {result} (Expected: {expected})")