#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void wallsAndGates(vector<vector<int>>& rooms) {
    int INF = 2147483647;
    int rows = rooms.size();
    if (rows == 0) return;
    int cols = rooms[0].size();
    queue<pair<int, int>> q;

    // 将所有门的位置加入队列
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (rooms[i][j] == 0) {
                q.push({i, j});
            }
        }
    }

    // 方向数组，用于探索上下左右四个方向
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    // 开始BFS
    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();
        for (auto& dir : directions) {
            int nr = r + dir[0], nc = c + dir[1];
            // 检查新位置是否有效
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && rooms[nr][nc] == INF) {
                rooms[nr][nc] = rooms[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }
}

int main() {
    vector<vector<int>> rooms = {
        {2147483647, -1, 0, 2147483647},
        {2147483647, 2147483647, 2147483647, -1},
        {2147483647, -1, 2147483647, -1},
        {0, -1, 2147483647, 2147483647}
    };
    
    wallsAndGates(rooms);
    
    // 打印更新后的二维数组
    for (const auto &row : rooms) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    return 0;
}