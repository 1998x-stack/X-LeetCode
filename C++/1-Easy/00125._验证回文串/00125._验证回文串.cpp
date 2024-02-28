#include <iostream>
#include <string>
#include <cctype> // 包含 isalnum 和 tolower 函数

using namespace std;

// 验证是否为回文串的函数
bool isPalindrome(string s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        // 从左向右移动，跳过非字母数字字符
        while (left < right && !isalnum(s[left])) left++;
        // 从右向左移动，跳过非字母数字字符
        while (left < right && !isalnum(s[right])) right--;
        // 比较字符，忽略大小写
        if (tolower(s[left]) != tolower(s[right])) return false;
        left++;
        right--;
    }
    return true;
}

int main() {
    // 示例字符串
    string testStr = "A man, a plan, a canal: Panama";
    // 调用函数并打印结果
    cout << (isPalindrome(testStr) ? "true" : "false") << endl;
    return 0;
}