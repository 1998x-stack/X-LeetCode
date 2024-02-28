
#include <iostream>
using namespace std;

// 链表节点的定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 判断链表是否有环的函数
bool hasCycle(ListNode *head) {
    if (head == NULL || head->next == NULL) {
        return false; // 边界条件处理
    }
    
    ListNode *slow = head; // 慢指针
    ListNode *fast = head; // 快指针
    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next; // 慢指针移动一步
        fast = fast->next->next; // 快指针移动两步
        
        if (slow == fast) { // 如果快慢指针相遇，则说明存在环
            return true;
        }
    }
    
    return false; // 如果快指针到达链表末尾，则说明链表无环
}

int main() {
    // 示例代码，实际测试时应根据问题的要求构造链表
    ListNode *head = new ListNode(3);
    ListNode *node1 = new ListNode(2);
    ListNode *node2 = new ListNode(0);
    ListNode *node3 = new ListNode(-4);
    
    head->next = node1;
    node1->next = node2;
    node2->next = node3;
    node3->next = node1; // 创建一个环
    
    cout << "链表是否有环: " << hasCycle(head) << endl;
    
    // 清理内存，防止内存泄漏，实际环境中可能需要更复杂的处理方式
    delete head;
    delete node1;
    delete node2;
    delete node3;
    
    return 0;
}