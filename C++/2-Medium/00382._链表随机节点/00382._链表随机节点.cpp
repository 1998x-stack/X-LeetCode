#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

// 链表节点的定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Solution类定义
class Solution {
private:
    ListNode* head;
public:
    Solution(ListNode* head) : head(head) {
        srand(time(0)); // 初始化随机数种子
    }
    
    int getRandom() {
        ListNode* current = head;
        int i = 1;
        int chosenValue = 0;
        while (current != NULL) {
            if (rand() % i == 0) { // 等概率选择
                chosenValue = current->val;
            }
            i++;
            current = current->next;
        }
        return chosenValue;
    }
};

int main() {
    // 构建链表1->2->3
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    
    // 初始化Solution对象
    Solution solution(head);
    
    // 打印10次随机节点的值，用于测试
    for(int i = 0; i < 10; i++) {
        cout << solution.getRandom() << endl;
    }
    
    return 0;
}