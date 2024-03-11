from typing import Optional

class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None, random: 'ListNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[ListNode]') -> 'Optional[ListNode]':
    if not head:
        return None
    
    # 创建旧节点到新节点的映射
    old_to_new = {}
    
    # 第一遍遍历：复制所有节点
    current = head
    while current:
        old_to_new[current] = ListNode(current.val)
        current = current.next
    
    # 第二遍遍历：复制 next 和 random 指针
    current = head
    while current:
        # 如果 next 不为空，则设置新节点的 next
        if current.next:
            old_to_new[current].next = old_to_new[current.next]
        # 如果 random 不为空，则设置新节点的 random
        if current.random:
            old_to_new[current].random = old_to_new[current.random]
        current = current.next
    
    # 返回新链表的头节点
    return old_to_new[head]

# 由于链表及其 random 指针的特殊性，无法直接在此环境中运行并验证代码的正确性。
# 此代码应在本地环境中，配合具体的链表输入进行测试。
