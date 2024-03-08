#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// 辅助函数：去除多余的空格
void removeExtraSpaces(string &s) {
    int n = s.length(), index = 0; // index用于记录处理后字符串的长度
    for (int i = 0; i < n; ++i) {
        if (s[i] != ' ' || (i > 0 && s[i - 1] != ' ')) { // 当前字符不是空格或者当前字符和前一个字符不都是空格
            if (index > 0 && s[i] != ' ') s[index++] = ' '; // 在单词前加空格，但不是第一个单词前
            s[index++] = s[i]; // 复制字符
        }
    }
    s.resize(index); // 调整字符串大小
}

// 主函数
int main() {
    string s = "  the sky is blue  ";
    // 1. 去除多余空格
    removeExtraSpaces(s);
    // 2. 翻转整个字符串
    reverse(s.begin(), s.end());
    // 3. 翻转每个单词
    int start = 0, end = 0, n = s.length();
    while (start < n) {
        while (end < n && s[end] != ' ') ++end; // 找到单词的末尾
        reverse(s.begin() + start, s.begin() + end); // 翻转单词
        start = end + 1; // 移动到下一个单词的开头
        end = start;
    }
    // 输出结果
    cout << s << endl;
    return 0;
}
