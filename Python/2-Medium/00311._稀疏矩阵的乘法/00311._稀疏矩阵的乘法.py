from typing import List

def sparse_matrix_multiplication(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    """
    计算两个稀疏矩阵的乘积。

    参数:
    mat1 (List[List[int]]): 第一个稀疏矩阵。
    mat2 (List[List[int]]): 第二个稀疏矩阵。

    返回:
    List[List[int]]: 两个稀疏矩阵的乘积。

    示例:
    >>> sparse_matrix_multiplication([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]])
    [[7, 0, 0], [-7, 0, 3]]
    """

    # 获取矩阵的维度
    mat1_rows, mat1_cols = len(mat1), len(mat1[0])
    mat2_cols = len(mat2[0])

    # 初始化结果矩阵
    result = [[0] * mat2_cols for _ in range(mat1_rows)]

    # 遍历mat1的每一行
    for i in range(mat1_rows):
        # 对于mat1的每一列，如果该元素不为0，则进行计算
        for j in range(mat1_cols):
            if mat1[i][j] != 0:
                # 对mat2的每一列进行遍历，计算乘积并累加到结果矩阵对应位置
                for k in range(mat2_cols):
                    result[i][k] += mat1[i][j] * mat2[j][k]

    return result

# 测试代码
mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
result = sparse_matrix_multiplication(mat1, mat2)
print(result)  # [[7, 0, 0], [-7, 0, 3]]