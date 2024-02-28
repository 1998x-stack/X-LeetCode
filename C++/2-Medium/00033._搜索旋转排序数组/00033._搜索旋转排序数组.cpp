#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            // 直接找到目标值
            if (nums[mid] == target) return mid;
            
            // 判断左半部分是否有序
            if (nums[left] <= nums[mid]) {
                // 判断目标值是否在左半部分
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else { // 右半部分有序
                // 判断目标值是否在右半部分
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
        return -1; // 未找到目标值
    }
};

int main() {
    Solution solution;
    vector<int> nums = {4,5,6,7,0,1,2};
    int target = 0;
    cout << "Index of target " << target << ": " << solution.search(nums, target) << endl;
    return 0;
}