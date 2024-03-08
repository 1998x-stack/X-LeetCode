#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

class NestedInteger {
public:
    NestedInteger() {}

    NestedInteger(int value) : intValue(value), isInt(true) {}

    bool isInteger() const { return isInt; }

    int getInteger() const { return intValue; }

    void setInteger(int value) { intValue = value; isInt = true; }

    void add(const NestedInteger &ni) { list.push_back(ni); }

    const vector<NestedInteger> &getList() const { return list; }

private:
    bool isInt = false;
    int intValue = 0;
    vector<NestedInteger> list;
};

NestedInteger deserialize(string s) {
    stack<NestedInteger> st;
    int number = 0;
    bool neg = false;
    for (int i = 0; i <= s.size(); ++i) {
        char c = i == s.size() ? ',' : s[i];
        if (c == '-') {
            neg = true;
        } else if (isdigit(c)) {
            number = number * 10 + c - '0';
        } else if (c == '[') {
            st.push(NestedInteger());
        } else if (c == ',' || c == ']') {
            if (isdigit(s[i - 1])) {
                if (neg) number = -number;
                st.top().add(NestedInteger(number));
            }
            number = 0;
            neg = false;
            if (c == ']' && st.size() > 1) {
                NestedInteger ni = st.top();
                st.pop();
                st.top().add(ni);
            }
        }
    }
    return st.top();
}

int main() {
    string input = "[123,[456,789]]";
    NestedInteger result = deserialize(input);
    // 简化输出，实际使用时需要根据NestedInteger的结构自定义输出逻辑
    cout << "Deserialized NestedInteger" << endl;
    return 0;
}