class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        """寻找x的根节点，并进行路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def findRedundantConnection(edges):
    uf = UnionFind(len(edges) + 1)
    for edge in edges:
        if not uf.union(*edge):
            return edge

edges = [[1,2], [1,3], [2,3]]
print(findRedundantConnection(edges)) # [2,3]