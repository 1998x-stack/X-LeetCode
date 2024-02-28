from typing import List, Tuple, Dict
import heapq

def findShortestWay(maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
    """
    在迷宫中找到从球到洞的最短路径。
    
    参数:
    maze -- 二维整数数组，表示迷宫，0表示空地，1表示墙。
    ball -- 起点坐标，形式为[x, y]。
    hole -- 终点坐标，形式为[x, y]。
    
    返回:
    如果可以到达洞，返回最短路径的方向序列（"u", "d", "l", "r"），否则返回"impossible"。
    """
    
    # 方向和对应的移动增量及标识符
    directions = {'u': (-1, 0, 'u'), 'd': (1, 0, 'd'), 'l': (0, -1, 'l'), 'r': (0, 1, 'r')}
    
    # 初始化优先队列，格式为(步数，路径，x坐标，y坐标)
    q = [(0, "", ball[0], ball[1])]
    
    # 访问标记，记录到达每个点的最短路径
    visited = {(ball[0], ball[1]): (0, "")}
    
    while q:
        steps, path, x, y = heapq.heappop(q)
        
        # 如果到达终点，返回当前路径
        if (x, y) == (hole[0], hole[1]):
            return path
        
        for dx, dy, di in directions.values():
            nx, ny, nsteps = x, y, steps
            
            # 模拟球滚动直到撞墙或到达洞
            while 0 <= nx + dx < len(maze) and 0 <= ny + dy < len(maze[0]) and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
                nsteps += 1
                if (nx, ny) == (hole[0], hole[1]):
                    break
            
            # 如果新路径更短或者字典序更小，则更新路径信息并加入队列
            if (nx, ny) not in visited or visited[(nx, ny)][0] > nsteps or (visited[(nx, ny)][0] == nsteps and visited[(nx, ny)][1] > path + di):
                visited[(nx, ny)] = (nsteps, path + di)
                heapq.heappush(q, (nsteps, path + di, nx, ny))
    
    # 如果无法到达终点，返回"impossible"
    return "impossible"

# 迷宫示例
maze = [[0, 0, 0, 0, 0], 
        [1, 1, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [0, 1, 0, 0, 0]]
ball = [4, 3]
hole = [0, 1]

# 执行函数并打印结果
print(findShortestWay(maze, ball, hole))