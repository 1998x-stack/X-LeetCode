from typing import List

def minCost(costs: List[List[int]]) -> int:
    """
    计算粉刷所有房子的最低成本。
    
    参数:
    costs: 一个二维列表，代表每个房子粉刷成每种颜色的成本。
    
    返回:
    int: 所有房子粉刷的最低成本。
    
    示例:
    >>> minCost([[17,2,17],[16,16,5],[14,3,19]])
    10
    """
    if not costs:
        return 0  # 如果没有房子，成本为0
    
    n = len(costs)
    dp = costs.copy()  # 初始化dp数组
    
    # 动态规划计算最低成本
    for i in range(1, n):
        # 粉刷第i个房子为红色的最低成本
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        # 粉刷第i个房子为蓝色的最低成本
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        # 粉刷第i个房子为绿色的最低成本
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
    
    # 返回所有房子粉刷的最低成本
    return min(dp[-1])

# 测试代码
test_costs = [[17,2,17],[16,16,5],[14,3,19]]
print(minCost(test_costs))  # 应输出最低成本