#include <iostream>
#include <vector>
#include <string>
using namespace std;

int minDistance(string word1, string word2) {
    int m = word1.size(), n = word2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    // 初始化边界条件
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j;
    }
    // 计算所有dp值
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i - 1] == word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]; // 字符相同，不需要操作
            } else {
                dp[i][j] = 1 + min(dp[i - 1][j - 1], // 替换操作
                                   min(dp[i][j - 1], // 插入操作
                                       dp[i - 1][j])); // 删除操作
            }
        }
    }
    return dp[m][n];
}

int main() {
    string word1 = "horse", word2 = "ros";
    cout << "The minimum edit distance is: " << minDistance(word1, word2) << endl;
    return 0;
}