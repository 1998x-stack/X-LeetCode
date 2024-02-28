#include <iostream>
#include <vector>
#include <algorithm> // 用于std::max函数

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0; // 左指针初始化为0
        int right = height.size() - 1; // 右指针初始化为数组的最后一个元素的索引
        int max_area = 0; // 最大面积初始化为0
        
        while (left < right) { // 当左指针小于右指针时循环
            // 计算当前左右指针对应的容器的面积
            int current_area = (right - left) * min(height[left], height[right]);
            max_area = max(max_area, current_area); // 更新最大面积
            
            // 移动指向较矮高度的指针
            if (height[left] < height[right]) {
                ++left; // 左边较矮，移动左指针
            } else {
                --right; // 右边较矮，移动右指针
            }
        }
        
        return max_area; // 返回计算出的最大面积
    }
};

int main() {
    Solution solution;
    vector<int> height = {1,8,6,2,5,4,8,3,7}; // 示例输入
    cout << "Maximum water that can be contained: " << solution.maxArea(height) << endl; // 输出结果
    return 0;
}