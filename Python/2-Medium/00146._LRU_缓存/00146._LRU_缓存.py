class LRUCache:
    def __init__(self, capacity: int):
        """
        初始化 LRU 缓存
        :param capacity: 缓存的容量
        """
        self.cache = {}  # 哈希表用于快速查找
        self.capacity = capacity
        self.head = ListNode()  # 虚拟头节点
        self.tail = ListNode()  # 虚拟尾节点
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        从缓存中获取键对应的值
        :param key: 键
        :return: 键对应的值，如果键不存在返回 -1
        """
        node = self.cache.get(key, None)
        if not node:
            return -1  # 键不存在
        self.move_to_head(node)  # 键存在，移动到头部
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        向缓存中添加键值对
        :param key: 键
        :param value: 值
        """
        node = self.cache.get(key)
        if not node:
            newNode = ListNode(key, value)
            self.cache[key] = newNode
            self.add_to_head(newNode)
            if len(self.cache) > self.capacity:
                removed = self.pop_tail()
                del self.cache[removed.key]
        else:
            node.value = value
            self.move_to_head(node)

    def add_to_head(self, node: ListNode) -> None:
        """
        在双向链表的头部添加节点
        :param node: 要添加的节点
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: ListNode) -> None:
        """
        从双向链表中删除节点
        :param node: 要删除的节点
        """
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def move_to_head(self, node: ListNode) -> None:
        """
        将节点移动到双向链表的头部
        :param node: 要移动的节点
        """
        self.remove_node(node)
        self.add_to_head(node)

    def pop_tail(self) -> ListNode:
        """
        删除并返回双向链表尾部的节点
        :return: 被删除的节点
        """
        node = self.tail.prev
        self.remove_node(node)
        return node
# 初始化 LRUCache
lru_cache = LRUCache(2)

# 进行一系列的 put 和 get 操作
lru_cache.put(1, 1)  # 缓存是 {1=1}
lru_cache.put(2, 2)  # 缓存是 {1=1, 2=2}
print(lru_cache.get(1))  # 返回 1
lru_cache.put(3, 3)  # 该操作会使密钥 2 作废，缓存是 {1=1, 3=3}
print(lru_cache.get(2))  # 返回 -1 (未找到)
lru_cache.put(4, 4)  # 该操作会使密钥 1 作废，缓存是 {4=4, 3=3}
print(lru_cache.get(1))  # 返回 -1 (未找到)
print(lru_cache.get(3))  # 返回 3
print(lru_cache.get(4))  # 返回 4
