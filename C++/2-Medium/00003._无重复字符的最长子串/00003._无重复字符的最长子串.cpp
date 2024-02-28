
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> charIndexMap; // 存储字符和其最新索引的映射
    int maxLength = 0; // 最长子串长度
    for (int start = 0, end = 0; end < s.length(); end++) {
        if (charIndexMap.find(s[end]) != charIndexMap.end()) {
            // 更新start指针，排除重复字符
            start = max(start, charIndexMap[s[end]] + 1);
        }
        // 更新字符的最新索引
        charIndexMap[s[end]] = end;
        // 更新最长子串长度
        maxLength = max(maxLength, end - start + 1);
    }
    return maxLength;
}

int main() {
    string input = "abcabcbb";
    cout << "Input: " << input << "\\n";
    cout << "Output: " << lengthOfLongestSubstring(input) << "\\n";
    return 0;
}