#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <tuple>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 函数用于执行二叉树的垂直遍历
vector<vector<int>> verticalOrder(TreeNode* root) {
    if (!root) return {};
    
    // 用来存储结果，外层map的key是列索引，内层map的key是行索引
    map<int, map<int, vector<int>>> nodes;
    // 队列用于BFS，存储节点以及其对应的行和列索引
    queue<tuple<TreeNode*, int, int>> q;
    q.push(make_tuple(root, 0, 0)); // 根节点位于(0, 0)
    
    while (!q.empty()) {
        auto [node, row, col] = q.front();
        q.pop();
        nodes[col][row].push_back(node->val);
        if (node->left) {
            q.push(make_tuple(node->left, row + 1, col - 1)); // 左子节点行+1，列-1
        }
        if (node->right) {
            q.push(make_tuple(node->right, row + 1, col + 1)); // 右子节点行+1，列+1
        }
    }
    
    // 将map中的结果转换为题目要求的格式
    vector<vector<int>> result;
    for (auto& p : nodes) {
        vector<int> colVals;
        for (auto& q : p.second) {
            colVals.insert(colVals.end(), q.second.begin(), q.second.end());
        }
        result.push_back(colVals);
    }
    
    return result;
}

// 主函数用于测试
int main() {
    // 构建测试用例的二叉树
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    
    // 执行垂直遍历
    vector<vector<int>> result = verticalOrder(root);
    // 打印结果
    for (auto& col : result) {
        for (int val : col) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    return 0;
}