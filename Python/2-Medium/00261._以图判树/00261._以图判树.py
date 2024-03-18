from typing import List, Tuple

class UnionFind:
    def __init__(self, size: int) -> None:
        """并查集初始化
        Args:
            size: 并查集的大小，即节点的数量
        """
        self.parent = [i for i in range(size)]  # 每个节点的父节点初始化为自己
    
    def find(self, x: int) -> int:
        """查找节点x的根节点
        Args:
            x: 要查找根节点的节点
        Returns:
            int: 节点x的根节点
        """
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """合并节点x和y所在的集合
        Args:
            x: 节点x
            y: 节点y
        Returns:
            bool: 如果合并成功（即x和y原本不在同一集合中），返回True，否则返回False
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False  # x和y已经在同一个集合中，合并失败
        self.parent[rootX] = rootY  # 合并集合
        return True

def validTree(n: int, edges: List[List[int]]) -> bool:
    """检查无向图是否构成一棵有效的树
    Args:
        n: 节点的数量
        edges: 边的列表
    Returns:
        bool: 如果给定的图可以构成一棵有效的树，则返回True，否则返回False
    """
    # 边的数量必须是节点数量减一
    if len(edges) != n - 1:
        return False
    
    # 初始化并查集
    uf = UnionFind(n)
    
    # 遍历所有边，尝试合并两个节点
    for x, y in edges:
        if not uf.union(x, y):  # 如果x和y已经在同一个集合中，说明产生了环路
            return False
    
    # 如果边的数量正确，并且没有发现环路，那么这是一棵树
    return True

# 测试用例
print(validTree(5, [[0,1], [0,2], [0,3], [1,4]]))  # 应该返回True
print(validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))  # 应该返回False