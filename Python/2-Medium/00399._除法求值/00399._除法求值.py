from typing import List, Dict, Tuple
from collections import defaultdict, deque

def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """
    根据给定的除法方程，求解多个除法查询的结果。
    
    Args:
    equations: 给定的除法方程，每个元素是由两个字符串组成的列表，表示被除数和除数。
    values: 每个方程的结果。
    queries: 需要求解的查询，每个查询是由两个字符串组成的列表，表示被除数和除数。
    
    Returns:
    一个浮点数列表，表示每个查询的结果。
    
    示例:
    >>> calc_equation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    [6.0, 0.5, -1.0, 1.0, -1.0]
    """
    
    # 构建图，每个节点代表一个变量，每条有向边代表一个除法关系，边的权重是除法的结果
    graph = defaultdict(dict)
    for (dividend, divisor), value in zip(equations, values):
        graph[dividend][divisor] = value  # 添加从 dividend 到 divisor 的边
        graph[divisor][dividend] = 1.0 / value  # 添加从 divisor 到 dividend 的逆边
    
    def bfs(start: str, end: str) -> float:
        """
        使用广度优先搜索在图中查找从 start 到 end 的路径，并计算路径上所有边的权重乘积。
        """
        # 如果起点或终点不在图中，查询无效，返回-1.0
        if start not in graph or end not in graph:
            return -1.0
        # 起点和终点相同，返回1.0
        if start == end:
            return 1.0
        visited = set([start])  # 记录已访问的节点，避免循环搜索
        queue = deque([(start, 1.0)])  # 使用队列进行BFS，存储（当前节点，到当前节点的路径权重乘积）
        while queue:
            current, current_product = queue.popleft()
            if current == end:
                return current_product  # 找到路径，返回路径权重乘积
            for neighbor, value in graph[current].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_product * value))  # 更新到达邻居节点的路径权重乘积
        return -1.0  # 如果找不到路径，返回-1.0
    
    # 处理每个查询，返回查询结果列表
    return [bfs(query[0], query[1]) for query in queries]

# 重新运行测试代码，确保注释后代码的正确性
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
calc_equation(equations, values, queries)
