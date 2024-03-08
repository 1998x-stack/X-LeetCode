#include <iostream>
#include <algorithm>
using namespace std;

// 定义二叉树节点结构
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// DFS函数声明
void dfs(TreeNode* node, int prev_val, int curr_length, int& max_length) {
    if (!node) return; // 如果当前节点为空，则返回
    if (node->val == prev_val + 1) {
        ++curr_length; // 如果当前节点的值是连续的，增加长度
    } else {
        curr_length = 1; // 否则，重置连续序列长度为1
    }
    max_length = max(max_length, curr_length); // 更新最长连续序列长度
    dfs(node->left, node->val, curr_length, max_length); // 对左子树进行DFS
    dfs(node->right, node->val, curr_length, max_length); // 对右子树进行DFS
}

// 计算二叉树的最长连续序列长度
int longestConsecutive(TreeNode* root) {
    if (!root) return 0;
    int max_length = 0;
    dfs(root, root->val - 1, 0, max_length); // 从根节点开始DFS遍历
    return max_length;
}

int main() {
    // 构建测试用例
    TreeNode *root = new TreeNode(1);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(2);
    root->right->right = new TreeNode(4);
    root->right->right->right = new TreeNode(5);
    
    // 计算最长连续序列长度并输出
    cout << "The longest consecutive sequence length is: " << longestConsecutive(root) << endl;
    
    return 0;
}