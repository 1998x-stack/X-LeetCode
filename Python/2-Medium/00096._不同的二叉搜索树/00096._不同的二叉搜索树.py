from typing import List

def num_trees(n: int) -> int:
    """
    计算由 1 到 n 作为节点值的二叉搜索树有多少种不同的形态。
    
    Args:
    n: int, 一个整数，表示节点值的范围。

    Returns:
    int, 不同的二叉搜索树的数量。
    
    示例:
    >>> num_trees(3)
    5
    """
    # 初始化 dp 数组，长度为 n+1，初始值全为 0。dp[i] 表示由 1 到 i 构成的二叉搜索树的数量。
    dp = [0] * (n + 1)
    
    # 初始条件
    dp[0], dp[1] = 1, 1
    
    # 从 2 到 n 计算 dp[i]
    for i in range(2, n + 1):
        # 计算每个数作为根节点时的树的数量，累加得到 dp[i]
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    
    # 返回由 1 到 n 构成的二叉搜索树的数量
    return dp[n]

# 运行代码，输入为 3，期望输出为 5
print(num_trees(3))