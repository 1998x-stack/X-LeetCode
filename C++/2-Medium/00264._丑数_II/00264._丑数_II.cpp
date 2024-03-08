#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int nthUglyNumber(int n) {
    vector<int> dp(n, 0);
    dp[0] = 1; // 第一个丑数为 1
    int p2 = 0, p3 = 0, p5 = 0; // 初始化三个指针
    
    for (int i = 1; i < n; ++i) {
        // 计算下一个丑数
        int next2 = dp[p2] * 2, next3 = dp[p3] * 3, next5 = dp[p5] * 5;
        dp[i] = min(next2, min(next3, next5));
        
        // 更新指针
        if (dp[i] == next2) ++p2;
        if (dp[i] == next3) ++p3;
        if (dp[i] == next5) ++p5;
    }
    return dp[n - 1];
}

int main() {
    int n;
    cout << "请输入 n 的值: ";
    cin >> n;
    cout << "第 " << n << " 个丑数是: " << nthUglyNumber(n) << endl;
    return 0;
}