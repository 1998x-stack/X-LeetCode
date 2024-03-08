#include <iostream>
#include <vector>
using namespace std;

class TrieNode {
public:
    bool isEnd;
    vector<TrieNode*> children;
    TrieNode() : isEnd(false), children(26, nullptr) {}
};

class Trie {
private:
    TrieNode* root;
public:
    Trie() {
        root = new TrieNode();
    }
    
    // 插入字符串到 Trie
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->isEnd = true;
    }
    
    // 搜索字符串在 Trie 中是否存在
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                return false;
            }
            node = node->children[index];
        }
        return node->isEnd;
    }
    
    // 检查是否存在以 prefix 开头的字符串
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                return false;
            }
            node = node->children[index];
        }
        return true;
    }
};

int main() {
    Trie trie;
    trie.insert("apple");
    cout << trie.search("apple") << endl;   // 输出：1
    cout << trie.search("app") << endl;     // 输出：0
    cout << trie.startsWith("app") << endl; // 输出：1
    trie.insert("app");
    cout << trie.search("app") << endl;     // 输出：1
    return 0;
}