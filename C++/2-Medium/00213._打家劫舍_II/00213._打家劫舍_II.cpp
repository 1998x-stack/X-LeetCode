#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        int size = nums.size();
        if (size == 1) return nums[0];
        return max(robRange(nums, 0, size - 2), robRange(nums, 1, size - 1));
    }
private:
    int robRange(vector<int>& nums, int start, int end) {
        if (start == end) return nums[start];
        vector<int> dp(nums.size(), 0);
        dp[start] = nums[start];
        dp[start + 1] = max(nums[start], nums[start + 1]);
        for (int i = start + 2; i <= end; i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        return dp[end];
    }
};

int main() {
    Solution solution;
    vector<int> nums1 = {2, 3, 2};
    cout << "Test case 1: " << solution.rob(nums1) << endl; // 应输出 3
    vector<int> nums2 = {1, 2, 3, 1};
    cout << "Test case 2: " << solution.rob(nums2) << endl; // 应输出 4
    return 0;
}