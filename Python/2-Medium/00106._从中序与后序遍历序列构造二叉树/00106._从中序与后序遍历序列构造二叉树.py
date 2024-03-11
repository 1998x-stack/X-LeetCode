from typing import List, Optional, Dict

# 定义二叉树的节点类
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    """
    从中序与后序遍历序列构造二叉树。

    参数:
    inorder (List[int]): 中序遍历序列。
    postorder (List[int]): 后序遍历序列。

    返回:
    Optional[TreeNode]: 构造的二叉树的根节点。
    """
    # 创建中序遍历的值到索引的映射，以便快速定位根节点
    in_map: Dict[int, int] = {val: idx for idx, val in enumerate(inorder)}
    
    def build(in_left: int, in_right: int, post_left: int, post_right: int) -> Optional[TreeNode]:
        if in_left > in_right:
            return None
        
        # 后序遍历的最后一个元素是当前子树的根节点
        root_val = postorder[post_right]
        root = TreeNode(root_val)
        
        # 在中序遍历中找到根节点的索引
        index = in_map[root_val]
        
        # 左子树的节点数
        left_size = index - in_left
        
        # 递归构造左子树
        root.left = build(in_left, index - 1, post_left, post_left + left_size - 1)
        # 递归构造右子树
        root.right = build(index + 1, in_right, post_left + left_size, post_right - 1)
        
        return root
    
    # 调用递归函数开始构造
    return build(0, len(inorder) - 1, 0, len(postorder) - 1)

# 示例中序和后序遍历序列
inorder_example = [9, 3, 15, 20, 7]
postorder_example = [9, 15, 7, 20, 3]

# 构造二叉树并返回根节点
root = buildTree(inorder_example, postorder_example)

# 为了验证我们的解决方案，我们需要一个辅助函数来以层序遍历的方式打印树
from collections import deque

def print_tree(root: Optional[TreeNode]) -> None:
    """以层序遍历的方式打印二叉树"""
    if not root:
        print("Empty Tree")
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=" ")
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("None", end=" ")
    print()

# 打印构造的二叉树
print_tree(root)