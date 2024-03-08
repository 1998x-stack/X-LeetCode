#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// 计数质数函数
int countPrimes(int n) {
    if (n <= 1) return 0; // 边界条件处理
    vector<bool> isPrime(n, true); // 初始化为 true
    isPrime[0] = isPrime[1] = false; // 0 和 1 不是质数
    for (int i = 2; i * i < n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = false; // 标记非质数
            }
        }
    }
    // 计算质数的数量
    int count = 0;
    for (int i = 2; i < n; i++) {
        if (isPrime[i]) count++;
    }
    return count;
}

int main() {
    int n;
    cout << "请输入 n 的值: ";
    cin >> n;
    cout << "小于 " << n << " 的质数数量是: " << countPrimes(n) << endl;
    return 0;
}