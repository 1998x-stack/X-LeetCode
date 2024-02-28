#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // 对数组进行排序，以便处理重复元素
        vector<vector<int>> res;
        vector<int> temp;
        backtrack(res, temp, nums, 0);
        return res;
    }
    
    void backtrack(vector<vector<int>>& res, vector<int>& temp, vector<int>& nums, int start) {
        res.push_back(temp); // 将当前路径添加到结果集中
        for (int i = start; i < nums.size(); ++i) {
            if (i > start && nums[i] == nums[i-1]) continue; // 跳过重复元素
            temp.push_back(nums[i]); // 选择当前元素
            backtrack(res, temp, nums, i + 1); // 递归
            temp.pop_back(); // 回溯
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 2}; // 示例输入
    vector<vector<int>> result = solution.subsetsWithDup(nums);
    
    // 打印结果
    for (const auto& subset : result) {
        cout << '[';
        for (int num : subset) {
            cout << num << ',';
        }
        if (!subset.empty()) cout << "\b";
        cout << "] ";
    }
    return 0;
}