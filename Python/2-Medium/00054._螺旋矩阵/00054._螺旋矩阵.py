def spiralOrder(matrix):
    """
    按顺时针螺旋顺序返回矩阵中的所有元素。

    Args:
    matrix (List[List[int]]): 一个二维整数数组。

    Returns:
    List[int]: 螺旋顺序的元素列表。
    """
    # 初始化结果列表和边界
    result = []
    if not matrix or not matrix[0]:
        return result
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while left <= right and top <= bottom:
        # 遍历上边界
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # 遍历右边界
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # 遍历下边界
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # 遍历左边界
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

# 测试代码
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix)) # 应输出: [1,2,3,6,9,8,7,4,5]

# 测试边界情况
matrix_empty = []
print(spiralOrder(matrix_empty)) # 应输出: []

matrix_one_row = [[1, 2, 3, 4]]
print(spiralOrder(matrix_one_row)) # 应输出: [1, 2, 3, 4]

matrix_one_col = [[1], [2], [3], [4]]
print(spiralOrder(matrix_one_col)) # 应输出: [1, 2, 3, 4]