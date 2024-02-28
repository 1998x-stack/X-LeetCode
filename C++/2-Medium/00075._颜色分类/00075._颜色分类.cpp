#include <iostream>
#include <vector>
using namespace std;

void sortColors(vector<int>& nums){
    int low = 0, high = nums.size() - 1, current = 0;
    while(current <= high){
        if(nums[current] == 0){
            swap(nums[current++], nums[low++]);
        }else if (nums[current] == 2){
            swap(nums[current], nums[high--]);
        }else{
            current++;
        }
    }
}

int main() {
    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sortColors(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}