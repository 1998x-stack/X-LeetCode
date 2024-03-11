from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: TreeNode) -> None:
    """
    恢复二叉搜索树。
    
    Args:
    - root: TreeNode, 二叉搜索树的根节点。
    
    Returns:
    None, 直接在原树上进行修改。
    """
    
    def find_two_swapped_nodes(root: TreeNode) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        """
        中序遍历以找到被错误交换的两个节点。
        
        Args:
        - root: TreeNode, 二叉搜索树的根节点。
        
        Returns:
        - Tuple[Optional[TreeNode], Optional[TreeNode]], 被错误交换的两个节点。
        """
        stack, x, y, pred = [], None, None, None
        
        while stack or root:
            # 向左遍历到底
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            # 检测逆序对
            if pred and root.val < pred.val:
                y = root
                if not x:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        
        return x, y
    
    def swap(x: TreeNode, y: TreeNode) -> None:
        """
        交换两个节点的值。
        
        Args:
        - x: TreeNode, 第一个节点。
        - y: TreeNode, 第二个节点。
        
        Returns:
        None, 直接在原节点上修改值。
        """
        x.val, y.val = y.val, x.val
    
    # 找到被错误交换的两个节点
    x, y = find_two_swapped_nodes(root)
    # 如果找到，交换它们的值
    if x and y:
        swap(x, y)

# 示例构建一棵被错误交换节点的二叉搜索树
root = TreeNode(1)
root.left = TreeNode(3)
root.right = None
root.left.right = TreeNode(2)

# 调用恢复函数
recoverTree(root)

# 定义一个中序遍历打印树的函数，用于验证结果
def inorder_traversal(root: TreeNode) -> None:
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)

# 打印恢复后的树，以验证结果
inorder_traversal(root)