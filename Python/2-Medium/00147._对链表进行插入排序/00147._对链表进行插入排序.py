from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    对链表进行插入排序。

    Args:
    head: ListNode - 链表的头节点。

    Returns:
    ListNode - 排序后的链表的头节点。
    """
    # 创建哑节点作为新链表的起始节点，便于处理边界情况
    dummy_head = ListNode(0)
    curr = head  # 当前正在排序的节点

    while curr:
        # prev 指针用于遍历找到 curr 应该插入的位置的前一个节点
        prev = dummy_head
        while prev.next and prev.next.val < curr.val:
            prev = prev.next

        # 将 curr 插入到 prev 和 prev.next 之间
        next_temp = curr.next  # 临时保存 curr 的下一个节点，因为插入过程中会改变 curr 的 next 指针
        curr.next = prev.next
        prev.next = curr
        curr = next_temp  # 移动 curr 到下一个待处理节点

    return dummy_head.next

# 辅助函数：创建链表
def create_list(arr):
    head = ListNode(arr[0]) if arr else None
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：打印链表
def print_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# 示例链表 4->2->1->3
head = create_list([4, 2, 1, 3])
sorted_head = insertionSortList(head)

# 打印排序后的链表
print_list(sorted_head)