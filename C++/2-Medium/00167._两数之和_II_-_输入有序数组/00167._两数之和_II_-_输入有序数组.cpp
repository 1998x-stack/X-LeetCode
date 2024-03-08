#include <iostream>
#include <vector>
using namespace std;

// 函数声明
vector<int> twoSum(vector<int>& numbers, int target){
    int left = 0;
    int right = numbers.size() - 1;
    while(left < right){
        int sum = numbers[left] + numbers[right];
        if (sum == target){
            return {left + 1, right + 1};
        }
        else if (sum < target){
            left++;
        }
        else{
            right--;
        }
    }
    return {-1, -1};
}



int main() {
    vector<int> numbers = {2, 7, 11, 15}; // 示例数组
    int target = 9; // 目标值
    vector<int> result = twoSum(numbers, target); // 调用函数
    cout << "Index: " << result[0] << ", " << result[1] << endl; // 打印结果
    return 0;
}