class TrieNode:
    def __init__(self) -> None:
        self.value = 0
        self.children = {}
        
class MapSum:
    def __init__(self) -> None:
        self.keys = {}
        self.root = TrieNode()
        
    def insert(self, key, val):
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val
        cur = self.root
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.value += delta
    
    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.value
    
# 创建 MapSum 对象并执行一系列操作进行验证
map_sum = MapSum()
map_sum.insert("apple", 3)
assert map_sum.sum("ap") == 3  # 预期输出 3
map_sum.insert("app", 2)
assert map_sum.sum("ap") == 5  # 预期输出 5

# 打印结果确认代码逻辑正确性
print("All test cases passed.")