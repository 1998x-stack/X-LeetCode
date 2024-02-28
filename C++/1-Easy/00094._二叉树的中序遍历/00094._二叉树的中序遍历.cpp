#include <iostream>
#include <vector>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // 用于存储中序遍历结果的数组
    std::vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> result;
        inorder(root, result);
        return result;
    }
    
    // 辅助函数，用于递归地执行中序遍历
    void inorder(TreeNode* node, std::vector<int>& result) {
        if (!node) return; // 基本情况：节点为空
        inorder(node->left, result); // 递归左子树
        result.push_back(node->val); // 访问根节点
        inorder(node->right, result); // 递归右子树
    }
};

int main() {
    // 示例二叉树的构建
    TreeNode *root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);

    Solution solution;
    std::vector<int> result = solution.inorderTraversal(root);
    
    // 打印中序遍历结果
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    return 0;
}