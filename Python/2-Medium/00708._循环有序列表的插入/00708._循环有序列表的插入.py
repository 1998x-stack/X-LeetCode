class Node:
    """
    定义循环链表的节点类
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert(head: Node, insertVal: int) -> Node:
    """
    在循环有序链表中插入一个节点，保持循环链表的有序性。

    Args:
    head (Node): 循环链表的头节点。
    insertVal (int): 需要插入的节点的值。

    Returns:
    Node: 插入新节点后的头节点。

    Examples:
    >>> head = Node(3, Node(4, Node(1)))
    >>> head.next.next.next = head  # 形成循环
    >>> new_head = insert(head, 2)
    >>> values = [new_head.val]
    >>> node = new_head.next
    >>> while node != new_head:
    ...     values.append(node.val)
    ...     node = node.next
    >>> values
    [3, 4, 2, 1]
    """
    new_node = Node(insertVal)
    if not head:
        new_node.next = new_node # make it a circle
        return new_node

    prev, curr = head, head.next
    to_insert = False
    while True:
        if prev.val <= insertVal <= curr.val:
            to_insert = True # find the position to insert
        elif prev.val > curr.val:
            if insertVal >= prev.val or insertVal <= curr.val: # insertVal is the max or min value
                to_insert = True
        
        if to_insert:
            prev.next = new_node
            new_node.next = curr
            return head
        
        prev, curr = curr, curr.next
        if prev == head:
            break
    
    # 如果所有节点值相同，插入到head的前面
    prev.next = new_node
    new_node.next = curr
    return head

# 测试代码
# 构建一个循环链表：3 -> 4 -> 1 -> 3
head = Node(3, Node(4, Node(1)))
head.next.next.next = head
# 插入节点 2
new_head = insert(head, 2)

# 打印循环链表，验证正确性
node = new_head
visited = set()
output = []
while node not in visited:
    output.append(node.val)
    visited.add(node)
    node = node.next

print(output)