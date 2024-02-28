#include <iostream>
#include <fstream>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Step 1: Check if both nodes are NULL
        if (!p && !q) return true;
        // If one is NULL and the other is not, or their values are not equal, return false
        if (!p || !q || p->val != q->val) return false;
        // Step 3: Recursively compare left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};