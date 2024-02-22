from typing import List
def jump(nums: List[int]) -> int:
    """
    使用贪心算法求解跳跃游戏 II 的最小跳跃次数。

    Args:
    nums: 一个非负整数数组，表示可以从当前位置跳跃的最大长度。

    Returns:
    int: 到达数组最后一个位置的最小跳跃次数。

    示例:
    >>> jump([2,3,1,1,4])
    2
    """
    jumps, furthest, end = 0, 0, 0
    for i in range(len(nums) - 1):  # 遍历数组，但不包括最后一个元素，因为跳跃动作在到达最后一个元素前完成
        furthest = max(furthest, i + nums[i])  # 更新能够到达的最远距离
        if i == end:  # 如果当前位置达到了这一跳的最远距离
            jumps += 1  # 进行一次跳跃
            end = furthest  # 更新下一次跳跃的最远距离
    return jumps

# 测试代码
test_cases = [
    [2, 3, 1, 1, 4],  # 示例 1
    [2, 3, 0, 1, 4],  # 示例 2
]

results = [jump(case) for case in test_cases]
print(results)  # [2, 2]