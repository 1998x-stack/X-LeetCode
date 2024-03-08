#include <iostream>
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    int row = 0;
    int col = matrix[0].size() - 1;
    
    // 从右上角开始搜索
    while (row < matrix.size() && col >= 0) {
        if (matrix[row][col] == target) {
            return true; // 找到目标值
        } else if (matrix[row][col] < target) {
            row++; // 向下移动
        } else {
            col--; // 向左移动
        }
    }
    return false; // 超出边界，未找到目标值
}

int main() {
    vector<vector<int>> matrix = {
        {1,   4,  7, 11, 15},
        {2,   5,  8, 12, 19},
        {3,   6,  9, 16, 22},
        {10, 13, 14, 17, 24},
        {18, 21, 23, 26, 30}
    };
    int target = 5;
    bool found = searchMatrix(matrix, target);
    cout << (found ? "true" : "false") << endl;
    
    target = 20;
    found = searchMatrix(matrix, target);
    cout << (found ? "true" : "false") << endl;
    
    return 0;
}