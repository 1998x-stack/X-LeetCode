from typing import List

def maxKilledEnemies(grid: List[List[str]]) -> int:
    """
    在网格中放置炸弹杀死最多敌人。

    Args:
    grid: List[List[str]], 网格信息，包含 'W', 'E', '0'。

    Returns:
    int, 最大可杀死的敌人数量。

    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    up, down, left, right = [[0] * cols for _ in range(rows)], [[0] * cols for _ in range(rows)], [[0] * cols for _ in range(rows)], [[0] * cols for _ in range(rows)]

    # 上方向敌人数量预处理
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'W': continue
            up[r][c] = (up[r-1][c] if r > 0 else 0) + (grid[r][c] == 'E')

    # 下方向敌人数量预处理
    for r in range(rows-1, -1, -1):
        for c in range(cols):
            if grid[r][c] == 'W': continue
            down[r][c] = (down[r+1][c] if r < rows - 1 else 0) + (grid[r][c] == 'E')

    # 左方向敌人数量预处理
    for c in range(cols):
        for r in range(rows):
            if grid[r][c] == 'W': continue
            left[r][c] = (left[r][c-1] if c > 0 else 0) + (grid[r][c] == 'E')

    # 右方向敌人数量预处理
    for c in range(cols-1, -1, -1):
        for r in range(rows):
            if grid[r][c] == 'W': continue
            right[r][c] = (right[r][c+1] if c < cols - 1 else 0) + (grid[r][c] == 'E')

    # 寻找最佳位置
    max_kill = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '0':
                max_kill = max(max_kill, up[r][c] + down[r][c] + left[r][c] + right[r][c])

    return max_kill

# 测试代码
grid =[
    ["0","E","0","0"],
    ["E","0","W","E"],
    ["0","E","0","0"]
]

# 运行
maxKilledEnemies(grid)
