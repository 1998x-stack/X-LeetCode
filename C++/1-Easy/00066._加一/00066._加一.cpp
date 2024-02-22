#include <vector>
#include <iostream>
using namespace std;

// 实现加一函数
vector<int> plusOne(vector<int>& digits) {
    // 从数组末尾开始迭代
    for (int i = digits.size() - 1; i >= 0; --i) {
        // 如果当前位小于9，直接加一并返回
        if (digits[i] < 9) {
            ++digits[i];
            return digits;
        }
        // 否则，当前位设为0，继续循环处理进位
        digits[i] = 0;
    }
    // 处理所有位都是9的情况，如[9,9,9]
    digits.insert(digits.begin(), 1);
    return digits;
}

int main() {
    // 示例数组
    vector<int> digits = {1, 2, 3};
    // 调用加一函数
    vector<int> result = plusOne(digits);
    // 打印结果
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}