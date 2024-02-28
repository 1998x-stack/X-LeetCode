#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int jump = 0, maxReach = 0, end = 0;
        // 遍历数组中的每个元素，除了最后一个元素，因为一旦到达最后一个元素，就不需要再跳跃了
        for (int i = 0; i < nums.size() - 1; i++) {
            // 更新能到达的最远距离
            maxReach = max(maxReach, i + nums[i]);
            // 如果到达当前探索的边界
            if (i == end) {
                // 进行跳跃，更新探索的边界
                end = maxReach;
                jump++;
            }
        }
        return jump;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << "Minimum jumps required: " << solution.jump(nums) << endl;
    return 0;
}