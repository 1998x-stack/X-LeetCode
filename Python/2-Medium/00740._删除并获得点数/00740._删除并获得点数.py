from typing import List

def delete_and_earn(nums: List[int]) -> int:
    """
    计算在数组`nums`中删除数字并获得最大点数。
    参数:
    - nums: 一个整数数组，代表可以删除的数字
    返回:
    - int: 最大可获得的点数

    示例:
    >>> delete_and_earn([3, 4, 2])
    6
    """
    # 如果 nums 为空，直接返回 0
    if not nums:
        return 0

    # 获取 nums 中的最大值
    max_num = max(nums)
    # 创建一个数组存储各个数的总点数
    points = [0] * (max_num + 1)
    for num in nums:
        points[num] += num  # 累积每个数字的点数

    # 初始化 dp 数组
    dp = [0] * (max_num + 1)
    dp[1] = points[1]
    
    # 填充 dp 数组
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

    return dp[max_num]

# 测试代码的功能
test_nums = [3, 4, 2]
max_points = delete_and_earn(test_nums)
print(max_points)