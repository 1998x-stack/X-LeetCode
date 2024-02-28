#include <iostream>
using namespace std;

// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 实现删除排序链表中的重复元素II的函数
ListNode* deleteDuplicates(ListNode* head) {
    if(!head || !head->next) return head;
    ListNode* dummy = new ListNode(-1);
    dummy->next = head;
    ListNode* pre = dummy;
    while (pre->next){
        ListNode* current =  pre->next;
        while(current->next && current->val == current->next->val){
            current = current->next;
        }
        if(pre->next != current){
            pre->next = current->next;
        } else {
            pre = pre->next;
        }
    }
    return dummy->next;
}

// 主函数，用于测试
int main() {
    // 创建链表 1->2->3->3->4->4->5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(3);
    head->next->next->next->next = new ListNode(4);
    head->next->next->next->next->next = new ListNode(4);
    head->next->next->next->next->next->next = new ListNode(5);
    
    // 删除重复元素
    ListNode* result = deleteDuplicates(head);
    
    // 打印结果
    while (result != NULL) {
        cout << result->val << "->";
        result = result->next;
    }
    cout << "NULL" << endl;
    
    return 0;
}