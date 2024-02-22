#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

// 罗马数字转整数函数
int romanToInt(string s) {
    // 创建罗马数字到整数的映射
    unordered_map<char, int> romanMap = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
                                         {'C', 100}, {'D', 500}, {'M', 1000}};
    
    int total = 0; // 初始化总和为0
    int prevValue = 0; // 存储前一个字符的值，初始为0

    // 从左到右遍历字符串
    for (int i = 0; i < s.length(); i++) {
        int value = romanMap[s[i]]; // 获取当前字符对应的整数值

        // 如果当前字符代表的值大于前一个字符的值，说明遇到了如IV或IX这样的特殊情况
        if (value > prevValue) {
            // 减去2倍的prevValue（因为之前加过一次，现在需要减去两次）
            total += value - 2 * prevValue;
        } else {
            // 否则，直接加上当前字符的值
            total += value;
        }
        prevValue = value; // 更新前一个字符的值
    }

    return total; // 返回最终的总和
}

int main() {
    string roman = "MCMXCIV";
    cout << "The integer value of " << roman << " is " << romanToInt(roman) << endl;
    return 0;
}