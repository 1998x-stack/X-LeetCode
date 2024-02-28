#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result(1, 0); // 初始化结果列表，开始时只包含一个元素0
        for (int i = 0; i < n; ++i) {
            int add = 1 << i; // 计算当前需要添加的值，即2的i次方
            // 从后向前遍历当前结果列表，为每个元素添加add后放入列表中
            for (int j = result.size() - 1; j >= 0; --j) {
                result.push_back(result[j] + add);
            }
        }
        return result; // 返回生成的格雷编码序列
    }
};

int main() {
    Solution solution;
    int n = 2; // 示例输入
    vector<int> gray_codes = solution.grayCode(n);
    cout << "Gray codes for n = " << n << ": ";
    for (int code : gray_codes) {
        cout << code << " ";
    }
    cout << endl;
    return 0;
}