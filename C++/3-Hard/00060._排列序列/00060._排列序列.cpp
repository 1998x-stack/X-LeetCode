#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 计算阶乘
int factorial(int n) {
    int result = 1;
    for(int i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

// 获取第k个排列的函数
string getPermutation(int n, int k) {
    string result = "";
    string numbers = "123456789"; // 可选数字字符串
    vector<int> fact(n); // 存储阶乘的数组
    // 初始化阶乘数组
    for(int i = 0; i < n; ++i) {
        fact[i] = factorial(i);
    }
    k -= 1; // 调整k值，因为索引从0开始
    // 寻找第k个排列
    for(int i = n; i >= 1; --i) {
        int j = k / fact[i-1];
        k %= fact[i-1];
        result.push_back(numbers[j]);
        numbers.erase(j, 1); // 从列表中移除已经使用的数字
    }
    return result;
}

int main() {
    int n = 3, k = 3;
    cout << "The " << k << "th permutation of " << n << " numbers is: " << getPermutation(n, k) << endl;
    return 0;
}