#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 创建一个哈希表来存储元素值和它们的索引
        unordered_map<int, int> index_map;
        for (int i = 0; i < nums.size(); ++i) {
            // 计算当前元素和目标值之间的差
            int complement = target - nums[i];
            // 检查差值是否已存在于哈希表中
            if (index_map.find(complement) != index_map.end()) {
                // 如果存在，返回当前索引和差值对应的索引
                return {index_map[complement], i};
            }
            // 将当前元素的值和索引存入哈希表
            index_map[nums[i]] = i;
        }
        // 如果没有找到符合条件的两个数，返回空向量
        return {};
    }
};

// 测试代码
#include <iostream>
int main() {
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = solution.twoSum(nums, target);
    if (!result.empty()) {
        cout << "索引: " << result[0] << " 和 " << result[1] << endl;
    } else {
        cout << "未找到有效的两数之和" << endl;
    }
    return 0;
}