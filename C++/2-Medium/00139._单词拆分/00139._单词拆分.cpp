#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

// 判断字符串s是否能够被拆分为一个或多个在字典wordDict中出现的单词
bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> dict(wordDict.begin(), wordDict.end()); // 将wordDict转换为哈希表，以便快速查询
    vector<bool> dp(s.size()+1, false); // dp[i]表示s的前i个字符是否能被拆分为字典中的单词
    dp[0] = true; // 空字符串可以被拆分

    for(int i = 1; i <= s.size(); ++i){
        for(int j = 0; j < i; ++j){
            if(dp[j] && dict.find(s.substr(j, i-j)) != dict.end()){
                dp[i] = true;
                break;
            }
        }
    }
    return dp[s.size()];
}

int main() {
    // 示例
    vector<string> wordDict = {"leet", "code"};
    string s = "leetcode";
    cout << (wordBreak(s, wordDict) ? "true" : "false") << endl;

    return 0;
}