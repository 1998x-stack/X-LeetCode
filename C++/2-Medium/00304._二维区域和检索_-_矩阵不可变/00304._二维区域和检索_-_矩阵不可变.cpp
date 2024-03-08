#include <vector>
#include <iostream>
using namespace std;

class NumMatrix {
private:
    vector<vector<int>> sums;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        sums.assign(rows + 1, vector<int>(cols + 1, 0));

        // 构建二维前缀和
        for (int i = 1; i <= rows; ++i) {
            for (int j = 1; j <= cols; ++j) {
                sums[i][j] = matrix[i - 1][j - 1] + sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        // 利用二维前缀和快速计算区域和
        return sums[row2 + 1][col2 + 1] - sums[row1][col2 + 1] - sums[row2 + 1][col1] + sums[row1][col1];
    }
};

int main() {
    // 示例输入
    vector<vector<int>> matrix = {
        {3, 0, 1, 4, 2},
        {5, 6, 3, 2, 1},
        {1, 2, 0, 1, 5},
        {4, 1, 0, 1, 7},
        {1, 0, 3, 0, 5}
    };
    NumMatrix numMatrix(matrix);
    cout << numMatrix.sumRegion(2, 1, 4, 3) << endl; // 应输出 8
    cout << numMatrix.sumRegion(1, 1, 2, 2) << endl; // 应输出 11
    cout << numMatrix.sumRegion(1, 2, 2, 4) << endl; // 应输出 12
    return 0;
}