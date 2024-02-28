#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size(); // 如果数组长度不大于2，直接返回原长度
        
        int i = 1; // 初始化慢指针
        for (int j = 2; j < nums.size(); j++) { // 快指针开始遍历数组
            if (nums[j] != nums[i] || nums[j] != nums[i - 1]) { // 如果当前元素符合条件
                i++; // 移动慢指针
                nums[i] = nums[j]; // 更新慢指针位置的元素值
            }
        }
        return i + 1; // 返回新的数组长度
    }
};

int main() {
    // 测试代码
    Solution solution;
    vector<int> nums = {1,1,1,2,2,3}; // 示例数组
    int newLength = solution.removeDuplicates(nums);
    cout << "New length: " << newLength << endl;
    cout << "Array after removing duplicates: ";
    for (int i = 0; i < newLength; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}