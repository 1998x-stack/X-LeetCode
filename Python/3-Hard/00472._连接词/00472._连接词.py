from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """向Trie树中插入一个单词"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        """在Trie树中搜索一个单词"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord

def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    trie = Trie()
    # 将所有单词插入Trie树中
    for word in words:
        if word:  # 排除空字符串
            trie.insert(word)

    def canForm(word: str, start: int) -> bool:
        """动态规划检查单词是否可以由其他单词组成"""
        if start == len(word):
            return True
        node = trie.root
        for i in range(start, len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            # 如果当前节点是单词的结尾，并且剩余的字符串也能由单词列表中的单词组成
            if node.isEndOfWord and canForm(word, i + 1):
                return True
        return False

    result = []
    for word in words:
        if canForm(word, 0):
            result.append(word)

    return result

# 示例数据
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 执行函数
findAllConcatenatedWordsInADict(words)
