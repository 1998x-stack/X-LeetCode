#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size() < 2) return 0;
        int min_val = *min_element(nums.begin(), nums.end());
        int max_val = *max_element(nums.begin(), nums.end());
        int bucketSize = max(1, (max_val - min_val) / ((int)nums.size() - 1));
        int bucketNum = (max_val - min_val) / bucketSize + 1;
        vector<pair<int, int>> bucket(bucketNum, {-1, -1}); // 存储每个桶的最小值和最大值
        
        // 分配元素至桶中
        for (int num : nums) {
            int idx = (num - min_val) / bucketSize;
            if (bucket[idx].first == -1) {
                bucket[idx].first = bucket[idx].second = num;
            } else {
                bucket[idx].first = min(bucket[idx].first, num);
                bucket[idx].second = max(bucket[idx].second, num);
            }
        }
        
        // 计算最大间距
        int maxGap = 0, prev = -1;
        for (int i = 0; i < bucketNum; i++) {
            if (bucket[i].first == -1) continue;
            if (prev != -1) maxGap = max(maxGap, bucket[i].first - bucket[prev].second);
            prev = i;
        }
        
        return maxGap;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {3, 6, 9, 1}; // 示例数组
    cout << "Maximum gap: " << solution.maximumGap(nums) << endl;
    return 0;
}