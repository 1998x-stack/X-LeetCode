
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void backtrack(vector<vector<int>>& ans, vector<int>& combination, int start, int n, int k){
        if(k==0){
            ans.push_back(combination);
            return;
        }

        for (int i = start; i <= n; ++i){
            combination.push_back(i);
            backtrack(ans, combination, i+1, n, k-1);
            combination.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> combination;
        backtrack(ans, combination, 1, n, k);
        return ans;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> results = sol.combine(4, 2);
    for (const auto& combo : results) {
        for (int num : combo) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}