from typing import Optional, List, Tuple, Dict
from collections import deque

class TreeNode:
    """定义二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    二叉树的垂直遍历

    Args:
        root: 二叉树的根节点

    Returns:
        按垂直顺序遍历的节点值列表

    说明:
        使用BFS遍历树，并记录每个节点的位置（列号和行号）。
        根据列号聚合节点值，并根据行号对每列的节点值排序。
    """
    if not root:
        return []

    # 初始化列号与节点值及行号的映射
    columns = {}  # type: Dict[int, List[Tuple[int, int]]]
    queue = deque([(root, 0, 0)])  # 存储（节点，列号，行号）

    while queue:
        node, col, row = queue.popleft()
        
        # 将节点值及其行号添加到对应列号的列表中
        if col not in columns:
            columns[col] = []
        columns[col].append((row, node.val))
        
        # 添加子节点到队列
        if node.left:
            queue.append((node.left, col - 1, row + 1))
        if node.right:
            queue.append((node.right, col + 1, row + 1))

    # 按列号排序，并对每列的节点按行号（和节点值）排序
    sorted_columns = sorted(columns.items())
    result = [[val for _, val in sorted(values)] for _, values in sorted_columns]

    return result

# 构建示例二叉树
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 运行代码
verticalOrder(root)
