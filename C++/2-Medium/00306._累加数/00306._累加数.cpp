#include <iostream>
#include <string>
using namespace std;

bool isValid(string s, int start, int len1, int len2) {
    if (s[start] == '0' && len1 > 1) return false; // 第一个数前导零
    if (s[start + len1] == '0' && len2 > 1) return false; // 第二个数前导零
    string num1 = s.substr(start, len1);
    string num2 = s.substr(start + len1, len2);
    string sum;
    for (int i = start + len1 + len2; i < s.length(); i += sum.length()) {
        // 大数加法
        int carry = 0, n = max(num1.length(), num2.length());
        sum = "";
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        for (int j = 0; j < n || carry; ++j) {
            if (j < num1.length()) carry += num1[j] - '0';
            if (j < num2.length()) carry += num2[j] - '0';
            sum += carry % 10 + '0';
            carry /= 10;
        }
        reverse(sum.begin(), sum.end());
        // 检查sum是否为下一个子串的前缀
        if (s.substr(i, sum.length()) != sum) return false;
        // 更新num1和num2以进行下一轮检查
        num1 = num2;
        num2 = sum;
    }
    return true;
}

bool isAdditiveNumber(string s) {
    int n = s.length();
    for (int i = 1; i <= n / 2; ++i) {
        for (int j = 1; j <= (n - i) / 2; ++j) {
            if (isValid(s, 0, i, j)) return true;
        }
    }
    return false;
}

int main() {
    // 测试用例
    string test1 = "112358";
    string test2 = "199100199";
    cout << "Is 112358 an additive number? " << isAdditiveNumber(test1) << endl;
    cout << "Is 199100199 an additive number? " << isAdditiveNumber(test2) << endl;
    return 0;
}