#include <iostream>
#include <vector>
#include <algorithm> // 用于sort函数
using namespace std;

// 计算H指数的函数
int hIndex(vector<int>& citations) {
    sort(citations.begin(), citations.end(), greater<int>()); // 1. 降序排序
    int i = 0; // 初始化遍历的索引
    while (i < citations.size() && citations[i] > i) { // 2. 线性扫描寻找H指数
        i++;
    }
    return i; // 返回H指数
}

// 主函数
int main() {
    vector<int> citations = {3, 0, 6, 1, 5}; // 示例引用次数
    int result = hIndex(citations); // 调用函数计算H指数
    cout << "H指数是: " << result << endl; // 输出H指数
    return 0;
}
