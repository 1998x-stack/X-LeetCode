from typing import Optional, List, Dict, Tuple
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        寻找二叉树中所有重复的子树。

        Args:
        root (Optional[TreeNode]): 二叉树的根节点。

        Returns:
        List[Optional[TreeNode]]: 所有重复的子树的根节点列表。
        """
        # 存储每个子树的序列化形式及其出现次数
        trees = defaultdict(int)
        duplicates = []
        def serialize(node: Optional[TreeNode])->str:
            if not node:
                return '#'
            serial = '{},{},{}'.format(node.val, serialize(node.left), serialize(node.right))
            trees[serial] += 1
            if trees[serial] == 2:
                duplicates.append(node.val)
            return serial
        serialize(root)
        return duplicates

# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)
solution = Solution()
print(solution.findDuplicateSubtrees(root)) # [[2, 4], [4]]