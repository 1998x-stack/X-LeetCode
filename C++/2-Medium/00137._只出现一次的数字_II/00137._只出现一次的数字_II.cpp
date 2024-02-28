#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int bitCounts[32] = {0}; // 用于存储32位整数的每一位的总和
        for (int num : nums) {
            for (int i = 0; i < 32; ++i) {
                bitCounts[i] += (num >> i) & 1; // 更新每一位的和
            }
        }
        int result = 0;
        for (int i = 0; i < 32; ++i) {
            result |= (bitCounts[i] % 3) << i; // 对每一位进行处理，并加到结果中
        }
        return result;
    }
};

// 主函数用于测试
int main() {
    Solution solution;
    vector<int> nums = {2,2,3,2}; // 示例
    cout << "The single number is: " << solution.singleNumber(nums) << endl;
    return 0;
}