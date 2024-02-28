#include <iostream>
using namespace std;

// 实现pow函数
double pow(double x, int n) {
    // 基本情况处理
    if (n == 0) return 1;
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    // 分治策略
    double half = pow(x, n / 2);
    if (n % 2 == 0) {
        return half * half;
    } else {
        return x * half * half;
    }
}

int main() {
    // 示例输入
    double x = 2.00000;
    int n = 10;
    // 调用pow函数并输出结果
    cout.precision(5); // 设置输出精度
    cout << fixed << pow(x, n) << endl; // 输出1024.00000
    return 0;
}