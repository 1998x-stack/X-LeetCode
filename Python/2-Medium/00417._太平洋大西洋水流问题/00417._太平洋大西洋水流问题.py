from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        if m == 0 or n == 0:
            return []

        # 创建两个集合记录能够流向太平洋和大西洋的点
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(x, y, reachable):
            # 将当前点标记为可达
            reachable.add((x, y))
            # 定义四个方向的偏移量
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 判断下一个点是否在矩阵范围内且未被访问过
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in reachable and matrix[nx][ny] >= matrix[x][y]:
                    dfs(nx, ny, reachable)

        # 从太平洋的边界开始进行深度优先搜索
        for i in range(m):
            dfs(i, 0, pacific_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)

        # 从大西洋的边界开始进行深度优先搜索
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)

        # 返回能够同时流向太平洋和大西洋的点
        return list(pacific_reachable.intersection(atlantic_reachable))

# 实例化Solution类
solution = Solution()
# 测试示例
matrix = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
result = solution.pacificAtlantic(matrix)
print(result)
