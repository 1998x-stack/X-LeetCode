#include <iostream>
#include <unordered_map>

using namespace std;

// 定义双向链表的节点结构
struct DLinkedNode {
    int key, value;
    DLinkedNode* prev;
    DLinkedNode* next;
    DLinkedNode(): key(0), value(0), prev(nullptr), next(nullptr) {}
    DLinkedNode(int _key, int _value): key(_key), value(_value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    unordered_map<int, DLinkedNode*> cache;
    DLinkedNode* head;
    DLinkedNode* tail;
    int size;
    int capacity;

    // 添加节点到双向链表头部
    void addToHead(DLinkedNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }

    // 移除双向链表中的节点
    void removeNode(DLinkedNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    // 将节点移动到头部
    void moveToHead(DLinkedNode* node) {
        removeNode(node);
        addToHead(node);
    }

    // 移除双向链表尾部节点
    DLinkedNode* removeTail() {
        DLinkedNode* node = tail->prev;
        removeNode(node);
        return node;
    }

public:
    LRUCache(int _capacity): size(0), capacity(_capacity) {
        // 使用伪头部和伪尾部节点
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (!cache.count(key)) {
            return -1;
        }
        DLinkedNode* node = cache[key];
        moveToHead(node);
        return node->value;
    }
    
    void put(int key, int value) {
        if (!cache.count(key)) {
            DLinkedNode* node = new DLinkedNode(key, value);
            cache[key] = node;
            addToHead(node);
            ++size;
            if (size > capacity) {
                DLinkedNode* removed = removeTail();
                cache.erase(removed->key);
                delete removed;
                --size;
            }
        } else {
            DLinkedNode* node = cache[key];
            node->value = value;
            moveToHead(node);
        }
    }
};

int main() {
    LRUCache* obj = new LRUCache(2);
    obj->put(1, 1);
    cout << "Put(1, 1)" << endl;
    obj->put(2, 2);
    cout << "Put(2, 2)" << endl;
    cout << "Get(1): " << obj->get(1) << endl; // 输出 1
    obj->put(3, 3); // 使得键 2 作废
    cout << "Put(3, 3)" << endl;
    cout << "Get(2): " << obj->get(2) << endl; // 输出 -1 (未找到)
    obj->put(4, 4); // 使得键 1 作废
    cout << "Put(4, 4)" << endl;
    cout << "Get(1): " << obj->get(1) << endl; // 输出 -1 (未找到)
    cout << "Get(3): " << obj->get(3) << endl; // 输出 3
    cout << "Get(4): " << obj->get(4) << endl; // 输出 4
    return 0;
}