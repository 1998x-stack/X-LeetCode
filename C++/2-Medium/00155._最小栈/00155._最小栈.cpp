#include <iostream>
#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> s; // 主栈，存储所有元素
    stack<int> minS; // 辅助栈，存储当前最小值

public:
    /** initialize your data structure here. */
    MinStack() {
        // 构造函数不需要初始化代码
    }

    void push(int x) {
        s.push(x); // 元素x入主栈
        // 如果辅助栈为空或x小于等于辅助栈顶元素，则x也入辅助栈
        if (minS.empty() || x <= minS.top()) {
            minS.push(x);
        }
    }

    void pop() {
        // 如果主栈顶元素等于辅助栈顶元素，辅助栈也要弹出
        if (s.top() == minS.top()) {
            minS.pop();
        }
        s.pop(); // 主栈弹出
    }

    int top() {
        return s.top(); // 返回主栈顶元素
    }

    int getMin() {
        return minS.top(); // 返回辅助栈顶元素，即当前最小值
    }
};

int main() {
    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    cout << "Min: " << minStack.getMin() << endl; // Returns -3
    minStack.pop();
    cout << "Top: " << minStack.top() << endl;    // Returns 0
    cout << "Min: " << minStack.getMin() << endl; // Returns -2
    return 0;
}