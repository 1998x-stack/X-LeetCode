from typing import List
from collections import deque

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # 建立图的邻接表和计算每个节点的入度
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for cur, pre in prerequisites:
        adj[pre].append(cur)
        indegree[cur] += 1

    # 初始化队列，加入所有入度为 0 的节点
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []  # 存储拓扑排序的结果，即课程的学习顺序

    # 执行拓扑排序
    while queue:
        pre = queue.popleft()
        order.append(pre)
        for cur in adj[pre]:
            indegree[cur] -= 1  # 减少依赖该课程的其他课程的入度
            if indegree[cur] == 0:
                queue.append(cur)  # 如果入度为 0，则加入队列

    # 检查是否所有课程都被访问
    return order if len(order) == numCourses else []

# 示例
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))  # [0,1,2,3] 或 [0,2,1,3]