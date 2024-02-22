#include <iostream>
#include <vector>
using namespace std;

// Function to remove elements equal to val and return the new length
int removeElement(vector<int>& nums, int val) {
    int j = 0; // Pointer for the next position of a non-val element
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != val) {
            nums[j] = nums[i]; // Move non-val elements to the front
            j++; // Increment the position for the next non-val element
        }
    }
    return j; // New length of the array after removal
}

int main() {
    // Example array
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;

    // Remove the elements equal to val and get the new length
    int newLength = removeElement(nums, val);

    // Print the new length and the modified array
    cout << "New length: " << newLength << endl;
    cout << "Modified array: ";
    for (int i = 0; i < newLength; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}