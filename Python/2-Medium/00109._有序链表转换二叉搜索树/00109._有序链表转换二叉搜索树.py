from typing import Optional

# 定义链表和树的节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    """
    将有序链表转换为高度平衡的二叉搜索树。
    
    参数:
    head (Optional[ListNode]): 链表的头节点。
    
    返回:
    Optional[TreeNode]: 高度平衡的二叉搜索树的根节点。
    """
    
    # 快慢指针法找到链表的中间节点
    def findMiddle(prev, head):
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None  # 断开链表
        return slow
    
    if not head:
        return None
    
    # 初始化前一个节点为None，以便于后面断开链表
    prev = None
    mid = findMiddle(prev, head)
    
    # 使用中间节点的值创建树的根节点
    node = TreeNode(mid.val)
    
    # 如果中间节点就是头节点，说明左边没有节点了
    if head == mid:
        return node
    
    # 递归构建左子树和右子树
    node.left = sortedListToBST(head)
    node.right = sortedListToBST(mid.next)
    
    return node

# 为了测试代码，首先创建一个有序链表
def createLinkedList(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 链表转换为数组（用于打印和验证结果）
def bstToArray(root):
    if not root:
        return []
    return bstToArray(root.left) + [root.val] + bstToArray(root.right)

# 测试数据
test_list = [-10, -3, 0, 5, 9]
linked_list = createLinkedList(test_list)

# 转换并打印结果
bst_root = sortedListToBST(linked_list)
print(bstToArray(bst_root))
