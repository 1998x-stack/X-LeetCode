from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    """二叉树节点定义类"""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def build_graph(node: Optional[TreeNode], parent: Optional[TreeNode], graph: defaultdict) -> None:
    """构建树的图表示
    
    Args:
        node: 当前树节点
        parent: 当前节点的父节点
        graph: 保存图结构的字典
    """
    if node is None:
        return
    if parent is not None:
        graph[node.val].append(parent.val)
        graph[parent.val].append(node.val)
    if node.left is not None:
        build_graph(node.left, node, graph)
    if node.right is not None:
        build_graph(node.right, node, graph)

# 定义测试二叉树结构
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """从列表构建二叉树
    
    Args:
        values: 二叉树节点值列表
    
    Returns:
        构建好的二叉树根节点
    """
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def find_closest_leaf(root: TreeNode, k: int) -> int:
    """找到目标节点 `k` 最近的叶节点
    
    Args:
        root: 二叉树根节点
        k: 目标节点的值
    
    Returns:
        离目标节点最近的叶节点值
    """
    # 用于保存无向图的结构
    graph = defaultdict(list)
    build_graph(root, None, graph)
    
    # 使用队列进行 BFS 搜索
    queue = deque([k])
    visited = {k}
    
    while queue:
        curr_node = queue.popleft()
        
        # 如果当前节点是叶节点，则直接返回
        if len(graph[curr_node]) == 1 and curr_node != root.val:
            return curr_node
        
        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        
# 测试样例
values = [1, 2, 3, 4, None, None, 5, None, None, 6, 7]
k = 3
root = build_tree(values)

# 查找距离目标节点 `k` 最近的叶节点
closest_leaf = find_closest_leaf(root, k)
print(closest_leaf)