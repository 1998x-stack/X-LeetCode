from typing import Optional

class TreeNode:
    """二叉树节点类"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    寻找二叉搜索树的最近公共祖先
    
    Args:
        root: TreeNode, 二叉搜索树的根节点
        p: TreeNode, 节点p
        q: TreeNode, 节点q
    
    Returns:
        TreeNode, 最近公共祖先节点
    
    示例:
        输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        输出: 6 (节点6是节点2和节点8的最近公共祖先)
    """
    current = root
    while current:
        # 如果当前节点值大于p和q的值，说明p和q都在当前节点的左子树中
        if current.val > p.val and current.val > q.val:
            current = current.left
        # 如果当前节点值小于p和q的值，说明p和q都在当前节点的右子树中
        elif current.val < p.val and current.val < q.val:
            current = current.right
        else:
            # 找到最近公共祖先
            return current
    return None

# 创建二叉搜索树的节点实例以供测试
# 示例树结构请根据实际需要构建