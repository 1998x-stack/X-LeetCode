#include <iostream>
#include <stack>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class BSTIterator {
private:
    stack<TreeNode*> nodeStack; // 栈用于存储中序遍历的状态

    // 将给定节点及其所有左子节点压入栈中
    void pushLeft(TreeNode* node) {
        while (node != nullptr) {
            nodeStack.push(node);
            node = node->left;
        }
    }

public:
    BSTIterator(TreeNode* root) {
        pushLeft(root); // 初始化时，将根节点及其所有左子节点压入栈中
    }
    
    // 返回二叉搜索树中的下一个最小的数
    int next() {
        TreeNode* nextNode = nodeStack.top();
        nodeStack.pop();
        pushLeft(nextNode->right); // 将下一个节点的右子节点及其所有左子节点压入栈中
        return nextNode->val;
    }
    
    // 返回二叉搜索树中是否还有下一个数
    bool hasNext() {
        return !nodeStack.empty();
    }
};

// 用于测试的主函数
int main() {
    // 示例树的构建
    TreeNode* root = new TreeNode(7);
    root->left = new TreeNode(3);
    root->right = new TreeNode(15);
    root->right->left = new TreeNode(9);
    root->right->right = new TreeNode(20);

    BSTIterator iterator(root);
    cout << iterator.next() << " ";    // 输出 3
    cout << iterator.next() << " ";    // 输出 7
    cout << (iterator.hasNext() ? "true" : "false") << " "; // 输出 true
    cout << iterator.next() << " ";    // 输出 9
    cout << (iterator.hasNext() ? "true" : "false") << " "; // 输出 true
    cout << iterator.next() << " ";    // 输出 15
    cout << (iterator.hasNext() ? "true" : "false") << " "; // 输出 true
    cout << iterator.next() << " ";    // 输出 20
    cout << (iterator.hasNext() ? "true" : "false") << endl; // 输出 false

    return 0;
}