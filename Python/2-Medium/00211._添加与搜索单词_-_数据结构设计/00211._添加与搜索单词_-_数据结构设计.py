from typing import Optional

class TrieNode:
    """
    字典树的节点类
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    """
    添加与搜索单词 - 数据结构设计
    """

    def __init__(self):
        """
        初始化字典树的根节点
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        向字典树中添加一个单词
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        在字典树中搜索一个单词，包括支持正则表达式中的'.'
        """
        return self._search_in_node(word, 0, self.root)
    
    def _search_in_node(self, word: str, index: int, node: TrieNode) -> bool:
        """
        递归搜索助手函数
        """
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        if char == '.':
            for child in node.children.values():
                if self._search_in_node(word, index + 1, child):
                    return True
            return False
        else:
            if char in node.children:
                return self._search_in_node(word, index + 1, node.children[char])
            else:
                return False

# 实例化并运行测试用例
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

# 输出应该为: False, True, True, True
test_cases = ["pad", "bad", ".ad", "b.."]
results = [wordDictionary.search(case) for case in test_cases]
print(results)