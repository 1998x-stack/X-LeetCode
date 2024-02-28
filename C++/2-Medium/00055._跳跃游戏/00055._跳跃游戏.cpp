#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0; // 初始化最远到达位置
        for (int i = 0; i < nums.size(); ++i) {
            if (i > maxReach) return false; // 如果当前位置不可达，则返回 false
            maxReach = max(maxReach, i + nums[i]); // 更新最远到达位置
            if (maxReach >= nums.size() - 1) return true; // 如果最远到达位置超过或等于最后一个位置，则返回 true
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2,3,1,1,4}; // 示例输入
    bool result = solution.canJump(nums); // 调用函数
    cout << (result ? "true" : "false") << endl; // 输出结果
    return 0;
}