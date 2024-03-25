from typing import List, Dict, Set

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    """
    找到所有最小高度树的根节点。

    Args:
    n (int): 节点的数量。
    edges (List[List[int]]): 边的列表，每个元素是一对节点。

    Returns:
    List[int]: 所有最小高度树的根节点列表。
    """
    if n == 1:  # 如果只有一个节点，直接返回这个节点
        return [0]
    # 构建图的邻接表和每个节点的度
    graph = [set() for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
        degree[u] += 1
        degree[v] += 1
    
    # 找到所有初始的叶子节点
    leaves = [i for i in range(n) if degree[i] == 1]
    
    # 逐层剥离叶子节点，直到剩下的节点数小于等于2
    while n > 2:
        n -= len(leaves)  # 更新剩余节点的数量
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()  # 获取叶子节点的邻居并从图中删除叶子节点
            graph[neighbor].remove(leaf)
            degree[neighbor] -= 1  # 更新邻居的度
            if degree[neighbor] == 1:  # 如果邻居变成叶子节点，加入到新的叶子节点列表中
                new_leaves.append(neighbor)
        leaves = new_leaves  # 准备下一轮的叶子节点剥离
    
    return leaves  # 返回剩下的节点作为最小高度树的根节点

# 测试用例
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
# 运行代码并打印结果
print(findMinHeightTrees(n, edges))