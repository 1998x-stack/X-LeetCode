#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 函数声明
vector<string> findStrobogrammatic(int n);
vector<string> helper(int n, int m);

int main() {
    int n = 2; // 示例输入
    vector<string> result = findStrobogrammatic(n); // 调用主函数获取中心对称数列表
    for (const string& num : result) {
        cout << num << endl; // 打印结果
    }
    return 0;
}

// 主函数，根据给定的n生成所有长度为n的中心对称数
vector<string> findStrobogrammatic(int n) {
    return helper(n, n);
}

// 递归帮助函数，用于构建长度为n的中心对称数
vector<string> helper(int n, int m) {
    if (n == 0) return {""};
    if (n == 1) return {"0", "1", "8"};
    
    // 对长度为n-2的中心对称数递归调用，然后在两边添加中心对称的数字对
    vector<string> list = helper(n - 2, m), res;
    for (string s : list) {
        if (n != m) res.push_back("0" + s + "0"); // 除了最外层，可以添加"00"
        res.push_back("1" + s + "1");
        res.push_back("6" + s + "9");
        res.push_back("8" + s + "8");
        res.push_back("9" + s + "6");
    }
    return res;
}