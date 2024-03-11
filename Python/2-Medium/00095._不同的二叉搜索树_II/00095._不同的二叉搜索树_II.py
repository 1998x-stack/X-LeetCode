from typing import List, Optional

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_trees(n: int) -> List[Optional[TreeNode]]:
    """
    生成所有可能的二叉搜索树
    
    参数:
        n (int): 节点数
    
    返回:
        List[Optional[TreeNode]]: 所有可能的二叉搜索树的根节点列表
    """
    # 用于生成树的递归函数
    def generate(start, end):
        if start > end:
            return [None,]  # 基本情况，返回一个包含空节点的列表
        
        all_trees = []
        # 从 start 到 end，尝试每个数字作为根节点
        for i in range(start, end + 1):
            # 递归生成所有可能的左子树和右子树
            left_trees = generate(start, i - 1)
            right_trees = generate(i + 1, end)
            
            # 组合左右子树到当前根节点 i
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
                    
        return all_trees
    
    return generate(1, n) if n else []

# 调用函数并打印结果（节点值）来验证实现
def print_trees(trees: List[Optional[TreeNode]]):
    """
    打印二叉树列表的辅助函数，仅用于验证和可视化
    """
    def print_tree(node):
        if not node:
            return "None"
        return f"{node.val} ({print_tree(node.left)}, {print_tree(node.right)})"
    
    for tree in trees:
        print(print_tree(tree))

# 由于直接打印所有树可能会产生大量输出，这里仅以 n=3 作为例子进行演示
trees = generate_trees(3)
print_trees(trees[:2])  # 限制输出以避免过多的示例