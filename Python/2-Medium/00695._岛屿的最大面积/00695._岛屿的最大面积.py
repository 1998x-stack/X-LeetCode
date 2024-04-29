from typing import List

def max_area_of_island(grid: List[List[int]]) -> int:
    """
    计算给定网格中最大的岛屿面积。
    
    :param grid: 二维列表，表示陆地和水的分布
    :return: 返回最大岛屿的面积
    
    示例:
    >>> max_area_of_island([[0,0,1,0,1,0], [0,1,1,0,1,0], [0,0,0,0,0,0], [0,0,0,0,1,1], [0,0,0,0,1,1]])
    4
    """
    if not grid:
        return 0
    
    visited = set()
    rows, cols = len(grid), len(grid[0])
    def dfs(x, y):
        if not(0 <= x < rows and 0 <= y < cols) or (grid[x][y] == 0) or ((x, y) in visited):
            return 0
        visited.add((x, y))
        return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
    
    max_area = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                max_area = max(max_area, dfs(i, j))
    return max_area


# 测试用例
test_grid = [
    [0,0,1,0,1,0],
    [0,1,1,0,1,0],
    [0,0,0,0,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,1,1]
]

# 运行函数并打印输出结果
print(max_area_of_island(test_grid))