#include <iostream>
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> left(n, 1), right(n, 1), output(n);
    
    // Compute left
    for (int i = 1; i < n; i++) {
        left[i] = left[i - 1] * nums[i - 1];
    }
    
    // Compute right
    for (int i = n - 2; i >= 0; i--) {
        right[i] = right[i + 1] * nums[i + 1];
    }
    
    // Compute output
    for (int i = 0; i < n; i++) {
        output[i] = left[i] * right[i];
    }
    
    return output;
}

int main() {
    vector<int> nums = {1, 2, 3, 4}; // Example input
    vector<int> result = productExceptSelf(nums);
    
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}