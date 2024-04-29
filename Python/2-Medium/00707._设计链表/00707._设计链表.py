class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = ListNode(val, current.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                current.next = current.next.next
            self.size -= 1

# 创建实例并执行一系列操作，进行测试
linked_list = MyLinkedList()
linked_list.addAtHead(1)  # 链表：1
linked_list.addAtTail(3)  # 链表：1->3
linked_list.addAtIndex(1, 2)  # 链表：1->2->3
print(linked_list.get(1))  # 输出：2
linked_list.deleteAtIndex(1)  # 链表：1->3
print(linked_list.get(1))  # 输出：3

# 对代码逻辑进行重检
print("链表当前大小：", linked_list.size)  # 输出链表的大小确保添加和删除操作正确更新大小
linked_list.addAtIndex(2, 5)  # 在索引为2的位置添加值为5的节点，链表：1->3->5
linked_list.addAtHead(6)  # 链表：6->1->3->5
print(linked_list.get(0))  # 输出：6
print(linked_list.get(2))  # 输出：3
