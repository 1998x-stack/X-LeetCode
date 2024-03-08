#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isMatch(string s, string p) {
    int m = s.size(), n = p.size();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    dp[0][0] = true;
    for (int i = 1; i <= n; ++i) {
        if (p[i - 1] == '*') dp[0][i] = true;
        else break;
    }
    
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            } else if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }
    return dp[m][n];
}

int main() {
    string s = "adceb", p = "*a*b"; // 示例输入
    cout << "Result: " << isMatch(s, p) << endl; // 输出结果
    return 0;
}