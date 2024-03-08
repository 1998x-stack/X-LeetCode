#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

// 函数声明：判断玩家是否能赢
bool canWin(string s, unordered_map<string, bool>& memo);

// 主函数
int main() {
    string s = "++++"; // 测试字符串
    unordered_map<string, bool> memo; // 记忆化存储
    bool result = canWin(s, memo); // 调用 canWin 函数判断先手是否必胜
    cout << (result ? "true" : "false") << endl; // 输出结果
    return 0;
}

// 使用递归和记忆化搜索判断先手玩家是否有必胜策略
bool canWin(string s, unordered_map<string, bool>& memo) {
    if (memo.count(s)) return memo[s]; // 如果已经计算过这个状态，直接返回结果
    for (int i = 0; i < int(s.length()) - 1; ++i) {
        if (s[i] == '+' && s[i + 1] == '+') { // 找到连续的 "++"
            string t = s.substr(0, i) + "--" + s.substr(i + 2); // 翻转 "++" 为 "--"
            if (!canWin(t, memo)) { // 递归检查这一操作后对手是否会输
                memo[s] = true; // 如果对手会输，当前玩家必胜
                return true;
            }
        }
    }
    memo[s] = false; // 遍历完所有可能都无法获胜，则当前玩家必败
    return false;
}
