from typing import List

def nthUglyNumber(n: int) -> int:
    """
    寻找第 n 个丑数。
    
    参数:
        n (int): 要找的丑数的序号。
        
    返回:
        int: 第 n 个丑数。
        
    示例:
        >>> nthUglyNumber(10)
        12
    """
    ugly = [1] * n  # 存储丑数的数组
    i2 = i3 = i5 = 0  # 初始化三个指针
    
    for i in range(1, n):
        # 分别计算乘以 2、3、5 的结果，并取最小值
        next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        ugly[i] = next_ugly
        
        # 如果当前丑数是由某个指针对应的值乘以对应的因子得到的，则该指针前进一步
        if next_ugly == ugly[i2] * 2: i2 += 1
        if next_ugly == ugly[i3] * 3: i3 += 1
        if next_ugly == ugly[i5] * 5: i5 += 1
    
    return ugly[-1]  # 返回第 n 个丑数

# 运行代码，以 n = 10 为例
print(nthUglyNumber(10))