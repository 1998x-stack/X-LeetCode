import math
from typing import List

def bulbSwitch(n: int) -> int:
    """
    计算在第n轮后亮着的灯泡数量。

    Args:
    - n: int, 总共的灯泡数量和轮数。

    Returns:
    - int, 亮着的灯泡数量。

    示例:
    >>> bulbSwitch(3)
    1

    注意:
    - 这里我们利用了完全平方数的特性来简化问题。
    """
    # 计算1到n之间完全平方数的数量，即为最终亮着的灯泡数量
    return int(math.sqrt(n))

# 运行示例
n = 3
result = bulbSwitch(n)
print(result)