from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    合并所有重叠的区间。

    Args:
    intervals: List[List[int]] 一个区间的集合，每个区间由两个整数表示（起始位置，结束位置）。

    Returns:
    List[List[int]] 合并后的区间列表。

    示例:
    >>> merge_intervals([[1,3],[2,6],[8,10],[15,18]])
    [[1,6],[8,10],[15,18]]

    """
    # 按照区间的起始位置进行排序
    intervals.sort(key=lambda x: x[0])

    merged = []  # 初始化合并后的区间列表
    for interval in intervals:
        # 如果合并列表为空或当前区间的起始位置大于合并列表中最后一个区间的结束位置
        # 则不重叠，将当前区间添加到合并列表中
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则，有重叠，合并区间，更新最后一个区间的结束位置为当前区间和最后一个区间结束位置的最大值
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# 测试代码
test_intervals = [[1,3],[2,6],[8,10],[15,18]]
merged_intervals = merge_intervals(test_intervals)
print("合并后的区间：", merged_intervals)
