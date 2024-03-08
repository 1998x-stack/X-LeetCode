#include <iostream>
#include <vector>
#include <algorithm> // 引入算法库，主要用于max和min函数

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0; // 如果数组为空，直接返回0
        int maxProduct = nums[0], imax = nums[0], imin = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < 0) swap(imax, imin); // 如果当前数为负数，交换imax和imin
            // 更新imax和imin
            imax = max(nums[i], imax * nums[i]);
            imin = min(nums[i], imin * nums[i]);
            // 更新最大乘积
            maxProduct = max(maxProduct, imax);
        }
        return maxProduct;
    }
};

// 主函数
int main() {
    Solution solution;
    vector<int> nums = {2,3,-2,4}; // 示例数组
    cout << "Maximum Product Subarray: " << solution.maxProduct(nums) << endl; // 打印结果
    return 0;
}