#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// 动态规划算法实现最大子数组和
int maxSubArray(vector<int>& nums) {
    int curMax = nums[0]; // 当前元素作为子数组末尾的最大和
    int maxSum = nums[0]; // 全局最大子数组和
    for (int i = 1; i < nums.size(); i++) {
        curMax = max(nums[i], curMax + nums[i]); // 更新curMax
        maxSum = max(maxSum, curMax); // 更新maxSum
    }
    return maxSum;
}

int main() {
    // 示例数组
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    cout << "Maximum Subarray Sum is " << maxSubArray(nums) << endl;
    return 0;
}