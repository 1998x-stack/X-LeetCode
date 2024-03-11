from typing import List

def partition(s: str) -> List[List[str]]:
    """
    分割字符串 s，使得分割出的每个子串都是回文串，并返回所有可能的分割方案。
    
    参数:
    s (str): 输入的字符串
    
    返回:
    List[List[str]]: 所有可能的分割方案，每个方案包含一组回文子串
    """
    
    # 动态规划表格，dp[i][j] 表示 s[i:j+1] 是否为回文串
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # 填充动态规划表格
    for i in range(n-1, -1, -1):  # 从后向前遍历，确保计算 dp[i][j] 时 dp[i+1][j-1] 已知
        for j in range(i, n):
            # s[i] == s[j] 时，如果 j-i < 3，说明长度为 1 或 2，必为回文；
            # 或者 dp[i+1][j-1] 为真，说明去掉两端后仍为回文
            if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                dp[i][j] = True
    
    # 结果列表
    res = []
    
    # 递归回溯函数，寻找所有可能的分割方案
    def backtrack(start: int, path: List[str]):
        # 如果起始位置已经到达字符串末尾，说明找到了一种分割方案
        if start == n:
            res.append(path[:])  # 添加当前分割方案的副本
            return
        # 尝试所有可能的分割点
        for i in range(start, n):
            # 如果当前子串是回文
            if dp[start][i]:
                # 将当前回文子串添加到路径中，并继续递归
                backtrack(i+1, path + [s[start:i+1]])
    
    # 从字符串的起始位置开始递归
    backtrack(0, [])
    
    # 返回所有可能的分割方案
    return res

# 测试代码
s = "aab"
partition(s)