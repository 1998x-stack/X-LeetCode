#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
using namespace std;

string removeDuplicateLetters(string s) {
    vector<int> count(256, 0); // 字符出现次数
    vector<bool> inStack(256, false); // 字符是否在栈中
    stack<char> st; // 用于构建最终结果的栈

    // 更新字符出现次数
    for (char c : s) count[c]++;
    
    for (char c : s) {
        // 减少字符出现的次数
        count[c]--;
        
        if (inStack[c]) continue; // 如果字符已在栈中，跳过
        
        // 字典序小于栈顶字符，且栈顶字符后面还会出现，则弹出栈顶字符
        while (!st.empty() && c < st.top() && count[st.top()] > 0) {
            inStack[st.top()] = false;
            st.pop();
        }
        
        // 将当前字符压入栈中
        st.push(c);
        inStack[c] = true;
    }
    
    // 构建最终结果
    string result = "";
    while (!st.empty()) {
        result = st.top() + result; // 注意这里的顺序
        st.pop();
    }
    
    return result;
}

int main() {
    string s = "cbacdcbc";
    cout << "Result: " << removeDuplicateLetters(s) << endl;
    return 0;
}