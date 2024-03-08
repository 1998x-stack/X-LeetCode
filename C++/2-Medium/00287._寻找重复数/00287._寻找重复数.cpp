#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[nums[0]];
        // 步骤3: 快慢指针移动直到相遇
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        // 步骤5: 将快指针重置到起点，再次移动直到快慢指针相遇
        fast = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow; // 步骤6: 返回相遇点，即重复的数字
    }
};

int main() {
    vector<int> nums = {1,3,4,2,2}; // 示例数组
    Solution solution;
    int duplicate = solution.findDuplicate(nums);
    cout << "The duplicate number is: " << duplicate << endl;
}