from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    """
    反转链表
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def add_one(head: ListNode) -> ListNode:
    """
    给单链表加一
    """
    # 反转链表
    head = reverse_list(head)
    
    # 加一处理
    carry = 1
    current = head
    while current and carry:
        current.val += carry
        carry = current.val // 10
        current.val %= 10
        if carry and current.next is None:
            current.next = ListNode(0)  # 如果最后还有进位，需要添加一个新的节点
        current = current.next
    
    # 再次反转链表以恢复原始顺序
    return reverse_list(head)

# 测试代码
def print_list(head: ListNode):
    """
    打印链表
    """
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# 创建测试链表 9 -> 9 -> 9
head = ListNode(9, ListNode(9, ListNode(9)))

# 执行加一操作
result_head = add_one(head)

# 打印结果
print_list(result_head)  # 预期输出：1 -> 0 -> 0 -> 0