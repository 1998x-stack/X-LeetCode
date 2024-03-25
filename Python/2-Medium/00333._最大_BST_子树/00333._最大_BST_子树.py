from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtree(root: Optional[TreeNode]) -> int:
    """
    寻找最大BST子树的大小。

    参数:
    root (Optional[TreeNode]): 二叉树的根节点。

    返回:
    int: 最大BST子树的节点数量。

    方法:
    使用后序遍历检查每个节点。
    """
    
    def postorder(node: TreeNode) -> Tuple[bool, int, int, int]:
        """
        后序遍历以验证BST并返回额外信息。
        
        返回的元组包含四个元素：
        - 当前子树是否为BST
        - 当前子树的最小值
        - 当前子树的最大值
        - 当前子树（如果是BST）的节点数
        """
        if not node:
            return True, float('inf'), float('-inf'), 0
        
        left_is_bst, left_min, left_max, left_size = postorder(node.left)
        right_is_bst, right_min, right_max, right_size = postorder(node.right)
        
        # 如果当前节点的左右子树都是BST，并且当前节点的值大于左子树的最大值且小于右子树的最小值，则当前子树是BST。
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            curr_size = 1 + left_size + right_size
            return True, min(left_min, node.val), max(right_max, node.val), curr_size
        else:
            # 如果当前子树不是BST，返回左右子树中较大BST的大小，并标记当前子树不是BST。
            return False, 0, 0, max(left_size, right_size)
    
    # 调用后序遍历函数并返回最大BST子树的大小。
    return postorder(root)[3]

# 测试代码
# 构建给定的二叉树 [10,5,15,1,8,null,7]
root = TreeNode(10)
root.left = TreeNode(5, TreeNode(1), TreeNode(8))
root.right = TreeNode(15, None, TreeNode(7))

# 执行并打印最大BST子树的大小
largest_bst_size = largestBSTSubtree(root)
print(f"最大BST子树的节点数量是: {largest_bst_size}")