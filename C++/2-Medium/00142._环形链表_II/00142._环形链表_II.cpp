#include <iostream>
using namespace std;

// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 函数：寻找环形链表的入口
ListNode *detectCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) { // 发现环
            fast = head; // 将fast重新指向头节点
            while (slow != fast) { // 移动指针直到再次相遇
                slow = slow->next;
                fast = fast->next;
            }
            return slow; // 返回环的入口
        }
    }
    return nullptr; // 无环，返回nullptr
}

// 主函数
int main() {
    // 构建示例链表，此处仅示例，实际使用时应动态构建链表
    ListNode *head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head->next; // 创建环

    ListNode *entry = detectCycle(head);
    if (entry != nullptr) {
        cout << "环的入口节点值为: " << entry->val << endl;
    } else {
        cout << "链表无环" << endl;
    }

    // 注意：此处未释放链表内存，实际使用时应注意内存管理
    return 0;
}