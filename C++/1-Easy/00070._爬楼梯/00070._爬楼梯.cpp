#include <iostream>
#include <vector>
using namespace std;

// 动态规划解决爬楼梯问题
int climbStairs(int n) {
    if (n <= 1) return n; // 基本情况
    vector<int> dp(n + 1); // 创建DP数组
    dp[1] = 1; // 到达第1阶的方法数
    dp[2] = 2; // 到达第2阶的方法数
    for (int i = 3; i <= n; i++) { // 从第3阶到第n阶
        dp[i] = dp[i - 1] + dp[i - 2]; // 到达第i阶的方法数
    }
    return dp[n]; // 返回到达第n阶的方法数
}

int main() {
    int n = 5; // 示例输入
    cout << "Number of ways to climb " << n << " stairs: " << climbStairs(n) << endl;
    return 0;
}