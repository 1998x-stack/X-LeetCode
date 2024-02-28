#include <iostream>
using namespace std;

// 定义二叉树节点结构
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 辅助函数：递归求根到叶子节点数字之和
int sumNumbersHelper(TreeNode* root, int currentSum) {
    if (!root) return 0; // 如果当前节点为空，返回0
    currentSum = currentSum * 10 + root->val; // 更新路径值
    if (!root->left && !root->right) { // 如果是叶子节点，返回当前累计的和
        return currentSum;
    }
    // 递归左右子树
    return sumNumbersHelper(root->left, currentSum) + sumNumbersHelper(root->right, currentSum);
}

// 主函数：计算从根节点到叶节点的数字之和
int sumNumbers(TreeNode* root) {
    return sumNumbersHelper(root, 0);
}

int main() {
    // 构建示例二叉树: [1,2,3]
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    
    // 调用函数并输出结果
    cout << "The sum of root-to-leaf numbers is: " << sumNumbers(root) << endl;
    
    // 清理分配的内存
    delete root->left;
    delete root->right;
    delete root;
    
    return 0;
}