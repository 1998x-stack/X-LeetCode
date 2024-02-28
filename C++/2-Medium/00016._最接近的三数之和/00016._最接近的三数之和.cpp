#include <iostream>
#include <vector>
#include <algorithm> // 用于std::sort
using namespace std;

// 函数：找出最接近的三数之和
int threeSumClosest(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end()); // 对数组进行排序
    int closestSum = nums[0] + nums[1] + nums[2]; // 初始化最接近的和为前三个数的和
    for (int i = 0; i < nums.size() - 2; i++) { // 遍历数组
        int left = i + 1, right = nums.size() - 1; // 初始化左右指针
        while (left < right) { // 当左指针小于右指针时循环
            int currentSum = nums[i] + nums[left] + nums[right]; // 当前三数之和
            if (abs(target - currentSum) < abs(target - closestSum)) { // 如果当前和更接近target
                closestSum = currentSum; // 更新最接近的和
            }
            if (currentSum > target) { // 根据和与target的比较结果移动指针
                right--; // 如果当前和大于target，右指针左移
            } else if (currentSum < target) {
                left++; // 如果当前和小于target，左指针右移
            } else {
                return currentSum; // 如果等于target，直接返回当前和
            }
        }
    }
    return closestSum; // 返回最接近的三数之和
}

// 主函数
int main() {
    vector<int> nums = {-1, 2, 1, -4}; // 示例数组
    int target = 1; // 目标值
    int result = threeSumClosest(nums, target); // 调用函数计算结果
    cout << "最接近的三数之和为: " << result << endl; // 输出结果
    return 0;
}