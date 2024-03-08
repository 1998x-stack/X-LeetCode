#include <iostream>
#include <vector>
#include <climits>
using namespace std;

bool increasingTriplet(vector<int>& nums) {
    int first = INT_MAX, second = INT_MAX;
    for (int num : nums) {
        if (num <= first) { // 更新最小值
            first = num;
        } else if (num <= second) { // 更新第二小的值
            second = num;
        } else { // 找到比first和second都大的值，即满足条件的三元子序列
            return true;
        }
    }
    return false; // 未找到满足条件的三元子序列
}

int main() {
    vector<int> nums = {2, 1, 5, 0, 4, 6};
    bool result = increasingTriplet(nums);
    cout << "Result: " << (result ? "true" : "false") << endl;
    return 0;
}