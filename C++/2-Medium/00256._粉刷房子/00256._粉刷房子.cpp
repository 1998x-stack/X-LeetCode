
#include <iostream>
#include <vector>
using namespace std;

// 动态规划解决粉刷房子问题的函数
int minCost(vector<vector<int>>& costs) {
    if (costs.empty()) return 0;
    int n = costs.size();
    vector<vector<int>> dp(n, vector<int>(3, 0));
    // 初始化第一个房子的成本
    for (int j = 0; j < 3; ++j) {
        dp[0][j] = costs[0][j];
    }
    // 动态规划计算每个房子的最低成本
    for (int i = 1; i < n; ++i) {
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1];
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2];
    }
    // 返回最后一个房子的最低成本
    return min(min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]);
}

int main() {
    // 示例
    vector<vector<int>> costs = {{17, 2, 17}, {16, 16, 5}, {14, 3, 19}};
    cout << "Minimum cost to paint all houses: " << minCost(costs) << endl;
    return 0;
}