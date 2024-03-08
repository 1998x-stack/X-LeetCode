#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

// 自定义比较函数
bool compareFunc(const int& a, const int& b) {
    return to_string(a) + to_string(b) > to_string(b) + to_string(a);
}

// 主函数
int main() {
    // 示例数组
    vector<int> nums = {3, 30, 34, 5, 9};
    
    // 排序
    sort(nums.begin(), nums.end(), compareFunc);
    
    // 拼接字符串
    string result;
    for (int num : nums) {
        result += to_string(num);
    }
    
    // 处理全0的情况
    if (result[0] == '0') {
        cout << "0" << endl;
    } else {
        cout << result << endl;
    }
    
    return 0;
}