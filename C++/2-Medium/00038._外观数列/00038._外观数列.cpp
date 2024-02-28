#include <iostream>
#include <string>
using namespace std;

// 生成外观数列的下一项
string getNext(const string &current) {
    string result;
    int count = 1; // 计数器，至少有一个字符
    // 从第一个字符开始遍历
    for (int i = 1; i <= current.length(); ++i) {
        // 如果当前字符与前一个相同，计数器增加
        if (i < current.length() && current[i] == current[i - 1]) {
            count++;
        } else {
            // 否则，添加前一个字符的计数和字符本身到结果字符串
            result += to_string(count) + current[i - 1];
            count = 1; // 重置计数器
        }
    }
    return result;
}

// 生成外观数列第 n 项
string countAndSay(int n) {
    string current = "1";
    // 从第二项开始，生成外观数列，直到第 n 项
    for (int i = 2; i <= n; ++i) {
        current = getNext(current);
    }
    return current;
}

int main() {
    // 测试代码
    int n = 4; // 可以修改 n 的值以测试不同的输入
    cout << "The " << n << "th term of the count-and-say sequence is: " << countAndSay(n) << endl;
    return 0;
}