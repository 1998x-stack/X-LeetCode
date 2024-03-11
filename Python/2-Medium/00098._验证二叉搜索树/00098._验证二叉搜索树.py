from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    验证二叉搜索树

    参数:
        root (Optional[TreeNode]): 二叉树的根节点
    
    返回:
        bool: 如果是二叉搜索树，返回 True；否则，返回 False。
    """
    def validate(node, low=float('-inf'), high=float('inf')) -> bool:
        # 如果当前节点为空，认为是有效的
        if not node:
            return True
        
        # 如果节点值不在允许的范围内，返回 False
        if node.val <= low or node.val >= high:
            return False
        
        # 递归检查左子树和右子树，更新上下界
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    
    return validate(root)

# 测试代码
# 构建示例树：[2,1,3]
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
# 构建示例树：[5,1,4,null,null,3,6]
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

# 验证
print(isValidBST(root1))  # 应当输出 True
print(isValidBST(root2))  # 应当输出 False