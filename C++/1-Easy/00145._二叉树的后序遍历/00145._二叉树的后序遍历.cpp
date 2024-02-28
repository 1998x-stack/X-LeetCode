#include <iostream>
#include <vector>
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
    // Function to perform postorder traversal
    std::vector<int> postorderTraversal(TreeNode* root) {
        std::vector<int> result;
        postorder(root, result); // Start the postorder traversal
        return result;
    }
    
    // Helper function to perform the traversal
    void postorder(TreeNode* node, std::vector<int>& result) {
        if (!node) return; // Base case: if node is null
        
        postorder(node->left, result);  // Traverse left subtree
        postorder(node->right, result); // Traverse right subtree
        result.push_back(node->val);    // Visit the node
    }
};

int main() {
    // Example usage
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    
    Solution solution;
    std::vector<int> result = solution.postorderTraversal(root);
    
    // Output the result
    std::ofstream out("/mnt/data/postorder_traversal_result.txt");
    for (int val : result) {
        std::cout << val << " ";
        out << val << " ";
    }
    out.close();
    
    return 0;
}