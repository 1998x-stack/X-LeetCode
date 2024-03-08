#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int longestValidParentheses(string s) {
    int n = s.length();
    vector<int> dp(n, 0);
    int maxLength = 0;
    for (int i = 1; i < n; i++) {
        if (s[i] == ')') {
            if (s[i-1] == '(') {
                dp[i] = (i >= 2 ? dp[i-2] : 0) + 2;
            } else if (i - dp[i-1] > 0 && s[i - dp[i-1] - 1] == '(') {
                dp[i] = dp[i-1] + ((i - dp[i-1]) >= 2 ? dp[i - dp[i-1] - 2] : 0) + 2;
            }
            maxLength = max(maxLength, dp[i]);
        }
    }
    return maxLength;
}

int main() {
    // 测试用例
    string test1 = "(()";
    string test2 = ")()())";
    
    cout << "Test 1: " << longestValidParentheses(test1) << endl; // 应输出 2
    cout << "Test 2: " << longestValidParentheses(test2) << endl; // 应输出 4
    
    return 0;
}