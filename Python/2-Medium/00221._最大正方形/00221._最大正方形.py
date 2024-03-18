from typing import List

def maximal_square(matrix: List[List[str]]) -> int:
    """
    在一个由 '0' 和 '1' 组成的二维二进制矩阵中，找到只包含 '1' 的最大正方形，并返回其面积。
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:  # 对于边界的行和列直接赋值为1
                    dp[i][j] = 1
                else:  # 状态转移方程
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])  # 更新最大正方形边长
    
    return max_side * max_side  # 计算最大正方形的面积

# 测试代码
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
print(maximal_square(matrix))  # 4