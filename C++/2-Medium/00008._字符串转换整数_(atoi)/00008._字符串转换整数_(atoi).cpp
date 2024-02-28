#include <iostream>
#include <climits>
#include <string>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        if (s.empty()) return 0;
        int sign = 1, result = 0, index = 0;
        
        // 1. 忽略前导空格
        while (index < s.size() && s[index] == ' ') index++;
        
        // 2. 检测正负号
        if (index < s.size() && (s[index] == '+' || s[index] == '-')) {
            sign = (s[index] == '+') ? 1 : -1;
            index++;
        }
        
        // 3. 转换数字，并处理溢出
        while (index < s.size() && isdigit(s[index])) {
            int digit = s[index] - '0';
            // 检查溢出
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10)) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            result = 10 * result + digit;
            index++;
        }
        
        return result * sign;
    }
};

int main() {
    Solution solution;
    // 示例测试
    cout << solution.myAtoi("42") << endl; // 应输出: 42
    cout << solution.myAtoi("   -42") << endl; // 应输出: -42
    cout << solution.myAtoi("4193 with words") << endl; // 应输出: 4193
    cout << solution.myAtoi("words and 987") << endl; // 应输出: 0
    cout << solution.myAtoi("-91283472332") << endl; // 应输出: -2147483648
    return 0;
}