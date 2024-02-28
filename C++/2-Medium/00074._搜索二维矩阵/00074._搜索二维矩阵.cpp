#include <iostream>
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target){
    if(matrix.empty() || matrix[0].empty()){
        return false;
    }
    int m = matrix.size(), n = matrix[0].size();
    int left = 0, right = m * n - 1;

    while(left <= right){
        int mid = left + (right - left) / 2;
        int midValue = matrix[mid / n][mid % n];
        if(midValue == target)
            return true;
        else if (midValue < target){
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    return false;
}
int main() {
    vector<vector<int>> matrix = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    int target = 3;
    cout << (searchMatrix(matrix, target) ? "true" : "false") << endl;
    
    target = 13;
    cout << (searchMatrix(matrix, target) ? "true" : "false") << endl;
    
    return 0;
}