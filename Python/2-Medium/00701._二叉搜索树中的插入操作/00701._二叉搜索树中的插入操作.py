from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    将一个值插入到二叉搜索树中，并返回树的根节点。

    Args:
    root (TreeNode): 二叉搜索树的根节点。
    val (int): 要插入的值。

    Returns:
    TreeNode: 插入新值后的二叉搜索树的根节点。

    示例:
    >>> tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    >>> insert = insert_into_bst(tree, 5)
    >>> insert.right.left.val
    5
    """
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root
# 打印插入后的树结构，特别检查新插入的值
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


# 重建测试用例树结构
tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
# 要插入的值
value_to_insert = 5


# 再次执行插入操作，这次使用修正后的函数
updated_tree = insert_into_bst(tree, value_to_insert)

# 使用中序遍历来验证树的整体结构，中序遍历应该输出有序数组
print(inorder_traversal(updated_tree))