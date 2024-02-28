#include <iostream>
#include <vector>
using namespace std;

bool search(vector<int>& nums, int target){
    int left = 0, right = nums.size() - 1;
    while(left <= right){
        int mid = left + (right - left) / 2;
        if(nums[mid]==target) return true;

        if (nums[left] ==  nums[mid] && nums[mid] == nums[right]){
            left++;
            right--;
        } else if(nums[left] < nums[mid]){ // 左半部分up
            if(nums[left] <= target && target < nums[mid]){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else{ // 右半部分up
            if(nums[mid] < target && target <= nums[right]){
                left = mid + 1;
            } else {
                right = mid - 1;
            }

        }
    }
    return false;
}

int main() {
    vector<int> nums = {2, 5, 6, 0, 0, 1, 2};
    int target = 0;
    cout << (search(nums, target) ? "true" : "false") << endl;
    
    nums = {2, 5, 6, 0, 0, 1, 2};
    target = 3;
    cout << (search(nums, target) ? "true" : "false") << endl;
    
    return 0;
}