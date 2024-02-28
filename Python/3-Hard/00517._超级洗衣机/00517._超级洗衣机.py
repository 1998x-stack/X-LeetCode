from typing import List

def find_min_moves(machines: List[int]) -> int:
    """
    计算使得所有洗衣机中衣物数量相等的最小转移次数。

    Args:
    machines: List[int] 每台洗衣机中的衣物数量列表。

    Returns:
    int 最小转移次数，如果无法平均分配，则返回-1。

    """
    total_dresses = sum(machines)  # 总衣物数量
    n = len(machines)  # 洗衣机数量

    # 如果总衣物数量不能被洗衣机数量整除，无法平均分配
    if total_dresses % n != 0:
        return -1

    avg_dresses = total_dresses // n  # 平均每台洗衣机的衣物数量
    max_moves = 0  # 需要的最大转移次数
    curr_flow = 0  # 当前累计流动的衣物数量（正为输出，负为输入）
    for dresses in machines:
        # 对于每台洗衣机，计算与平均值的差值
        diff = dresses - avg_dresses
        # 更新当前流动量
        curr_flow += diff
        # 最小转移次数取决于最大的单台需求（diff的绝对值）和当前的流动量（curr_flow的绝对值）
        max_moves = max(max_moves, abs(curr_flow), diff)

    return max_moves

# 测试代码
machines_example1 = [1, 0, 5]
machines_example2 = [0, 3, 0]
print(find_min_moves(machines_example1))  # 应输出3
print(find_min_moves(machines_example2))  # 应输出2