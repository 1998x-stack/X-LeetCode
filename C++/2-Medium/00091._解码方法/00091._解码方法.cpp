#include <iostream>
#include <string>
#include <vector>
using namespace std;

int numDecodings(string s) {
    if (s.empty() || s[0] == '0') return 0; // 处理前导零
    int n = s.size();
    vector<int> dp(n + 1, 0);
    dp[0] = 1; // 空字符串有一种解码方式
    dp[1] = s[0] != '0' ? 1 : 0; // 第一个字符如果不是'0'，有一种解码方式

    for (int i = 2; i <= n; i++) {
        int oneDigit = stoi(s.substr(i - 1, 1)); // 单个字符
        int twoDigit = stoi(s.substr(i - 2, 2)); // 两个字符组成的数字
        if (oneDigit >= 1) dp[i] += dp[i - 1]; // 如果单个字符有效
        if (twoDigit >= 10 && twoDigit <= 26) dp[i] += dp[i - 2]; // 如果两个字符组成的数字有效
    }

    return dp[n];
}

int main() {
    string s = "226";
    cout << "Number of ways to decode \"" << s << "\": " << numDecodings(s) << endl;
    return 0;
}