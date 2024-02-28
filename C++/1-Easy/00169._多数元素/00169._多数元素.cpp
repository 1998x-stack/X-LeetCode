#include <iostream>
#include <vector>
using namespace std;

// 函数：找出多数元素
int majorityElement(vector<int>& nums) {
    int candidate = 0;
    int count = 0;
    
    // 遍历数组，应用摩尔投票算法
    for (int num : nums) {
        if (count == 0) {
            candidate = num;
        }
        count += (num == candidate) ? 1 : -1;
    }
    
    // 候选者即为多数元素
    return candidate;
}

int main() {
    // 示例数组
    vector<int> nums = {2,2,1,1,1,2,2};
    
    // 调用函数，并输出结果
    cout << "多数元素是: " << majorityElement(nums) << endl;
    return 0;
}