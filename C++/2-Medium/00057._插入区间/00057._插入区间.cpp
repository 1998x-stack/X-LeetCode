#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int i = 0, n = intervals.size();
        // 处理所有在新区间左侧且无交集的区间
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i++]);
        }

        // 处理所有与新区间有交集的区间
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        // 添加合并后的区间
        result.push_back(newInterval);

        // 添加所有在新区间右侧且无交集的区间
        while (i < n) {
            result.push_back(intervals[i++]);
        }

        return result;
    }
};

void printIntervals(const vector<vector<int>>& intervals) {
    cout << "[";
    for (const auto& interval : intervals) {
        cout << "[" << interval[0] << "," << interval[1] << "]";
    }
    cout << "]" << endl;
}

int main() {
    Solution solution;
    vector<vector<int>> intervals = {{1, 3}, {6, 9}};
    vector<int> newInterval = {2, 5};
    auto result = solution.insert(intervals, newInterval);
    printIntervals(result);
    return 0;
}