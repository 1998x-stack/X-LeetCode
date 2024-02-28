#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> result;
        vector<string> mapping{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        string current;
        backtrack(result, digits, 0, current, mapping);
        return result;
    }

    void backtrack(vector<string>& result, const string& digits, int index, string& current, const vector<string>& mapping) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        string letters = mapping[digits[index] - '0'];
        for (char letter : letters) {
            current.push_back(letter); // 添加当前字母
            backtrack(result, digits, index + 1, current, mapping); // 递归
            current.pop_back(); // 回溯
        }
    }
};

int main() {
    Solution solution;
    string digits = "23";
    vector<string> combinations = solution.letterCombinations(digits);
    for (const string& combination : combinations) {
        cout << combination << endl;
    }
    return 0;
}