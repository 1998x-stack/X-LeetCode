#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Helper function to create a binary tree from a vector of integers (null represented by -1)
TreeNode* createTree(const vector<int>& nodes, int index) {
    if (index >= nodes.size() || nodes[index] == -1) return nullptr;
    
    TreeNode* root = new TreeNode(nodes[index]);
    root->left = createTree(nodes, 2 * index + 1);
    root->right = createTree(nodes, 2 * index + 2);
    return root;
}

// Function to perform in-order traversal
void inOrderTraversal(TreeNode* node, int &k, int &result) {
    if (node == NULL || k == 0) return;

    // Traverse the left subtree
    inOrderTraversal(node->left, k, result);

    // Visit the node
    if (--k == 0) {
        result = node->val;
        return;
    }

    // Traverse the right subtree
    inOrderTraversal(node->right, k, result);
}

// Main function to find the kth smallest element in a BST
int kthSmallest(TreeNode* root, int k) {
    int result = -1; // Initialize result
    inOrderTraversal(root, k, result);
    return result;
}

int main() {
    // Example: create a binary search tree
    vector<int> nodes = {5, 3, 6, 2, 4, -1, -1, 1}; // BST representation (level-order)
    TreeNode* root = createTree(nodes, 0);
    
    int k = 3; // Find the 3rd smallest element
    cout << "The " << k << "rd smallest element in the BST is: " << kthSmallest(root, k) << endl;
    
    return 0;
}