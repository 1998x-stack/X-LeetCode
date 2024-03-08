#include <iostream>
using namespace std;

// 定义树的节点结构
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 辅助函数，用于判断是否为同值子树，并统计数量
bool isUnivalTree(TreeNode* node, int& count, int parentVal) {
    if (!node) return true; // 空节点视为同值子树
    
    // 递归检查左右子树
    bool left = isUnivalTree(node->left, count, node->val);
    bool right = isUnivalTree(node->right, count, node->val);
    
    // 如果当前节点不是同值子树，则返回false
    if (!left || !right) return false;
    
    // 如果当前节点是同值子树，增加统计数量
    count++;
    
    // 返回当前节点值是否等于父节点值
    return node->val == parentVal;
}

// 主函数，用于统计同值子树的数量
int countUnivalSubtrees(TreeNode* root) {
    int count = 0;
    // 对于根节点，其父节点值不重要，可以任意设置
    isUnivalTree(root, count, 0);
    return count;
}

// 主函数，用于测试
int main() {
    // 构建测试用例的树
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(1);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(1);
    root->right->right = new TreeNode(1);

    // 计算并输出同值子树的数量
    cout << "The number of unival subtrees is: " << countUnivalSubtrees(root) << endl;

    return 0;
}