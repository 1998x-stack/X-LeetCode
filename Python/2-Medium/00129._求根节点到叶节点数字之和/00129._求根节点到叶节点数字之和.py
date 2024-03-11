from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: Optional[TreeNode]) -> int:
    """
    计算从根节点到叶子节点的所有路径所代表的数字之和。
    
    Args:
    - root: Optional[TreeNode], 二叉树的根节点。
    
    Returns:
    - int, 所有路径代表的数字之和。
    
    示例:
    >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> sumNumbers(root)
    25
    """
    def dfs(node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0
        current_sum = current_sum * 10 + node.val
        if not node.left and not node.right:
            return current_sum
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)
    
    return dfs(root, 0)

# 构建示例二叉树
#     1
#    / \
#   2   3
root = TreeNode(1, TreeNode(2), TreeNode(3))

# 调用函数并打印结果
print(sumNumbers(root))  # 预期输出：25