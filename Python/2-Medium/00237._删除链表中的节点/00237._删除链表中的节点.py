from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node: ListNode) -> None:
    """
    删除链表中的节点，不返回任何值。假设给定的节点不是链表的尾节点。

    Args:
    node (ListNode): 要删除的节点。
    
    注：由于不可以访问链表的头节点和前一个节点，此函数通过复制下一个节点的值到当前节点，然后删除下一个节点的方式来间接删除当前节点。
    """
    # 将下一个节点的值复制到当前节点
    node.val = node.next.val
    # 将当前节点的next指针指向下下个节点，从而删除下一个节点
    node.next = node.next.next

# 用于打印链表的函数，方便验证结果
def printLinkedList(head: Optional[ListNode]) -> None:
    """
    打印链表。

    Args:
    head (ListNode): 链表的头节点。
    """
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# 创建示例链表 4->5->1->9
head = ListNode(4)
head.next = ListNode(5)
node_to_delete = head.next  # 要删除的节点，值为5
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

# 打印原始链表
print("原始链表:")
printLinkedList(head)

# 删除节点
deleteNode(node_to_delete)

# 打印删除节点后的链表
print("删除节点后的链表:")
printLinkedList(head)