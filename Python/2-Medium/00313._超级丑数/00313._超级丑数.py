import heapq
from typing import List

def nthSuperUglyNumber(n: int, primes: List[int]) -> int:
    """
    寻找第n个超级丑数。
    
    参数:
        n (int): 超级丑数的序号。
        primes (List[int]): 质数列表。
    
    返回:
        int: 第n个超级丑数。
    
    方法：
        使用最小堆和动态规划的方法，通过质数列表生成超级丑数，并找到第n个。
    """
    
    # 初始化超级丑数列表，最初只有1
    ugly = [1]
    # 初始化一个最小堆，存储(乘积，质数，索引)，索引是该质数当前乘的ugly数的索引
    heap = [(prime, prime, 0) for prime in primes]
    heapq.heapify(heap)  # 把列表转换成堆结构
    
    # 使用集合记录已经存在的超级丑数，避免重复
    seen = set(ugly)
    
    # 循环，直到找到第n个超级丑数
    while len(ugly) < n:
        # 从堆中弹出最小元素
        val, prime, index = heapq.heappop(heap)
        if val not in seen:
            ugly.append(val)  # 将新的超级丑数添加到列表中
            seen.add(val)  # 添加到已见集合中，避免重复
        # 将新的(乘积，质数，索引+1)加入到堆中，确保下次能获取下一个更大的超级丑数
        heapq.heappush(heap, (prime * ugly[index + 1], prime, index + 1))
    
    return ugly[-1]  # 返回第n个超级丑数

# 示例
n = 12
primes = [2, 7, 13, 19]
print(nthSuperUglyNumber(n, primes))
