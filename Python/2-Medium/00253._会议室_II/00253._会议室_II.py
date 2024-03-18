from typing import List, Tuple
import heapq

def minMeetingRooms(intervals: List[Tuple[int, int]]) -> int:
    """
    计算举办所有会议所需的最少会议室数量。

    Args:
    intervals: 一个列表，其中包含若干个元组，每个元组代表一个会议的开始和结束时间。

    Returns:
    所需的最少会议室数量。

    示例:
    >>> minMeetingRooms([(0, 30), (5, 10), (15, 20)])
    2
    >>> minMeetingRooms([(7, 10), (2, 4)])
    1

    """

    # 检查边界情况：如果没有会议，则不需要会议室
    if not intervals:
        return 0
    
    # 对会议按开始时间进行排序
    intervals.sort(key=lambda x: x[0])
    
    # 初始化一个最小堆，用于维护当前正在使用的会议室的结束时间
    # 最小堆的顶部是最早结束的会议室
    heap = []
    
    # 遍历所有会议
    for interval in intervals:
        # 如果堆不为空且当前会议的开始时间晚于堆顶会议的结束时间
        # 则可以重用该会议室，因此移除堆顶元素
        if heap and interval[0] >= heap[0]:
            heapq.heappop(heap)
        
        # 将当前会议的结束时间加入堆中
        heapq.heappush(heap, interval[1])
    
    # 堆的大小即为所需的最少会议室数量
    return len(heap)

# 测试代码
print(minMeetingRooms([(0, 30), (5, 10), (15, 20)]))  # 应输出 2
print(minMeetingRooms([(7, 10), (2, 4)]))  # 应输出 1