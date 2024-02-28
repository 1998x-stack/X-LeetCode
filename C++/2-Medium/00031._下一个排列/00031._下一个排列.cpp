#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 2;
    // 从右向左查找第一个不满足递增关系的数字
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        int j = nums.size() - 1;
        // 从数组末尾向左遍历，找到第一个大于nums[i]的数字
        while (j >= 0 && nums[i] >= nums[j]) {
            j--;
        }
        // 交换nums[i]和nums[j]
        swap(nums[i], nums[j]);
    }
    // 从位置i+1到数组末尾进行反转，确保这部分是升序的
    reverse(nums.begin() + i + 1, nums.end());
}

int main() {
    vector<int> nums = {1, 2, 3}; // 示例输入
    nextPermutation(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}