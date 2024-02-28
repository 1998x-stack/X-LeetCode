#include <iostream>
#include <climits>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        // 处理溢出情况
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        // 使用long long类型防止溢出，处理符号
        long long a = dividend;
        long long b = divisor;
        bool sign = (a > 0) ^ (b > 0); // 异或操作，符号不同为true
        a = abs(a);
        b = abs(b);

        long long result = 0;
        // 快速除法
        for (int i = 31; i >= 0; i--) {
            if ((a >> i) >= b) { // 找到足够大的数*b
                result += 1LL << i; // 累加结果
                a -= b << i; // 减去已经计算的部分
            }
        }

        // 根据符号返回结果
        return sign ? -result : result;
    }
};

int main() {
    Solution solution;
    // 示例测试
    cout << "10 / 3 = " << solution.divide(10, 3) << endl;
    cout << "7 / -3 = " << solution.divide(7, -3) << endl;
    return 0;
}