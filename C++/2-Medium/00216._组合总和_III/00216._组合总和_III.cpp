#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> results;
        vector<int> combination;
        backtrack(1, k, n, combination, results);
        return results;
    }

    void backtrack(int start, int k, int n, vector<int>& combination, vector<vector<int>>& results) {
        // 终止条件：长度等于 k 且总和等于 n
        if (combination.size() == k && n == 0) {
            results.push_back(combination);
            return;
        }
        // 遍历可能的选择
        for (int i = start; i <= 9; ++i) {
            // 剪枝：如果当前数字大于 n，不再继续探索
            if (i > n) break;
            combination.push_back(i);
            // 递归探索下一个数字，总和减去当前数字
            backtrack(i + 1, k, n - i, combination, results);
            // 撤销选择
            combination.pop_back();
        }
    }
};

int main() {
    Solution solution;
    int k = 3, n = 7;
    vector<vector<int>> results = solution.combinationSum3(k, n);
    for (const auto& combination : results) {
        for (int num : combination) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}