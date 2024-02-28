#include <iostream>
#include <string>

using namespace std;

// 函数：寻找以left和right为中心的最长回文子串
string expandAroundCenter(const string& s, int left, int right) {
    while (left >= 0 && right < s.length() && s[left] == s[right]) {
        --left;  // 向左扩展
        ++right; // 向右扩展
    }
    // 返回找到的回文子串
    return s.substr(left + 1, right - left - 1);
}

// 主函数：寻找最长回文子串
string longestPalindrome(string s) {
    if (s.length() < 1) return "";
    
    string longest;
    for (int i = 0; i < s.length(); ++i) {
        // 假设回文串长度为奇数
        string p1 = expandAroundCenter(s, i, i);
        if (p1.length() > longest.length()) {
            longest = p1;
        }
        
        // 假设回文串长度为偶数
        string p2 = expandAroundCenter(s, i, i + 1);
        if (p2.length() > longest.length()) {
            longest = p2;
        }
    }
    return longest;
}

// 测试代码
int main() {
    string s = "babad";
    cout << "Input: " << s << endl;
    cout << "Longest Palindromic Substring: " << longestPalindrome(s) << endl;
    return 0;
}