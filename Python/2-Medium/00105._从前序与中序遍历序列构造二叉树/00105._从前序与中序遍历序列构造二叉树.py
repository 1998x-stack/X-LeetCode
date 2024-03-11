from typing import List, Optional, Dict

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    根据给定的前序遍历和中序遍历构建二叉树。
    
    参数:
        preorder (List[int]): 前序遍历结果
        inorder (List[int]): 中序遍历结果
    
    返回:
        TreeNode: 构建的二叉树的根节点
    """
    
    # 创建中序遍历的值到索引的映射，以便快速定位根节点
    index_map: Dict[int, int] = {value: idx for idx, value in enumerate(inorder)}
    
    def arrayToTree(left: int, right: int) -> Optional[TreeNode]:
        """
        递归函数，用于根据前序和中序遍历的子序列构建二叉树。
        
        参数:
            left (int): 中序遍历子序列的起始索引
            right (int): 中序遍历子序列的结束索引
        
        返回:
            TreeNode: 构建的二叉树的子树的根节点
        """
        # 递归的基本情况
        if left > right:
            return None
        
        # 前序遍历的第一个元素是根节点
        nonlocal preorder_index
        root_value = preorder[preorder_index]
        root = TreeNode(root_value)
        
        # 在中序遍历中定位根节点的索引
        index = index_map[root_value]
        
        # 移动到下一个根节点
        preorder_index += 1
        
        # 递归构建左子树和右子树
        root.left = arrayToTree(left, index - 1)
        root.right = arrayToTree(index + 1, right)
        
        return root
    
    preorder_index = 0
    return arrayToTree(0, len(inorder) - 1)

# 测试代码
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = buildTree(preorder, inorder)

# 为了验证构建的二叉树，我们可以进行一个简单的层序遍历打印
from collections import deque

def printTree(root: Optional[TreeNode]):
    """
    层序遍历打印二叉树
    
    参数:
        root (Optional[TreeNode]): 二叉树的根节点
    """
    if not root:
        print("Empty tree")
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

printTree(root)