#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

// 函数：计算最长连续序列的长度
int longestConsecutive(vector<int>& nums) {
    unordered_set<int> num_set(nums.begin(), nums.end());
    int longest = 0;

    for (int num : num_set) {
        // 只有当当前数字是连续序列的起始点时，才开始计算
        if (num_set.find(num - 1) == num_set.end()) {
            int currentNum = num;
            int currentStreak = 1;

            // 向上寻找连续的数字
            while (num_set.find(currentNum + 1) != num_set.end()) {
                currentNum += 1;
                currentStreak += 1;
            }

            // 更新最长连续序列的长度
            longest = max(longest, currentStreak);
        }
    }

    return longest;
}

int main() {
    vector<int> nums = {100, 4, 200, 1, 3, 2};
    cout << "最长连续序列的长度: " << longestConsecutive(nums) << endl;
    return 0;
}