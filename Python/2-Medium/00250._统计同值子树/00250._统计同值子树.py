from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # 初始化计数器
        self.count = 0
        
        def is_univalue_subtree(node: Optional[TreeNode], parent_value: int) -> bool:
            # 空节点默认为同值子树
            if not node:
                return True
            
            # 递归检查左右子树
            left_check = is_univalue_subtree(node.left, node.val)
            right_check = is_univalue_subtree(node.right, node.val)
            
            # 如果左右子树不是同值子树，返回False
            if not left_check or not right_check:
                return False
            
            # 如果当前节点为同值子树的根，增加计数
            self.count += 1
            
            # 返回当前节点是否为同值子树的一部分
            return node.val == parent_value
        
        # 从根节点开始递归
        is_univalue_subtree(root, -float('inf'))
        return self.count

# 创建测试用例的树结构
root = TreeNode(5, 
                TreeNode(1, TreeNode(5), TreeNode(5)), 
                TreeNode(5, right=TreeNode(5)))

# 实例化Solution并调用函数
sol = Solution()
count = sol.countUnivalSubtrees(root)
print(count)  # 应输出 4，表示找到的同值子树数量