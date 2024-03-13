from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    使用归并排序算法对链表进行排序。

    Args:
    head: ListNode - 链表的头节点。

    Returns:
    ListNode - 排序后的链表的头节点。

    示例:
    >>> lst = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    >>> sorted_lst = sortList(lst)
    >>> while sorted_lst:
    ...     print(sorted_lst.val, end=" ")
    ...     sorted_lst = sorted_lst.next
    1 2 3 4
    """
    
    # 如果链表为空或者只有一个元素，直接返回
    if not head or not head.next:
        return head
    
    # 使用快慢指针找到中点
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 分割链表
    mid, slow.next = slow.next, None
    
    # 递归排序左右两部分
    left, right = sortList(head), sortList(mid)
    
    # 合并两个有序链表
    return merge(left, right)

def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    合并两个有序链表。

    Args:
    l1: ListNode - 第一个有序链表的头节点。
    l2: ListNode - 第二个有序链表的头节点。

    Returns:
    ListNode - 合并后的有序链表的头节点。
    """
    dummy = ListNode(0)
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    return dummy.next

# 用于测试的辅助函数，将列表转换为链表
def list_to_linkedlist(elements):
    head = ListNode(0)  # Dummy node
    tail = head
    for element in elements:
        tail.next = ListNode(element)
        tail = tail.next
    return head.next

# 用于测试的辅助函数，将链表转换为列表
def linkedlist_to_list(node):
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    return elements

# 测试代码
test_list = [4, 2, 1, 3]
head = list_to_linkedlist(test_list)
sorted_head = sortList(head)
sorted_list = linkedlist_to_list(sorted_head)
sorted_list