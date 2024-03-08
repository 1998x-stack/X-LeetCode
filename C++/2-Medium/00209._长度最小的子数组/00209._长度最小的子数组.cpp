#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int minSubArrayLen(int target, vector<int>& nums) {
    int n = nums.size();
    int minLength = INT_MAX; // 初始化最小长度为最大整数，便于后续比较
    int left = 0, sum = 0; // 初始化左指针和子数组的和
    
    for (int right = 0; right < n; right++) {
        sum += nums[right]; // 累加右指针指向的元素
        while (sum >= target) { // 当子数组的和大于等于目标值时，尝试缩小窗口
            minLength = min(minLength, right - left + 1); // 更新最小长度
            sum -= nums[left++]; // 移动左指针并更新子数组的和
        }
    }
    
    return minLength == INT_MAX ? 0 : minLength; // 如果minLength未被更新过，返回0
}

int main() {
    vector<int> nums = {2,3,1,2,4,3};
    int target = 7;
    cout << "The minimum length of a contiguous subarray of which the sum is at least " << target << " is: " << minSubArrayLen(target, nums) << endl;
    return 0;
}