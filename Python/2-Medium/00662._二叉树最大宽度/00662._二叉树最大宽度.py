from typing import Optional, List, Tuple
from collections import deque

# 定义二叉树的节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_width_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    计算给定二叉树的最大宽度。
    
    参数:
        root (Optional[TreeNode]): 二叉树的根节点。
        
    返回:
        int: 二叉树的最大宽度。
        
    示例:
        输入: [1,3,2,5,3,null,9]
        输出: 4
    """
    if not root:
        return 0
    max_width = 0
    queue = deque([(root, 0)])
    while queue:
        level_length = len(queue)
        _, first_index = queue[0]
        for _ in range(level_length):
            node, index = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
        
        last_index = queue[-1][1] if queue else index
        max_width = max(max_width, last_index - first_index + 1)
    return max_width
# 创建一个示例二叉树
#      1
#    /   \
#   3     2
#  / \     \
# 5   3     9
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

# 计算并打印最大宽度
max_width = max_width_of_binary_tree(root)
print(max_width)