from typing import Optional

class ListNode:
    """定义链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    检测链表中的环并返回入环的第一个节点。
    
    Args:
    head: 链表的头节点。
    
    Returns:
    环的入口节点，如果没有环，则返回None。
    
    """
    # 快慢指针初始化
    slow, fast = head, head
    
    # 使用快慢指针找到环中的相遇点
    while True:
        if not (fast and fast.next):
            return None  # 没有环
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # 将一个指针移回头部，两指针同速移动找环入口
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow  # 环的入口
