from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    检查是否可以完成所有课程的学习。

    Args:
    - numCourses: int, 课程总数
    - prerequisites: List[List[int]], 课程的先决条件列表，每个元素是一个列表[ai, bi]，表示要学习课程ai，必须先完成课程bi

    Returns:
    - bool, 如果可以完成所有课程返回True，否则返回False

    示例:
    >>> canFinish(2, [[1,0]])
    True
    >>> canFinish(2, [[1,0], [0,1]])
    False
    """

    from collections import defaultdict, deque

    # 构建图：课程 -> 其先修课程列表
    graph = defaultdict(list)
    # 每门课程的先修课程数量
    in_degree = [0] * numCourses

    # 构建图并更新每门课程的先修课程数量
    for cur, pre in prerequisites:
        graph[pre].append(cur)
        in_degree[cur] += 1

    # 找到所有没有先修课程的课程
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

    # 已学习的课程数量
    learned_courses = 0

    # BFS遍历
    while queue:
        course = queue.popleft()
        learned_courses += 1
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            # 如果next_course的先修课程已经全部学习完，加入队列
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # 如果所有课程的先修课程数量都为0，表示可以完成所有课程的学习
    return learned_courses == numCourses

# 测试代码
print(canFinish(2, [[1, 0]]))  # 应该输出：True
print(canFinish(2, [[1, 0], [0, 1]]))  # 应该输出：False