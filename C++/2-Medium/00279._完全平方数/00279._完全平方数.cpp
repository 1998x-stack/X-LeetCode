#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        
        // 动态规划填表
        for (int i = 1; i <= n; ++i) {
            // 尝试所有可能的完全平方数
            for (int j = 1; j * j <= i; ++j) {
                dp[i] = min(dp[i], dp[i - j * j] + 1);
            }
        }
        
        return dp[n];
    }
};

int main() {
    Solution solution;
    int n = 12; // 示例输入
    cout << "The minimum number of perfect squares for " << n << " is " << solution.numSquares(n) << endl;
    n = 13; // 示例输入
    cout << "The minimum number of perfect squares for " << n << " is " << solution.numSquares(n) << endl;
    return 0;
}