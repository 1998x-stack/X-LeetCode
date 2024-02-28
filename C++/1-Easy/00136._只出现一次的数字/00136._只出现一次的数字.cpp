#include <iostream>
#include <vector>

using namespace std;

// 定义 singleNumber 函数，接收一个整数数组作为参数，返回只出现一次的数字
int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num; // 将 result 与数组中的每个元素进行异或运算
    }
    return result;
}

int main() {
    // 示例
    vector<int> nums = {4, 1, 2, 1, 2}; // 定义一个测试用的数组
    cout << "The single number is: " << singleNumber(nums) << endl; // 调用 singleNumber 函数并打印结果
    return 0;
}