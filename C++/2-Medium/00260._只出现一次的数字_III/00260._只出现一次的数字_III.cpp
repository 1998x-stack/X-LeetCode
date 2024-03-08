#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        // 第一步：找到两个唯一数的异或结果
        int xorResult = 0;
        for (int num : nums) {
            xorResult ^= num;
        }
        
        // 第二步：找到异或结果中的任意一个为1的位
        int mask = 1;
        while ((xorResult & mask) == 0) {
            mask = mask << 1;
        }
        
        // 第三步：根据这个位将数组分为两组，并分别进行异或操作
        int a = 0, b = 0;
        for (int num : nums) {
            if (num & mask) { // 分组
                a ^= num;
            } else {
                b ^= num;
            }
        }
        
        return vector<int>{a, b};
    }
};

int main() {
    vector<int> nums = {1, 2, 1, 3, 2, 5};
    Solution solution;
    vector<int> result = solution.singleNumber(nums);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}