from typing import Dict, Optional

class TrieNode:
    """定义 Trie 节点类"""
    def __init__(self):
        # 每个节点存储对子节点的引用
        self.children: Dict[str, 'TrieNode'] = {}
        # 标记该节点是否是某个单词的结束
        self.is_end_of_word: bool = False

class Trie:
    """实现 Trie (前缀树)"""
    
    def __init__(self):
        """初始化 Trie"""
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """向 Trie 中插入一个单词"""
        node = self.root
        for char in word:
            # 如果字符不存在，则创建一个新的 TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # 移动到下一个节点
            node = node.children[char]
        # 标记单词的结束节点
        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        """在 Trie 中搜索一个单词"""
        node = self.root
        for char in word:
            # 如果字符不在子节点中，返回 False
            if char not in node.children:
                return False
            # 移动到下一个节点
            node = node.children[char]
        # 返回最后节点的 is_end_of_word 值
        return node.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        """检查 Trie 中是否有以指定前缀开始的单词"""
        node = self.root
        for char in prefix:
            # 如果字符不在子节点中，返回 False
            if char not in node.children:
                return False
            # 移动到下一个节点
            node = node.children[char]
        # 如果能走到这一步，说明找到了对应的前缀
        return True

# 测试代码
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))    # False
print(trie.startsWith("app"))# True
trie.insert("app")
print(trie.search("app"))    # True