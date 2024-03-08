#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <ctime>

using namespace std;

class Solution {
private:
    vector<int> original;
    vector<int> array;

public:
    Solution(vector<int>& nums) {
        original = nums;
        array = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        array = original;
        return array;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        for (int i = 0; i < array.size(); i++) {
            int pos = i + rand() % (array.size() - i);
            swap(array[i], array[pos]);
        }
        return array;
    }
};

int main() {
    // 初始化随机种子
    srand(time(NULL));
    
    vector<int> nums = {1, 2, 3, 4, 5};
    Solution solution(nums);
    
    // 打印原始数组
    cout << "Original array: ";
    for (int num : solution.reset()) {
        cout << num << " ";
    }
    cout << "\\n";
    
    // 打印打乱后的数组
    cout << "Shuffled array: ";
    for (int num : solution.shuffle()) {
        cout << num << " ";
    }
    cout << "\\n";
    
    // 再次打印恢复后的数组
    cout << "Reset array: ";
    for (int num : solution.reset()) {
        cout << num << " ";
    }
    cout << "\\n";
    
    return 0;
}