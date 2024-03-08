#include <iostream>
using namespace std;

// 定义二叉树节点结构
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 函数声明
TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p);

// 主函数
int main() {
    // 构建示例树
    TreeNode* root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);

    // 测试用例
    TreeNode* p = root->left; // 查找节点1的中序后继
    TreeNode* successor = inorderSuccessor(root, p);
    if (successor) {
        cout << "Inorder Successor of " << p->val << " is: " << successor->val << endl;
    } else {
        cout << "Inorder Successor of " << p->val << " is: nullptr" << endl;
    }

    // 释放内存
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}

// 实现查找中序后继的函数
TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
    TreeNode* successor = nullptr;
    while (root) {
        if (p->val < root->val) {
            successor = root; // 可能的后继节点
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return successor;
}