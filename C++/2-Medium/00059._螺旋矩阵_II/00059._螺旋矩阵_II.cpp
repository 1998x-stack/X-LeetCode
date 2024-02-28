#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0)); // 初始化 n x n 矩阵
    int num = 1; // 当前填充的数字
    int top = 0, bottom = n - 1, left = 0, right = n - 1;
    
    while (num <= n * n) {
        for (int i = left; i <= right && num <= n * n; ++i) // 从左到右
            matrix[top][i] = num++;
        top++;
        
        for (int i = top; i <= bottom && num <= n * n; ++i) // 从上到下
            matrix[i][right] = num++;
        right--;
        
        for (int i = right; i >= left && num <= n * n; --i) // 从右到左
            matrix[bottom][i] = num++;
        bottom--;
        
        for (int i = bottom; i >= top && num <= n * n; --i) // 从下到上
            matrix[i][left] = num++;
        left++;
    }
    
    return matrix;
}

int main() {
    int n = 3; // 示例输入
    vector<vector<int>> result = generateMatrix(n);
    for (const auto &row : result) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << "\\n";
    }
    return 0;
}