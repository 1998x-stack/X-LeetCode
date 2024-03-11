from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    """
    使用层次遍历的方法连接二叉树每个节点的下一个右侧节点指针。
    
    Args:
    - root: Node - 二叉树的根节点。
    
    Returns:
    - Optional[Node] - 连接后的二叉树的根节点。
    
    说明:
    - 此函数通过使用哨兵节点简化每层的连接过程，并利用两个指针分别遍历当前层和链接下一层的节点。
    """
    
    if not root:
        return None
    
    # 哨兵节点，用于标记每一层的开始
    dummy = Node(0)
    # 当前层的第一个节点
    cur = root
    while cur:
        # 每层的遍历开始前，将哨兵节点的 next 设置为 None
        tail = dummy  # tail 用于连接下一层的节点
        tail.next = None  # 重置哨兵节点的 next 指针
        while cur:
            # 左子节点存在，将 tail 的 next 指向左子节点
            if cur.left:
                tail.next = cur.left
                tail = tail.next
            # 右子节点存在，同上
            if cur.right:
                tail.next = cur.right
                tail = tail.next
            # 移动到当前层的下一个节点
            cur = cur.next
        # 移动到下一层的第一个节点
        cur = dummy.next
    
    return root

# 测试代码
def test():
    # 构建测试用例的二叉树
    node4 = Node(4)
    node5 = Node(5)
    node7 = Node(7)
    node2 = Node(2, left=node4, right=node5)
    node3 = Node(3, right=node7)
    root = Node(1, left=node2, right=node3)
    
    # 连接节点
    connect(root)
    
    # 验证结果
    print(root.val, "->", root.next)
    print(root.left.val, "->", root.left.next.val, "->", root.left.next.next)
    print(root.left.left.val, "->", root.left.right.val, "->", root.left.right.next.val, "->", root.left.right.next.next)

test()