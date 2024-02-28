#include <iostream>
using namespace std;

// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 删除链表的倒数第N个节点并返回头节点
ListNode* removeNthFromEnd(ListNode* head, int n) {
    // 创建一个虚拟头节点，方便处理边界情况
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode *fast = dummy, *slow = dummy;
    
    // fast指针先前移动n+1步
    for(int i = 0; i < n + 1; i++) {
        fast = fast->next;
    }
    
    // 同时移动fast和slow指针
    while(fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }
    
    // 删除slow指针的下一个节点
    ListNode* toDelete = slow->next;
    slow->next = slow->next->next;
    delete toDelete; // 释放内存
    
    // 返回更新后的链表头节点
    ListNode* newHead = dummy->next;
    delete dummy; // 释放虚拟头节点的内存
    return newHead;
}

// 主函数，用于演示删除操作
int main() {
    // 创建示例链表 1->2->3->4->5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    
    int n = 2; // 设置需要删除的倒数第N个节点
    ListNode* result = removeNthFromEnd(head, n);
    
    // 打印结果链表
    while(result != NULL) {
        cout << result->val << "->";
        result = result->next;
    }
    cout << "NULL" << endl;
    
    return 0;
}