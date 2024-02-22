#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0; // 处理边界情况
        int i = 0; // 初始化慢指针
        for (int j = 1; j < nums.size(); j++) { // 使用快指针遍历数组
            if (nums[j] != nums[i]) { // 当发现不重复元素时
                i++; // 移动慢指针
                nums[i] = nums[j]; // 更新不重复元素的位置
            }
        }
        return i + 1; // 返回新的数组长度
    }
};

int main() {
    // 示例
    vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
    Solution solution;
    int newLength = solution.removeDuplicates(nums);
    cout << "New length: " << newLength << endl;
    for (int i = 0; i < newLength; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}