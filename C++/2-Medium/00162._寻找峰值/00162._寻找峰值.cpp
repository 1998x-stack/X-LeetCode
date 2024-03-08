#include <iostream>
#include <vector>
using namespace std;

// 寻找峰值函数
int findPeakElement(vector<int>& nums) {
    int left = 0, right = nums.size() - 1, mid;
    
    // 使用二分查找定位峰值
    while (left < right) {
        mid = left + (right - left) / 2;
        if (nums[mid] > nums[mid + 1])
            right = mid; // 峰值在左侧
        else
            left = mid + 1; // 峰值在右侧
    }
    return left; // left 和 right 相遇，指向峰值
}

int main() {
    // 示例数组
    vector<int> nums = {1, 2, 1, 3, 5, 6, 4};
    cout << "峰值元素的位置: " << findPeakElement(nums) << endl;
    return 0;
}