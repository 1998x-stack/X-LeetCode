#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> result;
        for (int i = 1; i <= 9; ++i) {
            dfs(i, n, result);
        }
        return result;
    }

    void dfs(int cur, int n, vector<int>& result) {
        if (cur > n) return;
        result.push_back(cur);
        for (int i = 0; i <= 9; ++i) {
            if (10 * cur + i > n) break;
            dfs(10 * cur + i, n, result);
        }
    }
};

int main() {
    Solution solution;
    int n = 13; // 示例输入
    vector<int> result = solution.lexicalOrder(n);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}