
#include <iostream>
#include <vector>
using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    bool firstRowHasZero = false, firstColHasZero = false;
    int rows = matrix.size(), cols = matrix[0].size();
    
    // Step 1: Check if the first row and first column have any zeros
    for (int i = 0; i < rows; ++i) {
        if (matrix[i][0] == 0) {
            firstColHasZero = true;
            break;
        }
    }
    for (int j = 0; j < cols; ++j) {
        if (matrix[0][j] == 0) {
            firstRowHasZero = true;
            break;
        }
    }
    
    // Step 2: Use first row and column as markers for rows and cols to be zeroed
    for (int i = 1; i < rows; ++i) {
        for (int j = 1; j < cols; ++j) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    
    // Step 3: Zero out cells based on the markers in the first row and column
    for (int i = 1; i < rows; ++i) {
        for (int j = 1; j < cols; ++j) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }
    
    // Step 4: Zero out the first row and column if needed
    if (firstColHasZero) {
        for (int i = 0; i < rows; ++i) matrix[i][0] = 0;
    }
    if (firstRowHasZero) {
        for (int j = 0; j < cols; ++j) matrix[0][j] = 0;
    }
}

int main() {
    vector<vector<int>> matrix = {{1,1,1}, {1,0,1}, {1,1,1}};
    setZeroes(matrix);
    for (const auto &row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    return 0;
}