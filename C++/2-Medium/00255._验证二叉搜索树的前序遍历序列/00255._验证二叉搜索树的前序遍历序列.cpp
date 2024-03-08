#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// 验证是否为二叉搜索树的前序遍历序列
bool verifyPreorder(vector<int>& preorder) {
    stack<int> stk;
    int lower_bound = INT_MIN; // 设置当前节点值可以取的最小值
    for (int num : preorder) {
        // 如果当前元素小于lower_bound，则不是有效的前序遍历序列
        if (num < lower_bound) return false;
        // 当前元素大于栈顶元素，更新lower_bound
        while (!stk.empty() && num > stk.top()) {
            lower_bound = stk.top(); // 更新为右子树的新的最小值
            stk.pop();
        }
        stk.push(num); // 将当前元素压入栈中
    }
    return true; // 遍历完毕，未发现违反规则的情况
}

int main() {
    // 示例
    vector<int> preorder1 = {5, 2, 6, 1, 3};
    vector<int> preorder2 = {5, 2, 1, 3, 6};
    cout << "Example 1: " << (verifyPreorder(preorder1) ? "true" : "false") << endl;
    cout << "Example 2: " << (verifyPreorder(preorder2) ? "true" : "false") << endl;
    return 0;
}