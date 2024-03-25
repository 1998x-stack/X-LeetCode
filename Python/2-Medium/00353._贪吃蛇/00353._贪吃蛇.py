from collections import deque
from typing import List, Deque, Set, Tuple

class SnakeGame:
    """
    贪吃蛇游戏类。
    
    Attributes:
        width (int): 游戏区域的宽度。
        height (int): 游戏区域的高度。
        score (int): 游戏得分。
        food (Deque[Tuple[int, int]]): 食物位置的队列。
        snake (Deque[Tuple[int, int]]): 蛇身位置的队列。
        snake_set (Set[Tuple[int, int]]): 蛇身位置的集合，用于快速判断位置是否被蛇身占据。
    """
    
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """初始化游戏状态。"""
        self.width = width
        self.height = height
        self.score = 0
        self.food = deque([(x, y) for x, y in food])  # 食物位置队列
        self.snake = deque([(0, 0)])  # 蛇的初始位置
        self.snake_set = {(0, 0)}  # 快速查找蛇身位置
        self.directions = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}  # 移动方向映射
    
    def move(self, direction: str) -> int:
        """蛇根据给定的方向移动一步。"""
        # 获取新的蛇头位置
        current_head = self.snake[0]
        delta = self.directions[direction]
        new_head = (current_head[0] + delta[0], current_head[1] + delta[1])
        
        # 检查蛇头移动后是否出界或撞到自己
        if (new_head[0] < 0 or new_head[0] >= self.height or 
            new_head[1] < 0 or new_head[1] >= self.width or 
            (new_head in self.snake_set and new_head != self.snake[-1])):
            return -1  # 游戏结束
        
        # 检查蛇头是否移动到食物位置
        if self.food and self.food[0] == new_head:
            self.score += 1  # 得分加1
            self.food.popleft()  # 移除食物
            self.snake_set.add(new_head)  # 更新蛇身位置集合
        else:
            tail = self.snake.pop()  # 移除尾部
            self.snake_set.remove(tail)  # 更新蛇身位置集合
            if new_head in self.snake_set:  # 再次检查是否撞到自己
                return -1
            self.snake_set.add(new_head)
        
        self.snake.appendleft(new_head)  # 更新蛇头位置
        return self.score  # 返回当前得分

# 实例化并运行游戏
snake_game = SnakeGame(3, 2, [[1, 2], [0, 1]])
moves = ["R", "D", "R", "U", "L"]
results = [snake_game.move(direction) for direction in moves]

# 输出每一步的结果
print(results)  # [0, 0, 1, 1, 2]