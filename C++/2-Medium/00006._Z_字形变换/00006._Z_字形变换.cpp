#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }
        
        vector<string> rows(min(numRows, int(s.length())));
        int curRow = 0;
        bool goingDown = false;
        
        // 遍历字符串，按Z字形分配到各行
        for (char c : s) {
            rows[curRow] += c;
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }
        
        // 合并各行为最终字符串
        string ret;
        for (string row : rows) ret += row;
        return ret;
    }
};

int main() {
    Solution solution;
    string test_str = "PAYPALISHIRING";
    cout << solution.convert(test_str, 3) << endl; // Expected: "PAHNAPLSIIGYIR"
    cout << solution.convert(test_str, 4) << endl; // Expected: "PINALSIGYAHRPI"
    return 0;
}