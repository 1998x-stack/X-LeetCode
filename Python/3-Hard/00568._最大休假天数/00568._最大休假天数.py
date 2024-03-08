from typing import List

def maxVacationDays(flights: List[List[int]], days: List[List[int]]) -> int:
    """
    计算可以获得的最大休假天数。

    Args:
    flights: List[List[int]] -- 航班信息矩阵
    days: List[List[int]] -- 每个城市每周的休假天数矩阵

    Returns:
    int -- 最大休假天数
    """
    N, K = len(days), len(days[0])  # N 代表城市数量，K 代表总周数
    dp = [[0] * N for _ in range(K+1)]  # 初始化 dp 矩阵，多一周是为了方便处理边界情况
    
    # 倒序遍历周数，因为每个城市的最大休假天数依赖于下一周的状态
    for i in range(K-1, -1, -1):
        for j in range(N):
            # 初始化 dp[i][j] 为如果留在当前城市的休假天数
            dp[i][j] = days[j][i]
            # 遍历所有城市，查看是否有航班可以到达，并更新休假天数
            for k in range(N):
                if flights[j][k] == 1 or j == k:  # 如果有直飞航班或者留在当前城市
                    dp[i][j] = max(dp[i][j], days[k][i] + dp[i+1][k])  # 选择最大休假天数
                    
    # 返回第0周在城市0的最大休假天数
    return dp[0][0]

# 测试用例
flights = [[0,1,1],[1,0,1],[1,1,0]]
days = [[1,3,1],[6,0,3],[3,3,3]]
print(maxVacationDays(flights, days))  # 应输出: 12