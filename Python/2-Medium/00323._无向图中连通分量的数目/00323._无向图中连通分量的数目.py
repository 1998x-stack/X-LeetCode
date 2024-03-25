from typing import List

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        # 路径压缩
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # 按秩合并
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def count(self) -> int:
        # 计算连通分量的数量
        return len(set(self.find(i) for i in range(len(self.root))))

def countComponents(n: int, edges: List[List[int]]) -> int:
    uf = UnionFind(n)
    for edge in edges:
        uf.union(edge[0], edge[1])
    return uf.count()

# 示例输入
n = 5
edges = [[0, 1], [1, 2], [3, 4]]

# 运行代码
print(countComponents(n, edges))