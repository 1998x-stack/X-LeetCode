from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # 初始化全局变量，记录最长同值路径的长度
        self.max_length = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        寻找最长同值路径的主函数

        Args:
        root (Optional[TreeNode]): 二叉树的根节点

        Returns:
        int: 最长同值路径的长度
        """
        self.dfs(root)
        return self.max_length

    def dfs(self, node: Optional[TreeNode]) -> int:
        """
        深度优先搜索，以node为起点向下寻找最长同值路径

        Args:
        node (Optional[TreeNode]): 当前遍历的节点

        Returns:
        int: 从当前节点出发的最长同值单侧路径长度
        """
        if node is None:
            return 0
        
        # 递归计算左右子节点的同值路径长度
        left_path_length = self.dfs(node.left)
        right_path_length = self.dfs(node.right)
        
        # 初始化从当前节点向左、向右的同值路径长度
        left_univalue_length = 0
        right_univalue_length = 0
        
        # 如果左子节点与当前节点值相同，则当前节点的左同值路径长度更新
        if node.left and node.left.val == node.val:
            left_univalue_length = left_path_length + 1
        # 如果右子节点与当前节点值相同，则当前节点的右同值路径长度更新
        if node.right and node.right.val == node.val:
            right_univalue_length = right_path_length + 1
        
        # 更新全局最长同值路径长度
        self.max_length = max(self.max_length, left_univalue_length + right_univalue_length)
        
        # 返回以当前节点为终点的最长同值路径长度
        return max(left_univalue_length, right_univalue_length)

# 示例构建二叉树
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

# 创建解决方案实例，并求解
solution = Solution()
output = solution.longestUnivaluePath(root)
print(output)  # 2