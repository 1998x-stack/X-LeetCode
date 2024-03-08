#include <iostream>
#include <vector>
using namespace std;

// 计算活细胞的数量
int liveNeighbors(vector<vector<int>>& board, int rows, int cols, int i, int j) {
    int lives = 0;
    for (int x = max(i-1, 0); x <= min(i+1, rows-1); ++x) {
        for (int y = max(j-1, 0); y <= min(j+1, cols-1); ++y) {
            lives += board[x][y] & 1; // 只关注最低位
        }
    }
    lives -= board[i][j] & 1; // 减去中心细胞自己的状态
    return lives;
}

// 生命游戏主函数
void gameOfLife(vector<vector<int>>& board) {
    if (board.empty()) return;
    int rows = board.size(), cols = board[0].size();
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            int lives = liveNeighbors(board, rows, cols, i, j);
            
            // 规则1或3
            if (board[i][j] == 1 && (lives < 2 || lives > 3)) board[i][j] = 1; // 保持活着
            // 规则4
            if (board[i][j] == 0 && lives == 3) board[i][j] = 2; // 复活
        }
    }
    
    // 更新板上的细胞状态
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            board[i][j] >>= 1; // 右移一位，获取下一个状态
        }
    }
}

int main() {
    vector<vector<int>> board = {
        {0, 1, 0},
        {0, 0, 1},
        {1, 1, 1},
        {0, 0, 0}
    };
    
    gameOfLife(board);
    
    // 打印结果
    for (int i = 0; i < board.size(); ++i) {
        for (int j = 0; j < board[i].size(); ++j) {
            cout << board[i][j] << " ";
        }
        cout << "\\n";
    }
    return 0;
}