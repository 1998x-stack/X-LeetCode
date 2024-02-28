#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        generate("", n, n, result);
        return result;
    }

    void generate(string current, int left, int right, vector<string>& result) {
        if (left == 0 && right == 0) {
            result.push_back(current);
            return;
        }
        // 如果左括号剩余数量大于0，可以添加一个左括号
        if (left > 0) {
            generate(current + "(", left - 1, right, result);
        }
        // 如果右括号剩余数量大于左括号，可以添加一个右括号
        if (right > left) {
            generate(current + ")", left, right - 1, result);
        }
    }
};

// 主函数
int main() {
    Solution solution;
    vector<string> result = solution.generateParenthesis(3);
    for (const string& s : result) {
        cout << s << endl;
    }
    return 0;
}
