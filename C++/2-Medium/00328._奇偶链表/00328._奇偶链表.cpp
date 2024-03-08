#include <iostream>
#include <vector> // 包含 vector 头文件
using namespace std;

// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 实现奇偶链表函数
ListNode* oddEvenList(ListNode* head) {
    if (head == NULL || head->next == NULL) return head;
    
    ListNode* odd = head; // 奇数节点起始点
    ListNode* even = head->next; // 偶数节点起始点
    ListNode* evenHead = even; // 保存偶数链表的头节点
    
    // 遍历链表，重新组织奇偶节点
    while (even != NULL && even->next != NULL) {
        odd->next = even->next; // 将奇数节点指向下一个奇数节点
        odd = odd->next; // 移动奇数节点指针
        even->next = odd->next; // 将偶数节点指向下一个偶数节点
        even = even->next; // 移动偶数节点指针
    }
    odd->next = evenHead; // 连接奇数链表和偶数链表
    
    return head;
}

// 辅助函数，用于创建链表
ListNode* createList(const vector<int>& vals) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int val : vals) {
        tail->next = new ListNode(val);
        tail = tail->next;
    }
    return dummy.next;
}

// 辅助函数，用于打印链表
void printList(ListNode* head) {
    while (head != NULL) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

int main() {
    // 示例链表：1->2->3->4->5->NULL
    vector<int> vals = {1, 2, 3, 4, 5};
    ListNode* head = createList(vals);

    cout << "Original List: ";
    printList(head);

    ListNode* result = oddEvenList(head);

    cout << "Odd-Even List: ";
    printList(result);

    return 0;
}