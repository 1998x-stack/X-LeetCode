from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root: Optional[TreeNode]) -> int:
    """
    在给定的二叉树结构中，计算不触动警报情况下能偷窃到的最大金额。
    
    Args:
    - root: TreeNode，二叉树的根节点
    
    Returns:
    - int，能偷窃到的最大金额
    
    说明:
    使用深度优先搜索（DFS）遍历树的每个节点，并采用动态规划的方式解决问题。
    对于每个节点，分别计算偷和不偷时的最大金额，并返回。
    """
    
    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        # 空节点，不偷和偷的金额都是0
        if not node:
            return (0, 0)
        
        # 递归处理左右子节点
        left = dfs(node.left)
        right = dfs(node.right)
        
        # 不偷当前节点时的最大金额：左子节点的最大金额 + 右子节点的最大金额
        # 由于不偷当前节点，所以左右子节点偷与不偷的最大值都可以考虑
        not_rob = max(left) + max(right)
        
        # 偷当前节点时的最大金额：当前节点的值 + 左右子节点不偷时的金额
        rob = node.val + left[0] + right[0]
        
        # 返回当前节点不偷和偷时的最大金额
        return (not_rob, rob)
    
    # 计算给定树的根节点开始，不偷和偷时的最大金额，并返回其最大值
    return max(dfs(root))

# 构建示例树进行测试
# 示例树1
root1 = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
# 示例树2
root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))

# 运行代码并打印结果
print(f"示例树1的最大盗窃金额：{rob(root1)}")  # 期望输出：7
print(f"示例树2的最大盗窃金额：{rob(root2)}")  # 期望输出：9