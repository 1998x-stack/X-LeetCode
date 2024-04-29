from typing import List, Set, Tuple

def number_of_distinct_islands_normalized(grid: List[List[int]]) -> int:
    """
    通过标准化岛屿形状来识别不同的岛屿。
    """
    def dfs(x: int, y: int, origin_x: int, origin_y: int, path: List[Tuple[int, int]], visited: Set[Tuple[int, int]]):
        """
        DFS搜索，使用相对于起始点的偏移量。
        """
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == 0 or (x, y) in visited:
            return
        visited.add((x, y))
        path.append((x - origin_x, y - origin_y))
        
        dfs(x + 1, y, origin_x, origin_y, path, visited)
        dfs(x - 1, y, origin_x, origin_y, path, visited)
        dfs(x, y + 1, origin_x, origin_y, path, visited)
        dfs(x, y - 1, origin_x, origin_y, path, visited)

    def normalize_island_shape(shape: List[Tuple[int, int]]) -> Tuple[Tuple[int, int]]:
        """
        标准化岛屿形状：通过将形状转换为相对于最小坐标的偏移来标准化。
        """
        if not shape:
            return tuple()
        min_x = min(pos[0] for pos in shape)
        min_y = min(pos[1] for pos in shape)
        # 归一化到最小坐标
        normalized = sorted((x - min_x, y - min_y) for x, y in shape)
        return tuple(normalized)

    if not grid:
        return 0
    
    unique_islands: Set[Tuple[Tuple[int, int]]] = set()
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                visited = set()
                path = []
                dfs(i, j, i, j, path, visited)
                # 归一化并添加到集合中
                unique_islands.add(normalize_island_shape(path))
    
    # 输出归一化后的岛屿形状，用于验证和调试
    print("Normalized unique islands shapes:", unique_islands)
    
    return len(unique_islands)


# 测试用例
test_grid = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,0,1,1],
  [0,0,0,1,1]
]
print(number_of_distinct_islands_normalized(test_grid))  # 1