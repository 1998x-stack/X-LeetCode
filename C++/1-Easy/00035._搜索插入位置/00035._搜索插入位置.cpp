#include <iostream>
#include <vector>

using namespace std;

// Function to search insert position of target in sorted array
int searchInsert(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            // Target found, return its index
            return mid;
        } else if (nums[mid] < target) {
            // Target is greater, ignore left half
            left = mid + 1;
        } else {
            // Target is smaller, ignore right half
            right = mid - 1;
        }
    }
    // Target not found, return the insertion position
    return left;
}

int main() {
    // Example usage
    vector<int> nums = {1, 3, 5, 6};
    int target = 5;
    cout << "Insert position of target " << target << " is: " << searchInsert(nums, target) << endl;
    return 0;
}