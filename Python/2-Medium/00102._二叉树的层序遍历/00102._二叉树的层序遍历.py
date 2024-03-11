from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    二叉树的层序遍历

    Args:
    root (Optional[TreeNode]): 二叉树的根节点

    Returns:
    List[List[int]]: 层序遍历的结果

    示例:
    输入: [3,9,20,null,null,15,7]
    输出: [[3],[9,20],[15,7]]
    """
    if not root:
        return []
    
    queue = [root]  # 初始化队列，首先将根节点加入队列
    result = []  # 存储层序遍历的结果
    
    while queue:
        level_size = len(queue)  # 当前层的节点数
        level = []  # 存储当前层的节点值
        
        for _ in range(level_size):  # 遍历当前层的每个节点
            node = queue.pop(0)  # 从队列中取出一个节点
            level.append(node.val)  # 将节点的值加入到当前层的列表中
            
            # 如果节点有左子节点，则将左子节点加入队列
            if node.left:
                queue.append(node.left)
            # 如果节点有右子节点，则将右子节点加入队列
            if node.right:
                queue.append(node.right)
        
        result.append(level)  # 将当前层的节点值列表加入到结果中
    
    return result

# 构建示例二叉树 [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 进行层序遍历并打印结果
level_order_result = levelOrder(root)
print(level_order_result)
