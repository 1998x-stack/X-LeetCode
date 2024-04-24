from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    """
    修剪二叉搜索树，使所有节点的值位于[low, high]区间内。
    
    参数:
    root (TreeNode): 二叉搜索树的根节点。
    low (int): 区间下限。
    high (int): 区间上限。
    
    返回:
    TreeNode: 修剪后的二叉搜索树的根节点。
    
    示例:
    >>> trimBST(TreeNode(1), 1, 2)
    TreeNode(val=1, left=None, right=None)
    """
    if root is None:
        return None
    if root.val < low:
        return trimBST(root.right, low, high)
    elif root.val > high:
        return trimBST(root.left, low, high)
    else:
        root.left = trimBST(root.left, low, high)
        root.right = trimBST(root.right, low, high)
        return root
    
# 构建示例二叉搜索树
#        3
#       / \
#      0   4
#       \
#        2
#       /
#      1
root = TreeNode(3)
root.left = TreeNode(0, None, TreeNode(2, TreeNode(1)))
root.right = TreeNode(4)

# 调用函数并打印结果
trimmed_tree = trimBST(root, 1, 3)

# 辅助函数以可视化方式显示修剪后的树
def print_tree(node):
    """ 以层序遍历方式打印树 """
    if not node:
        return "Empty"
    queue = [node]
    res = []
    while queue:
        current = queue.pop(0)
        if current:
            res.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            res.append("None")
    from pprint import pprint
    pprint(res)
    return res

print_tree(trimmed_tree)