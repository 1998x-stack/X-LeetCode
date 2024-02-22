#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isValid(string s) {
    stack<char> stk;
    for (char c : s) {
        switch (c) {
            case '(':
            case '{':
            case '[':
                stk.push(c);
                break;
            case ')':
                if (stk.empty() || stk.top() != '(') return false;
                stk.pop();
                break;
            case '}':
                if (stk.empty() || stk.top() != '{') return false;
                stk.pop();
                break;
            case ']':
                if (stk.empty() || stk.top() != '[') return false;
                stk.pop();
                break;
        }
    }
    return stk.empty();
}

int main() {
    // 示例输入
    string input = "(){[]}"; // 期望输出：true
    bool result = isValid(input);
    cout << (result ? "true" : "false") << endl;
    return 0;
}