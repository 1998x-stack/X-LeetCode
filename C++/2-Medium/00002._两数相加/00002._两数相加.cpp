#include <iostream>

// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 实现两数相加函数
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummyHead = new ListNode(0); // 创建哑节点，简化头节点的插入操作
        ListNode *p = l1, *q = l2, *curr = dummyHead;
        int carry = 0; // 初始化进位为0
        while (p != nullptr || q != nullptr) {
            int x = (p != nullptr) ? p->val : 0;
            int y = (q != nullptr) ? q->val : 0;
            int sum = carry + x + y;
            carry = sum / 10; // 更新进位
            curr->next = new ListNode(sum % 10); // 创建新节点，加入到结果链表
            curr = curr->next;
            if (p != nullptr) p = p->next;
            if (q != nullptr) q = q->next;
        }
        if (carry > 0) {
            curr->next = new ListNode(carry); // 处理最后的进位
        }
        ListNode *result = dummyHead->next; // 获取结果链表的头节点
        delete dummyHead; // 释放哑节点
        return result;
    }
};

// 辅助函数，用于创建和打印链表，仅为了完整演示，实际提交时不需要
ListNode* createList(std::initializer_list<int> vals) {
    ListNode *dummyHead = new ListNode(0);
    ListNode *curr = dummyHead;
    for (int val : vals) {
        curr->next = new ListNode(val);
        curr = curr->next;
    }
    ListNode *result = dummyHead->next;
    delete dummyHead;
    return result;
}

void printList(ListNode *node) {
    while (node != nullptr) {
        std::cout << node->val << " -> ";
        node = node->next;
    }
    std::cout << "nullptr" << std::endl;
}

// 主函数，仅为了演示如何使用，实际提交时不需要
int main() {
    Solution solution;
    ListNode *l1 = createList({2, 4, 3});
    ListNode *l2 = createList({5, 6, 4});
    ListNode *result = solution.addTwoNumbers(l1, l2);
    printList(result);
    // 应该输出：7 -> 0 -> 8 -> nullptr
    return 0;
}