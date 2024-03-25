from typing import List, Optional, Dict
# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        寻找并删除二叉树的所有叶子节点。

        Args:
            root (Optional[TreeNode]): 二叉树的根节点。

        Returns:
            List[List[int]]: 按从根到叶的顺序，每层叶子节点的值。
        """
        # 存储叶子节点，键为叶子节点的深度，值为该深度的所有叶子节点的值
        leaves = {}

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1  # 空节点的深度为-1
            
            left_depth = dfs(node.left)  # 左子树深度
            right_depth = dfs(node.right)  # 右子树深度
            depth = max(left_depth, right_depth) + 1  # 当前节点深度
            
            # 按深度添加节点值
            if depth not in leaves:
                leaves[depth] = []
            leaves[depth].append(node.val)
            
            return depth
        
        dfs(root)  # 执行DFS搜索
        
        # 按深度顺序返回叶子节点的值
        return [leaves[depth] for depth in sorted(leaves)]

# 构建示例二叉树
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

# 解决方案实例
sol = Solution()
# 调用并打印结果
print(sol.findLeaves(root))  # [[4, 5, 3], [2], [1]]