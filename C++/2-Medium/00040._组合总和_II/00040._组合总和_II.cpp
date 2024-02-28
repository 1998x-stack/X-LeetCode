#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        sort(candidates.begin(), candidates.end());
        backtrack(result, candidates, current, target, 0);
        return result;
    }

private:
    void backtrack(vector<vector<int>>& result, const vector<int>& candidates, vector<int>& current, int remain, int start) {
        if (remain == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); ++i) {
            // Skip duplicates
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            // Break if the remaining target is less than the current number
            if (remain - candidates[i] < 0) break;
            current.push_back(candidates[i]);
            backtrack(result, candidates, current, remain - candidates[i], i + 1);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> candidates = {10,1,2,7,6,1,5};
    int target = 8;
    vector<vector<int>> result = solution.combinationSum2(candidates, target);
    for (const auto& combination : result) {
        for (int num : combination) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}