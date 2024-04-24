from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root: Optional[TreeNode]) -> List[List[str]]:
    """
    根据给定的二叉树 root，返回其二维打印表示。

    Args:
    root (Optional[TreeNode]): 二叉树的根节点。

    Returns:
    List[List[str]]: 二叉树的二维打印列表。

    示例:
    >>> root = TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3))
    >>> print_tree(root)
    [['', '', '', '1', '', '', ''],
     ['', '2', '', '', '', '3', ''],
     ['', '', '4', '', '', '', '']]
    """
    def tree_height(node):
        if not node:
            return 0
        return 1 + max(tree_height(node.left), tree_height(node.right))
    
    height = tree_height(root)
    width = 1<< height -1
    matrix = [
        [''] * width for _ in range(height)
    ]
    def fill_matrix(node, row, left, right):
        if not node:
            return 
        mid = (left + right) // 2
        matrix[row][mid] = str(node.val)
        fill_matrix(node.left, row + 1, left, mid - 1)
        fill_matrix(node.right, row + 1, mid + 1, right)
    
    fill_matrix(root, 0, 0, width - 1)
    return matrix

# 构造示例树并打印输出结果
root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
print(print_tree(root))