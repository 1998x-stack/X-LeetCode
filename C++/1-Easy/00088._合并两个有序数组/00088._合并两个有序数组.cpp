#include <iostream>
#include <vector>
using namespace std;

// 合并两个有序数组的函数
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m - 1; // nums1的末尾索引
    int j = n - 1; // nums2的末尾索引
    int k = m + n - 1; // 合并后的nums1的末尾索引
    
    // 从后向前遍历nums1和nums2，并填充到nums1的末尾
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
}

int main() {
    vector<int> nums1 = {1,2,3,0,0,0};
    int m = 3;
    vector<int> nums2 = {2,5,6};
    int n = 3;

    merge(nums1, m, nums2, n);

    for (int num : nums1) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}