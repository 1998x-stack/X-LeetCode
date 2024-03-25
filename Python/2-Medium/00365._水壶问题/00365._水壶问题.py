from typing import Tuple

def gcd(a: int, b: int) -> int:
    """
    计算两个数的最大公约数（GCD）。
    
    Args:
    a: 第一个数。
    b: 第二个数。
    
    Returns:
    两个数的最大公约数。
    """
    while b != 0:
        a, b = b, a % b
    return a

def can_measure_water(x: int, y: int, z: int) -> bool:
    """
    判断是否可以使用两个水壶测量出恰好z升的水。
    
    Args:
    x: 第一个水壶的容量。
    y: 第二个水壶的容量。
    z: 目标容量。
    
    Returns:
    如果可以测量出z升水，返回True；否则返回False。
    """
    # 边界情况处理
    if x + y < z:
        return False
    if z == 0:
        return True
    if x == 0 or y == 0:
        return z == x + y

    # 计算x和y的最大公约数
    return z % gcd(x, y) == 0

# 示例测试
print(can_measure_water(3, 5, 4)) # 应返回True
print(can_measure_water(2, 6, 5)) # 应返回False
