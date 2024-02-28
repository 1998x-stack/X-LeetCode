from typing import List
import heapq  # 引入heapq库来使用最小堆

def findMaximizedCapital(k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
    """
    找到最大化的资本

    Args:
    k: int, 最多可以启动的项目数
    W: int, 初始资本
    Profits: List[int], 每个项目的利润
    Capital: List[int], 每个项目的启动资本

    Returns:
    int: 最大化后的总资本

    算法步骤：
    1. 首先将所有项目按照启动资本进行排序。
    2. 使用最小堆来存储当前可以启动的项目，按照利润大小排序。
    3. 不断地从最小堆中取出利润最大的项目，直到达到项目数限制或者没有项目可以启动。
    """
    # 将项目按照启动资本进行排序，以便后续快速筛选可以启动的项目
    projects = sorted(zip(Capital, Profits), key=lambda x: x[0])
    # 初始化一个最小堆，用于存放可以启动的项目
    available_projects = []
    
    # 对每一轮投资进行迭代
    for _ in range(k):
        # 将所有当前可启动的项目添加到最小堆中
        while projects and projects[0][0] <= W:
            cap, pro = projects.pop(0)
            # 使用负利润作为堆的键值，因为heapq是最小堆，但我们需要最大利润
            heapq.heappush(available_projects, (-pro, cap))
        
        # 如果没有可启动的项目，跳出循环
        if not available_projects:
            break
        
        # 启动利润最大的项目
        W -= heapq.heappop(available_projects)[0]  # 取出利润最大的项目，更新W
    
    return W

# 测试代码
k = 2
W = 0
Profits = [1, 2, 3]
Capital = [0, 1, 1]

# 运行并打印结果
max_capital = findMaximizedCapital(k, W, Profits, Capital)
print(f"最大化后的总资本: {max_capital}")