#include <iostream>
#include <vector>
#include <algorithm> // 用于排序
using namespace std;

// 定义四数之和函数
vector<vector<int>> fourSum(vector<int>& nums, int target) {
    vector<vector<int>> res;
    if (nums.size() < 4) return res; // 边界条件判断
    sort(nums.begin(), nums.end()); // 对数组进行排序

    for (int i = 0; i < nums.size() - 3; i++) {
        if (i > 0 && nums[i] == nums[i-1]) continue; // 跳过重复元素
        for (int j = i + 1; j < nums.size() - 2; j++) {
            if (j > i + 1 && nums[j] == nums[j-1]) continue; // 跳过重复元素
            int left = j + 1, right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[j] + nums[left] + nums[right];
                if (sum < target) {
                    left++;
                } else if (sum > target) {
                    right--;
                } else {
                    res.push_back({nums[i], nums[j], nums[left], nums[right]});
                    while (left < right && nums[left] == nums[left+1]) left++; // 跳过重复元素
                    while (left < right && nums[right] == nums[right-1]) right--; // 跳过重复元素
                    left++; right--;
                }
            }
        }
    }
    return res;
}

// 主函数
int main() {
    vector<int> nums = {1, 0, -1, 0, -2, 2};
    int target = 0;
    vector<vector<int>> result = fourSum(nums, target);

    for (const auto &quad : result) {
        for (int num : quad) {
            cout << num << " ";
        }
        cout << "\n";
    }

    return 0;
}
