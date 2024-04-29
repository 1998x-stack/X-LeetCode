from typing import Optional, Dict

class TrieNode:
    def __init__(self):
        """
        初始化 Trie 节点。
        """
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False  # 标记是否为单词的结尾

class Trie:
    def __init__(self):
        """
        初始化 Trie 结构。
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向 Trie 中插入一个单词。
        
        参数:
            word (str): 要插入的单词。
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def longest_word(self) -> Optional[str]:
        longest = ''
        stack = [(self.root, '')]
        while stack:
            node, path = stack.pop()
            if node.is_end_of_word or node == self.root:
                if node !=self.root:
                    if len(path) > len(longest) or (len(path) == len(longest) and path < longest): # 字典序更小
                        longest = path
                for char in sorted(node.children.keys(), reverse=True):
                    stack.append((node.children[char], path + char))
        return longest
    
# 创建 Trie 并插入示例数据
words = ["w", "wo", "wor", "worl", "world"]
trie = Trie()
for word in words:
    trie.insert(word)

# 使用 Trie 方法查找最长单词
longest_valid_word = trie.longest_word()
print(longest_valid_word)