from typing import Optional

class TreeNode:
    """二叉树的节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLCA(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    寻找最近公共祖先

    Args:
    - root: TreeNode, 二叉树的根节点
    - p: TreeNode, 第一个节点
    - q: TreeNode, 第二个节点

    Returns:
    - TreeNode, 最近公共祖先节点
    """
    if root is None or root == p or root == q:
        return root
    
    left = findLCA(root.left, p, q)  # 在左子树中查找
    right = findLCA(root.right, p, q)  # 在右子树中查找

    if left and right:
        return root  # 如果p和q位于root的两侧，root即为最近公共祖先
    return left if left else right  # 返回非空的子结果

# 示例使用和测试
if __name__ == "__main__":
    # 构建示例树
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # 定位特定节点
    p = root.left  # 节点5
    q = root.right  # 节点1

    # 查找最近公共祖先
    lca = findLCA(root, p, q)
    print(f"最近公共祖先为: {lca.val}")