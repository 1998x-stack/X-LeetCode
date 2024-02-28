#include <iostream>
using namespace std;

// 定义链表的节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 实现两两交换链表中的节点的函数
ListNode* swapPairs(ListNode* head) {
    ListNode *dummy = new ListNode(0);
    dummy->next = head;
    ListNode *current = dummy;
    while (current->next != nullptr && current->next->next != nullptr) {
        ListNode *first = current->next;
        ListNode *second = current->next->next;
        first->next = second->next;
        second->next = first;
        current->next = second;
        current = first;
    }
    return dummy->next;
}

// 主函数，用于演示和测试
int main() {
    // 创建示例链表：1->2->3->4
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);

    // 调用函数并打印结果
    ListNode *result = swapPairs(head);
    while (result != nullptr) {
        cout << result->val << " ";
        result = result->next;
    }
    return 0;
}