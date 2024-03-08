#include <iostream>
#include <stack>
#include <string>
using namespace std;

int calculate(string s) {
    stack<int> nums; // 存储数字
    stack<char> ops; // 存储操作符
    int num = 0; // 当前解析的数值
    char op = '+'; // 前一个操作符，默认为加号以处理第一个数字
    for (int i = 0; i <= s.size(); i++) {
        if (i < s.size() && isdigit(s[i])) {
            num = num * 10 + (s[i] - '0'); // 处理多位数
        } else if (i == s.size() || s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
            if (op == '+' || op == '-') {
                nums.push(op == '+' ? num : -num); // 加减法，直接入栈
            } else {
                int last = nums.top(); nums.pop(); // 取出栈顶元素进行乘除法运算
                nums.push(op == '*' ? last * num : last / num);
            }
            num = 0; // 重置num
            op = i < s.size() ? s[i] : '+'; // 更新操作符
        }
    }
    int res = 0;
    while (!nums.empty()) { // 计算栈中剩余的加减法
        res += nums.top(); nums.pop();
    }
    return res;
}

int main() {
    string expression = "3+2*2";
    cout << "The result of \"" << expression << "\" is: " << calculate(expression) << endl;
    return 0;
}