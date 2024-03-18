from typing import List

def majority_element(nums: List[int]) -> List[int]:
    """
    使用摩尔投票法找出所有出现次数超过 ⌊ n/3 ⌋ 次的元素。

    Args:
    nums: 一个整数列表。

    Returns:
    出现次数超过 ⌊ n/3 ⌋ 次的元素列表。

    """
    if not nums:
        return []

    # 初始化两个候选者和它们的计票数
    candidate1, candidate2, count1, count2 = 0, 0, 0, 0

    # 第一次遍历：找出两个主要候选者
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # 重置计票数，准备确认候选者
    count1, count2 = 0, 0

    # 第二次遍历：确认候选者
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    n = len(nums)
    
    # 根据最终计票数，确定最终结果
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# 运行示例
nums_examples = [
    [3, 2, 3],
    [1],
    [1, 2],
    [2, 2, 1, 3],
    [3,3,4]
]
for nums in nums_examples:
    print(f"输入: {nums}, 输出: {majority_element(nums)}")