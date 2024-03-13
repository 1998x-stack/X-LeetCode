from typing import Optional

class ListNode:
    """定义链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    """
    重排链表
    
    参数:
        head (Optional[ListNode]): 链表的头节点
    
    返回:
        None，直接在输入的链表上修改
    """
    if not head or not head.next or not head.next.next:
        # 如果链表长度小于3，无需重排
        return
    
    # 找到中点
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # 反转后半部分链表
    prev, cur = None, slow.next
    while cur:
        cur.next = prev
        prev = cur
        cur = cur.next
        # cur.next, prev, cur = prev, cur, cur.next
    slow.next = None  # 断开前半部分和后半部分的连接
    
    # 重排链表
    head1, head2 = head, prev
    while head2:
        head1.next, head1 = head2, head1.next
        head2.next, head2 = head1, head2.next

# 由于我们需要在代码解释器中运行并可视化这个过程，我们将构建一个辅助函数来创建和打印链表，以验证我们的解决方案是否正确。

def create_list(elements: list) -> Optional[ListNode]:
    """从列表创建链表"""
    head = ListNode(elements[0]) if elements else None
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def print_list(head: Optional[ListNode]) -> None:
    """打印链表"""
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements))

# 示例运行
elements = [1, 2, 3, 4, 5]
head = create_list(elements)
print("原始链表:")
print_list(head)

reorderList(head)
print("重排后的链表:")
print_list(head)