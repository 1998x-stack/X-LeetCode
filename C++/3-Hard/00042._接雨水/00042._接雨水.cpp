
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height){
        int left = 0, right = height.size() - 1;
        int maxLeft = 0, maxRight = 0;
        int result = 0;

        while (left < right){
            if (height[left] < height[right]) {
                // 左侧较低，处理左侧, 哪侧更低，就处理哪侧（哪侧就一定可以被另外一侧hold住）
                if (height[left] >= maxLeft) {
                    // 更新左侧最大高度
                    maxLeft = height[left];
                } else {
                    // 计算并累加雨水量
                    result += maxLeft - height[left];
                }
                ++left;
            } else {
                // 右侧较低，处理右侧
                if (height[right] >= maxRight) {
                    // 更新右侧最大高度
                    maxRight = height[right];
                } else {
                    // 计算并累加雨水量
                    result += maxRight - height[right];
                }
                --right;
            }
        }
        return result;
    }
};

int main() {
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    Solution solution;
    cout << "Trapped rainwater: " << solution.trap(height) << endl;
    return 0;
}