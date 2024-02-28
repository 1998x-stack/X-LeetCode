#include <iostream>
#include <vector>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result; // 处理空矩阵的情况

    int m = matrix.size(), n = matrix[0].size(); // m和n分别为矩阵的行数和列数
    int left = 0, right = n - 1, top = 0, bottom = m - 1; // 初始化左、右、上、下四个边界

    while (left <= right && top <= bottom) {
        // 从左到右遍历上边界
        for (int column = left; column <= right; column++) {
            result.push_back(matrix[top][column]);
        }
        // 上边界向下缩进
        top++;

        // 从上到下遍历右边界
        for (int row = top; row <= bottom; row++) {
            result.push_back(matrix[row][right]);
        }
        // 右边界向左缩进
        right--;

        if (left <= right && top <= bottom) {
            // 从右到左遍历下边界
            for (int column = right; column >= left; column--) {
                result.push_back(matrix[bottom][column]);
            }
            // 下边界向上缩进
            bottom--;

            // 从下到上遍历左边界
            for (int row = bottom; row >= top; row--) {
                result.push_back(matrix[row][left]);
            }
            // 左边界向右缩进
            left++;
        }
    }
    return result;
}

int main() {
    vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
    vector<int> result = spiralOrder(matrix);
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}