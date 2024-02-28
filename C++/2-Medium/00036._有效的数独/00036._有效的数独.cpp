#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool isValidSudoku(vector<vector<char>>& board) {
    // 使用哈希表来存储每行、每列和每个宫格中数字的出现情况
    unordered_set<string> seen;
    
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            char number = board[i][j];
            if (number != '.') {
                // 构造在行、列、宫格中唯一标识该数字的字符串
                string rowKey = to_string(number) + " in row " + to_string(i);
                string colKey = to_string(number) + " in col " + to_string(j);
                string boxKey = to_string(number) + " in box " + to_string(i / 3) + "-" + to_string(j / 3);
                
                // 检查数字是否已经在行、列或宫格中出现过
                if (seen.find(rowKey) != seen.end() || seen.find(colKey) != seen.end() || seen.find(boxKey) != seen.end()) {
                    return false;
                }
                seen.insert(rowKey);
                seen.insert(colKey);
                seen.insert(boxKey);
            }
        }
    }
    return true;
}

int main() {
    // 示例数独
    vector<vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };
    
    // 检查数独是否有效
    bool isValid = isValidSudoku(board);
    cout << (isValid ? "Valid" : "Invalid") << " Sudoku" << endl;
    
    return 0;
}