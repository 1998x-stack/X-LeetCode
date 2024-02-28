#include <vector>
#include <algorithm> // 用于sort函数
#include <iostream>
#include <fstream>
using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        vector<bool> used(nums.size(), false);
        sort(nums.begin(), nums.end()); // 排序，以便于处理重复元素
        backtrack(res, nums, path, used);
        return res;
    }

    void backtrack(vector<vector<int>>& res, vector<int>& nums, vector<int>& path, vector<bool>& used) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1])) continue; // 跳过重复元素
            used[i] = true;
            path.push_back(nums[i]);
            backtrack(res, nums, path, used);
            used[i] = false; // 回溯
            path.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> result = solution.permuteUnique(nums);

    // 输出结果
    for (const auto& perm : result) {
        for (int num : perm) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}