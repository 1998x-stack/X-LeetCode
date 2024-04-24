from typing import List, Optional

class TreeNode:
    """定义二叉树节点."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
    """
    构建最大二叉树。

    Args:
    nums (List[int]): 输入的整数数组。

    Returns:
    Optional[TreeNode]: 构建的最大二叉树的根节点。
    """
    def build_tree(left, right):
        if left > right:
            return None
        max_val = max(nums[left:right + 1])
        max_index = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = build_tree(left, max_index - 1)
        root.right = build_tree(max_index + 1, right)
        return root
    return build_tree(0, len(nums) - 1)

# 测试代码，打印出树的结构来确认是否正确
def print_tree(node: Optional[TreeNode], level: int = 0):
    """辅助函数，用于打印二叉树结构."""
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.left, level + 1)

# 示例数组
nums = [3, 2, 1, 6, 0, 5]
tree_root = construct_maximum_binary_tree(nums)
print_tree(tree_root)  # 可视化打印树