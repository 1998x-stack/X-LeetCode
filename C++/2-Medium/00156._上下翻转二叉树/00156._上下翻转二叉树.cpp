#include <iostream>
using namespace std;

// 定义二叉树节点结构
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 上下翻转二叉树的函数
TreeNode* upsideDownBinaryTree(TreeNode* root) {
    // 边界条件：如果节点为空，或者没有左子节点，直接返回当前节点
    if (!root || !root->left) {
        return root;
    }
    // 递归翻转左子树，并获取新的根节点
    TreeNode* newRoot = upsideDownBinaryTree(root->left);
    // 将当前节点的左子节点指向当前节点的右兄弟节点，实现翻转
    root->left->left = root->right;
    // 将当前节点的左子节点的右子节点指向当前节点，完成翻转
    root->left->right = root;
    // 避免循环引用，将当前节点的左右子节点设为null
    root->left = NULL;
    root->right = NULL;
    // 返回新的根节点
    return newRoot;
}

// 辅助函数，用于创建示例二叉树
TreeNode* createExampleTree() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    return root;
}

// 主函数
int main() {
    // 创建示例二叉树
    TreeNode* root = createExampleTree();
    // 进行上下翻转
    TreeNode* newRoot = upsideDownBinaryTree(root);
    // 输出结果，此处省略输出代码，实际中可以遍历打印树来验证结果
    cout << "Upside down transformation completed." << endl;
    return 0;
}