from typing import List

def check_records(n: int) -> int:
    """
    计算满足出勤要求的记录数
    
    Args:
    - n: 天数，整数
    
    Returns:
    - 满足条件的出勤记录的数量，整数
    
    说明:
    - 动态规划方法，使用三维数组dp[i][j][k]记录到第i天，有j个'A'，结尾连续k个'L'的记录数。
    """
    # 模1000000007取余，防止整数溢出
    mod = 1000000007
    
    # 初始化dp数组，考虑到边界条件，数组大小为(n+1)x2x3
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
    
    # 初始化第一天的情况
    dp[1][0][0] = 1  # 'P'
    dp[1][1][0] = 1  # 'A'
    dp[1][0][1] = 1  # 'L'
    
    # 从第二天开始计算
    for i in range(2, n+1):
        for j in range(2):  # 缺勤'A'的数量：0或1
            for k in range(3):  # 连续迟到'L'的天数：0、1或2
                # 'P'的情况，不影响'A'数量和'L'的连续天数，连续迟到天数重置为0
                dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % mod
                
                # 'A'的情况，只有当之前没有'A'时，才能加上一个'A'
                if j == 1:
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j-1][k]) % mod
                
                # 'L'的情况，只有k>0时，才能继续加'L'
                if k > 0:
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % mod
    
    # 结果是最后一天所有情况的总和
    return sum(dp[n][j][k] for j in range(2) for k in range(3)) % mod

# 测试代码
n = 2  # 示例输入
result = check_records(n)  # 调用函数计算结果
print(result)  # 输出结果