from typing import Optional

class TreeNode:
    """定义一个二叉树节点类"""
    def __init__(self, x: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = x
        self.left = left
        self.right = right

def tree2str(t: Optional[TreeNode]) -> str:
    """
    根据二叉树创建字符串

    Args:
    t (TreeNode): 二叉树的根节点

    Returns:
    str: 构造得到的字符串

    Examples:
    输入: Binary tree: [1, 2, 3, 4]
       1
     /   \
    2     3
   /    
  4     

    输出: "1(2(4))(3)"

    Explanation: 原本的是"1(2(4)())(3())", 
    在你需要输出的字符串中，你需要仅仅删除不影响表示和不必要的空括号对。
    """
    if not t:
        return ""

    # 当前节点值转为字符串
    result = str(t.val) + (f"({tree2str(t.left)})" if t.left else "") + (f"({tree2str(t.right)})" if t.right else "")
    
    # # 如果有左子树或者没有左子树但有右子树
    # if t.left or t.right:
    #     result += f"({tree2str(t.left)})"  # 递归处理左子树
    #     if t.right:
    #         result += f"({tree2str(t.right)})"  # 递归处理右子树

    return result

# 测试代码
# 创建一个示例树：1(2(4))(3)
node4 = TreeNode(4)
node2 = TreeNode(2, left=node4)
node3 = TreeNode(3)
root = TreeNode(1, left=node2, right=node3)

# 生成字符串
result = tree2str(root)
print(result)  # 应该输出：1(2(4))(3)