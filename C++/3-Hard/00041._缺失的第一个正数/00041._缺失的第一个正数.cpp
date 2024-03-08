#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for(int& num : nums){
            if (num <= 0){
                num = n + 1;
            }
        }

        for(int i = 0; i < n; ++i){
            int num = abs(nums[i]);
            if (num <= n){
                nums[num - 1] = -abs(nums[num - 1]);
            }
        }
        for (int i = 0; i < n; ++i){
            if (nums[i] > 0){
                return i + 1;
            }
        }
        return n + 1;
    }
};

int main() {
    Solution solution;
    vector<int> nums1 = {1, 2, 0};
    vector<int> nums2 = {3, 4, -1, 1};
    vector<int> nums3 = {7, 8, 9, 11, 12};
    cout << "Example 1: " << solution.firstMissingPositive(nums1) << endl;
    cout << "Example 2: " << solution.firstMissingPositive(nums2) << endl;
    cout << "Example 3: " << solution.firstMissingPositive(nums3) << endl;
    return 0;
}