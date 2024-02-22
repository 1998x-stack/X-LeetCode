class ListNode:
    def __init__(self, val=0, next=None):
        """链表节点的初始化函数
        
        Args:
            val (int): 节点值，默认为0
            next (ListNode): 指向下一个节点的指针，默认为None
        """
        self.val = val
        self.next = next
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """删除链表的倒数第N个节点并返回链表头节点
    
    Args:
        head (ListNode): 链表的头节点
        n (int): 需要删除的倒数第N个节点
    
    Returns:
        ListNode: 删除节点后的链表头节点
    """
    dummy = ListNode(0, head)  # 创建一个哑节点，指向头节点，简化边界情况处理
    fast = slow = dummy  # 初始化快慢指针指向哑节点
    
    # 快指针先前移n+1步
    for _ in range(n + 1):
        fast = fast.next
    
    # 快慢指针同时移动，直到快指针到达链表末尾
    while fast:
        fast = fast.next
        slow = slow.next
    
    # 删除倒数第N个节点
    slow.next = slow.next.next
    
    return dummy.next  # 返回哑节点的下一个节点，即新的头节点


# 辅助函数：构建链表
def buildLinkedList(elements: list) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# 辅助函数：打印链表
def printLinkedList(head: ListNode) -> None:
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print("->".join(elements))

# 构建链表并测试
head = buildLinkedList([1, 2, 3, 4, 5])
n = 2
head = removeNthFromEnd(head, n)
printLinkedList(head)  # 预期输出：1->2->3->5