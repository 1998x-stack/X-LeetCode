from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    根据给定的单链表，重新排列以使所有奇数位置的节点位于偶数位置节点之前。
    
    参数:
    head: ListNode - 链表的头节点。
    
    返回:
    ListNode - 重排后的链表的头节点。
    
    示例:
    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL
    """
    # 边界条件：如果链表为空或只有一个节点，直接返回
    if not head or not head.next:
        return head
    
    # 初始化奇数、偶数指针和偶数头部指针
    odd = head
    even = head.next
    evenHead = head.next
    
    # 遍历链表，重新链接奇偶节点
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        # 注意：上下文顺序
        odd = odd.next
        even = even.next
    
    # 将偶数链表拼接到奇数链表后
    odd.next = evenHead
    
    return head

# 辅助函数：创建链表
def create_list(nodes):
    head = ListNode(nodes[0])
    current = head
    for value in nodes[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 辅助函数：打印链表
def print_list(head):
    current = head
    while current:
        print(current.val, end=' -> ' if current.next else '')
        current = current.next
    print('NULL')

# 示例
nodes = [1, 2, 3, 4, 5]
head = create_list(nodes)
print("原始链表:")
print_list(head)

# 运行代码
new_head = oddEvenList(head)
print("重排后的链表:")
print_list(new_head)