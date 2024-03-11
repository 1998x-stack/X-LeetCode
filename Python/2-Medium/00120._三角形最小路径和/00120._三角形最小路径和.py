from typing import List

def minimum_total(triangle: List[List[int]]) -> int:
    """
    计算三角形的最小路径和。

    Args:
    triangle: 一个列表的列表，表示三角形。

    Returns:
    一个整数，表示最小路径和。

    示例:
    >>> minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]])
    11
    """
    # 获取三角形的行数
    n = len(triangle)
    # 初始化动态规划数组，以三角形的最后一行为基础
    dp = triangle[-1]
    # 从倒数第二行开始向上计算每一行的最小路径和
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            # 状态转移方程：选择下一行相邻两个数中较小的一个加上当前数
            dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
    # 最终的最小路径和存储在dp数组的第一个元素
    return dp[0]

# 示例测试
test_triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

# 执行函数并打印结果
minimum_total_result = minimum_total(test_triangle)
print(minimum_total_result)