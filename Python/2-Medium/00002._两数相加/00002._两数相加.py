class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # 哨兵节点，简化边界情况处理
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    # 同时遍历两个链表
    while l1 or l2:
        # 如果链表已经遍历完，就使用0作为值
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        sum = carry + x + y
        carry = sum // 10  # 更新进位
        current.next = ListNode(sum % 10)  # 创建新节点，加入到结果链表
        current = current.next  # 移动指针
        
        # 移动l1和l2指针
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # 检查最后的进位
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy_head.next  # 返回哨兵节点的下一个节点，即结果链表的头节点

# Helper function to convert list to ListNode
def list_to_listnode(numbers):
    dummy_root = ListNode(0)
    ptr = dummy_root
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummy_root.next
    return ptr

# Helper function to print ListNode
def print_listnode(ln: ListNode):
    while ln:
        print(ln.val, end=" -> " if ln.next else "")
        ln = ln.next

# Test cases
l1 = list_to_listnode([2, 4, 3])
l2 = list_to_listnode([5, 6, 4])

result = addTwoNumbers(l1, l2)

# Output the result
print_listnode(result)