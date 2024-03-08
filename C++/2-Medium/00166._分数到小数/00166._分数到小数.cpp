#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

string fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) return "0";
    string result;
    // 处理符号
    if (numerator < 0 ^ denominator < 0) result += "-";
    // 转换为正数处理，注意溢出问题
    long num = numerator < 0 ? (long)numerator * -1 : (long)numerator;
    long den = denominator < 0 ? (long)denominator * -1 : (long)denominator;
    // 处理整数部分
    result += to_string(num / den);
    long remainder = num % den;
    if (remainder == 0) return result; // 能够整除
    result += ".";
    unordered_map<long, int> remainderMap;
    while (remainder != 0) {
        if (remainderMap.find(remainder) != remainderMap.end()) {
            result.insert(remainderMap[remainder], "(");
            result += ")";
            break;
        }
        remainderMap[remainder] = result.size();
        remainder *= 10;
        result += to_string(remainder / den);
        remainder %= den;
    }
    return result;
}

int main() {
    cout << "1/2 = " << fractionToDecimal(1, 2) << endl;
    cout << "2/1 = " << fractionToDecimal(2, 1) << endl;
    cout << "2/3 = " << fractionToDecimal(2, 3) << endl;
    cout << "-2/3 = " << fractionToDecimal(-2, 3) << endl;
    cout << "2/-3 = " << fractionToDecimal(2, -3) << endl;
    cout << "-2/-3 = " << fractionToDecimal(-2, -3) << endl;
    return 0;
}