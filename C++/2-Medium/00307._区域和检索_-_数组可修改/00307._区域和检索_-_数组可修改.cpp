#include <vector>
#include <iostream>
using namespace std;

class NumArray {
public:
    vector<int> tree;
    int n;

    NumArray(vector<int>& nums) {
        n = nums.size();
        tree.resize(n * 4);
        buildTree(nums, 0, 0, n - 1);
    }
    
    void buildTree(vector<int>& nums, int treeIndex, int l, int r) {
        if (l == r) {
            tree[treeIndex] = nums[l];
            return;
        }
        int mid = l + (r - l) / 2;
        buildTree(nums, 2 * treeIndex + 1, l, mid);
        buildTree(nums, 2 * treeIndex + 2, mid + 1, r);
        tree[treeIndex] = tree[2 * treeIndex + 1] + tree[2 * treeIndex + 2];
    }
    
    void update(int index, int val) {
        updateTree(0, 0, n - 1, index, val);
    }
    
    void updateTree(int treeIndex, int l, int r, int idx, int val) {
        if (l == r) {
            tree[treeIndex] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) {
            updateTree(2 * treeIndex + 1, l, mid, idx, val);
        } else {
            updateTree(2 * treeIndex + 2, mid + 1, r, idx, val);
        }
        tree[treeIndex] = tree[2 * treeIndex + 1] + tree[2 * treeIndex + 2];
    }
    
    int sumRange(int left, int right) {
        return sumRangeTree(0, 0, n - 1, left, right);
    }
    
    int sumRangeTree(int treeIndex, int l, int r, int left, int right) {
        if (left > r || right < l) {
            return 0;
        }
        if (left <= l && right >= r) {
            return tree[treeIndex];
        }
        int mid = l + (r - l) / 2;
        int sumLeft = sumRangeTree(2 * treeIndex + 1, l, mid, left, right);
        int sumRight = sumRangeTree(2 * treeIndex + 2, mid + 1, r, left, right);
        return sumLeft + sumRight;
    }
};

int main() {
    vector<int> nums = {1, 3, 5};
    NumArray* obj = new NumArray(nums);
    cout << obj->sumRange(0, 2) << endl;
    obj->update(1, 2);
    cout << obj->sumRange(0, 2) << endl;
    delete obj;
    return 0;
}