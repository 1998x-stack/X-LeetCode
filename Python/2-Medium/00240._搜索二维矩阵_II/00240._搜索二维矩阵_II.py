from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    在一个每行从左到右升序、每列从上到下升序的二维矩阵中搜索一个给定的值。

    Args:
    - matrix: List[List[int]]，一个二维列表，代表给定的矩阵。
    - target: int，需要搜索的目标值。

    Returns:
    - bool，如果矩阵中存在目标值，则返回 True；否则返回 False。

    示例:
    >>> search_matrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
    True
    >>> search_matrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)
    False
    """
    if not matrix or not matrix[0]:
        return False  # 矩阵为空的边界条件处理

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # 从右上角开始搜索

    while row < rows and col >= 0:
        if matrix[row][col] == target:  # 找到目标值
            return True
        elif matrix[row][col] < target:  # 当前值小于目标值，向下移动
            row += 1
        else:  # 当前值大于目标值，向左移动
            col -= 1

    return False  # 搜索结束，未找到目标值

# 示例测试
matrix_example_1 = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target_example_1 = 5
target_example_2 = 20

# 运行测试用例
print(search_matrix(matrix_example_1, target_example_1))  # 应输出 True
print(search_matrix(matrix_example_1, target_example_2))  # 应输出 False