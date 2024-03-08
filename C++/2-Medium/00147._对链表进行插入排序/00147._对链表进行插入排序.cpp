#include <iostream>
#include <climits> // Include for INT_MIN
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 插入排序的实现
ListNode* insertionSortList(ListNode* head) {
    // 使用哑节点简化头部插入操作
    ListNode dummy(INT_MIN);
    ListNode *prev = &dummy;

    while (head != NULL) {
        ListNode *temp = head->next; // 保存下一个节点
        // 寻找插入位置
        if (prev->val >= head->val) prev = &dummy; // 重置prev为dummy，如果当前节点小于prev节点的值
        while (prev->next != NULL && prev->next->val < head->val) {
            prev = prev->next;
        }
        // 插入操作
        head->next = prev->next;
        prev->next = head;
        head = temp; // 移动到下一个待排序的节点
    }
    return dummy.next;
}

void printList(ListNode *head) {
    while (head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    ListNode *head = new ListNode(4);
    head->next = new ListNode(2);
    head->next->next = new ListNode(1);
    head->next->next->next = new ListNode(3);

    cout << "Original list: ";
    printList(head);

    ListNode *sortedList = insertionSortList(head);
    cout << "Sorted list: ";
    printList(sortedList);

    return 0;
}