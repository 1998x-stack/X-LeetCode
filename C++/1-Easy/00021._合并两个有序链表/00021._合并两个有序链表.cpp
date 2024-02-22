#include <iostream>
using namespace std;

// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 实现合并两个有序链表的函数
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0); // 创建哨兵节点
    ListNode* tail = &dummy; // 使用tail指针跟踪新链表的最后一个节点
    
    while (l1 != NULL && l2 != NULL) {
        if (l1->val <= l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    
    // 直接将未遍历完的链表接到合并链表的尾部
    if (l1 != NULL) {
        tail->next = l1;
    } else if (l2 != NULL) {
        tail->next = l2;
    }
    
    return dummy.next; // 返回合并后链表的头节点
}

// 主函数，用于测试
int main() {
    // 创建测试链表节点...
    // 测试mergeTwoLists函数...
    return 0;
}