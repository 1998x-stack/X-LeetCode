from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    旋转图像：原地顺时针旋转输入的二维矩阵 90 度。
    
    Args:
        matrix (List[List[int]]): 需要旋转的 n x n 的二维矩阵。
        
    Returns:
        None: 该方法不返回任何值，而是直接在原地修改输入的矩阵。
    """
    n = len(matrix)
    
    # 转置矩阵
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # 翻转每一行
    for i in range(n):
        matrix[i].reverse()

# 测试代码
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
rotate(matrix)

# 输出旋转后的矩阵以验证正确性
print(matrix)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]