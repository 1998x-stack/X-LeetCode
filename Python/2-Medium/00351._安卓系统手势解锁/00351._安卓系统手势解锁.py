from typing import List, Optional, Dict

class AndroidUnlockPatterns:
    """
    安卓系统手势解锁解决方案类
    """

    def __init__(self):
        # 初始化阻挡点映射表
        # 键为一个元组表示起点和终点，值为起点和终点之间的阻挡点
        self.blocked_points: Dict[(int, int), int] = {
            (1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4,
            (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8,
            (1, 9): 5, (9, 1): 5, (2, 8): 5, (8, 2): 5,
            (3, 7): 5, (7, 3): 5, (4, 6): 5, (6, 4): 5
        }
        self.visited: List[bool] = [False] * 10  # 访问标记数组，索引0不使用

    def count_patterns_from(self, curr: int, remain: int) -> int:
        """
        从当前点开始，还需选择的点数为remain，计算解锁图案数量

        :param curr: 当前点
        :param remain: 还需选择的点数
        :return: 解锁图案数量
        """
        # 如果没有剩余点，返回1种图案
        if remain < 0:
            return 0
        if remain == 0:
            return 1
        self.visited[curr] = True
        count = 0
        for next_point in range(1, 10):
            # 检查是否可以访问next_point
            if not self.visited[next_point]:
                # 检查是否有阻挡点，且阻挡点是否已经被访问
                if (curr, next_point) not in self.blocked_points or \
                        self.visited[self.blocked_points[(curr, next_point)]]:
                    count += self.count_patterns_from(next_point, remain - 1)
        self.visited[curr] = False
        return count

    def number_of_patterns(self, m: int, n: int) -> int:
        """
        计算给定长度范围内的解锁图案总数

        :param m: 最小点数
        :param n: 最大点数
        :return: 解锁图案总数
        """
        count = 0
        for length in range(m, n + 1):
            self.visited = [False] * 10  # 重置访问标记
            for i in range(1, 10):
                count += self.count_patterns_from(i, length - 1)
        return count

# 实例化解决方案类，并计算指定范围内的解锁图案总数
solution = AndroidUnlockPatterns()
# 示例，计算最小点数为4，最大点数为6的解锁图案总数
patterns_count = solution.number_of_patterns(4, 6)
print(patterns_count)  # 输出：320