#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int left = 0, right = citations.size() - 1, mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            // 如果这篇论文的引用次数小于等于其后面论文的数量，说明H指数至少为citations.size() - mid
            if (citations[mid] < citations.size() - mid) left = mid + 1;
            else right = mid - 1;
        }
        // 数组长度减去左边界位置，得到H指数
        return citations.size() - left;
    }
};

int main() {
    // 示例：引用次数数组
    vector<int> citations = {0, 1, 3, 5, 6};
    Solution solution;
    // 计算并输出H指数
    cout << "H-Index is: " << solution.hIndex(citations) << endl;
    return 0;
}