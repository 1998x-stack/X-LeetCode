from typing import List, Deque
from collections import deque

class HitCounter:
    def __init__(self):
        """
        初始化敲击计数器，使用队列记录敲击的时间戳。
        """
        self.hits: Deque[int] = deque()  # 存储敲击的时间戳

    def hit(self, timestamp: int) -> None:
        """
        记录一次敲击事件的时间戳。
        
        Args:
        timestamp (int): 敲击发生的时间戳(秒)。
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        获取过去5分钟内的敲击次数。
        
        Args:
        timestamp (int): 当前的时间戳(秒)。
        
        Returns:
        int: 过去5分钟内的敲击次数。
        """
        # 移除超过5分钟的敲击记录
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)

# 实例化敲击计数器
counter = HitCounter()

# 模拟敲击
counter.hit(1)
counter.hit(2)
counter.hit(3)
hit_count_at_300 = counter.getHits(300)  # 期望返回4
counter.hit(300)
hit_count_at_301 = counter.getHits(301)  # 期望返回3

print(hit_count_at_300, hit_count_at_301)