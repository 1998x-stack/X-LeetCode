#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(candidates, target, result, current, 0);
        return result;
    }

private:
    void backtrack(vector<int>& candidates, int target, vector<vector<int>>& result, vector<int>& current, int start) {
        // 终止条件：如果目标数为0，说明当前组合满足条件
        if (target == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); ++i) {
            // 选择当前数如果它不使得组合之和超过目标数
            if (candidates[i] <= target) {
                current.push_back(candidates[i]);
                // 递归探索下一个数，注意目标数需要减去当前数
                backtrack(candidates, target - candidates[i], result, current, i);
                // 撤销选择
                current.pop_back();
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> candidates = {2,3,6,7};
    int target = 7;
    vector<vector<int>> result = solution.combinationSum(candidates, target);

    for (const auto& combination : result) {
        for (int num : combination) {
            cout << num << " ";
        }
        cout << "\\n";
    }

    return 0;
}