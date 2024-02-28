#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<long long>> dp(m, vector<long long>(n, 0));
        
        // 如果起点或终点有障碍物，直接返回0
        if (obstacleGrid[0][0] == 1 || obstacleGrid[m-1][n-1] == 1) return 0;
        
        // 初始化起点
        dp[0][0] = 1;
        
        // 初始化第一列
        for (int i = 1; i < m; ++i) {
            if (obstacleGrid[i][0] == 1) break; // 遇到障碍物停止
            dp[i][0] = 1;
        }
        
        // 初始化第一行
        for (int j = 1; j < n; ++j) {
            if (obstacleGrid[0][j] == 1) break; // 遇到障碍物停止
            dp[0][j] = 1;
        }
        
        // 填充dp数组
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0; // 当前位置有障碍物，路径数为0
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]; // 从左边和上面转移而来
                }
            }
        }
        
        return dp[m-1][n-1]; // 返回到达终点的路径数
    }
};

int main() {
    Solution solution;
    vector<vector<int>> obstacleGrid = {{0,0,0}, {0,1,0}, {0,0,0}};
    cout << "Unique Paths II: " << solution.uniquePathsWithObstacles(obstacleGrid) << endl;
    return 0;
}