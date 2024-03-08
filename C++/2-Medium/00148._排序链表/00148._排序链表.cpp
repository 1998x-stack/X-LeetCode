#include <iostream>
using namespace std;

// 链表节点定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 函数声明
ListNode* sortList(ListNode* head);
ListNode* findMid(ListNode* head);
ListNode* merge(ListNode* l1, ListNode* l2);

int main() {
    // 构造链表 4->2->1->3
    ListNode* head = new ListNode(4);
    head->next = new ListNode(2);
    head->next->next = new ListNode(1);
    head->next->next->next = new ListNode(3);
    
    // 排序链表
    ListNode* sorted = sortList(head);
    
    // 打印排序后的链表
    while (sorted != nullptr) {
        cout << sorted->val << " ";
        sorted = sorted->next;
    }
    
    return 0;
}

ListNode* sortList(ListNode* head){
    if(!head || !head->next) return head;
    ListNode* mid = findMid(head);
    ListNode* left = sortList(head);
    ListNode* right = sortList(mid);
    return merge(left, right);
}

ListNode* findMid(ListNode* head){
    ListNode* slow = head;
    ListNode* fast = head;
    ListNode* prev = nullptr;
    while(fast && fast->next){
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    if(prev) prev->next = nullptr;
    return slow;
}

ListNode* merge(ListNode* l1, ListNode* l2){
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while(l1 && l2){
        if(l1->val < l2->val){
            tail->next = l1;
            l1 = l1->next;
        }
        else{
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    tail->next = l1 ? l1 : l2;
    return dummy.next;
}