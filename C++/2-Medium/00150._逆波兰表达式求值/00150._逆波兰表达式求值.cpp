#include <iostream>
#include <vector>
#include <stack>
#include <string>
using namespace std;

int evalRPN(vector<string>& tokens) {
    stack<int> stk;
    for (string& token : tokens) {
        if (token == "+" || token == "-" || token == "*" || token == "/") {
            int num2 = stk.top(); stk.pop();
            int num1 = stk.top(); stk.pop();
            if (token == "+") stk.push(num1 + num2);
            else if (token == "-") stk.push(num1 - num2);
            else if (token == "*") stk.push(num1 * num2);
            else if (token == "/") stk.push(num1 / num2);
        } else {
            stk.push(stoi(token));
        }
    }
    return stk.top();
}

int main() {
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    cout << "Result: " << evalRPN(tokens) << endl;
    return 0;
}