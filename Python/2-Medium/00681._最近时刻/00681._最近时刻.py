from typing import List, Tuple

class NextClosestTime:
    """
    使用给定数字找到最接近的下一个时间。

    方法:
    - __init__: 初始化方法，存储时间字符串。
    - _parse_time: 解析时间字符串，提取小时和分钟。
    - _generate_times: 生成由输入数字可能组成的所有有效时间。
    - _find_next_time: 找到比当前时间稍晚的最接近时间。
    - get_next_closest_time: 返回计算的下一个最近时间。
    """
    def __init__(self, time: str) -> None:
        """
        初始化方法。
        
        参数:
        time (str): 输入的时间字符串，格式为 "HH:MM"。
        """
        self.original_time = time
        self.hours, self.minutes = self._parse_time(time)
        self.digits = set(time.replace(':', ''))  # 移除冒号，提取所有数字

    def _parse_time(self, time: str) -> Tuple[int, int]:
        """
        解析时间字符串，提取小时和分钟。
        
        参数:
        time (str): 时间字符串，格式为 "HH:MM"。
        
        返回:
        Tuple[int, int]: 小时和分钟组成的元组。
        """
        hour, minute = time.split(':')
        return int(hour), int(minute)

    def _generate_times(self) -> List[str]:
        """
        生成可能的时间列表。
        
        返回:
        List[str]: 所有可能组成的有效时间列表，格式为 "HH:MM"。
        """
        valid_times = []
        for h1 in self.digits:
            for h2 in self.digits:
                for m1 in self.digits:
                    for m2 in self.digits:
                        hour = h1 + h2
                        minute = m1 + m2
                        if 0 <= int(hour) < 24 and 0 <= int(minute) < 60:
                            valid_times.append(f"{hour}:{minute}")
        return sorted(valid_times)

    def _find_next_time(self, times: List[str]) -> str:
        """
        在有效时间列表中找到最接近的下一个时间。
        
        参数:
        times (List[str]): 所有可能组成的有效时间列表，已排序。
        
        返回:
        str: 下一个最近的时间。
        """
        current_time = f"{self.hours:02}:{self.minutes:02}"
        for time in times:
            if time > current_time:
                return time
        return times[0]  # 如果没有更晚的时间，返回最小时间

    def get_next_closest_time(self) -> str:
        """
        获取下一个最近的时间。
        
        返回:
        str: 下一个最近的时间。
        """
        possible_times = self._generate_times()
        next_time = self._find_next_time(possible_times)
        return next_time

# 实例化并使用类来解决问题
solver = NextClosestTime("19:34")
next_time = solver.get_next_closest_time()
print(next_time)  # 输出 "19:39"