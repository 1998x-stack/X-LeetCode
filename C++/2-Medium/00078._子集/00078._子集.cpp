
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums){
        vector<vector<int>> ans;
        vector<int> path;
        backtrack(nums, 0, path, ans);
        return ans;
    }
    
    void backtrack(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& result) {
        result.push_back(path); // 将当前路径添加到结果中
        for (int i = start; i < nums.size(); ++i) {
            path.push_back(nums[i]); // 选择当前元素
            backtrack(nums, i + 1, path, result); // 递归探索下一步
            path.pop_back(); // 撤销选择
        }
    }
};


int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3}; // 示例输入
    vector<vector<int>> result = solution.subsets(nums);

    // 打印输出
    cout << "[";
    for (int i = 0; i < result.size(); ++i) {
        cout << "[";
        for (int j = 0; j < result[i].size(); ++j) {
            cout << result[i][j];
            if (j < result[i].size() - 1) cout << ",";
        }
        cout << "]";
        if (i < result.size() - 1) cout << ",";
    }
    cout << "]" << endl;

    return 0;
}