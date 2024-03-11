from typing import Optional, List
from collections import deque

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    实现二叉树的锯齿形层序遍历

    参数:
        root (Optional[TreeNode]): 二叉树的根节点

    返回:
        List[List[int]]: 锯齿形层序遍历的结果
    """
    # 如果根节点为空，则直接返回空列表
    if not root:
        return []

    # 初始化队列，将根节点加入队列
    queue = deque([root])
    # 初始化结果列表
    result = []
    # 标志位，用于控制遍历方向
    left_to_right = True

    # 当队列不为空时，进行遍历
    while queue:
        # 当前层的节点数
        level_length = len(queue)
        # 当前层的遍历结果
        level = []

        for _ in range(level_length):
            # 根据遍历方向从队列中取出节点
            node = queue.popleft()
            # 如果当前是从左到右遍历，则正常添加节点值
            if left_to_right:
                level.append(node.val)
            # 如果当前是从右到左遍历，则将节点值插入到列表开头
            else:
                level.insert(0, node.val)
            
            # 将节点的左右子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 添加当前层的遍历结果到最终结果列表中
        result.append(level)
        # 切换遍历方向
        left_to_right = not left_to_right
    
    return result

# 构建示例二叉树
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

# 调用函数并打印结果
zigzag_result = zigzagLevelOrder(root)
print(zigzag_result)