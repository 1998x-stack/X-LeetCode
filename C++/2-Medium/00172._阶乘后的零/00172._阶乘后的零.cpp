#include <iostream>
using namespace std;

int trailingZeroes(int n) {
    int count = 0;
    while (n > 0) {
        n /= 5;
        count += n;
    }
    return count;
}

int main() {
    // 测试案例
    cout << "5! has " << trailingZeroes(5) << " trailing zero(s)." << endl;
    cout << "10! has " << trailingZeroes(10) << " trailing zero(s)." << endl;
    return 0;
}