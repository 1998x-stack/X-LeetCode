#include <iostream>
using namespace std;

bool isPalindrome(int x) {
    // 排除负数和末尾为0的数的情况
    if(x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    int reversedHalf = 0;
    while(x > reversedHalf) {
        reversedHalf = reversedHalf * 10 + x % 10;
        x /= 10;
    }

    // 对于奇数长度的数字，通过`reversedHalf/10`去掉中间的数字
    return x == reversedHalf || x == reversedHalf / 10;
}

int main() {
    int testNumber = 121; // 示例数字
    bool result = isPalindrome(testNumber);
    cout << (result ? "true" : "false") << endl;
    return 0;
}