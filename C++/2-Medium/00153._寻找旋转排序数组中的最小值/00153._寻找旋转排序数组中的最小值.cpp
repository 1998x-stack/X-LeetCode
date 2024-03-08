#include <iostream>
#include <vector>
using namespace std;

// Function to find the minimum element in a rotated sorted array
int findMin(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[right]) {
            // The minimum element is in the right part
            left = mid + 1;
        } else {
            // The minimum element is in the left part
            right = mid;
        }
    }
    // When left == right, we found the minimum element
    return nums[left];
}

int main() {
    // Example cases
    vector<int> nums1 = {3, 4, 5, 1, 2};
    vector<int> nums2 = {4, 5, 6, 7, 0, 1, 2};
    // Output the results
    cout << "The minimum element in the first array is: " << findMin(nums1) << endl;
    cout << "The minimum element in the second array is: " << findMin(nums2) << endl;
    return 0;
}