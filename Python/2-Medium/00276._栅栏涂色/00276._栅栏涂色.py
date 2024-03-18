from typing import Tuple

def paint_fence(n: int, k: int) -> int:
    """
    使用动态规划解决栅栏涂色问题。

    参数:
    n: 栅栏的柱子数量。
    k: 可用颜色的数量。

    返回:
    int: 涂色的方式数。

    示例:
    >>> paint_fence(3, 2)
    6
    """
    if n == 0 or k == 0:
        return 0
    if n == 1:
        return k
    same, diff = 0, k
    for i in range(2, n + 1):
        # 上一次迭代的 diff 将成为这一次的 same
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff

# 运行示例
n = 3
k = 2
total_ways = paint_fence(n, k)
print(total_ways)