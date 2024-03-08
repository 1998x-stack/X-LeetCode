#include <iostream>
using namespace std;

// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 实现删除节点的函数
void deleteNode(ListNode* node) {
    if (node == nullptr || node->next == nullptr) return; // 如果节点为空或者是尾节点，则不做任何操作
    node->val = node->next->val; // 将下一个节点的值复制到当前节点
    ListNode* toDelete = node->next; // 临时保存下一个节点，以便删除
    node->next = node->next->next; // 将当前节点的next指针指向下一个节点的next
    delete toDelete; // 删除下一个节点
}

// 主函数，用于测试
int main() {
    // 创建链表 4 -> 5 -> 1 -> 9
    ListNode* head = new ListNode(4);
    head->next = new ListNode(5);
    head->next->next = new ListNode(1);
    head->next->next->next = new ListNode(9);
    
    cout << "Original list: ";
    for(ListNode* cur = head; cur != nullptr; cur = cur->next) {
        cout << cur->val << " ";
    }
    cout << endl;
    
    // 删除节点值为5的节点
    deleteNode(head->next); // 假设这是我们要删除的节点
    
    cout << "List after deletion: ";
    for(ListNode* cur = head; cur != nullptr; cur = cur->next) {
        cout << cur->val << " ";
    }
    cout << endl;
    
    // 清理分配的内存
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}