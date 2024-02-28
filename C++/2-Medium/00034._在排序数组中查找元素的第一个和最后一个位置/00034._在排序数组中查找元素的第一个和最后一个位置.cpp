#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = findFirst(nums, target);
        int last = findLast(nums, target);
        return {first, last};
    }
    
    int findFirst(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1, res = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                res = mid;
                high = mid - 1; // 继续在左侧搜索
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return res;
    }
    
    int findLast(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1, res = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                res = mid;
                low = mid + 1; // 继续在右侧搜索
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return res;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {5,7,7,8,8,10};
    int target = 8;
    vector<int> result = solution.searchRange(nums, target);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}