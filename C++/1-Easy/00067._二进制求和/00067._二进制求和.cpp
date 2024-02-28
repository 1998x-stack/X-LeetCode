#include <iostream>
#include <string>
using namespace std;

// 实现二进制求和函数
string addBinary(string a, string b) {
    string result = "";
    int i = a.size() - 1, j = b.size() - 1, carry = 0;
    
    // 从后向前遍历两个字符串
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0'; // 将a的当前位加到sum上
        if (j >= 0) sum += b[j--] - '0'; // 将b的当前位加到sum上
        
        // 计算当前位的结果和新的进位
        carry = sum / 2;
        result = char(sum % 2 + '0') + result; // 将当前结果位添加到结果字符串的前面
    }
    
    return result;
}

int main() {
    // 示例
    string a = "11", b = "1";
    cout << addBinary(a, b) << endl;
    return 0;
}