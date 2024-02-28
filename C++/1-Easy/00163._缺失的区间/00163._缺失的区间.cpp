#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Helper function to format the range string
string formatRange(int low, int high) {
    return low == high ? to_string(low) : to_string(low) + "->" + to_string(high);
}

// Function to find missing ranges
vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
    vector<string> result;
    int next = lower;
    for (int i = 0; i < nums.size(); ++i) {
        // If the current number is smaller than the next expected number, continue.
        if (nums[i] < next) continue;
        
        // If the current number is greater than the next expected number, a range is missing.
        if (nums[i] > next) {
            result.push_back(formatRange(next, nums[i] - 1));
        }
        
        // Update next number, taking care of integer overflow.
        if (nums[i] == INT_MAX) return result;
        next = nums[i] + 1;
    }
    
    // Check if there's a missing range between the last number and upper.
    if (next <= upper) {
        result.push_back(formatRange(next, upper));
    }
    return result;
}

int main() {
    vector<int> nums = {0, 1, 3, 50, 75};
    int lower = 0, upper = 99;
    vector<string> missingRanges = findMissingRanges(nums, lower, upper);
    for (string& range : missingRanges) {
        cout << range << endl;
    }
    return 0;
}