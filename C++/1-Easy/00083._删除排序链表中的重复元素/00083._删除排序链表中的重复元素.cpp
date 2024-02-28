#include <iostream>

// 链表节点的定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // 如果链表为空或只有一个元素，直接返回
        if (head == NULL || head->next == NULL) return head;
        
        ListNode* current = head;
        while (current->next != NULL) {
            if (current->val == current->next->val) {
                // 发现重复元素，删除之
                ListNode* temp = current->next;
                current->next = current->next->next;
                delete temp; // 防止内存泄漏
            } else {
                // 移动到下一个不重复的元素
                current = current->next;
            }
        }
        return head;
    }
};

// 注意：这里不提供main函数的完整实现，因为我们的目标是将代码保存到本地文件
