#include <iostream>
#include <vector>
#include <algorithm>
#include <climits> // Include for INT_MAX and INT_MIN
using namespace std;

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
    struct Info {
        bool isBST;
        int size;
        int minVal;
        int maxVal;
    };

    int largestBSTSubtree(TreeNode* root) {
        int maxSize = 0;
        dfs(root, maxSize);
        return maxSize;
    }

    Info dfs(TreeNode* node, int& maxSize) {
        if (!node) return {true, 0, INT_MAX, INT_MIN};

        auto left = dfs(node->left, maxSize);
        auto right = dfs(node->right, maxSize);

        if (left.isBST && right.isBST && node->val > left.maxVal && node->val < right.minVal) {
            int size = left.size + right.size + 1;
            maxSize = max(maxSize, size);
            return {true, size, min(node->val, left.minVal), max(node->val, right.maxVal)};
        } else {
            return {false, 0, 0, 0};
        }
    }
};

int main() {
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5, new TreeNode(1), new TreeNode(8));
    root->right = new TreeNode(15, nullptr, new TreeNode(7));
    
    Solution solution;
    cout << "Largest BST Subtree Size: " << solution.largestBSTSubtree(root) << endl;
    
    delete root->left->left;
    delete root->left->right;
    delete root->right->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}