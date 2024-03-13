from typing import Optional, Generator

class TreeNode:
    def __init__(self, x: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = x
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """
        初始化二叉搜索树迭代器，使用栈来存储从根节点到最左侧节点的路径。
        
        :param root: 二叉搜索树的根节点
        """
        self.stack = []
        self._leftmost_inorder(root)
    
    def _leftmost_inorder(self, root: Optional[TreeNode]):
        """
        将给定节点到最左侧节点的路径推入栈中。
        
        :param root: 当前节点
        """
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        """
        返回二叉搜索树中的下一个最小的数。
        
        :return: 下一个最小的数
        """
        # 弹出栈顶元素，即当前的最小节点
        topmost_node = self.stack.pop()
        # 如果这个节点有右子节点，则将右子节点及其所有左子节点推入栈中
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val
    
    def hasNext(self) -> bool:
        """
        返回二叉搜索树中是否还有下一个更小的数。
        
        :return: 如果还有下一个最小的数，则返回True；否则返回False
        """
        return len(self.stack) > 0

# 构建示例二叉搜索树
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))

# 初始化迭代器并演示其功能
iterator = BSTIterator(root)
operations = ['next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext']
results = []

for op in operations:
    if op == 'next':
        results.append(iterator.next())
    elif op == 'hasNext':
        results.append(iterator.hasNext())

print(results)  # [3, True, 7, True, 9, True, 15, True, 20, False]