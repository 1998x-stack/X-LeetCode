#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // 寻找最近公共祖先的递归函数
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || root == p || root == q) return root; // 基础情况处理
        TreeNode* left = lowestCommonAncestor(root->left, p, q); // 在左子树中查找
        TreeNode* right = lowestCommonAncestor(root->right, p, q); // 在右子树中查找
        if (left && right) return root; // 如果在两边都找到了，当前节点是LCA
        return left ? left : right; // 返回非空的子结果
    }
};

int main() {
    // 构建示例树并测试
    TreeNode *root = new TreeNode(3);
    root->left = new TreeNode(5);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(6);
    root->left->right = new TreeNode(2);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(8);
    root->left->right->left = new TreeNode(7);
    root->left->right->right = new TreeNode(4);

    Solution solution;
    TreeNode* p = root->left; // Node 5
    TreeNode* q = root->right; // Node 1
    TreeNode* lca = solution.lowestCommonAncestor(root, p, q);
    cout << "LCA: " << lca->val << endl; // 应输出 3，即节点3是5和1的最近公共祖先

    // 清理分配的节点
    delete root->left->right->right;
    delete root->left->right->left;
    delete root->right->right;
    delete root->right->left;
    delete root->left->right;
    delete root->left->left;
    delete root->right;
    delete root->left;
    delete root;

    return 0;
}