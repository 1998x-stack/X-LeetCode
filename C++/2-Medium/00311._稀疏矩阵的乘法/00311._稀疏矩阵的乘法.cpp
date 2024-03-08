#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
    int rows1 = mat1.size(), cols1 = mat1[0].size();
    int rows2 = mat2.size(), cols2 = mat2[0].size();
    vector<vector<int>> result(rows1, vector<int>(cols2, 0));
    
    for (int i = 0; i < rows1; ++i) {
        for (int k = 0; k < cols1; ++k) {
            if (mat1[i][k] != 0) { // 只处理非零元素
                for (int j = 0; j < cols2; ++j) {
                    if (mat2[k][j] != 0) { // 寻找对应的非零元素
                        result[i][j] += mat1[i][k] * mat2[k][j]; // 计算乘积并累加
                    }
                }
            }
        }
    }
    return result;
}

int main() {
    vector<vector<int>> mat1 = {{1,0,0},{-1,0,3}};
    vector<vector<int>> mat2 = {{7,0,0},{0,0,0},{0,0,1}};
    vector<vector<int>> result = multiply(mat1, mat2);

    for (const auto &row : result) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << "\\n";
    }

    return 0;
}