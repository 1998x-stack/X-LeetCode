#include <iostream>
#include <climits> // 用于 INT_MIN 和 INT_MAX

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            // 溢出检查
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};

int main() {
    Solution solution;
    // 测试用例
    cout << "Reverse of 123 is " << solution.reverse(123) << endl;
    cout << "Reverse of -123 is " << solution.reverse(-123) << endl;
    cout << "Reverse of 120 is " << solution.reverse(120) << endl;
    cout << "Reverse of 0 is " << solution.reverse(0) << endl;
    return 0;
}