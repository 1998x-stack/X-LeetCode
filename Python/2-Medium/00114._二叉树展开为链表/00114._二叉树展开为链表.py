from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: Optional[TreeNode]) -> None:
    """
    将二叉树展开为链表
    
    Args:
    - root: TreeNode - 二叉树的根节点
    
    Returns:
    None - 直接在原地修改二叉树结构
    """
    # 当前节点为空时返回
    if not root:
        return
    
    # 先将左右子树分别展开
    flatten(root.left)
    flatten(root.right)
    
    # 保存右子树的引用
    right = root.right
    # 将左子树插入到右子树的位置
    root.right = root.left
    root.left = None  # 清空左子树
    
    # 找到现在右子树的最末端节点，并将保存的原右子树接上去
    p = root
    while p.right:
        p = p.right
    p.right = right

# 构造示例二叉树
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(5, None, TreeNode(6))

# 展开二叉树为链表
flatten(root)

# 验证结果，按顺序输出展开后链表的每个节点值
def print_flatten_tree(root: Optional[TreeNode]):
    """顺序输出展开后的链表节点值"""
    current = root
    while current:
        print(current.val, end=" -> ")
        current = current.right
    print("None")

# 输出展开后的链表
print_flatten_tree(root)