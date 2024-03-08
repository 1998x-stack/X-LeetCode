#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 函数声明：为了递归调用
vector<int> diffWaysToCompute(string input);

// 主要的递归函数
vector<int> compute(string& input, int start, int end) {
    vector<int> ways;
    // 遍历字符串，寻找运算符
    for (int i = start; i < end; ++i) {
        char c = input[i];
        if (c == '+' || c == '-' || c == '*') {
            // 对于每个运算符，计算左右两边的所有可能结果
            vector<int> left = compute(input, start, i);
            vector<int> right = compute(input, i + 1, end);
            // 组合左右两边的结果
            for (int l : left) {
                for (int r : right) {
                    switch (c) {
                        case '+': ways.push_back(l + r); break;
                        case '-': ways.push_back(l - r); break;
                        case '*': ways.push_back(l * r); break;
                    }
                }
            }
        }
    }
    // 如果没有运算符，直接返回数字
    if (ways.empty()) ways.push_back(stoi(input.substr(start, end - start)));
    return ways;
}

// 工具函数，处理输入字符串并调用递归函数
vector<int> diffWaysToCompute(string input) {
    return compute(input, 0, input.size());
}

int main() {
    // 示例测试
    string input = "2*3-4*5";
    vector<int> result = diffWaysToCompute(input);
    cout << "Possible results: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}