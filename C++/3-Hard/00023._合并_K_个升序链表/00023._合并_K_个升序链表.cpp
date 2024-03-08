#include <iostream>
#include <vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Function to merge two sorted lists
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(0);
    ListNode* tail = dummy;
    while (l1 && l2) {
        if (l1->val < l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    tail->next = l1 ? l1 : l2;
    return dummy->next;
}

// Function to merge k sorted lists using divide and conquer
ListNode* mergeKLists(vector<ListNode*>& lists, int start, int end) {
    if (start > end) return nullptr;
    if (start == end) return lists[start];
    int mid = start + (end - start) / 2;
    ListNode* left = mergeKLists(lists, start, mid);
    ListNode* right = mergeKLists(lists, mid + 1, end);
    return mergeTwoLists(left, right);
}

ListNode* mergeKLists(vector<ListNode*>& lists) {
    return mergeKLists(lists, 0, lists.size() - 1);
}

int main() {
    // Example usage
    ListNode* l1 = new ListNode(1, new ListNode(4, new ListNode(5)));
    ListNode* l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
    ListNode* l3 = new ListNode(2, new ListNode(6));
    vector<ListNode*> lists = {l1, l2, l3};
    ListNode* result = mergeKLists(lists);
    while (result) {
        cout << result->val << " ";
        result = result->next;
    }
    return 0;
}