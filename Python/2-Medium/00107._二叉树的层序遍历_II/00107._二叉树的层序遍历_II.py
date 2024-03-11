from typing import List, Optional
from collections import deque

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    """
    二叉树的层序遍历 II
    
    参数:
        root (Optional[TreeNode]): 二叉树的根节点
    
    返回:
        List[List[int]]: 自底向上的层序遍历结果
    
    示例:
        输入: [3,9,20,null,null,15,7]
        输出: [[15,7],[9,20],[3]]
    """
    # 处理空树的情况
    if not root:
        return []
    
    # 初始化队列，用于层序遍历
    queue = deque([root])
    # 初始化结果列表
    result = []
    
    # 当队列不为空，执行层序遍历
    while queue:
        # 记录当前层的节点数量
        level_length = len(queue)
        # 初始化当前层的结果列表
        level_nodes = []
        
        for _ in range(level_length):
            # 将当前节点从队列中出队
            node = queue.popleft()
            # 将当前节点的值加入到当前层的结果列表
            level_nodes.append(node.val)
            # 如果当前节点有左子节点，则将左子节点入队
            if node.left:
                queue.append(node.left)
            # 如果当前节点有右子节点，则将右子节点入队
            if node.right:
                queue.append(node.right)
        
        # 将当前层的结果加入到最终结果列表
        result.append(level_nodes)
    
    # 将结果反转，以实现自底向上的顺序
    return result[::-1]

# 示例代码运行
# 构建示例二叉树 [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 执行层序遍历
print(levelOrderBottom(root))