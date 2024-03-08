#include <iostream>
#include <vector>
#include <algorithm> // 用于sort函数
using namespace std;

// 定义三数之和小于target的函数
int threeSumSmaller(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end()); // 对数组进行排序
    int count = 0; // 用于计数满足条件的三元组数量
    int n = nums.size();
    // 遍历数组
    for (int i = 0; i < n - 2; ++i) {
        int left = i + 1, right = n - 1; // 设置左右指针
        while (left < right) { // 当左指针小于右指针时循环
            int sum = nums[i] + nums[left] + nums[right];
            if (sum < target) { // 如果三数之和小于target
                count += right - left; // 更新计数，right-left是因为如果a+b+c<target，则a+b+(c到right之间的任意数)都满足条件
                ++left; // 移动左指针
            } else {
                --right; // 移动右指针以减小和
            }
        }
    }
    return count; // 返回满足条件的三元组数量
}

int main() {
    vector<int> nums = {-2, 0, 1, 3}; // 示例数组
    int target = 2; // 目标值
    cout << "满足条件的三元组数量为: " << threeSumSmaller(nums, target) << endl;
    return 0;
}