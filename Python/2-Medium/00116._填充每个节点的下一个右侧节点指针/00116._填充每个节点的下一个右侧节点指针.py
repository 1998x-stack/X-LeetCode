from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: Optional[Node]) -> Optional[Node]:
    """
    使用层序遍历的思想填充每个节点的下一个右侧节点指针。
    Args:
        root (Optional[Node]): 树的根节点。
    Returns:
        Optional[Node]: 修改后的树的根节点。
    """
    if not root:
        return None

    leftmost = root
    # 当前层的最左边的节点，用于遍历当前层
    while leftmost.left:
        # 遍历当前层的节点，为下一层的节点设置 next 指针
        head = leftmost
        while head:
            # 连接同一个父节点的两个子节点
            head.left.next = head.right
            # 连接不同父节点但相邻的子节点
            if head.next:
                head.right.next = head.next.left
            head = head.next
        # 移动到下一层的最左边的节点
        leftmost = leftmost.left
    
    return root

# 辅助函数，用于打印每层节点的 next 值，以验证算法正确性
def print_levels(root: Optional[Node]):
    """
    打印树中每一层节点的值及其 next 指向的节点的值。
    Args:
        root (Optional[Node]): 树的根节点。
    """
    level_start = root
    while level_start:
        cur = level_start
        while cur:
            next_val = cur.next.val if cur.next else "NULL"
            print(f"{cur.val}->{next_val}", end=" ")
            cur = cur.next
        print("-> NULL")
        level_start = level_start.left

# 构建题目中的树
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

# 运行代码
connected_root = connect(root)

# 验证结果
print_levels(connected_root)