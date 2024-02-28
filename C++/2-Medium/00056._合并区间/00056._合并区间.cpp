#include <iostream>
#include <vector>
#include <algorithm> // 用于std::sort

using namespace std;

// 合并区间的函数
vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
    if (intervals.empty()) return {}; // 处理空数组的情况
    
    // 按区间的起始位置排序
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    vector<vector<int>> merged;
    for (const auto& interval : intervals) {
        // 如果merged为空或当前区间与merged中最后一个区间不重叠，直接添加
        if (merged.empty() || merged.back()[1] < interval[0]) {
            merged.push_back(interval);
        } else {
            // 否则，有重叠，合并区间
            merged.back()[1] = max(merged.back()[1], interval[1]);
        }
    }
    
    return merged;
}

int main() {
    // 示例输入
    vector<vector<int>> intervals = {{1,3},{2,6},{8,10},{15,18}};
    
    // 调用函数并打印结果
    vector<vector<int>> mergedIntervals = mergeIntervals(intervals);
    cout << "Merged intervals: ";
    for (const auto& interval : mergedIntervals) {
        cout << "[" << interval[0] << "," << interval[1] << "] ";
    }
    
    return 0;
}