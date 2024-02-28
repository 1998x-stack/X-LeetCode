#include <iostream>
using namespace std;

// 链表节点的定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 旋转链表函数
ListNode* rotateRight(ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;
    
    // 计算链表长度
    int length = 1;
    ListNode* temp = head;
    while (temp->next) {
        temp = temp->next;
        length++;
    }
    
    // 处理k大于链表长度的情况
    k = k % length;
    if (k == 0) return head;
    
    // 找到新的尾节点和头节点
    temp->next = head; // 将链表连成环
    for (int i = 0; i < length - k; i++) {
        temp = temp->next;
    }
    
    // 断开环，形成新的链表
    head = temp->next;
    temp->next = nullptr;
    
    return head;
}

// 打印链表
void printList(ListNode* head) {
    while (head) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

// 主函数进行测试
int main() {
    // 创建链表 1->2->3->4->5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    
    // 旋转链表
    head = rotateRight(head, 2);
    
    // 打印旋转后的链表
    printList(head);
    
    return 0;
}