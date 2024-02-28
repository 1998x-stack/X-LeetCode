from typing import List, Dict, Tuple, Any
import math

def smallestGoodBase(n: str) -> str:
    """
    寻找最小好进制。
    
    Args:
    - n: 字符串形式的正整数
    
    Returns:
    - 字符串形式的最小好进制 k
    
    说明:
    - 通过枚举可能的 m 值，逐一尝试计算对应的 k 值，直到找到满足条件的最小 k 值。
    """
    n = int(n)  # 将输入转换为整数，便于计算
    max_m = int(math.log2(n))  # 计算最大可能的 m 值
    
    for m in range(max_m, 1, -1):
        k = int((n - 1) ** (1 / m))  # 计算当前 m 下的 k 值
        if (k ** (m + 1) - 1) // (k - 1) == n:
            return str(k)  # 如果 k 满足条件，则返回 k 的字符串形式
    
    return str(n - 1)  # 如果没有找到满足条件的 k，则按题目要求返回 n-1

# 运行代码测试
test_n = "13"
print(smallestGoodBase(test_n))  # 应输出 "3"