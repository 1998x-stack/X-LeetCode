from typing import List

def wiggle_sort(nums: List[int]) -> None:
    """
    对数组进行摆动排序 II。
    
    Args:
        nums: 需要排序的数组。
        
    Returns:
        None，原地修改数组。
    """
    # 步骤1：排序
    nums.sort()
    
    # 步骤2：找到中位数
    half = len(nums) // 2
    
    # 步骤3：分割数组并倒序，以便从两个子数组的末尾开始穿插
    smaller_nums = nums[:half][::-1]
    larger_nums = nums[half:][::-1]
    
    # 步骤4：穿插合并，交替取自两个子数组的元素
    for i in range(len(nums)):
        # 奇数索引取较大一半，偶数索引取较小一半
        if i % 2 == 0:
            nums[i] = smaller_nums[i // 2]
        else:
            nums[i] = larger_nums[i // 2]

# 测试
nums = [1, 5, 1, 1, 6, 4]
wiggle_sort(nums)
print("摆动排序后的数组:", nums)