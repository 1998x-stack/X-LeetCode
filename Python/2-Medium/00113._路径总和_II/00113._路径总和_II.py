from typing import Optional, List, Tuple

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    """
    寻找所有从根节点到叶子节点的路径，这些路径上的节点值之和等于给定的目标和。

    Args:
    - root: Optional[TreeNode], 二叉树的根节点。
    - targetSum: int, 目标和。

    Returns:
    - List[List[int]]: 符合条件的路径集合。

    """
    # 结果列表
    paths = []
    
    # 辅助函数，用于递归寻找路径
    def findPaths(node: Optional[TreeNode], currentSum: int, path: List[int]):
        if not node:
            return
        
        # 加入当前节点到路径
        currentSum += node.val
        path.append(node.val)
        
        # 如果是叶子节点且当前路径和等于目标和，则将其加入结果集
        if not node.left and not node.right and currentSum == targetSum:
            paths.append(path.copy())

        # 递归遍历左右子树
        findPaths(node.left, currentSum, path)
        findPaths(node.right, currentSum, path)
        
        # 回溯，从路径中移除当前节点
        path.pop()
    
    # 从根节点开始递归寻找路径
    findPaths(root, 0, [])
    return paths

# 测试代码
# 构建一个测试用例的二叉树
#    5
#   / \
#  4   8
# /   / \
#11  13  4
#/  \    / \
#7    2  5   1
root = TreeNode(5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))

# 目标和为 22
targetSum = 22

# 调用函数并打印结果
paths = pathSum(root, targetSum)
for path in paths:
    print(path)