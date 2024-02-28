#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 打印三元组，用于测试验证结果
void printTriplets(vector<vector<int>>& triplets) {
    for (auto& triplet : triplets) {
        cout << "[";
        for (int i = 0; i < triplet.size(); ++i) {
            cout << triplet[i];
            if (i < triplet.size() - 1) cout << ", ";
        }
        cout << "]" << endl;
    }
}

// 三数之和函数实现
vector<vector<int>> threeSum(vector<int>& nums) {
    
    vector<vector<int>> result;
    sort(nums.begin(), nums.end()); // 排序
    for (int i = 0; i < nums.size() && nums[i] <= 0; ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // 跳过重复元素
        int left = i + 1, right = nums.size() - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum < 0) {
                ++left;
            } else if (sum > 0) {
                --right;
            } else {
                result.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1]) ++left; // 跳过重复元素
                while (left < right && nums[right] == nums[right - 1]) --right; // 跳过重复元素
                ++left; --right;
            }
        }
    }
    return result;
}

int main() {
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> triplets = threeSum(nums);
    printTriplets(triplets);
    return 0;
}