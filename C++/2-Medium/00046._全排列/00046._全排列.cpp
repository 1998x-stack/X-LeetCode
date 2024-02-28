#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void backtrack(vector<int>& nums, vector<vector<int>>& res, vector<int>& path, vector<bool>& used) {
        if (path.size() == nums.size()) { // 当前路径长度等于输入数组长度，说明找到了一个全排列
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (used[i]) continue; // 如果这个数已经使用过了，则跳过
            path.push_back(nums[i]); // 选择当前数
            used[i] = true; // 标记为已使用
            backtrack(nums, res, path, used); // 进入下一层决策树
            path.pop_back(); // 取消选择
            used[i] = false; // 回溯，撤销标记
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        vector<bool> used(nums.size(), false); // 初始化未使用标记
        backtrack(nums, res, path, used); // 调用回溯函数
        return res;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3}; // 示例输入
    vector<vector<int>> result = solution.permute(nums); // 调用permute函数
    for (const auto &perm : result) {
        for (int num : perm) {
            cout << num << " ";
        }
        cout << "\\n";
    }
    return 0;
}