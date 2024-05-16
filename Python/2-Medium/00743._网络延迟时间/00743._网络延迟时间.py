import heapq
from typing import List, Tuple

def network_delay_time(times: List[Tuple[int, int, int]], N: int, K: int) -> int:
    """
    计算从起始节点 K 发送信号到所有其他节点所需的最短时间。
    使用 Dijkstra 算法在正权重的图中查找最短路径。
    
    :param times: 网络中各条边的列表，每条边由 (起点 u, 终点 v, 权重 w) 表示
    :param N: 网络中节点的总数
    :param K: 信号开始发送的起始节点
    :return: 所有节点接收到信号的最短时间，如果有节点不可达则返回 -1
    """
    # 使用邻接表表示图
    graph = {i: [] for i in range(1, N + 1)}
    for u, v, w in times:
        graph[u].append((v, w))
        
    # 使用优先队列（最小堆）进行 Dijkstra 算法
    min_heap = [(0, K)]
    # 初始距离都设置为正无穷
    shortest_time = {i: float('inf') for i in range(1, N + 1)}
    shortest_time[K] = 0
    
    while min_heap:
        curr_time, curr_node = heapq.heappop(min_heap)
        if curr_time > shortest_time[curr_node]:
            continue
        
        # 遍历邻接节点并更新最短时间
        for neighbor, time in graph[curr_node]:
            new_time = curr_time + time
            if new_time < shortest_time[neighbor]:
                shortest_time[neighbor] = new_time
                heapq.heappush(min_heap, (new_time, neighbor))
    
    # 返回最大的最短时间，如果有节点不可达则返回 -1
    max_time = max(shortest_time.values())
    return max_time if max_time < float('inf') else -1
        
# 示例运行
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
result = network_delay_time(times, N, K)
print(f"示例运行结果: {result}")