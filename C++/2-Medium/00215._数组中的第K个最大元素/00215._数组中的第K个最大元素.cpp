#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left = 0, right = nums.size() - 1;
        // 目标位置
        int target = nums.size() - k;
        while (true) {
            int index = partition(nums, left, right);
            if (index == target) {
                return nums[index];
            } else if (index < target) {
                left = index + 1;
            } else {
                right = index - 1;
            }
        }
    }

private:
    int partition(vector<int>& nums, int left, int right) {
        int pivot = nums[left];
        int j = left;
        // 分区操作
        for (int i = left + 1; i <= right; i++) {
            if (nums[i] < pivot) {
                j++;
                swap(nums[i], nums[j]);
            }
        }
        swap(nums[left], nums[j]);
        return j;
    }
};

// 主函数示例
int main() {
    Solution solution;
    vector<int> nums = {3,2,1,5,6,4};
    int k = 2;
    cout << "第 " << k << " 个最大元素是: " << solution.findKthLargest(nums, k) << endl;
    return 0;
}
/*
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // 使用最小堆
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        for (int num : nums) {
            minHeap.push(num);
            // 如果堆的大小超过 k，则移除堆顶元素
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        // 堆顶元素即为第 k 个最大元素
        return minHeap.top();
    }
};

// 主函数示例
int main() {
    Solution solution;
    vector<int> nums = {3,2,1,5,6,4};
    int k = 2;
    cout << "第 " << k << " 个最大元素是: " << solution.findKthLargest(nums, k) << endl;
    return 0;
}
*/