class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode() # 创建根节点
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children.keys():
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word):
        node = self.root
        shortest_root = ""
        for char in word:
            if char in node.children.keys():
                shortest_root += char
                node = node.children[char]
                if node.isEnd:
                    return shortest_root
            else:
                break
        return word
    
def replace_words(dict, senetence):
    trie = Trie()
    for word in dict:
        trie.insert(word)
    
    words = senetence.split()
    replaced_words = [trie.search(word) for word in words]
    return ' '.join(replaced_words)

# 测试示例
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
replaced_sentence = replace_words(dictionary, sentence)
print(replaced_sentence)