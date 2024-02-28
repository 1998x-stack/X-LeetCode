#include <iostream>
using namespace std;

// 链表节点的定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 分隔链表的函数
ListNode* partition(ListNode* head, int x){
    ListNode lessHead(0), greaterHead(0);
    ListNode *lessPtr = &lessHead, *greaterPtr = &greaterHead;
    
    while(head){
        if(head->val < x){
            lessPtr->next = head;
            lessPtr = lessPtr->next;
        }else{
            greaterPtr->next = head;
            greaterPtr = greaterPtr->next;
        }
        head = head->next;
    
    }
    greaterPtr->next = nullptr; // 避免环形链表的产生
    lessPtr->next = greaterHead.next; // 连接两个部分
    return lessHead.next; // 返回新链表的头节点
}

// 打印链表的函数
void printList(ListNode* head) {
    while (head) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

// 主函数
int main() {
    // 构建示例链表 [1,4,3,2,5,2]
    ListNode a(1), b(4), c(3), d(2), e(5), f(2);
    a.next = &b; b.next = &c; c.next = &d; d.next = &e; e.next = &f;
    
    int x = 3;
    ListNode* result = partition(&a, x);
    
    // 打印分隔后的链表
    printList(result);
    
    return 0;
}