#include <iostream>
#include <vector>
using namespace std;

// 动态规划解决不同路径问题
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 1)); // 初始化dp数组
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]; // 状态转移方程
        }
    }
    return dp[m - 1][n - 1]; // 返回结果
}

int main() {
    int m = 3, n = 7; // 示例输入
    cout << "Unique paths for " << m << " x " << n << " grid: " << uniquePaths(m, n) << endl; // 输出结果
    return 0;
}