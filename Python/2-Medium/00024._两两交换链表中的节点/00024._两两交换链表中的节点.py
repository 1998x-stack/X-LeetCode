class ListNode:
    """
    定义链表节点类
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    """
    两两交换链表中的节点

    Args:
    head: ListNode - 链表的头节点

    Returns:
    ListNode - 交换节点后的链表头节点

    示例:
    输入：1->2->3->4
    输出：2->1->4->3
    """
    # 创建哑节点，哑节点的 next 指向链表头部，方便处理头部节点的交换
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    # 遍历链表，直到当前节点或下一个节点为空，因为需要成对处理
    while head and head.next:
        # 初始化成对的两个节点
        first = head
        second = head.next

        # 交换节点
        prev.next = second
        first.next = second.next
        second.next = first

        # 更新指针，准备下一对交换
        prev = first
        head = first.next

    # 返回哑节点的下一个节点，即交换后的头节点
    return dummy.next

# 辅助函数：创建链表
def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

# 辅助函数：打印链表
def print_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print("->".join(map(str, elements)))

# 测试代码
elements = [1, 2, 3, 4]
head = create_linked_list(elements)
print("原链表：")
print_linked_list(head)

# 执行两两交换
swapped_head = swapPairs(head)
print("交换后的链表：")
print_linked_list(swapped_head)