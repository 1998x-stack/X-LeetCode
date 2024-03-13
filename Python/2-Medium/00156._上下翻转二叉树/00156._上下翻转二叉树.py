from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def upsideDownBinaryTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    上下翻转二叉树。

    Args:
    - root: Optional[TreeNode] - 二叉树的根节点。

    Returns:
    - Optional[TreeNode] - 翻转后的二叉树的根节点。

    示例:
    >>> 树 [1,2,3,4,5] 翻转后变为 [4,5,2,None,None,3,1]
    """
    # 递归基: 如果当前节点为空或者是叶子节点，直接返回当前节点
    if not root or (not root.left and not root.right):
        return root

    # 递归翻转左子树
    newRoot = upsideDownBinaryTree(root.left)

    # 当前节点的左子节点的右子节点设置为当前节点的右子节点
    root.left.right = root.right
    # 当前节点的左子节点的左子节点设置为当前节点
    root.left.left = root
    # 断开当前节点的左右子节点链接
    root.left = None
    root.right = None

    # 返回新的根节点
    return newRoot

# 辅助函数：构建二叉树
def buildTree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = buildTree(nodes, 2 * index + 1)
    root.right = buildTree(nodes, 2 * index + 2)
    return root

# 辅助函数：层次遍历
def levelOrder(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# 构建并翻转二叉树
treeNodes = [1, 2, 3, 4, 5]
root = buildTree(treeNodes)
newRoot = upsideDownBinaryTree(root)

# 打印翻转后的二叉树层次遍历结果
print(levelOrder(newRoot))