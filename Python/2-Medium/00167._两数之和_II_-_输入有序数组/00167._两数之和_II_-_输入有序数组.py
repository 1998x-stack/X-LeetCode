from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    使用双指针法寻找两个数，使得它们的和等于目标数target。
    
    Args:
    numbers: 一个按非递减顺序排列的整数数组。
    target: 目标和。
    
    Returns:
    一个包含两个下标的列表，这两个下标对应的数的和等于目标数target。
    下标从1开始计数。
    
    示例:
    >>> two_sum([2, 7, 11, 15], 9)
    [1, 2]
    """
    left, right = 0, len(numbers) - 1  # 初始化左右指针
    while left < right:
        sum = numbers[left] + numbers[right]  # 计算当前两数之和
        if sum == target:  # 如果和等于目标值，返回结果
            return [left + 1, right + 1]
        elif sum < target:  # 如果和小于目标值，移动左指针
            left += 1
        else:  # 如果和大于目标值，移动右指针
            right -= 1
    return []  # 根据题目描述，这种情况不会发生

# 运行代码并打印关键信息
numbers = [2, 7, 11, 15]
target = 9
print(f"输入的数组为: {numbers}")
print(f"目标和为: {target}")
print(f"结果下标为: {two_sum(numbers, target)}")