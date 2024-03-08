#include <iostream>
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL) return NULL;
        if (root->val > p->val && root->val > q->val) {
            // 如果root的值大于p和q的值，向左子树递归
            return lowestCommonAncestor(root->left, p, q);
        } else if (root->val < p->val && root->val < q->val) {
            // 如果root的值小于p和q的值，向右子树递归
            return lowestCommonAncestor(root->right, p, q);
        } else {
            // 如果当前节点的值在p和q的值之间，当前节点即为最近公共祖先
            return root;
        }
    }
};

int main() {
    // 构造示例树
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(2);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(9);
    root->left->right->left = new TreeNode(3);
    root->left->right->right = new TreeNode(5);

    Solution sol;
    TreeNode* p = root->left; // 节点2
    TreeNode* q = root->right; // 节点8
    TreeNode* ans = sol.lowestCommonAncestor(root, p, q);
    cout << "LCA of " << p->val << " and " << q->val << " is " << ans->val << endl;

    // 清理分配的内存
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