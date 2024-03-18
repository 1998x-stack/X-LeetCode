from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        在二叉搜索树中查找第K小的元素。
        
        Args:
        - root: TreeNode, 二叉搜索树的根节点。
        - k: int, 指定的第K小的元素的序号。
        
        Returns:
        - int, 第K小的元素的值。
        
        示例:
        >>> tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        >>> sol = Solution()
        >>> sol.kthSmallest(tree, 1)
        1
        
        """
        # 使用中序遍历的方法，初始化计数器和结果变量
        self.k = k
        self.result = None
        self.count = 0
        
        def inorder(node: Optional[TreeNode]):
            """ 中序遍历辅助函数 """
            if not node or self.result is not None:
                return
            
            inorder(node.left)
            self.count += 1
            if self.count == self.k:
                self.result = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return self.result

# 构建示例二叉树进行测试
tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
sol = Solution()
# 查找第1小的元素
result = sol.kthSmallest(tree, 1)
print(result)  # 预期输出：1