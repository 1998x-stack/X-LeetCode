from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        使用深度优先搜索（DFS）计算岛屿数量。

        Args:
        grid: 二维列表，表示地图，其中'1'表示陆地，'0'表示水。

        Returns:
        int: 岛屿的数量。

        """
        if not grid or not grid[0]:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(i, j)
                    count += 1
        
        return count
    def dfs(self, x: int, y: int, grid: List[List[str]]):
        """在给定位置启动DFS，标记所有相连的陆地为已访问。"""
        # 检查边界条件
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
            return
        # 标记当前单元格为已访问
        grid[x][y] = '0'
        # 在四个方向上递归搜索
        self.dfs(x+1, y)
        self.dfs(x-1, y)
        self.dfs(x, y+1)
        self.dfs(x, y-1)
        

# 测试用例
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
solution = Solution()
print(solution.numIslands(grid))
