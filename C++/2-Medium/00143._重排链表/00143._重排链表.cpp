#include <iostream>
using namespace std;

// 链表节点的定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 找到链表的中点
ListNode* findMid(ListNode* head) {
    ListNode *slow = head, *fast = head;
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

// 反转链表
ListNode* reverseList(ListNode* head) {
    ListNode *prev = NULL, *curr = head, *next = NULL;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

// 重排链表
void reorderList(ListNode* head) {
    if (!head || !head->next || !head->next->next) return;
    
    // 找到中点，并分割链表
    ListNode* mid = findMid(head);
    ListNode* second = reverseList(mid->next);
    mid->next = NULL;
    
    // 合并两个链表
    ListNode* first = head;
    while (first != NULL && second != NULL) {
        ListNode* temp1 = first->next;
        ListNode* temp2 = second->next;
        
        first->next = second;
        second->next = temp1;
        
        first = temp1;
        second = temp2;
    }
}

// 打印链表
void printList(ListNode* head) {
    while (head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // 创建链表1->2->3->4->5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    cout << "Original List: ";
    printList(head);

    // 重排链表
    reorderList(head);
    
    cout << "Reordered List: ";
    printList(head);

    return 0;
}