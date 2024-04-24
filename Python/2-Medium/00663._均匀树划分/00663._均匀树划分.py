from typing import Optional, Tuple

class TreeNode:
    """定义二叉树节点类"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkEqualTree(root: TreeNode) -> bool:
    """检查是否可以将二叉树均匀划分为和相等的两部分"""
    def compute_total_sum(node):
        """计算二叉树的总和"""
        if not node:
            return 0
        return node.val + compute_total_sum(node.left) + compute_total_sum(node.right)
    
    def check_partition(node, target):
        """后序遍历计算子树和，并判断是否能形成目标分割"""
        if node is None:
            return False, 0
        left_found, left_sum = check_partition(node.left, target)
        right_found, right_sum = check_partition(node.right, target)
        current_sum = node.val + left_sum + right_sum
        if left_found or right_found or (current_sum == target and node != root):
            return True, current_sum
        return False, current_sum
    
    total_sum = compute_total_sum(root)
    if total_sum % 2 != 0:
        return False
    return check_partition(root, total_sum // 2)[0]

# 二叉树示例
# 创建一个简单的树: 1
#                    / \
#                   2   10
#                      /  \
#                     2    2
node1 = TreeNode(1)
node2 = TreeNode(2)
node10 = TreeNode(10)
node2_left = TreeNode(2)
node2_right = TreeNode(2)
node1.left = node2
node1.right = node10
node10.left = node2_left
node10.right = node2_right

# 检查是否可以均匀划分
print("可以均匀划分：" if checkEqualTree(node1) else "无法均匀划分")