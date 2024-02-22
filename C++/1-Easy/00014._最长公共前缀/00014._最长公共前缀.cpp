#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return ""; // 如果数组为空，立即返回空字符串

        for (int i = 0; i < strs[0].length(); ++i) { // 遍历第一个字符串的每个字符
            char c = strs[0][i];
            for (int j = 1; j < strs.size(); ++j) { // 遍历其他字符串
                // 如果当前字符不匹配或字符串已经结束，返回当前已找到的前缀
                if (i == strs[j].length() || strs[j][i] != c) {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0]; // 所有字符串均匹配第一个字符串，返回第一个字符串
    }
};

int main() {
    // 示例测试
    Solution solution;
    vector<string> strs = {"flower", "flow", "flight"};
    cout << "The longest common prefix is: " << solution.longestCommonPrefix(strs) << endl;
    return 0;
}