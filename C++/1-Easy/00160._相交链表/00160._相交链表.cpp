#include <iostream>

// 链表节点的定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// 实现寻找两个链表相交节点的函数
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    if (headA == nullptr || headB == nullptr) return nullptr;
    
    ListNode *pA = headA, *pB = headB;
    
    // 当两个链表不相交时，最终pA和pB都将指向null，循环结束
    while (pA != pB) {
        // 如果当前指针到达链表末尾，则跳转到另一个链表的头部继续遍历
        pA = pA == nullptr ? headB : pA->next;
        pB = pB == nullptr ? headA : pB->next;
    }
    
    // 返回相交节点，如果不相交则为null
    return pA;
}

int main() {
    // 示例代码，实际环境中需要根据链表实际情况构造
    ListNode a1(4), a2(1), c1(8), c2(4), c3(5);
    ListNode b1(5), b2(6), b3(1);
    a1.next = &a2; a2.next = &c1; c1.next = &c2; c2.next = &c3;
    b1.next = &b2; b2.next = &b3; b3.next = &c1;
    
    ListNode *intersectionNode = getIntersectionNode(&a1, &b1);
    if (intersectionNode) {
        std::cout << "Intersection node value: " << intersectionNode->val << std::endl;
    } else {
        std::cout << "No intersection node." << std::endl;
    }
    
    return 0;
}