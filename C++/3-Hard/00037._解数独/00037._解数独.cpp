#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
    
    bool solve(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) { // 尝试1到9每一个数字
                        if (isValid(board, i, j, c)) {
                            board[i][j] = c; // 放置数字
                            
                            if (solve(board)) // 递归尝试下一个空格
                                return true;
                            else
                                board[i][j] = '.'; // 回溯，撤销数字
                        }
                    }
                    return false; // 无法填入有效数字，回溯
                }
            }
        }
        return true; // 解决数独
    }
    
    bool isValid(vector<vector<char>>& board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == c) return false; // 检查列
            if (board[row][i] == c) return false; // 检查行
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) return false; // 检查3x3宫格
        }
        return true;
    }
};

int main() {
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
    
    Solution().solveSudoku(board);
    
    // 打印解决后的数独板
    for (const auto &row : board) {
        for (char c : row) {
            cout << c << " ";
        }
        cout << "\\n";
    }
    
    return 0;
}