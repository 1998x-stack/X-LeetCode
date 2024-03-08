#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> result;
        vector<int> combination;
        backtrack(n, combination, result, 2);
        return result;
    }

private:
    void backtrack(int n, vector<int>& combination, vector<vector<int>>& result, int start) {
        if (n == 1) {
            if (combination.size() > 1) { // 确保至少有两个因子
                result.push_back(combination);
            }
            return;
        }
        
        for (int i = start; i <= n; ++i) {
            if (n % i == 0) { // 如果i是n的一个因子
                combination.push_back(i); // 添加因子到当前组合
                backtrack(n / i, combination, result, i); // 继续搜索剩余的因子
                combination.pop_back(); // 回溯，移除最后一个因子，尝试下一个可能的因子
            }
        }
    }
};

int main() {
    Solution solution;
    vector<vector<int>> result = solution.getFactors(16);
    for (const auto& factors : result) {
        for (int factor : factors) {
            cout << factor << " ";
        }
        cout << endl;
    }
    return 0;
}