#include <iostream>
#include <vector>
#include <algorithm> // 使用 std::max

using namespace std;

// 动态规划解决最长递增子序列问题的函数
int lengthOfLIS(vector<int>& nums) {
    if (nums.empty()) return 0; // 边界情况：空数组
    int n = nums.size();
    vector<int> dp(n, 1); // 初始化dp数组，每个元素的初始值为1
    for (int i = 1; i < n; ++i) { // 从第二个元素开始遍历
        for (int j = 0; j < i; ++j) { // 遍历当前元素之前的所有元素
            if (nums[j] < nums[i]) { // 如果存在一个递增的关系
                dp[i] = max(dp[i], dp[j] + 1); // 更新dp[i]为最大值
            }
        }
    }
    return *max_element(dp.begin(), dp.end()); // 返回dp数组中的最大值，即为答案
}

// 主函数
int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18}; // 示例数组
    cout << "Length of LIS: " << lengthOfLIS(nums) << endl; // 输出最长递增子序列的长度
    return 0;
}