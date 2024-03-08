#include <iostream>
#include <vector>
using namespace std;

// Function to perform the wiggle sort
void wiggleSort(vector<int>& nums) {
    for (size_t i = 0; i < nums.size() - 1; i++) {
        // For even index, if the current element is greater than the next one, swap them
        if ((i % 2 == 0) && (nums[i] > nums[i + 1])) {
            swap(nums[i], nums[i + 1]);
        }
        // For odd index, if the current element is less than the next one, swap them
        else if ((i % 2 == 1) && (nums[i] < nums[i + 1])) {
            swap(nums[i], nums[i + 1]);
        }
    }
}

int main() {
    // Example usage
    vector<int> nums = {3, 5, 2, 1, 6, 4};
    wiggleSort(nums);

    // Print the sorted array
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}