from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    # 边界检查
    if not head or m == n:
        return head

    # 初始化指针和计数器
    current, prev, next = head, None, None
    count = 1

    # 定位到第 m 个节点
    while count < m:
        prev = current
        current = current.next
        count += 1

    # 记录反转部分的起始和结束节点
    start, end = prev, current

    # 反转第 m 到 n 个节点
    while count <= n:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    # 将反转后的链表与原链表连接起来
    if start:
        start.next = prev
    else:
        head = prev

    end.next = current

    return head

# 示例用法
input_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
m_val, n_val = 2, 4
result = reverse_between(input_list, m_val, n_val)

# 打印结果
current = result
while current:
    print(current.val, end="->")
    current = current.next
print("NULL")